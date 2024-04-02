# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import csv files
BCS = pd.read_csv("BCS_ann.csv")
print('\nBarclays:\n', BCS)

BP = pd.read_csv("BP_ann.csv")
print('\nBP:\n', BP)

TSCO = pd.read_csv("TSCO_ann.csv")
print('\nTESCO:\n', TSCO)

VOD = pd.read_csv("VOD_ann.csv")
print('\nVodafone:\n', VOD)

# plot histogram
plt.figure()
plt.subplot(2, 2, 1)  # subplot count starts at 1
plt.hist(BCS['ann_return'], label="Barclays", density=True, color='cyan')
plt.legend()

plt.subplot(2, 2, 2)  # subplot count starts at 2
plt.hist(BP['ann_return'], label="BP", density=True, color='blue')
plt.legend()

plt.subplot(2, 2, 3)  # subplot count starts at 3
plt.hist(TSCO['ann_return'], label="TESCO", density=True, color='red')
plt.legend()

plt.subplot(2, 2, 4)  # subplot count starts at 4
plt.hist(VOD['ann_return'], label ="Vodafone", density=True, color='magenta')
plt.legend()

plt.show()

# take two stocks to create combined histogram
plt.figure()
plt.hist(BP['ann_return'], label="BP", density=True, alpha=0.7)
plt.hist(TSCO['ann_return'], label="TESCO", density=True, alpha=0.6)
plt.legend()
plt.show()

# create a boxplot for return distribution of the four companies
plt.figure()
plt.boxplot([BCS['ann_return'], BP['ann_return'], TSCO['ann_return'], \
             VOD['ann_return']], labels=["Barclays", "BP", "TESCO", "Vodafone"])
plt.show()

# save figure as .png
plt.savefig('Visualisation.png')


# create an array of market capitalisation
market_cap = np.array([33367, 68785, 20979, 29741])
company = ["Barclays", "BP", "TESCO", "Vodafone"]

# plot pie chart for the 4 companies
plt.figure()
plt.pie(market_cap, labels=company)
plt.title("Market Capitalisation (£)")
plt.show()

# market capitalisation as a fraction of total market capitalisation
total_market_cap = 1814000
new_market_cap = market_cap / total_market_cap

# plot pie chart
plt.figure()
plt.pie(new_market_cap, labels=company)
plt.title("New Market Capitalisation (£)")
plt.show()

# create a bar plot
plt.figure()
plt.bar(company, market_cap)
plt.title("Market Capitalisation (£)")
plt.ylabel("Market Cap")
plt.xlabel("Company")
plt.show()
