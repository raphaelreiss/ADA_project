# ADA_project: You are what you eat

# Abstract

In this project, we aim to tell a very complete and sometimes suprisingly detailed story about the identity of the people that participated in the survey of shopping habits. We believe that despite their anonimity, we are able to get to know the people behind those transactions.

A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

# Research questions
- How to deal with "card usage bias"
  - Location bias (living far from the store)
  - Time bias
  - Frequency bias
  - Age category bias
- Influence of demographic factores on shopping habits
  - Income
  - Age category
  - Size of household, number of children
- Correlate total amount of calories consumed per houshold with health parameters (obesitsy) ? -> combination with health dataset
- Determine family stability (definition of stability?) according to consumption
- Predict individual behaviour based on consumption
- Identify consumption patterns that are suggestive of addiction (alcohol, tobacco, prescription drugs)
- Transaction frequency and amount
- Effect of marketing strategies (coupons) on customer engagement
- Time spent in store and amount spent
- Budgeting: calculate price per kilo and identify outliers that appears systematically
- Correlate macro-consumption trends with important local news events
- Identify different shopper profiles using unsupervised clustering
- Identify items that are only purchased at specific times of day
- Observe seasonal variation of shooping trends (Holiday season)

# Dataset
- Dunnhumby: The complete journey, csv 300mb
- A WHO dataset on health in the region (Atlanta)
- Dunnhumby: Carbo-loading, csv 115mb
- Dataset with nutritional facts of food items sold
- Dataset with local news. (ex: Atlanta New Now)

## Usage of supplementary datasets
- Dataset on health to make the correlation between caloric intake and health state by using parameters such as prevalence of diabetes or obesity per neighborhood.
- Carbo-loading dataset to retrieve the zip codes of the stores in the study to be able to make geographical analysis.
- Nutritional info dataset to be able to calculate the food consumptio for each household and compare it against recommended amount, while taking demographics into account
- Local news dataset to male correltaion with sudden changes in consumption trend (ex: news annoucement of correlation of red meat consumption and cancer rates increase)

All the datasets chosen are not too large in order to be able to perform most of the computations on personal computers.

# A list of internal milestones up until project milestone 2
- Find all the extra datasets to complete our analysis
- First look at features distribution, variance, ...

# Questions for TAs
Is it possible to find the zip code of each store or household in the study in order to enrich our analysis with geographical maps?
Is it feasible to webscrape all the nutritional info of the food products on sale in this store, given that they are from very different brands? Is there a centralized dataset for this? (maybe from the FDA)


