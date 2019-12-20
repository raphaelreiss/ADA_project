
The aim of this project is to find out *hidden* household clusters in the "The Complete Journey" dataset from Dunnhumby company.

The Dunnhumby company process and analyses tonnes of data to improve data-driven businesses knowledge. However, us as group we were not intserested in market targeting but in how using such datasets for **social good**.

With all that transaction-related informations and advanced web scrapping tools, we were able to build a nice prototype which associate calories and nutriments composition to most of sold food product. This technology open a new way of questioning the data to cluster household based on food/drink consumption which was not possible with the default dataset only. This way, we expected finding out meaningful difference between the poorest and richest households consumption habits, between old and young people, etc...

But the dataset is far much richer than food related products. Indeed, we can find huge amount of purchases of daily life such as gasoline (oil) transactions and natality products. Thus, in a second step we enlarged our analysis to detect categories of household based on their overall purchases. We expected that people consumption would demonstrate tendencies related to healthy vs. unhealthy life styles.

Finally we built a graph which.........








# Health and Nutrition
As we saw previously, the food represents a major part of our dataset: an in-depth analysis of this section seemed thus natural to us. Unfortunately, no nutrition values were available in the dataset. We solved this issue by using another dataset coming from the U.S. Department of Agriculture (USDA) which gave us access to a great variety of food products alongst with their respective nutritional values. The challenge consisted mainly in the difference between the article names of the two dataset: for instance, classical onions are called ONIONS SWEET (BULK&BAG) in the dunnhumby dataset, whereas  "Onion, mature raw" in the USDA dataset.

We therefore developped a parser which analyzes the name of the articles present in the dunnhumby dataset and associates them with the most similar USDA articles according to a tailored recursive algorithm.

In addition to that, a second parser was developped in order to extract and standardize the heterogeneous types of weight/volume units for each article.

## An incredible soup
The question is: can we trust our data at this point? Indeed, the parser does not always perform 100% accurately, and some incoherences of the dataset are present as we can see here:


<p align="center">
  <img src="/assets/images_health/banana.png" alt="drawing" width="300"/>
</p>

Most of the bananas items were sold by amount of 40 LB (~ 18kg). A possible hypothesis would be that the Dunnhumby supermarkets do some reselling to smaller markets.
Nevertheless, we persisted, and analyzed the average nutrition profile of what was sold in the dunnhumby dataset by computing the mean of each nutriments weighted by the total bought mass across all transactions and articles. The result looks as follows, displayed alongst with the otimal food intakes as adviced by the National Health Service of UK as a reference and calibrating on the energy intake.
<p align="center">
  <img src="/assets/images_health/soup.png" alt="drawing" width="300"/>
</p>

As we can see, the data looks coherent: for a same intake of energy, the "average soup" does not fall apart of the optimal values.
## A mass of food
First things first, we take a look at the nutritional values of the most consumed articles in terms of mass: it is the occasion to check how well the parser performs by comparing the article and parsed names.

<iframe width="100%" height="650" src="/assets/images_health/Mass_sorted_items.html" /></iframe>

We notice a few things: the eggs and the meat are significantly richer than the other articles in terms of cholesterol while canola and soybean oils look way richer for polyunsaturated fat.

The idea consists now to identify which articles are the most responsible for the mass consumption of a given nutrient: i.e. to find the items which bring the biggest mass of a given nutrient in people's plates.


<iframe width="100%" height="650" src="/assets/images_health/nutrient_responsability.html" /></iframe>

Interestingly, despite the fact that milk contains about 30 times less cholesterol than egg, it ends up being the main source of cholesterol for people due to its massive mass consumption. Overall, dairy and meat represent the main sources.

Concerning energy, basic items as potatoes, sugars and margarine are responsible.


## What people eat
Taking advantage of the rest of the datas, we analyzed the nutritional values by separating classes of customers according to various features. One noticeable trend is represented by the fat consumption which tends to  decrease with the income. To compute theses datas, the households were distributed in 2 classes, low and high income. An indicative p-value of t-test is displayed with the graph: however for the test to be statistically significant, the data should be tested for equal variance, normality and random sampling.

![image](/assets/images_health/cholesterol_pvalue.png)
![image](/assets/images_health/fatty_acids_total_monounsaturated_pvalue.png)
![image](/assets/images_health/fatty_acids_total_polyunsaturated_pvalue.png)
![image](/assets/images_health/total_lipid_pvalue.png)
![image](/assets/images_health/cholesterol_pvalue.png)

