# Motivations

With the increasing space that Information Technologies took in individual daily life, it became soon clear to the governments that
protecting people's numeric life was essential for social cohesion. In this perspective, the European Union adopted in 1995 the [Data Protection Directive](https://en.wikipedia.org/wiki/Data_Protection_Directive) in order to regulate how personal data was processed. This text states that personal data should not be processed at all, except, for instance, if the data subject has given his consent. However, the generalisation of massive personal data collection from credit cards, promotion cards, social medias, etc... made this directive soon outdated. To face privacy issues that the previous directive did not address properly, a new concept was more and more discussed to the European parliament regarding the [Right to be forgotten]("https://en.wikipedia.org/wiki/Right_to_be_forgotten"). This right states that the development of autonomous individual's life must not be *perpetually* dependent of the actions performed in the the past. This right has been formalised in the [General Data Protection Regulation]("https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679") and is applied since the 25th of May 2019.


In this project we aim at giving an **educational and interactive example able to explain to anyone the reasons why he/she should or should not share his/her data.** More specifically, it aims at showing **what kind of information an apparently harmless data collection can bring to a data scientist.**

To try answering this question we used "The Complete Journey" dataset from Dunnhumby which is a company that process and analyses tonnes of data mainly to improve data-driven business knowledge. This dataset is the result of a two year long study over 2500 households aiming at measuring marketing effects over customers. In the objective to bring valuable information for the general interest, we repurposed the marketing initial goal of this study.

Finally, we would like to emphasize the fact that all the information we will deliver here is anonym due to the relatively personal nature of the dataset.



