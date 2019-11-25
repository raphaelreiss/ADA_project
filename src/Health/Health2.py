#!/usr/bin/env python
# coding: utf-8

# ### Remarks / TODO:
#     -there are a few food items in MISC. TRANS
#     - add the nutrients present under different names and ids, such as: carbohydrates or carbohydrates by difference

import re
import os
import nltk
import time
import pickle
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(1, './utilities/')
from health_functions import *

# # Import Data
def import_data(path1, path2):
    dfList = {}
    for r, d, f in os.walk(path1):
        for file in f:
            if '.csv' in file:
                print(file)
                dfList[file] = pd.read_csv(os.path.join(r, file))

    products_df = dfList['product.csv']
    transaction_data_df = dfList['transaction_data.csv']

    dfList = {}
    for r, d, f in os.walk(path2):
        for file in f:
            if '.csv' in file:
                # print(file)
                dfList[file] = pd.read_csv(os.path.join(r, file))

    # link the nutrient id with its name
    nutrient_df = dfList['nutrient.csv']
    # contains the food articles name and their id test commit
    food_df = dfList['food.csv']
    # contains the nutrients for each food article
    food_nutrients_df = dfList['food_nutrient.csv']
    # linke the food articles ids to their category
    food_category_df = dfList['food_category.csv']
    return products_df,transaction_data_df, nutrient_df, food_df, food_nutrients_df, food_category_df

# ### Most sold items
def compute_most_sold_items(products_df,transaction_data_df,selected_categories):
    #select all the items sold at least 1000 times
    sales_qte_df = transaction_data_df[['PRODUCT_ID','QUANTITY']]    .groupby(['PRODUCT_ID']).sum().sort_values(by=['QUANTITY'],ascending=False)
    sales_qte_df = sales_qte_df[sales_qte_df['QUANTITY'] > 1000]
    sales_qte_df.head(5)

    #select only the categories which are food related and sort them
    products_sales_df = products_df.loc[(products_df['DEPARTMENT'].isin(selected_categories))].join(sales_qte_df, on='PRODUCT_ID', how='inner')
    products_sales_df.sort_values(by='QUANTITY',ascending=False,inplace=True)

    #we put all the description in a ingredients column
    products_sales_df['ingredients'] = products_sales_df.COMMODITY_DESC + " " + products_sales_df.SUB_COMMODITY_DESC
    products_sales_df.drop(["DEPARTMENT","BRAND","COMMODITY_DESC","SUB_COMMODITY_DESC"],axis = 1, inplace = True)
    products_sales_df.ingredients = products_sales_df.ingredients.apply(parse_words)

    return products_sales_df

def clean_dfs(food_nutrients_df,nutrient_df,food_category_df,food_df,list_relevant_nutrients):
    #drop unnecessary columns and rename to be more understandable
    food_nutrients_df.drop(["data_points","min","max","median","footnote","min_year_acquired","derivation_id"],axis=1,inplace=True)
    nutrient_df.drop(["nutrient_nbr","rank"],axis=1,inplace=True)
    food_category_df.drop(["code"],axis=1,inplace=True)
    food_df.drop(["publication_date"],axis=1,inplace=True)

    food_category_df.rename(columns={'id':'food_category_id','description':'category'},inplace= True)
    #filter out only the necessary food nutrients
    nutrient_df = nutrient_df[nutrient_df.name.isin(list_relevant_nutrients)]

    #simplyfy and normalize the nutrient names
    simplified_names = nutrient_df.name.apply(trim_nutrient_name)
    nutrient_df.loc[:,"name"] = simplified_names
    # add the names of the nutrients contained in the food

    return food_nutrients_df, nutrient_df, food_category_df, food_df


