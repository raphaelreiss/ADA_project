# Motivations

With the increasing space that Information Technologies took in individual daily life, it became soon clear to the governments that
protecting people's numeric life was essential for social cohesion. In this perspective, the European Union adopted in 1995 the [Data Protection Directive](https://en.wikipedia.org/wiki/Data_Protection_Directive) in order to regulate how personal data was processed. This text states that personal data should not be processed at all, except, for instance, if the data subject has given his consent. However, the generalisation of massive personal data collection from credit cards, promotion cards, social medias, etc... made this directive soon outdated. To face privacy issues that the previous directive did not address properly, a new concept was more and more discussed to the European parliament regarding the [Right to be forgotten]("https://en.wikipedia.org/wiki/Right_to_be_forgotten"). This right states that the development of autonomous individual's life must not be *perpetually* dependent of the actions performed in the the past. This right has been formalised in the [General Data Protection Regulation]("https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679") and is applied since the 25th of May 2019.


In this project we aim at giving an **educational and interactive example able to explain to anyone the reasons why he/she should or should not share his/her data.** More specifically, it aims at showing **what kind of information an apparently harmless data collection can bring to a data scientist.**

To try answering this question we used "The Complete Journey" dataset from Dunnhumby which is a company that process and analyses tonnes of data mainly to improve data-driven business knowledge. This dataset is the result of a two year long study over 2500 households aiming at measuring marketing effects over customers. In the objective to bring valuable information for the general interest, we repurposed the marketing initial goal of this study.

Finally, we would like to emphasize the fact that all the information we will deliver here is anonym due to the relatively personal nature of the dataset.


# Exploitation


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
<iframe width="100%" height="650" src="/assets/images_health/Mass_sorted_items.html" /></iframe>

We notice a few things: the eggs and the meat are significantly richer than the other articles in terms of cholesterol while canola and soybean oils look way richer for polyunsaturated fat.

The idea consists now to identify which articles are the most responsible for the mass consumption of a given nutrient: i.e. to find the items which bring the biggest mass of a given nutrient in people's plates.


<iframe width="100%" height="650" src="/assets/images_health/nutrient_responsability.html" /></iframe>

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

## Average nutriment consumption
A mandatory step consists in defining which type of nutriments are consumed together: this was achieved by computing the correlation matrix of the average nutrients consumption per household between all nutrients (first matrix). However, food items present a natural correlation across nutrients, as different types of fats are usually present together in a given product. In order to counteract this trend, we subtracted the second matrix to the first one in order to identify correlations which are not explained by the natural presence in items, but because people tend to consume them together.

<img src="/assets/images_health/consumption_nutriments_correlation.png" alt="drawing" width="1500"/>

First, we observe that nutrients which are correlated across food items are correlated in average people consumption as well: this goes along with the fact that people can't "separate" the nutrient once an item is bought. Amongst these natural correlations, note the ones between all type of fat.

Then, let's take a look at the correlations that are not explained by items only: the most important one concern protein, cholesterol, sodium, vitamin b-12 and vitamin k. A quick look at the dataset (or a google search) shows that vitamin b-12 is mainly present in meat: this hypothesis goes along with an alimentation mainly based on cheap factorized items and high meat consumption of the occidental diet as described in [Processed red meat contribution to dietary patterns and the associated cardio-metabolic outcomes.Lenighan YM1, Nugent AP2, Li KF2, Brennan L2, Walton J3, Flynn A3, Roche HM1, McNulty BA2. 2017](https://www.ncbi.nlm.nih.gov/pubmed/28831958)

Our dataset thus definitely present symptoms of malnutrtion at some scale.


## Households Detection
We just saw that with a few data at first look innocent, we can gain suprising insight into people's life using a few data-analysis tools and a bit of time. Does that mean that one should systematically refuse to share his/her data? We think personally answer negatively, as we will see in this section that data science can be used for good as well.
We indeed developped a basic tool where we detect the outliers householdsfor which the average food consumption is abnormal for a specific nutrient using the interquantile-range method: the households are then projected on the 2 first principal components computed on their average nutrition values for sake of visualization.

<iframe width="100%" height="650" src="/assets/images_health/Outliers_detection.html" /></iframe>

As we can see, the first PC seems strongly correlated with fat and energy in general, while the second one looks more specific to sugar. Taking the strong correlation between fat and cholesterol discovered in the previous section into account, we see that outliers for cholesterol and protein are massively overlapping with the one for fat in general, but don't share much with the sugar, showing that cholesterol/fat/protein and sugars excessive consumptions are two separate issues to tackle differently, at least for extreme consumption.

