# ADA_project: You are what you eat

## Abstract

In this project, we aim to tell a comprehensive and sometimes surprisingly detailed story regarding the identity of participants in a survey on shopping habits. We believe that despite their anonymity, we are able to acquaint ourselves with the individuals behind these transactions. Here we illustrate our process, whereby observation of subjects’ behaviour on multiple levels and analysis of sample parameters, from macro-trends all the way down to specific individual consumption patterns, enable us to gain such insight.

## Research questions
### 1. Dealing with bias
  1.1: "Card usage" bias: We need to be aware that the information comes from the subsample of population that uses the shopping cards. These users might be younger and technologically savyer than the typical buyer. The consumption patterns might be skewed towards this demographic.  
  
  1.2: Location bias (living far from the store): Can we assume that most of the buyers live in the area of the store? 
  
  1.3: Time bias: For how long did the study take place? At what time was it done?
  
  1.4: Frequency bias: How can we balance the transaction expense with the frequency of the transactions. For example, someone might go very often and buy very few items, while someone might go a single time per month and buy many things. 
 ### 2. Metrics
  2.1: Since we want to look at the correlation of different parameters related to shopping habbits, we must research/use/develop adapted metrics in order to assess these datas.
    
    First ideas:
    
      -quality of bought items (bio,organic, processed,"junk",etc)
      
      -transaction value
      
      -frequency of transactions
      
      -diversity or entropy measure of bought items(Does a family buy vegetables, proteins, grains, breads, etc. Or only one kind of item?)
      
      - nutrient value (compare equivalent nutrient amount in bought foods with recommended nutrient intake per person per time).

 ### 3. Categories Discovery (supervised / unsupervised learning)
  3.1: Influence of demographic factors on shopping habits. 
  
  3.2: How is income related to shopping habits? 
  
  3.3: How is age related to shopping habits?
  
  3.4: How is the size of household, or the family structure related to shopping habits?
  
  3.5: Correlate total amount of calories consumed per houshold with health parameters
  
  3.6: Budgeting: calculate price per kilo and identify outliers that appear systematically to track consumption 
  
  3.7: Identify items that are only purchased at specific times of day

  3.8: Observe seasonal variation of shoping trends (Holiday season)
  
  3.9: Correlate macro-consumption trends with important local news events


  ### 4. Creating Useful Tools
  4.1: Create a suggestion method which given the budget profile/nutrition habit of the customer would allow him to purchase more nutritious and balanced food for an equivalent price
  
  4.2: Suggest to the customer the best time when to do his groceries according to the affluence
  
  4.3: Identify consumption patterns that are suggestive of addiction (alcohol, tobacco, prescription drugs)
  
  4.4: Predict as precisely as possible consumption of perishable food (such as vegetable) in order to prevent food waste.
  
  4.5: Predict the date and amount of the next transaction

  4.6 Predict the Effect of marketing strategies (coupons) on customer engagement
  
  4.7: Time spent in store and amount spent  

## Usage of additional datasets
- A WHO dataset on health in the region (Atlanta): this would allow us to find a potential correlation between caloric intake and health state by using parameters such as prevalence of diabetes or obesity per neighborhood.
- Dunnhumby: Carbo-loading (_csv 115mb_): Carbo-loading dataset to retrieve the zip codes of the stores in the study to be able to make geographical analysis.
- Dataset with nutritional facts of food items sold: Nutritional info dataset to be able to calculate the food consumption for each household and compare it against recommended amount, while taking demographics into account
- Dataset with local news. (_ex: Atlanta New Now_): Local news dataset to male correltaion with sudden changes in consumption trend (ex: news annoucement of correlation of red meat consumption and cancer rates increase)

All the datasets chosen are not too large in order to be able to perform most of the computations on personal computers.

## A list of internal milestones up until project milestone 2
- Find all the extra datasets in order to complete our analysis
- Define more specifically our approach/goal depending on the feasability of the different aforementioned points.
- Getting a first look at features distribution, variance
- Design good metrics that can be reused amongst different studies

## Questions for TAs
Is it possible to find the zip code of each store or household in the study in order to enrich our analysis with geographical maps?
Is it feasible to webscrape all the nutritional info of the food products on sale in this store, given that they are from very different brands? Is there a centralized dataset for this? (maybe from the FDA)



