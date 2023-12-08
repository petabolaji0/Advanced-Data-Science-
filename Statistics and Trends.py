# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Define function and manipulate/clean data
def Popular_Indicators(Popular_indicators):
    """
    define a function which takes the filename as argument, reads a dataframe 
    and returns two dataframes: one with years as columns and the other with 
    countries as columns
    """
    # Import csv file
    df_popular_ind = pd.read_csv("Popular_indicators.csv")

    # Print dataframe 1 with column = country name
    print('\nPopular Indicators:\n', df_popular_ind.head())

    # Transpose the dataframe
    df_pop_ind = df_popular_ind.transpose()

    # Set column
    df_pop_ind.columns = df_pop_ind.iloc[0]

    # Rename index/rows to Year
    df_pop_ind.index.names = ["Year"]

    # Print dataframe 2 with column = year
    print('\nPopular Indicators:\n', df_pop_ind.head())

    return df_pop_ind, df_popular_ind


# Load and process data
df_pop_ind, df_popular_ind = Popular_Indicators('df_popular_indicators')


# Display summary statistics
# Filter data for selected countries
selected_countries = ["Argentina", "India", "Nigeria", "Saudi Arabia"]
selected_df = df_popular_ind[df_popular_ind["Country Name"].isin(selected_countries)]


# Display summary statistics using .describe()
summary_stats = selected_df.groupby(['Country Name']).describe()
print("Summary Statistics:\n", summary_stats)

# Other statistical methods
# 1. Average
average_values = selected_df.groupby(['Country Name']).mean()
print("\nAverage Values:\n", average_values)

# 2. Median
median_values = selected_df.groupby(['Country Name']).median()
print("\nMedian Values:\n", median_values)

# 3. Variance
variance_values = selected_df.groupby(['Country Name']).var()
print("\nVariance Values:\n", variance_values)

# 4. Correlation
corr_values = selected_df.groupby(['Country Name']).corr()
print("\n Correlation Values:\n", corr_values)

# Skewness
skew_value = selected_df.groupby(['Country Name']).skew()
print("\n Skewness Values:\n", skew_value)

# Time series plot
# Filter data for the population density indicator
population_density_data = df_popular_ind[df_popular_ind['Series Name'] ==\
                        'Population density (people per sq. km of land area)']

# Set 'Country Name' as the index for better grouping
population_density_data.set_index('Country Name', inplace=True)

# Transpose the data for easier plotting
population_density_data = population_density_data.transpose()

