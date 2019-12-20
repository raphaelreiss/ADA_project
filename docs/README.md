
With the increasing space that Information Technologies took in individual daily life, it became soon clear to the governments that
protecting people's numeric life was essential for social cohesion. In this perspective, the European Union adopted in 1995 the [Data Protection Directive](https://en.wikipedia.org/wiki/Data_Protection_Directive) in order to regulate how personal data was processed. This text states that personal data should not be processed at all, except, for instance, if the data subject has given his consent. However, the generalisation of massive personal data collection from credit cards, promotion cards, social medias, etc... made this directive soon outdated. To face privacy issues that the previous directive did not address properly, a new concept was more and more discussed to the European parliament regarding the [Right to be forgotten]("https://en.wikipedia.org/wiki/Right_to_be_forgotten"). This right states that the development of autonomous individual's life must not be *perpetually* dependent of the actions performed in the the past. This right has been formalised in the [General Data Protection Regulation]("https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679").

In this project we aimed at illustrate the importance of such laws in our interconnected world tackling the following question: **What kind of information a *harmless data collection* can bring to a data scientist ?** In the following work, we don't take into account any moral aspect. By this, we are saying what is possible to know and not if it is moral or not to do so.  




The aim of this project is to find out *hidden* household clusters in the "The Complete Journey" dataset from Dunnhumby company.

The Dunnhumby company process and analyses tonnes of data to improve data-driven businesses knowledge. However, us as group we were not intserested in market targeting but in how using such datasets for **social good**.

With all that transaction-related informations and advanced web scrapping tools, we were able to build a nice prototype which associate calories and nutriments composition to most of sold food product. This technology open a new way of questioning the data to cluster household based on food/drink consumption which was not possible with the default dataset only. This way, we expected finding out meaningful difference between the poorest and richest households consumption habits, between old and young people, etc...

But the dataset is far much richer than food related products. Indeed, we can find huge amount of purchases of daily life such as gasoline (oil) transactions and natality products. Thus, in a second step we enlarged our analysis to detect categories of household based on their overall purchases. We expected that people consumption would demonstrate tendencies related to healthy vs. unhealthy life styles.

Finally we built a graph which.........



# Data


The data we use for this project is taken from the Dunnhumby data science company.
Inside we find a two years long study over 2500 households who are frequent shoppers
at a specific retailer brand. In the dataset we can also find interesting information
about the household demographic and marketing contact history.

This dataset was initially proposed for academic research to study the effect of
direct marketing to customers. But we, as a group, were interested in repurposing
the dataset for social good.




########


## Introduction

The goal of this section is to group households based on what they consume the most. In order to get better insight into the households in our dataset, we decided to group them using k-means clustering. We computed the number of times each household has ever bought a specific item. Since the number of purchasable items at the stores is about 2400, it is very difficult to cluster the households based on their bought items. We need to do a dimensionality reduction on the bought items, and turn them into groups. To do so, we will create a **bag of words** analogue, which we call **bag of commodities**. Then we will do SVD, where keep 300 features. We get a **household vs. group** , and a **group vs. item** matrix describing all the groups in terms of items. We applied TF-IDF normalisation in order to reduce the importance of the articles bought frequently by almost every household.  

We can then take the household vs. group matrix and find k-means clusters.  

Finally we can find if there is any relation between these clusters and the demographic data.  
The results show that there are groups of items often bought together, such as baby items or wine and cigarettes. However, the groups that overshadowed all others was the gasoline group, as it is the most bought item overall by far.

## Kmeans

We chose the optimal number of cluster by calculating the silhouette coefficient for each possible cluster number and taking the highest one.

<img src="/assets/images_hh_groups/kmeans_nb_of_clusters.png" alt="Optimal_number_k_" style="zoom:50%;float: left; margin-right: 10px;" />



The groups obtained by kmeans clustering appear to be well separated if we plot them with the 3 groups that explain most of the variance.

