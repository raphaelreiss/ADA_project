# -*- coding: utf-8 -*-
"""some helper functions for the health analysis"""
import re
import numpy as np
import pandas as pd
import nltk

#definition of stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords 
STOP_WORDS = list(set(stopwords.words('english')))
STOP_WORDS.append('NFS')
#Manual addition of words that we want to ignore to the Stopwords list
to_delete = ["added","ns","made","eaten","type","all","as","to","of"]
STOP_WORDS.append(to_delete)

#definition of foodwords
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
FOOD_WORDS = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

#We see words in the product dataset, we would like to write them out completely for clarity
#TO ADD: SNKSCKYS/CRKR/CNDY
to_transform = dict({"frzn":"frozen","refrgratd":"refrigerated","brkfst":"breakfast","whlsm":"wholesome",\
                     "crkr":"cracker","cndy":"candy"})

def parse_words(str1): 
    """
    parses the string in a list of string (words) with all type of separators thanks to regexes
    """
    #matches any separator and any whitespace and transforms to mathc to lower case
    str1 = str1.lower()
    str1 = list(filter(None,re.split("[\s;&@\/:,\*\.\(\)\{\}\\-%\"\'0-9\_]",str1)))
    #remove duplicate word, as there are many
    str1 = list(dict.fromkeys(str1))
    str1 = [i for i in str1 if not i in STOP_WORDS]
    str1 = [to_transform[i] if i in to_transform else i for i in str1]
    
    return str1

def trim_nutrient_name(temp):
    """
    simplifies the names of the nutrients for easier access afterwards
    """
    #matches any separator and any whitespace and transforms to match to lower case
    temp = temp.lower()
    temp = list(filter(None,re.split("[;&@\/:,\*\.\(\)\{\}\\%\"\']",temp)))
    #remove duplicate word, as there are many
    temp = [i for i in temp if not i in STOP_WORDS]
    if(temp[0] == "fatty acids"):
        return str.strip(temp[0] + temp[1])
    else:
        return str.strip(temp[0])

def get_amount(to_convert):
    """Returns the amount of a nutrient by taking into account the specified unit
    """
    if(to_convert.unit_name == "UG"):
        return to_convert.amount * 1e-6
    elif(to_convert.unit_name == "MG"):
        return to_convert.amount * 1e-3
    else:
        return to_convert.amount
    
def normalize_text(str1):
    """
    simplifies the names of the foods for easier access afterwards
    """
    #matches any separator and any whitespace and transforms to mathc to lower case
    temp = re.sub("[;&@\/:,\*\.\(\)\{\}\\%\"\']", ' ', str1)
    temp = temp.lower()
    words = temp.split()
    words = [i for i in words if not i in STOP_WORDS]
    temp = " ".join(sorted(set(words), key=words.index))
    return temp

def get_allwords(serie):
    """
    serie: serie containing lists of words
    return a dataframe containing
      - column name: name of the unique articles found in the lists of the serie
      - column count: how many times they appear in the serie
    """
    allwords = np.concatenate(serie.ravel())
    allwords = pd.Series(allwords)
    allwords = pd.DataFrame(allwords,columns= ["name"])
    allwords.reset_index(inplace = True)
    allwords.rename(columns = {'index':'number'},inplace = True)
    allwords = allwords.groupby('name').count().sort_values(by = 'number',ascending = False)
    return allwords.reset_index()

def get_matches(test:list,food_list):
    """
    test = list of strings to test
    food_list: pandas dataframe linking the food article/id to the lists of words of its name
    return all the articles whose words contain all of the words of test
    """
    assert(type(test[0]) == str)
    res = []
    fdc_id = []
    for word_list,id_ in food_list[["description","fdc_id"]].itertuples(index=False):
        if all([word_test in word_list for word_test in test]):
            res.append(word_list)
            fdc_id.append(id_)
    return pd.DataFrame(data={'match':res, 'fdc_id':fdc_id})