# Convert the data to numeric type
population_density_data = population_density_data.apply(pd.to_numeric,\
                                                        errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Loop through each country and plot its population density over time
for country in population_density_data.columns:
    plt.plot(population_density_data.index, population_density_data[country], label=country)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population Density (people per sq. km of land area)')
plt.title('Population Density Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()

# Filter data for the agricultural land indicator
agricultural_land_data = df_popular_ind[df_popular_ind['Series Name'] ==\
                                'Agricultural land (% of land area)']

# Set 'Country Name' as the index for better grouping
agricultural_land_data.set_index('Country Name', inplace=True)

# Transpose the data for easier plotting
agricultural_land_data = agricultural_land_data.transpose()

# Convert the data to numeric type
agricultural_land_data = agricultural_land_data.apply(pd.to_numeric,\
                                                      errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Loop through each country and plot its agricultural land over time
for country in agricultural_land_data.columns:
    plt.plot(agricultural_land_data.index,agricultural_land_data[country],\
             label=country)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Agricultural Land (% of land area)')
plt.title('Agricultural Land Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()

# Filter data for the arable land indicator
arable_land_data = df_popular_ind[df_popular_ind['Series Name']==\
                          'Arable land (% of land area)']

# Set 'Country Name' as the index for better grouping
arable_land_data.set_index('Country Name', inplace=True)

# Transpose the data for easier plotting
arable_land_data = arable_land_data.transpose()

# Convert the data to numeric type
arable_land_data = arable_land_data.apply(pd.to_numeric, errors='coerce')

# Plotting
plt.figure(figsize=(12, 8))

# Loop through each country and plot its arable land over time
for country in arable_land_data.columns:
    plt.plot(arable_land_data.index, arable_land_data[country], label=country)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Arable Land (% of land area)')
plt.title('Arable Land Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()

# Correlation heatmap
# Filter data for Argentina
argentina_data = df_popular_ind[df_popular_ind['Country Name'] == 'Argentina']

# Select relevant indicators
selected_indicators = ['Population density (people per sq. km of land area)',\
                       'Agricultural land (% of land area)', 'Arable land (% of land area)']

# Set 'Series Name' as the index for better grouping
argentina_data.set_index('Series Name', inplace=True)

# Filter data for selected indicators
argentina_data = argentina_data.loc[selected_indicators]

# Transpose the data for easier plotting
argentina_data = argentina_data.transpose()

# Convert the data to numeric type
argentina_data = argentina_data.apply(pd.to_numeric, errors='coerce')

# Plotting correlation matrix
correlation_matrix = argentina_data.corr()

# Plotting heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', linewidths=0.5)
plt.title('Correlation Matrix for Indicators in Argentina')
plt.show()

# Filter data for India
india_data = df_popular_ind[df_popular_ind['Country Name'] == 'India']

# Select relevant indicators
selected_indicators = ['Population density (people per sq. km of land area)',\
                       'Agricultural land (% of land area)', 'Arable land (% of land area)']

# Set 'Series Name' as the index for better grouping
india_data.set_index('Series Name', inplace=True)

# Filter data for selected indicators
india_data = india_data.loc[selected_indicators]

# Transpose the data for easier plotting
india_data = india_data.transpose()

# Convert the data to numeric type
india_data = india_data.apply(pd.to_numeric, errors='coerce')

# Plotting correlation matrix
correlation_matrix = india_data.corr()

# Plotting heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix for Indicators in India')
plt.show()

# Filter data for Nigeria
nigeria_data = df_popular_ind[df_popular_ind['Country Name'] == 'Nigeria']

# Select relevant indicators
selected_indicators = ['Population density (people per sq. km of land area)',\
                       'Agricultural land (% of land area)', 'Arable land (% of land area)']

# Set 'Series Name' as the index for better grouping
nigeria_data.set_index('Series Name', inplace=True)

# Filter data for selected indicators
nigeria_data = nigeria_data.loc[selected_indicators]

# Transpose the data for easier plotting
nigeria_data = nigeria_data.transpose()

# Convert the data to numeric type
nigeria_data = nigeria_data.apply(pd.to_numeric, errors='coerce')

# Plotting correlation matrix
correlation_matrix = nigeria_data.corr()

# Plotting heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Greens', linewidths=0.5)
plt.title('Correlation Matrix for Indicators in Nigeria')
plt.show()

# Filter data for Saudi Arabia
saudi_arabia_data = df_popular_ind[df_popular_ind['Country Name'] == 'Saudi Arabia']

# Select relevant indicators
selected_indicators = ['Population density (people per sq. km of land area)',\
                       'Agricultural land (% of land area)', 'Arable land (% of land area)']

# Set 'Series Name' as the index for better grouping
saudi_arabia_data.set_index('Series Name', inplace=True)

# Filter data for selected indicators
saudi_arabia_data = saudi_arabia_data.loc[selected_indicators]

# Transpose the data for easier plotting
saudi_arabia_data = saudi_arabia_data.transpose()

# Convert the data to numeric type
saudi_arabia_data = saudi_arabia_data.apply(pd.to_numeric, errors='coerce')

# Plotting correlation matrix
correlation_matrix = saudi_arabia_data.corr()

# Plotting heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Oranges', linewidths=0.5)
plt.title('Correlation Matrix for Indicators in Saudi Arabia')
plt.show()