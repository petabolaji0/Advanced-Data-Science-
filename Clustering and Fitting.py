# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from scipy.optimize import curve_fit
from errors import error_prop, covar_to_corr

# Read CSV file
df_pop_data = pd.read_csv('population_growth.csv')
print(df_pop_data)
print(df_pop_data.describe())

# Transpose and clean data
df_world_data = df_pop_data.transpose()
df_world_data.columns = df_world_data.iloc[0]
df_world_data = df_world_data[4:-1]

# Set index as Year
df_world_data.index.names = ["Year"]
print(df_world_data)
print(df_world_data.describe())

# Drop non-numeric columns
numeric_df = df_pop_data.drop(['Country Name', 'Country Code', 
                               'Indicator Name', 'Indicator Code'], axis=1)

# Impute missing values with the mean of the respective columns
imputer = SimpleImputer(strategy='mean')
numeric_df_imputed = pd.DataFrame(imputer.fit_transform(numeric_df),\
                                  columns=numeric_df.columns)

# Clustering
# Perform KMeans clustering
kmeans = KMeans(n_clusters=3).fit(numeric_df_imputed)
df_pop_data['cluster'] = kmeans.labels_

# Plot original data points colored by cluster  
plt.figure(figsize=(10, 6))
for i in range(kmeans.n_clusters):
    cluster_df = df_pop_data[df_pop_data['cluster'] == i]
    plt.scatter(cluster_df.index, cluster_df["1980"], label=f'Cluster {i}')

# Plot cluster centers   
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],\
           marker='x', c='black', label='Centroids')

# Add x-label and y-label
plt.xlabel('Index')
plt.ylabel('Population Growth (1980)')

# Add title and legend
plt.title('KMeans Clustering')
plt.legend()

# Show plot
plt.show()

# Examine the cluster centre
print(kmeans.cluster_centers_)

# Find some example countries in each cluster
for i in range(kmeans.n_clusters):
  print(f'Cluster {i}:') 
  print(df_pop_data[df_pop_data['cluster'] == i]['Country Name'].sample(3).values)
  print('')

# Plot growth trajectories by cluster using scatter plots
fig, axs = plt.subplots(nrows=1, ncols=kmeans.n_clusters, figsize=(16, 5))

for i, ax in enumerate(axs):
    for idx in df_pop_data[df_pop_data['cluster']==i].index:
        years = np.arange(1980, 2021)
        growth_values = df_pop_data.loc[idx][[str(y) for y in range(1980, 2021)]]
        ax.scatter(years, growth_values)

    # Add legend, title, x-label and y-label
    ax.set_title(f'Cluster {i}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population Growth')
    ax.legend()

# Show plot
plt.tight_layout()
plt.show()

# Analyze cluster statistics 
for i in range(kmeans.n_clusters):
  cluster_df = df_pop_data[df_pop_data['cluster']==i]
  
  print(f'Cluster {i} size: {len(cluster_df)}')
  
  pop_1980 = cluster_df['1980'].mean() 
  pop_2020 = cluster_df['2020'].mean()
  
  avg_growth_rate = 100 * (pop_2020 / pop_1980) ** (1 / 40) - 100
  print(f'Cluster {i} avg annual growth rate: {avg_growth_rate:.2f}%')

# Read CSV file
df_co2_emission = pd.read_csv("CO2_emission.csv")
print(df_co2_emission)
print(df_co2_emission.describe())

# Transpose and clean data
df_co2_emission = df_co2_emission.transpose()
df_co2_emission.columns = df_co2_emission.iloc[0]
df_co2_emission = df_co2_emission[4:]

# Set index as Year
df_co2_emission.index.names = ["Year"]
print(df_co2_emission)
print(df_co2_emission.describe())

# Extract data for Argentina
years = np.arange(1990, 2021)
co2_emissions_argentina = df_co2_emission['Argentina']


# Define the exponential model function
def exponential_model(x, a, b, c):
    """ defining a function to create a simple exponential model used for 
    prediction and confidence range """
    return a * np.exp(b * (x - years[0])) + c


# Fit the model to the data
params_exp, covariance_exp = curve_fit(exponential_model, years, 
                                       co2_emissions_argentina, maxfev=2000)

# Predict CO2 emissions for future years (e.g., 2030 and 2040)
future_years = np.array([2030, 2040])
predicted_emissions_exp = exponential_model(future_years, *params_exp)

# Plot the original data and the fitted exponential model
plt.figure(figsize=(10, 6))
plt.plot(years, co2_emissions_argentina, 'o', label='Original Data')
plt.plot(future_years, predicted_emissions_exp, 's', label='Predicted Data')
plt.plot(years, exponential_model(years, *params_exp), label=
         'Fitted Exponential Model')

# Add x-label and y-label
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (kt)')

# Add title and legend
plt.title('CO2 Emissions in Argentina - Fitted Exponential Model')
plt.legend()

# Show plot
plt.show()

# Print values of fitted parameters
print("\n Fitted parameters (a, b, c):\n", params_exp)

# Estimate lower and upper limits of the confidence range
# Calculate 1 sigma error ranges for each parameter
errors = error_prop(years, exponential_model, params_exp, covariance_exp)

# Calculate lower and upper bounds using broadcasting
lower_bound = exponential_model(years, params_exp[0] - errors[0],\
                        params_exp[1] - errors[1], params_exp[2] - errors[2])
upper_bound = exponential_model(years, params_exp[0] + errors[0],\
                        params_exp[1] + errors[1], params_exp[2] + errors[2])

# Plot the original data, the fitted exponential model, and confidence intervals
plt.figure(figsize=(10, 6))
plt.plot(years, co2_emissions_argentina, 'o', label='Original Data')
plt.plot(future_years, predicted_emissions_exp, 's', label='Predicted Data')
plt.plot(years, exponential_model(years, *params_exp), label=
         'Fitted Exponential Model')

# Plot confidence intervals
plt.fill_between(years, lower_bound, upper_bound, color='red', alpha=0.9, 
                 label='Confidence Interval')

# Add x-label, y-label and title
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (kt)')
plt.title(\
 'CO2 Emissions in Argentina(Fitted Exponential Model with Confidence Intervals)')

# Add legend and show plot
plt.legend()
plt.show()

# Print confidence interval
print("\n Confidence Intervals:\n", errors)

# Convert covariance matrix to correlation matrix
correlation_matrix = covar_to_corr(covariance_exp)
print("\n Correlation Matrix:\n", correlation_matrix)