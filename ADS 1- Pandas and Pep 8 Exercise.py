# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:45:45 2023
@author: Peter Adedeji
"""

import pandas as pd
import matplotlib.pyplot as plt

# read csv file
countries  = pd.read_csv("countries_top10.csv")
print('\n', countries)

# convert into dataframe
countries_top10 = pd.DataFrame(data=countries, \
                        columns=("Country", "Population",  "Area", "GDP"))
print('\n', countries_top10)

# create new column Population/Area
countries_top10["Population/Area"] = countries_top10["Population"] / \
    countries_top10["Area"]
print('\n', countries_top10)

# create new column of GDP per head
countries_top10["GDP/Population"] = countries_top10["GDP"] / countries["Population"]
print('\n', countries_top10)

# writing into an excel file
countries_top10.to_excel("countries_top10.xlsx")

# read the xlsx file
GDP_2015dollars = pd.read_excel("GDP_2015dollars.xlsx")
print('\n', GDP_2015dollars)

# convert into dataframe
GDP_2015dollars = pd.DataFrame(data=GDP_2015dollars, \
            columns=("Year", "China",  "Germany", "Japan", "United States"))
print('\n', GDP_2015dollars)

# plot all four times series
plt.figure()
plt.plot(GDP_2015dollars["Year"], GDP_2015dollars["China"], ":", label="China")
plt.plot(GDP_2015dollars["Year"], GDP_2015dollars["Germany"], "--", label="Germany")
plt.plot(GDP_2015dollars["Year"], GDP_2015dollars["Japan"], "-.", label="Japan")
plt.plot(GDP_2015dollars["Year"], GDP_2015dollars["United States"], "-", label="United States")
plt.title('Countries/Year')
plt.xlabel("Year")
plt.ylabel("Countries")
plt.legend()

plt.show()

# extract and print data from 2011 to 2020
GDP_2015dollars_2011_2020 = (GDP_2015dollars[41:])
print('\n GDP_2015dollars_2011_2020:\n', GDP_2015dollars_2011_2020)