As expected, the energy outliers overlapp on both fats and sugars.

Once more developped, this type of method could easily allow any supermarket (and middle-range to big-scale company) detecting potential alimentation issues early enough in the life of their customers, and use this type of data to improve and sensitize people to eat in a more healthy manner.

However, the story does not stop here: we adopted a food exclusive point of view so far, but the dataset has other items in general, and therefore other secrets to reveal.






# Clustering households





The second question that came to our mind was trivially if it was possible to group households based on what they consume the most. Since the number of purchasable items from the store is high (~2400) we needed to perform dimensionality reduction to turn them into groups. So we performed basic clustering algorithms computing the total sales items per household.



>## Dimensionality reduction
*Technical:* we created a "bag-of-words" analogue and performed a single-value-decomposition keeping only 300 abstract features. This created household vs. group and a group vs. item matrices. We also used TF-IDF normalisation to reduce the importance of the articles bought frequently by every household.


After performing dimensionality reduction, we observed groups of purchased items, and we tried to label them with keywords representing these items.
The chosen items are as follows. The following list shows the label, together with the items of top score.
* Gasoline: GASOLINE-REG UNLEADED (0.97)	BEERALEMALT (0.15), soft drinks (0.05) We can see this group contains a high score in gasoline compared to the next groups
* Liquor and Cigarettes: BEERALEMALT LIQUORS	CIGARETTES	AUSTRALIAN/NZ WINES
* Baby items: BABY DIAPERS(0.95)	INFANT FORMULA MILK BASE (0.40)	BEERALEMALT LIQUORS(0.05)
* Premium Items: FRZN SS PREMIUM ENTREES/DNRS/N (0.8)	CIGARETTES (0.15)	YOGURT NOT MULTI-PACKS (0.05)
* Soft Drinks: SOFT DRINKS 12/18&15PK CAN CAR(0.3)	SOFT DRINKS 20PK&24PK CAN CARB (0.2)	FRZN SS PREMIUM ENTREES/DNRS/N(0.1)

Now households can be compared amongst these groups instead of a huge list of items. From these groups we chose the most meaningful ones which were used to cluster households.

>## Kmeans
**Technical:** We chose the optimal number of cluster by calculating the silhouette coefficient for each possible cluster number and taking the highest one. The groups obtained by kmeans clustering appear to be well separated if we plot them with the 3 groups that explain most of the variance.

<!-- <img src="/assets/images_hh_groups/kmeans_nb_of_clusters.png" alt="Optimal_number_k_" style="zoom:50%;float: left; margin-right: 10px;" /> -->


<img src="/assets/images_hh_groups/3d_scatter_plot_of_groups.png" alt="Optimal_number_k_" width="700" class="center">





<p align="center">
  <img src="/assets/images_hh_groups/scatter_matrix_kmeans_labels.png" alt="draw" width="600">
</p>
[filename](_media/kmeans_clusters.html ':include')




| Color         |  Group                  |
| ------------- |:-----------------------:|
| Red           |  Late night snacks      |
| Blue          |  Gasoline group         |
| Green         |  Cigs & liquor          |
| Yellow        |  Baby items             |
| Cyan          |  Soft drinks            |


We see that even though some clusters overlap we see that clusters are representative:

There is a blue group
* Blue: Gasoline group: gasoline consumption clearly higher than all other groups, But there is significant separation with the late night snacks group, which indicates that people who come to buy gasoline often also get food. Some overlapp with cigs & liquors and baby items.

* Red: Late night snackers: Also buy gasoline but barely anything else, also some overlap with soft drinks and baby items

* Green: Smokers and Drinkers: medium snacks and high gasoline

* Yellow: Responsible Drivers : also consume snacks, medium consumption of cigarettes and liquor!

* Magenta: Dinner: Clearly stands out for high gasoline, cigarettes and liquor consumption

* Cyan: Soft drinks: Very diffuse/ sparse group, Indicates that the households in this group have a very varied consumption of items in other groups. Suggests that soft drinks appeal to a very large demographic group



From the distributions we see that the gasoline group is strongly skewed to the right, approximately follows a heavy tailed distribution and all the values are positive, which means that all the households consume from this group. Liquor and cigarettes and Late night snacks have similar distributions skewed to the left, meaning that most people do not buy from these groups.

