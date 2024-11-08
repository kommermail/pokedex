# portfolio

This is a collection of projects I have done recently.  There are three: pokedex, multiple linear regression, and World Bank SciTech Data Analysis.  

In Pokedex (see 'kpokedex.sqlite', 'pdexjson.json', 'pdexmodel.py', and 'pokemon.py',) I take data on Pokemon (fantasy creatures) in JSON format and load it into a database using Python.  Then, I plot the points on a bubble chart to show the sizes and weaknesses of pokemon.  See 'exeggutorisbig.png' for a preview of what the chart will look like.  

For the Multiple Linear Regression project (see 'multiple-linear-regression.ipynb'), Multiple Linear Regression is explained and I show the relationship between sales and three types of advertising: TV, newspaper, and radio.  I show things like the pearson correlation of these data, and use a little machine learning with scikit-learn and yellowbrick to decide whether to keep newspaper in the model.

In the World Bank SciTech Data Analysis (see 'statspyran.ipynb'), I use the science_tech_2009 and science_tech_2018 CSV datasets.  First, I clean the data, dropping any N/A values, then, I get to exploring the data, which is important to see if there are tons of outliers, which there are in certain categories.  After that, I use my knowledge of the data to filter it so it only shows the normal data and not the outliers.  More pearson correlations, and then to some scatter plots for visualization of this data.  Using T-Tests, I calculate if the change in data from 2009 to 2018 was statistically significant using p-values.