<img src="/assets/images_hh_groups/3d_scatter_plot_of_groups.png" alt="Optimal_number_k_" style="zoom:72%; float: right; margin-right: 10px;" />

In order to get a more detailed view, we use the scatter plot matrix. We indeed see that the three first categories explain most of the variance because the groups are clearly separated along these axis. The gasoline group, in red is clearly separated from all others. This is a particularity of the shopping habbits of these households. Indeed, as it was shown before, gasoline is the highest bought item by sales value by far.

Another interesting point is that the soft drinks group does not seem to have specific consumption patterns in the other groups, rather, it seems to include households from all the other groups indiscriminantely. This makes sense, as soft drinks are consumed by people from a very broad demographic and there are also many variants of soft drinks marketed towards different demographics.

<img src="/assets/images_hh_groups/scatter_matrix_kmeans_labels.png" alt="Optimal_number_k_" style="zoom:72%;" />

We see that even though some clusters overlap we see that clusters are representative:

* Red: Gasoline group: gasoline consumption clearly higher than all other groups, But there is significant separation with the late night snacks group, which indicates that people who come to buy gasoline often also get food. Some overlapp with cigs & liquors and baby items.

* Blue: Late night snacks: Also buy gasoline but barely anything else, also some overlap with soft drinks and baby items

* Green: Cigs & liquor: medium snacks and high gasoline

* Yellow: Baby items: also consume snacks, medium consumption of cigarettes and liquor!

* Magenta: Dinner: Clearly stands out for high gasoline, cigarettes and liquor consumption

* Cyan: Soft drinks: Very diffuse/ sparse group, Indicates that the households in this group have a very varied consumption of items in other groups. Suggests that soft drinks appeal to a very large demographic group



From the distributions we see that the gasoline group is strongly skewed to the right, approximately follows a heavy tailed distribution and all the values are positive, which means that all the households consume from this group. Liquor and cigarettes and Late night snacks have similar distributions skewed to the left, meaning that most people do not buy from these groups.

Another reason why there are not more specific individual patterns emerging from this analysis is that all our transaction data is at the household level and the composition of a household can be very heterogeneous, so we would almost certainly find other more granular consumption patterns with individual transaction data.

Also, the shopping card might only be used for the weekly grocery shopping but the individual members of a household might go to the store for smaller transactions without using the card, as it may remain with a single person.

## Demographics



A more detailed analysis of the demographic composition of our cluster seems to confirm this hypothesis. Here, the demographic distributions are shown for each group to enable to get a better sense of their respective demographic compositions.

<img src="/assets/images_hh_groups/demo_distr_dummy.png" alt="Optimal_number_k_" style="zoom:65%;" />

 Indeed, even tough the products purchased by the different groups are vastly different, think of baby items versus cigarettes and wine, he most representative individual of each group has exactly the same age, income and lives in a household of the same size. It is however interesting to note that these parameters differ significantly from the US median demographic parameters.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>income</th>
      <th>household size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gasoline</td>
      <td>45-54</td>
      <td>50-74K</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Late snacks</td>
      <td>45-54</td>
      <td>35-49K</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Cigs &amp; liquor</td>
      <td>45-54</td>
      <td>50-74K</td>
      <td>2</td>
    </tr>
    <tr>
      <td>US population</td>
      <td>38.2</td>
      <td>32K</td>
      <td>2.6</td>
    </tr>
  </tbody>
</table>

Also, observing the distribution of the demographic parameters visually in the clusters do not yield explicit groups. The households appear to be randomly distributed.

<img src="/assets/images_hh_groups/demographic_grps_dummy.png" alt="Optimal_number_k_" style="zoom:72%;" />

To summarise, our clustering approach to discover household groups who have similar consumption patterns yielded many different groups that focus on different item categories. However, the explained variance of this approach was not very high and the groups were mainly overshadowed by the enormous gasoline consumption. One interesting aspect uncovered is that unhealthy eating habbits such as soft drinks and alcohol consumption are widespread among these household.  

In the next part, we will take a closer look at food consumption among different population subgroups.


















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