Another reason why there are not more specific individual patterns emerging from this analysis is that all our transaction data is at the household level and the composition of a household can be very heterogeneous, so we would almost certainly find other more granular consumption patterns with individual transaction data.

Also, the shopping card might only be used for the weekly grocery shopping but the individual members of a household might go to the store for smaller transactions without using the card, as it may remain with a single person.

## Demographics



A more detailed analysis of the demographic composition of our cluster seems to confirm this hypothesis. Here, the demographic distributions are shown for each group to enable to get a better sense of their respective demographic compositions.

<img src="/assets/images_hh_groups/demo_distr_dummy.png" alt="Optimal_number_k_" style="zoom:65%;" />

 Indeed, even tough the products purchased by the different groups are vastly different, think of baby items versus cigarettes and wine, he most representative individual of each group has exactly the same age, income and lives in a household of the same size. It is however interesting to note that these parameters differ significantly from the US median demographic parameters.


| age          |	income |	household | size |
|--------------|:-------:|:----------:|----- |
|Gasoline      |	45-54  |	50-74K    | 	2  |
|Late snacks   |	45-54  |	35-49K 	  |  2   |
|Cigs & liquor |	45-54  |	50-74K 	  |  2   |
|US population |	38.2 	 |  32K 	    | 2.6  |



Also, observing the distribution of the demographic parameters visually in the clusters do not yield explicit groups. The households appear to be randomly distributed.

<img src="/assets/images_hh_groups/demographic_grps_dummy.png" alt="Optimal_number_k_" style="zoom:72%;" />

To summarise, our clustering approach to discover household groups who have similar consumption patterns yielded many different groups that focus on different item categories. However, the explained variance of this approach was not very high and the groups were mainly overshadowed by the enormous gasoline consumption. One interesting aspect uncovered is that unhealthy eating habbits such as soft drinks and alcohol consumption are widespread among these household.  

In the next part, we will take a closer look at food consumption among different population subgroups.


















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

![filename](_media/graph_commodities.html ':include :type=iframe width=100% height=500px')


Many interesting groups appear. Most notably there is a strongly connected cluster at the center that has food items such as pasta, sugar, beef, and there are smaller clusters around it, with few
isolated pairs orbitating in the atmosphere. Let's look at different features from this graph

### Item Similarity
While the central cluster contains mainly food items, very interesting smaller groups are seen in the surroundings.
* **Sea food Group**
 <img src="/assets/images_graph/seafood_groups.png" alt="sea food group" width="500"/>


* **Cleaning Products Group**
 <img src="/assets/images_graph/cleaning_groups.png" alt="cleaning group" width="300"/>


* **Gasoline Group**
 <img src="/assets/images_graph/gasoline_group.PNG" alt="gasoline group" width="500"/>

But there's many many more groups. Can you find some more?
### Recipe Discovery
Sometimes unrelated products are observed, but after googling, we realize these correspond to recipes:
* **Sweet Potato Dinner Rolls**
 <img src="/assets/images_graph/sweet_potato_v2.PNG" alt="Sweet_potatoes" width="400"/>

* **Mushroom Gravy**
 <img src="/assets/images_graph/mushroom_gravy_combo.PNG" alt="Mushroom_Gravy" height="400"/>

* **Pina Colada**
<img src="/assets/images_graph/pina_colada.PNG" alt="Pina_Colada" width="400"/>

## Item Importance
We can rank items based on how connected they are. The following figure shows the degree distribution of the graph:
<img src="/assets/images_graph/degree_distribution1.png" alt="deg distribution" width="400"/>

We see that while most items have only one neighbor, there is a group of items with 20-40 neighbors.

The following figure shows what these most connected components are on the top plot,
and these are compared with the most popular items on the bottom plot:
<img src="/assets/images_graph/degree_freq_distribution.png" alt="top degree" width="400"/>

We see that the most of the connected items are not very healthy items such as snacks and canned foods.
It is interesting to see that the most popular items, such as milk or bananas are not the most connected items in the graph.
The reason for this is that the most connected items in the graph correspond to the items that relative to their abundance, appear always together with the same items.
Therefore, it is understandable why unhealthy items are probably always bought by the same households.
This corroborates the finding that in the present dataset that fatty and salty items are consumed together.

# Conclusion
We indeed saw through the nutriton project that data analysis could be used for good, if handled properly. On another hand, consumers should really be aware of the personnal data gathered on their behalf, and know what type of products big companies developp based on these precious values. We hope that this project helped you  to understand that.