def construct_dic_score(common_w):
    """
    common_w: dataframe containing the common names btwn products and nutrition
    In order to give a score to a word, the priority is to check if it is present in the ntds list. If it is,
    it gets a score of 1.
    The rest of the score is a max-normalized ratio of the occurence in the product dataset.
    
    return a dic where each of these common names + food_words have their score linked
    """
    common_w = common_w.copy()
    maxo = common_w.number_supermarket.max()
    common_w.number_supermarket = common_w.number_supermarket / maxo
    common_w.drop(columns= ["number_nutrition"],axis = 1,inplace = True)

    food_word_df = pd.DataFrame(columns = common_w.columns)
    food_word_df.name = pd.Series(FOOD_WORDS)

    food_word_df.name = food_word_df.name.apply(parse_words)
    food_word_df = food_word_df.explode('name')
    food_word_df.drop_duplicates(inplace = True)
    food_word_df.fillna(1,inplace = True)

    dic_score = pd.concat([food_word_df,common_w])
    dic_score = dic_score.rename(columns = {"number_supermarket":"score"})
    dic_score = dic_score.groupby("name").sum()
    dic_score.sort_values('score',ascending = False)
    dic_score = pd.Series(dic_score.score.values,index = dic_score.index).to_dict()
    return dic_score

def find_food(test,food_list, dic_score,verb = True):
    """
    implementation of the graphic above
    test = list of strings to test
    food_list: pandas dataframe linking the food article/id to the lists of words of its name
    return the best article's ingredient list AND fdc_id
    """
    def printo(stringo,verb): 
        if verb:
            print(stringo)
    
    #printo("############# Analyzing the sample:{}###########".format(test),verb)
    if len(test) == 0:
        #give up the sample
        printo("END no match was found!",verb)
        return [],np.nan #dummy
    
    matches_df = get_matches(test,food_list)
    if matches_df.size == 0:
        #printo("No Match: ",verb)
        scores = [dic_score.get(i,0) for i in test]
           
        #for i,j in zip(test,scores):
            #printo("word {} has score {}".format(i,j),verb)
        
        armin = np.argmin(scores)
        #printo("minscore:({},{}) will be deleted \n".format(scores[armin],test[armin]),verb)
        
        test = [elem for i,elem in enumerate(test) if i != armin]
        return find_food(test,food_list,dic_score,verb)
    
    elif matches_df.size == 1:
        match = matches_df.loc[0]
        #match = matches[0]
        printo("Found a single match:{}".format(match["match"]),verb)
        return match
    else:
        sizes = [len(i) for i in matches_df["match"]]
        #sizes = [len(i) for i in matches]
        minsize = np.min(sizes)
        minsiz_matches_df = matches_df[(matches_df.match.apply(len).values) == minsize]
        #minsiz_matches_df = [i for i in matches if len(i) == minsize]
        if minsiz_matches_df.size == 1:
            printo("Single match of minsize:{}".format(minsiz_matches.loc[0]["match"]),verb)
            return minsiz_matches_df.loc[0]
        else:
            #printo("Many matches of minsize:{}".format(minsiz_matches),verb)
            #scores = [np.sum([dic_score.get(j,0) for j in trial]) for trial in minsiz_matches]
            minsiz_matches_df["scores"] = [np.sum([dic_score.get(j,0) for j in trial]) for trial in minsiz_matches_df["match"]]
            
            #for i,j in zip(minsiz_matches,scores):
                #printo("{} match has {} score".format(i,j),verb)
            
            #armin_imp = np.argmin(scores)
            #printo("Match of smallest importance:{}".format(minsiz_matches[armin_imp]),verb)
            #return minsiz_matches[armin_imp]
            return minsiz_matches_df.loc[minsiz_matches_df.scores.idxmin()][["match","fdc_id"]]
        
        
def get_nutrient_amount(product_id,nutrient,products_df1,food_nutrients_df1):
    """
    product_id = id of product of which we want to know the nutritional info, int
    nutrient = the nutrient of which we want to know the amount, string
    products_df1 = the df which contains the products id
    returns the amount of the specified nutrient contained in the specified product
    """
    mask = (products_df1["PRODUCT_ID"] == product_id)
    if any(mask):
        index = products_df1[mask].ref_fdc_id.values[0]
        return food_nutrients_df1.loc[index,nutrient]["amount"].values[0]
    else:
        print("Product not found")
        return 0