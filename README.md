# portfolio

This is a collection of projects I have done recently.  There are three: Pokemon Size vs Weaknesses of Pokemon, Multiple Linear Regression Notebook, and World Bank SciTech Data Analysis.  

In Pokemon Size vs Weaknesses of Pokemon (see 'kpokedex.sqlite', 'pdexjson.json', 'pdexmodel.py', and 'pokemon.py',) I downloaded data on Pokemon (fantasy creatures) in JSON format, took the parts I needed, and loaded it into a database using Python.  Then, I plot the points on a bubble chart to show the sizes and weaknesses of pokemon.  This bubble chart also shows each Pokemon's name and their height.  This bubble chart shows us that most pokemon have around 3 weaknesses, and are below 150kg.  The next visualization is a histogram of the larger than normal pokemon.  We see that most of these pokemon are 2-3m in height, and it is equally likely for these pokemon to have 3 or 4 weaknesses.  Three pokemon out of the larger pokemon have 6 or 7 weaknesses.  Looking at the next three visualizations of pokemon smaller than 1m, we can see that there are about 4 pokemon out of this larger amount of datapoints that have 6 or 7 weaknesses.  This shows that while size of pokemon doesn't dictate how many weaknesses they have, a large pokemon is more likely to have a lot of weaknesses.  See '.png' files for a preview of each visualization.

For the Multiple Linear Regression project (see 'multiple-linear-regression.ipynb'), Multiple Linear Regression is explained and I show the relationship between sales and three types of advertising: TV, newspaper, and radio.  I show things like the pearson correlation of these data, and use a little machine learning with scikit-learn and yellowbrick to decide whether to keep newspaper in the model.

In the World Bank SciTech Data Analysis (see 'statspyran.ipynb'), I use the science_tech_2009 and science_tech_2018 CSV datasets.  First, I clean the data, dropping any N/A values, then, I get to exploring the data, which is important to see if there are tons of outliers, which there are in certain categories.  After that, I use my knowledge of the data to filter it so it only shows the normal data and not the outliers.  More pearson correlations, and then to some scatter plots for visualization of this data.  Using T-Tests, I calculate if the change in data from 2009 to 2018 was statistically significant using p-values.