# Health and Nutrition
After a quick look of the data, we saw that the food represented the major part of our entries: an in-depth and exclusive analysis of this section seemed thus necessary to us. Unfortunately, no nutrition values were available in the dataset. We solved this issue by using another dataset coming from the [U.S. Department of Agriculture (USDA)](https://fdc.nal.usda.gov/)  which gave us access to a great variety of food products along with their respective nutritional values. The challenge consisted mainly associating the similar articles of the two datasets based on their name exclusively: for instance, classical onions are called ONIONS SWEET (BULK&BAG) in the dunnhumby dataset, whereas  "Onion, mature raw" in the USDA dataset.

We therefore developped a parser which analyzes the name of the articles present in the dunnhumby dataset and associates them with the most similar USDA articles according to a tailored recursive algorithm.

In addition to that, a second parser was developped in order to extract and standardize the heterogeneous types of weight/volume units for each article.

## An incredible soup
The question is: can we trust our data at this point? Indeed, the parser does not always perform 100% accurately, and some incoherences of the dataset are present as we can see here:


![image](/assets/images_health/banana.png)
<!-- <p align="center">
  <img src="/assets/images_health/banana.png" alt="drawing" width="300"/>
</p> -->

Most of the bananas items were sold by amount of 40 LB (~ 18kg). A possible hypothesis would be that the Dunnhumby supermarkets do some reselling to smaller markets.
Nevertheless, we persisted, and analyzed the average nutrition profile of what was sold in the dunnhumby dataset by computing the mean of each nutriments weighted by the total bought mass across all transactions and articles. The result looks as follows, displayed alongst with the otimal food intakes as adviced by the [National Health Service of UK](https://www.nhs.uk/) as a reference and calibrating on the energy intake.
<!-- <p align="center">
  <img src="/assets/images_health/soup.png" alt="drawing" width="300"/>
</p> -->

![image](/assets/images_health/soup.png)

As we can see, the data looks coherent: for a same intake of energy, the "average soup" does not fall apart of the optimal values.
## A mass of food
First things first, we take a look at the nutritional values of the most consumed articles in terms of mass: it is the occasion to check how well the parser performs by comparing the article and parsed names.

<!-- ![filename](assets/images_health/Mass_sorted_items.html ':include :type=iframe width=100% height=500px') -->
<iframe width="100%" height="650" src="_media/Mass_sorted_items.html" /></iframe>

We notice a few things: the eggs and the meat are significantly richer than the other articles in terms of cholesterol while canola and soybean oils look way richer for polyunsaturated fat.

The idea consists now to identify which articles are the most responsible for the mass consumption of a given nutrient: i.e. to find the items which bring the biggest mass of a given nutrient in people's plates.


<iframe width="100%" height="650" src="_media/nutrient_responsability.html" /></iframe>

Interestingly, despite the fact that milk contains about 30 times less cholesterol than egg, it ends up being the main source of cholesterol for people due to its massive mass consumption. Overall, dairy and meat represent the main sources.

Concerning energy, basic items as potatoes, sugars and margarine are responsible.


## What people eat
Taking advantage of the rest of the datas, we analyzed the nutritional values by separating classes of customers according to various features. One noticeable trend is represented by the fat consumption which tends to  decrease with the income. To compute theses datas, the households were distributed in 2 classes, low and high income by separating the housholds according to their median. An indicative p-value of t-test is displayed with the graph: however for the test to be statistically significant, the data should be tested for equal variance, normality and random sampling.

![image](/assets/images_health/cholesterol_pvalue.png)
![image](/assets/images_health/fatty_acids_total_monounsaturated_pvalue.png)
![image](/assets/images_health/fatty_acids_total_polyunsaturated_pvalue.png)
![image](/assets/images_health/total_lipid_pvalue.png)
![image](/assets/images_health/cholesterol_pvalue.png)

This goes along with the lowering of energy costs through technological innovation as described in the ["Fat and Sugar: An Economic Analysis"(Drewnowski A.) 2003](https://www.ncbi.nlm.nih.gov/pubmed/12612164) and confirms that our parser system performs well overall: all the fat-related nutriments seem to change significantly between the 2 classes.

## Average nutrient consumption
A mandatory step consists in defining which type of nutriments are consumed together: this was achieved by computing the correlation matrix of the average nutrients consumption per household between all nutrients (first matrix). However, food items present a natural correlation across nutrients, as different types of fats are usually present together in a given product. In order to counteract this trend, we subtracted the second matrix to the first one in order to identify correlations which are not explained by the natural presence in items, but because people tend to consume them together.

<img src="/assets/images_health/consumption_nutriments_correlation.png" alt="drawing" width="1500"/>

First, we observe that nutrients which are correlated across food items are correlated in average people consumption as well: this goes along with the fact that people can't "separate" the nutrient once an item is bought. Amongst these natural correlations, note the ones between all type of fat.

Then, let's take a look at the correlations that are not explained by items only: the most important one concern protein, cholesterol, sodium, vitamin b-12 and vitamin k. A quick look at the dataset (or a google search) shows that vitamin b-12 is mainly present in meat: this hypothesis goes along with an alimentation mainly based on cheap factorized items and high meat consumption of the occidental diet as described in [Processed red meat contribution to dietary patterns and the associated cardio-metabolic outcomes.Lenighan YM1, Nugent AP2, Li KF2, Brennan L2, Walton J3, Flynn A3, Roche HM1, McNulty BA2. 2017](https://www.ncbi.nlm.nih.gov/pubmed/28831958)

Our dataset thus definitely present symptoms of malnutrtion at some scale.


## Households Detection
We just saw that with a few data at first look innocent, we can gain suprising insight into people's life using a few data-analysis tools and a bit of time. Does that mean that one should systematically refuse to share his/her data? We think personally answer negatively, as we will see in this section that data science can be used for good as well.
We indeed developped a basic tool where we detect the outliers householdsfor which the average food consumption is abnormal for a specific nutrient using the interquantile-range method: the households are then projected on the 2 first principal components computed on their average nutrition values for sake of visualization.

<iframe width="100%" height="650" src="_media/Outliers_detection.html" /></iframe>

As we can see, the first PC seems strongly correlated with fat and energy in general, while the second one looks more specific to sugar. Taking the strong correlation between fat and cholesterol discovered in the previous section into account, we see that outliers for cholesterol and protein are massively overlapping with the one for fat in general, but don't share much with the sugar, showing that cholesterol/fat/protein and sugars excessive consumptions are two separate issues to tackle differently, at least for extreme consumption.

As expected, the energy outliers overlapp on both fats and sugars.

Once more developped, this type of method could easily allow any supermarket (and middle-range to big-scale company) detecting potential alimentation issues early enough in the life of their customers, and use this type of data to improve and sensitize people to eat in a more healthy manner.

However, the story does not stop here: we adopted a food exclusive point of view so far, but the dataset has other items in general, and therefore other secrets to reveal.






# Clustering households





The second question that came to our mind was trivially if it was possible to group households based on what they consume the most. Since the number of purchasable items from the store is high (~2400) we needed to perform dimensionality reduction to turn them into groups. So we performed basic clustering algorithms computing the total sales items per household.



>## Dimensionality reduction
*Technical:* we created a "bag-of-words" analogue and performed a single-value-decomposition keeping only 300 abstract features. This created household vs. group and a group vs. item matrices. We also used TF-IDF normalisation to reduce the importance of the articles bought frequently by every household.


After performing dimensionality reduction, we observed groups of purchased items, and we tried to label them with keywords representing these items.
The chosen items are as follows. The following list shows the label, together with the items of top score per group. 
* 1. **Gasoline**: GASOLINE-REG UNLEADED (0.97)	BEERALEMALT (0.15), SOFT DRINKS (0.05),... 
    * We can see this group contains a high score in gasoline compared to the next items. This group is the top group from SVD, so we thought it was important to explain the varaince of the data.
* 2. **Liquor and Cigarettes**: BEERALEMALT LIQUORS (0.75)	CIGARETTES(0.47)	AUSTRALIAN/NZ WINES (0.04) VALUE GLASS WINE(0.04) PREMIUM 750ML WINES (0.04)...
    * We can see this group contains liquor and cigerette items.
* 3. **Baby items**: BABY DIAPERS(0.95)	INFANT FORMULA MILK BASE (0.40), BEERALEMALT LIQUORS (0.25)	INFANT FORMULA SPECIALTY(0.16)
    * Even though this group contains beer as the third item, its weight is much smaller compared to the first 2. Also, the consecutive items are all related to babies.
* 4. **Premium Items**: FRZN SS PREMIUM ENTREES/DNRS/N (0.8)	CIGARETTES (0.15)	PREMIUM BREAD(0.1) PREMIUM 750ML WINES (0.09)
    * These are discounted items that are in promotion.
* 5. **Soft Drinks**: SOFT DRINKS 12/18&15PK CAN CAR(0.3)	SOFT DRINKS 20PK&24PK CAN CARB (0.2)	FRZN SS PREMIUM ENTREES/DNRS/N(0.1)
    * Soft drinks are very recurrent in this group

Now households can be compared amongst these groups instead of a huge list of items. From these groups we chose the most meaningful ones which were used to cluster households.

>## Kmeans
**Technical:** We chose the optimal number of cluster by calculating the silhouette coefficient for each possible cluster number and taking the highest one. The groups obtained by kmeans clustering appear to be well separated if we plot them with the 3 groups that explain most of the variance.

<!-- <img src="/assets/images_hh_groups/kmeans_nb_of_clusters.png" alt="Optimal_number_k_" style="zoom:50%;float: left; margin-right: 10px;" /> -->


<!-- <img src="/assets/images_hh_groups/3d_scatter_plot_of_groups.png" alt="Optimal_number_k_" width="700" class="center"> -->





<!--<p align="center">
  <img src="/assets/images_hh_groups/scatter_matrix_kmeans_labels.png" alt="draw" width="600">
</p>-->

<iframe width="80%" height="450" src="_media/kmeans_clusters.html" /></iframe>




| Color         |  Group                  |  Description                  
| ------------- |:-----------------------:|:-----------------------:
| Red           |  New Parents            |  High in Baby Items and low on cigarettes.            
| Blue          |  Drivers                |  High in Gasoline.              
| Green         |  Passive consumers      |  Low in all groups and high on premium items (not shown here)      
| Yellow        |  Smokers and Drinkers   |  High in cigarettes and liquor and low on baby items (thankfully)


This analysis shows that we can profile households based on their purchases by very little effort without needing to manually classify the purchased items. The next step is to see how these clusters relate to the known demographic data.


## Demographics

### Household Age Distribution
The following graph shows the distribution of the age groups with respect to the clusters. The y axis corresponds to the fraction of households of the group.
<iframe width="100%" height="450" src="_media/Age_distributions.html" /></iframe>

* Drivers: Even though there is not large correlation with age, the age group with the largest amount of drivers is the age of 35-45.
* Passive Consumers: We see that the group is largest at older ages. This is expected since old people are probably less interested in buying things.
* Drinkers and Smokers: Not large correlation, but we see that the maximum proportion of households is observed at the younger ages.
* New parents: As expected, most of the new parents occur at the age of 25-34, and there's no new parents older than 54. 
A more detailed analysis of the demographic composition of our cluster seems to confirm this hypothesis. Here, the demographic distributions are shown for each group to enable to get a better sense of their respective demographic compositions.

### Household Size Distribution
The following graph shows the distribution of the household size with respect to the clusters.
<iframe width="100%" height="450" src="_media/Family_size_distributions.html" /></iframe>

* Drivers: No visual correlation.
* Passive Consumers: No visual correlation.
* Drinkers and Smokers: Interstingly the proportion of drinkers and smokers seems to increase with household size. 
* New parents: Houses with 2 members have the largest fraction of new parents. We see that the fraction decreases with an increasing household size as expected. 



########################




# What Do Transactions Say About Items?
Now that we have seen all the information that can be found about users and their consumer habits, we can also see what information we can find about items themselves.
Another way of studying what people eat and buy in this study is by looking at the items that are bought together the most.
Perhaps we will confirm that people are likely to buy nachos and dip, or burgers and bacon, etc.

The best way to visualize the relations between items is by depicting a graph where the nodes are the items, and the edges symbolize that they are bought together often.

## Implementation
To do so, all the sales are grouped by shopping carts. Then, for all the shopping carts we looked at the number of times a pair of items appeared together.
We then divide the frequency of the co-ocurrence by the frequency of the most popular item (highest frequency) in the pair. We can then create a graph by setting a threshold on the minimum
similarity score needed to have an edge.

## Item Similarity Based on Co-Ocurrence in Shopping Carts:
The following graph depicts the resulting item similarity from their co-ocurrence. The size of the nodes represents the frequency of the item.
If you hover your mouse on the item, you can see the specific number of times it appeared in all the shopping carts.

Feel free to play with the physics package (controls are under the graph)!  

The spring constant of the edges represents the weight of the edges.

[graph](_media/graph_commodities.html ':include :type=iframe width=100% height=500px')


Many interesting groups appear. Most notably there is a strongly connected cluster at the center that has food items such as pasta, sugar, beef, and there are smaller clusters around it, with few
isolated pairs orbitating in the atmosphere. Let's look at different features from this graph

### Item Similarity
While the central cluster contains mainly food items, very interesting smaller groups are seen in the surroundings.
* **Sea food Group**
![image]("assets/images_graph/seafood_groups.png")
 <img src="/assets/images_health/seafood_groups.png" alt="sea food group" width="400px"/>
<!-- what's wrong with this???-->

* **Cleaning Products Group**
 <img src="/assets/images_health/cleaning_groups.png" alt="cleaning group" width="400px"/>


* **Gasoline Group**
 <img src="/assets/images_health/gasoline_group.png" alt="gasoline group" width="400px"/>

But there's many many more groups. Can you find some more?
### Recipe Discovery
Sometimes unrelated products are observed, but after googling, we realize these correspond to recipes:
* **Sweet Potato Dinner Rolls**
 <img src="/assets/images_health/sweet_potato_v2.png" alt="Sweet_potatoes" width="400px"/>

* **Mushroom Gravy**
 <img src="/assets/images_health/mushroom_gravy_combo.png" alt="Mushroom_Gravy" height="400px"/>

* **Pina Colada**
<img src="/assets/images_health/pina_colada.png" alt="Pina_Colada" width="400px"/>

## Item Importance
We can rank items based on how connected they are. The following figure shows the degree distribution of the graph:
<img src="/assets/images_health/degree_distribution1.png" alt="deg distribution" width="400"/>

We see that while most items have only one neighbor, there is a group of items with 20-40 neighbors.

The following figure shows what these most connected components are on the top plot,
and these are compared with the most popular items on the bottom plot:
<img src="/assets/images_health/degree_freq_distribution.png" alt="top degree" width="400"/>

We see that the most of the connected items are not very healthy items such as snacks and canned foods.
It is interesting to see that the most popular items, such as milk or bananas are not the most connected items in the graph.
The reason for this is that the most connected items in the graph correspond to the items that relative to their abundance, appear always together with the same items.
Therefore, it is understandable why unhealthy items are probably always bought by the same households.
This corroborates the finding that in the present dataset that fatty and salty items are consumed together.

# Conclusion
The powers of data are elucidated in this project: just starting with transaction data and assuming zero knowledge on the items or the buyers themselves, 
we were able to get incredible insight on people's health, who they are, and what they consume. First, we analyzed the nutrient consumption 
by doing some natural language processing and web-scrapping. We found that fat consumption seems to be higher than the recommended intake for the aggregate community, 
and for the lower income groups it is even higher. 
Second, using the total sales value of every item bought by the households, we grouped items 
and clustered households with respect to how they consumed these groups. The clusters studied were the group of drivers, smokers and drinkers, passive consumers and new parents. 
Even though the analysis done is at a very general level, it shows the exposure of people's privacy and potentially sensitive information from a seemingly harmless gathering of data. Nevertheless, 
this gathering of data also allows us to draw interesting links between the items being bought. 
These links range from trivial/obvious relations such as the one between pears-bananas,
to much deeper relations such as the one between tequila and salt, which serve as echos of the underlying culture.  