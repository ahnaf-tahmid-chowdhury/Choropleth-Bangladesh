# Population density of Bangladesh according to district 
---
1. The current population of Bangladesh is 166,387,872 as of Friday, July 16, 2021, based on Worldometer elaboration of the latest United Nations data.
2. Bangladesh 2020 population is estimated at 164,689,383 people at mid year according to UN data.
3. Bangladesh population is equivalent to 2.11% of the total world population.
4. Bangladesh ranks number 8 in the list of countries (and dependencies) by population.
5. The population density in Bangladesh is 1265 per Km2 (3,277 people per mi2).
6. The total land area is 130,170 Km2 (50,259 sq. miles)

## Plotting Choropleth Bangladesh Map
---
A choropleth map is a type of thematic map in which areas are shaded or patterned in proportion to a statistical variable that represents an aggregate summary of a geographic characteristic within each area, such as population density or per-capita income.


<p align="center">
  <a href="" rel="noopener">
 <img src="https://github.com/ahnaf-tahmid-chowdhury/Choropleth-Bangladesh/blob/master/image.png" alt="Map logo"></a>
</p>

## Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting_started)
- [Process](#process)

## About <a name = "about"></a>

A choropleth map is a type of thematic map in which areas are shaded or patterned in proportion to a statistical variable that represents an aggregate summary of a geographic characteristic within each area, such as population density or per-capita income.


## Prerequisites <a name = "prerequisites"></a>

What things you need to install the software and how to install them.

```
$ pip install plotly
$ pip install notebook
$ pip install numpy
$ pip install matplotlib
$ pip install pandas
```

A step by step process who the geojson data is collected described here

[Geojson files](https://github.com/yasserius/bangladesh_geojson_shapefile)


## Getting Started <a name = "getting_started"></a>

After installing all recomanded tools run <b>Choropleth-bangladesh.ipynb</b> file to get started

### Process <a name = "process"></a>
- At first the district based geojson data is loaded
- Collected population data from Wikipedia and saved as csv format
- Load them to pandas dataframe
- Marge two dataset according to district using an unique id
- Plot choropleth map of Bangladesh