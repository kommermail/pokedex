#using kpokedex.sqlite, analyze the relationship between number
#of weaknesses and size of pokemon.

import sqlite3
import plotly.express as px
import pandas as pd
import re

#establish connection to database
conec=sqlite3.connect('kpokedex.sqlite')
cur=conec.cursor()

#extract data from database
allpkmn=cur.execute('''SELECT Pokemon.name, Weaknesses.weaknesses_num, Height.ht, Weight.wt 
                FROM Pokemon
                    JOIN Weaknesses
                        ON Weaknesses.id = Pokemon.id
                    JOIN Height
                        ON Height.id = Weaknesses.id
                    JOIN Weight
                        ON Weight.id = Height.id''')

#load into pkmndf
pkmndf=pd.DataFrame(allpkmn).reset_index(drop=True)

#set column names for use in plotly
pkmndf.columns=['Name','Number of Weaknesses','height','weight']

#data is in string form. use convert function
def convert_to_number(xs):
    #e.g. 16.0 m to 16.0
    return (float(re.sub(r'[^0-9.]', '', xs)))
    
    
pkmndf['Height (in m)']=pkmndf.height.apply(convert_to_number)
pkmndf['Weight (in kg)']=pkmndf.weight.apply(convert_to_number)

#bigboypkmn will be same data filtered for big boys, or pokemon larger than a large human
bigboypkmn=cur.execute('''SELECT Pokemon.name, Weaknesses.weaknesses_num, Height.ht, Weight.wt 
                FROM Pokemon
                    JOIN Weaknesses
                        ON Weaknesses.id = Pokemon.id
                    JOIN Height
                        ON Height.id = Weaknesses.id
                    JOIN Weight
                        ON Weight.id = Height.id WHERE ht>'1.84m';''')

bigpkmndf=pd.DataFrame(bigboypkmn)
bigpkmndf.columns=['Name','Number of Weaknesses','height','weight']
bigpkmndf['Height (in m)']=bigpkmndf.height.apply(convert_to_number)
bigpkmndf['Weight (in kg)']=bigpkmndf.weight.apply(convert_to_number)
 
#use plotly for analysis: bubble plot, histogram, and density heatmap.

fig=px.scatter(pkmndf, x="Number of Weaknesses", y="Weight (in kg)", size="Height (in m)", hover_data="Name")
fig.show()

fig2=px.histogram(data_frame=bigpkmndf, x="Height (in m)", color="Number of Weaknesses")
fig2.show()

fig3=px.density_heatmap(data_frame=bigpkmndf, x="Number of Weaknesses", y="Height (in m)", nbinsx=5, nbinsy=10)
fig3.show()
