# ADA_project: You are what you eat

File to correct: **TermProject.ipynb**

The whole data story was deployed and is accessible [here](https://raphaelreis.github.io/ADA_project/#/)


!!Since we had troubles with github-pages that did not want to show the plotly figures, we must ask you two do some manipulation!!:

We basically used docsify to run the website:


```bash
sudo npm i docsify-cli -g
cd docs/
docsify serve
```




## Abstract

In this project, we aim to tell a comprehensive and sometimes surprisingly detailed story regarding the identity of participants in a survey on shopping habits. We believe that despite their anonymity, we are able to acquaint ourselves with the individuals behind these transactions. Here we illustrate our process, whereby observation of subjects’ behaviour on multiple levels and analysis of sample parameters, from macro-trends all the way down to specific individual consumption patterns, enable us to gain such insight.

## Research questions

### 1. Research questions
   #### 1.1: Influence of demographic factors on shopping habits.

Cluster the households into 6 meaningful groups using kmeans after applying SVD of the matrix of counts of items bought per household. This analysis allows us to answer the following questions:

  * How is income related to shopping habits?

  * How is age related to shopping habits?

  * How is the size of household, or the family structure related to shopping habits?

  #### 1.2: Analysis and identification of unhealthy shopping habits.

	- Calculation of the total consumption of nutrients
	- Computation the average nutrient content of the food items consumed by a single household
	- Identification of consumption patterns depending on demographic factors
	- Analysis of correlating nutrients
	- Identification of outliers

  #### 1.3: Time series analysis

	-  Calculation of alcohol content per transaction 

  * Detection of alcoholic behavior by regular purchases over extended periods of time

  #### 1.4: What items are purchased together

 -   Creation of a weighted graph based of frequency of simaltaneous purchase of items
 -  Identification of meaningful groups, ie: ingredients for recipes 

### 2. Creating Useful Tools
  #### 2.1: Scrapping of nutritional information to detect trends and anomalies in the consumption of various nutrients

  #### 


## Usage of additional datasets
- Dataset with nutritional facts of food items sold: Nutritional info dataset to be able to calculate the food consumption for each household and compare it against recommended amount, while taking demographics into account


All chosen datasets are not too large in order to be able to perform most of the computations on personal computers.