This goes along with the lowering of energy costs through technological innovation as described in the "Fat and Sugar: An Economic Analysis" ################TODO ADD CITATION######### and confirms that our parser system performs well overall.

## Average nutriment consumption
A mandatory step consists in defining which type of nutriments are consumed together: this was achieved by computing the correlation matrix of the average nutrients consumption per household between all nutrients (first matrix). However, food items present a natural correlation across nutrients, as different types of fats are usually present together in a given product. In order to counteract this trend, we subtracted the second matrix to the first one in order to identify correlations which are not explained by the natural presence in items, but because people tend to consume them together.

<img src="/assets/images_health/consumption_nutriments_correlation.png" alt="drawing" width="1500"/>

First, we observe that nutrients which are correlated across food items are correlated in average people consumption as well: this goes along with the fact that people can't "separate" the nutrient once an item is bought. Amongst these natural correlations, note the ones between all type of fat.

Then, let's take a look at the correlations that are not explained by items only: the most important one concern protein, cholesterol, sodium, vitamin b-12 and vitamin k. A quick look at the dataset (or a google search) shows that vitamin b-12 is mainly present in meat: this hypothesis goes along with an alimentation mainly based on cheap factorized items and high meat consumption of the occidental diet as described in ######TODO PAPER#######

Our dataset thus definitely present symptoms of malnutrtion at some scale.


## Households Detection
We just saw that with a few data at first look innocent, we can gain suprising insight into people's life using a few data-analysis tools and a bit of time. Does that mean that one should systematically refuse to share his/her data? We think personally answer negatively, as we will see in this section that data science can be used for good as well.
We indeed developped a basic tool where we detect the outliers householdsfor which the average food consumption is abnormal for a specific nutrient using the interquantile-range method: the households are then projected on the 2 first principal components computed on their average nutrition values for sake of visualization. 

<iframe width="100%" height="650" src="/assets/images_health/Outliers_detection.html" /></iframe>

As we 

 This type of method could allow the supermarket (and any middle-range to big-scale company) detecting potential alimentation issues early enough in the life of their customers, and use this type of data to improve and sensitize people to eat in a more healthy manner. This is an example








########################




# Graph of Commodities
Another way of studying what people eat and buy in this study is by looking at the items that are bought together the most.

Perhaps we will confirm that people are likely to buy nachos and dip, or burgers and bacon, etc.

The best way to visualize the relations between items is by depicting a graph where the nodes are the items, and the edges symbolize that they are bought together often.

## Implementation
To do so, all the sales are grouped by shopping carts. Then, for all the shopping carts we looked at the number of times a pair of items appeared together.
We then divide the frequency of the co-ocurrence by the frequency of the highest-frequency item in the pair of items. We can then create a graph by setting a threshold on the minimum
score needed to have an edge.

## Results
Please feel free to zoom in and observe the resulting graph! It's interactive.

<!-- [filename](_media/graph_commodities.html ':include :type=iframe width=100% height=400px') -->


Many interesting groups appear. Most notably there is a strongly connected cluster at the center that has food items such as pasta, sugar, beef, and there are smaller clusters around it, with few
isolated pairs in the atmosphere. Let's look at different features from this graph
### Item Similarity
While the central cluster contains mainly food items, very interesting smaller groups are seen in the surroundings.
* **School Supplies Group**
![School_Supplies_Group](/assets/images_graph/student_supplies.png)
* **Sea food Group**
![Sea_Food_Group](/assets/images_graph/seafood_group.png)
* **Cleaning Products Group**
![Cleaning_Products_Group](/assets/images_graph/cleaning_products_group.png)

### Recipe Discovery
We can also find unrelated items that appear together.  
Perhaps popular recipes contain these items:
* Sweet Potato Dinner Rolls:
![Sweet_potatoes](/assets/images_graph/sweet_potatoes.png)


Perhaps cultural traditions. Let's see:

<script src="//unpkg.com/docsify/lib/plugins/external-script.min.js"></script>






<!-- Html Elements for Search -->
<div id="search-container">
<input type="text" id="search-input" placeholder="<name>...">
<ul id="results-container"></ul>
</div>

<!-- Script pointing to jekyll-search.js -->
<script src="https://unpkg.com/simple-jekyll-search/dest/simple-jekyll-search.min.js"></script>

<script>
      simpleJekyllSearch = new SimpleJekyllSearch({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('results-container'),
        json: 'graph_data.json',
        searchResultTemplate: '<li>{node}::::::{neighbors}</li>',
        noResultsText: 'No results found',
        limit: 10,
        fuzzy: false,
	      exclude: ['neighbors:']
      })
</script>
