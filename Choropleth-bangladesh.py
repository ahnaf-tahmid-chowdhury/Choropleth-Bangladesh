# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Plotting Choropleth Bangladesh Map using Python
# ---
# A choropleth map is a type of thematic map in which areas are shaded or patterned in proportion to a statistical variable that represents an aggregate summary of a geographic characteristic within each area, such as population density or per-capita income.
# 
# %% [markdown]
# Load all districts from geojson file

# %%
from json import load
bd_districts=load(open('bangladesh_geojson_adm2_64_districts_zillas.json','r'))

# %% [markdown]
# Lets check all keys available in geojson file

# %%
bd_districts['features'][61].keys()


# %%
bd_districts["features"][61]['properties']

# %% [markdown]
# To get population info from wikipedia we can use pandas read_html module

# %%
import pandas as pd
dfs= pd.read_html('https://en.wikipedia.org/wiki/Districts_of_Bangladesh')

# %% [markdown]
# In the website there are many tables available. These are stored in list format. We can check the lenth and by selecting the correct index we can get our required table.

# %%
print("No of lists are:",len(dfs))

# %% [markdown]
# Store data as csv format for offline use

# %%
for i in range(len(dfs)):
    a = "Population (thousands)[28]" in dfs[i]
    if a == True:
        df=dfs[i].to_csv("Districts_of_Bangladesh.csv")
    

# %% [markdown]
# Storing csv data into a dataframe

# %%
df=pd.read_csv("Districts_of_Bangladesh.csv")

# %% [markdown]
# Checking dataframe head

# %%
df.head()

# %% [markdown]
# Removing District string from each row as geojson data do not have this district level after each district name.

# %%
df.District


# %%
df.District = df.District.apply(lambda x: x.replace(" District",""))
    


# %%
df.District

# %% [markdown]
# Now it is the time to map this dataframe with geojson file. For this we have to Index the district name for each dataframe. However, we can label a specific id for each district.

# %%
district_id_map = {}
for feature in bd_districts["features"]:
    feature["id"] = feature["id"]
    district_id_map[feature["properties"]["ADM2_EN"]] = feature["id"]


# %%
district_id_map

# %% [markdown]
# Merge both dataframe according to id

# %%
df['id'] = df.District.apply(lambda x: district_id_map[x])

# %% [markdown]
# Now we can see an id column in the dataframe

# %%
df.head()

# %% [markdown]
# Renaming columns for looking good

# %%
df = df.rename(columns={
    'Population (thousands)[28]' : 'Population (thousands)',
    'Area (km2)[28]' : 'Area (km2)' })

# %% [markdown]
# A bar plot can be used to show population level in each district

# %%
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

color = cm.inferno_r(np.linspace(.3, .7, 64))
df = df.set_index('District')
fig = plt.figure(figsize=(20,10)).add_subplot(1,1,1)
fig.bar(df.index, df["Population (thousands)"],color=color)
fig.set_xticklabels(df.index,
                        rotation=90,
                        fontsize='7',
                        )
fig.set_title("Population level in each district")
fig.set_ylabel('Population (thousands)')
plt.show()

# %% [markdown]
# Now lets make choropleth map of Bangladesh with population density

# %%
import plotly.express as px
import plotly.io as pio
#pio.renderers.default = 'vscode'


# %%
fig = px.choropleth(
    df,
    locations='id',
    geojson=bd_districts,
    color='Population (thousands)',
    title='Bangladesh Population',
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()

# %% [markdown]
# As Dhaka has the most population, this part looks yellow. But others are not showing well as these locations have very few population against Dhaka. However, we can make log scale to solve the issue.

# %%
df['Population scale'] = np.log10(df['Population (thousands)'])

# %% [markdown]
# Now, dataframe has new column named "Population scale"

# %%
df.head()

# %% [markdown]
# Changing color to 'Population scale' and adding hover_name with hover_data the we can get a more informative graph.

# %%
fig = px.choropleth(
    df,
    locations='id',
    geojson=bd_districts,
    color='Population scale',
    hover_name='Bengali',
    hover_data=['Population (thousands)','Area (km2)'],
    title='Bangladesh Population'
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()

# %% [markdown]
# Customizing choropleth graph with mapbox looks more better.

# %%
fig=px.choropleth_mapbox(df,
        locations='id',
        geojson=bd_districts,
        color='Population scale',
        hover_name='Bengali',
        hover_data=['Population (thousands)','Area (km2)'],
        title='Bangladesh Population',
        mapbox_style='carto-positron',
        center= { 'lat' : 23.6850, 'lon' : 90.3563},
        zoom=4.8,
        opacity=0.6)
fig.show()

