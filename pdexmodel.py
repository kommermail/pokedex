#using kpokedex.sqlite, make a bubble plot of pokemon with number of weaknesses on the X axis
#and weight on the Y axis with bubble size being height

import sqlite3
import plotly.express as px
import pandas as pd
import re

conec=sqlite3.connect('kpokedex.sqlite')
cur=conec.cursor()
#Pokemon.name
#put height in here v

data=cur.execute('''SELECT Pokemon.name, Weaknesses.weaknesses_num, Height.ht, Weight.wt 
                FROM Pokemon
                    JOIN Weaknesses
                        ON Weaknesses.id = Pokemon.id
                    JOIN Height
                        ON Height.id = Weaknesses.id
                    JOIN Weight
                        ON Weight.id = Height.id''')

df=pd.DataFrame(data).reset_index(drop=True)

df.columns=['Name','Number of Weaknesses','height','weight']
def convert_to_number(xs):
    #e.g. 16.0 m to 16.0
    return (float(re.sub(r'[^0-9.]', '', xs)))
    
    
df['Height (in m)']=df.height.apply(convert_to_number)
df['Weight (in kg)']=df.weight.apply(convert_to_number)
print(df)

#lambda xs: convert_to_number(xs)
#lambda xs: 1+ convert_to_number(xs)
 

fig=px.scatter(df, x="Number of Weaknesses", y="Weight (in kg)", size="Height (in m)", hover_data="Name")
fig.show()

