# ADA_project: You are what you eat

# Abstract

In this project, we aim to tell a very complete and detailed story about the identity of the people who participated in the survey of shopping habits. We believe that despite their anonymity, we are able to get relevant information about the people behind those transactions. We are going to analyse as many possible parameters to enable thus to get strong relevant insights into their shopping habits. We aim to analyse behaviour on all possible levels, from macro-trends of the whole sample all the way down to individual specific comsumption patterns.

# Research questions
q1: Since we want to look at the correlation of different parameters with shopping habbits. We must develop metrics to assess the shopping    habbits. What kind of metrics should we use to assess shopping habbits?  
    Proposed answer: These are the metrics we can try:
      -quality of bought items (bio,organic, processed,"junk",etc)
      -transaction value
      -frequency of transactions
      -diversity or entropy measure of bought items(Does a family buy vegetables, proteins, grains, breads, etc. Or only one kind of            item?)
      - nutrient value (compare equivalent nutrient amount in bought foods with recommended nutrient intake per person per time).
q2: How can we deal with different biases?
  q2.1: "card usage" bias: We must be aware that the information comes from the subsample that uses the shopping cards. These users       might be     younger and technologically savyer than the typical buyer. The consumption patterns might be skewed towards this           demographic.  
  q2.2: Location bias (living far from the store): Can we assume that most of the buyers live in the area of the store? 
  q2.3: Time bias: For how long did the study take place? 
  q2.4: Frequency bias: How can we balance the transaction expense with the frequency of the transactions. For example, someone might go   very often and buy very few items, while someone might go a single time per month and buy many things. 

q3: Influence of demographic factors on shopping habits. 
  
  q3.1: How is income related to shopping habits? 
  q3.2: How is age related to shopping habits?
  q3.3: How is the size of household, or the family structure related to shopping habits?
  q3.4: Correlate total amount of calories consumed per houshold with health parameters
  q3.5: Determine family stability (definition of stability?) according to consumption
  q3.6: Predict individual behaviour based on consumption
  q3.7: Identify consumption patterns that are suggestive of addiction (alcohol, tobacco, prescription drugs)
  q3.8 Effect of marketing strategies (coupons) on customer engagement
  q3.9: Time spent in store and amount spent
  q3.10: Budgeting: calculate price per kilo and identify outliers that appear systematically to track consumption 
  q3.11: Correlate macro-consumption trends with important local news events
  q3.12: Identify different shopper profiles using unsupervised clustering
  q3.13: Identify items that are only purchased at specific times of day
  q3.14: Observe seasonal variation of shooping trends (Holiday season)
  q3.15: Predict the date and amount of the next transaction

# Dataset
- Dunnhumby: The complete journey, csv 300mb
- A WHO dataset on health in the region (Atlanta)
- Dunnhumby: Carbo-loading, csv 115mb
- Dataset with nutritional facts of food items sold
- Dataset with local news. (ex: Atlanta New Now)

## Usage of supplementary datasets
- Dataset on health to make the correlation between caloric intake and health state by using parameters such as prevalence of diabetes or obesity per neighborhood.
- Carbo-loading dataset to retrieve the zip codes of the stores in the study to be able to make geographical analysis.
- Nutritional info dataset to be able to calculate the food consumption for each household and compare it against recommended amount, while taking demographics into account
- Local news dataset to male correltaion with sudden changes in consumption trend (ex: news annoucement of correlation of red meat consumption and cancer rates increase)

All the datasets chosen are not too large in order to be able to perform most of the computations on personal computers.

# A list of internal milestones up until project milestone 2
- Find all the extra datasets to complete our analysis
- First look at features distribution, variance, ...
- Design good metrics that can be reused amongst different studies

# Questions for TAs
Is it possible to find the zip code of each store or household in the study in order to enrich our analysis with geographical maps?
Is it feasible to webscrape all the nutritional info of the food products on sale in this store, given that they are from very different brands? Is there a centralized dataset for this? (maybe from the FDA)