def complete_food_dfs(food_nutrients_df, food_df):
    food_nutrients_df = food_nutrients_df.join(nutrient_df.set_index('id'), on='nutrient_id', how='inner')

    #takes a long time to run
    #food_nutrients_df.amount = food_nutrients_df[["amount","unit_name"]].apply(get_amount, axis=1)
    #food_nutrients_df.drop("unit_name",axis=1,inplace=True))

    #energy is duplicated because we have both kcal and kj, we take only kcal
    food_nutrients_df = food_nutrients_df.pivot_table(index='fdc_id', columns='name', values='amount',aggfunc='first')
    food_nutrients_df.fillna(value=0, inplace=True)

    #add categories to the food df
    food_df = food_df.join(food_category_df.set_index("food_category_id"),on="food_category_id",how="left")
    food_df.drop(["food_category_id"],axis=1,inplace=True)
    food_df.description = food_df.description.apply(parse_words)

    return food_nutrients_df, food_df

if __name__ == "__main__":
    DUNNHUMBY_PATH = '../data/dunnhumby - The Complete Journey CSV/'
    HEALTH_PATH = '../data/health'
    products_df, transaction_data_df, nutrient_df, food_df, food_nutrients_df, food_category_df = import_data(DUNNHUMBY_PATH,HEALTH_PATH)

    food_related_categories = np.array(
        ['NUTRITION', 'GROCERY', 'PASTRY', 'MEAT-PCKGD', 'SEAFOOD-PCKGD', 'PRODUCE', 'DELI', 'MEAT', 'SALAD BAR',
         'GRO BAKERY', 'FROZEN GROCERY', 'SPIRITS', 'RESTAURANT'])
    list_relevant_nutrients = ["Protein", "Total Carbohydrate", "Total lipid (fat)", "Sucrose", "Glucose (dextrose)",
                               "Sugars, total including NLEA", "Fatty acids, total monounsaturated",
                               "Fatty acids, total polyunsaturated", "Fatty acids, total trans",
                               "Fatty acids, total saturated", "Cholesterol", "Vitamin E, added",
                               "Vitamin K (phylloquinone)", "Vitamin B-12", "Vitamin B-6", "Vitamin D",
                               "Vitamin A, RAE", "Sodium, Na", "Total fat (NLEA)", "Fiber, total dietary", "Energy",
                               "Carbohydrate, by summation", "Fructose"]

    products_sales_df = compute_most_sold_items(products_df, transaction_data_df, food_related_categories)
    food_nutrients_df, nutrient_df, food_category_df, food_df = clean_dfs(food_nutrients_df, nutrient_df, food_category_df, food_df, list_relevant_nutrients)
    food_nutrients_df, food_df = complete_food_dfs(food_nutrients_df, food_df)

    all_information_df = food_df.join(food_nutrients_df, on='fdc_id', how='inner')
    all_information_df.drop(["data_type", "description", "category"], axis=1, inplace=True)

    #Compute word importance for algo
    # all words present in the nutrition dataset
    all_words_nutrition = get_allwords(food_df.description)
    # all words present in the product dataset
    all_words_supermarket = get_allwords(products_sales_df.ingredients)

    # #### Inner merge between the 2 sets of words:
    common_words = pd.merge(all_words_supermarket, all_words_nutrition, left_on='name', right_on='name',
                            suffixes=('_supermarket', '_nutrition'))
    DIC_SCORE = construct_dic_score(common_words)

    #matching the two datasets
    #there is an error in the code, so for now we only using the top 10 items
    temp_df = products_sales_df.head(10).copy()
    find_food1 = lambda list_words: find_food(list_words, food_df, DIC_SCORE)
    temp_df["ref_fdc_id"] = temp_df.ingredients.apply(find_food1).fdc_id

    #create our final df with the nutrient information of the supermarket items
    all_df = temp_df.merge(all_information_df, how="left", left_on="ref_fdc_id", right_on="fdc_id")
    all_df.drop(["MANUFACTURER", "ref_fdc_id", "fdc_id"], axis=1, inplace=True)
    all_df.set_index("PRODUCT_ID", inplace=True)

    # saves results of this lengthy computation
    all_df.to_pickle("../data/results/products_with_link_to_nutrients_df.pickle")

    print("done")
