# ADA_project: You are what you eat

## Abstract

In this project, we aim to tell a comprehensive and sometimes surprisingly detailed story regarding the identity of participants in a survey on shopping habits. We believe that despite their anonymity, we are able to acquaint ourselves with the individuals behind these transactions. Here we illustrate our process, whereby observation of subjects’ behaviour on multiple levels and analysis of sample parameters, from macro-trends all the way down to specific individual consumption patterns, enable us to gain such insight.

## Research questions
### 1. Dealing with bias
  ####1.1: "Card usage" bias: We need to be aware that the information comes from the subsample of population that uses the shopping cards. These users might be younger and technologically savyer than the typical buyer. The consumption patterns might be skewed towards this demographic.  

  #### 1.2: Location bias (living far from the store): Can we assume that most of the buyers live in the area of the store?

  #### 1.3: Time bias: For how long did the study take place? At what time was it done?

  #### 1.4: Frequency bias: How can we balance the transaction expense with the frequency of the transactions. For example, someone might go very often and buy very few items, while someone might go a single time per month and buy many things.


### 2. Research questions
  #### 2.1: Influence of demographic factors on shopping habits.

  ##### 2.1.1 How is income related to shopping habits?

  ##### 2.1.2 How is age related to shopping habits?

  ##### 2.1.3 How is the size of household, or the family structure related to shopping habits?

  #### 2.2: Correlate total amount of calories consumed per household with health parameters

  #### 2.3: Analysis and identification of un/healthy shopping habits.

  #### 2.4: Time series analysis /
  ##### 2.4.1 Even with time absolute value, is it possible to find the season of the year where the data was sampled ?
  ##### 2.4.2 Identify items that are only purchased at specific times of day
  ##### 2.4.3 Trending products (identify items that are only purchased at specific times of day)

  #### 2.5 (Clustering) Find out amount of calories consumed per household and make groups out of it (obesity detection)

  #### (Bonus) Create folium map for the stores.  

### 3. Creating Useful Tools
  #### 3.1: Create a suggestion method which given the budget profile/nutrition habit of the customer would allow him to purchase more nutritious and balanced food for an equivalent price

  #### 3.2: Identify consumption patterns that are suggestive of addiction (alcohol, tobacco, prescription drugs)

  #### 3.3: To what extant do discount really benefit households ?


## Usage of additional datasets
- A WHO dataset on health in the region (Atlanta): this would allow us to find a potential correlation between caloric intake and health state by using parameters such as prevalence of diabetes or obesity per neighborhood.
- Dunnhumby: Carbo-loading (_csv 115mb_): Carbo-loading dataset to retrieve the zip codes of the stores in the study to be able to make geographical analysis.
- Dataset with nutritional facts of food items sold: Nutritional info dataset to be able to calculate the food consumption for each household and compare it against recommended amount, while taking demographics into account


All the datasets chosen are not too large in order to be able to perform most of the computations on personal computers.

## A list of internal milestones up until project milestone 2
- Find all the extra datasets in order to complete our analysis
- Define more specifically our approach/goal depending on the feasability of the different aforementioned points.
- Getting a first look at features distribution, variance
- Design good metrics that can be reused amongst different studies

## Questions for TAs
NA
