# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:35:18 2023
@author: pc
"""
# Import standard math and graphics library
import pandas as pd
import matplotlib.pyplot as plt

# Import data from a csv file
df_matches = pd.read_csv('wc_matches.csv')

# Create a line plot for cummulative goals of Team 1 vs Team 2
# Get cumulative goals for each team
team1_goals = df_matches.groupby('team1')['score1'].cumsum()
team2_goals = df_matches.groupby('team2')['score2'].cumsum()

# Create line plot
plt.plot(team1_goals, label='Team 1', color='blue')
plt.plot(team2_goals, label='Team 2', color='red')

# Add labels and legend
plt.xlabel('Matches Played')
plt.ylabel('Cumulative Goals')
plt.title('Cumulative Goals per Match')
plt.legend()

# Save and show plot
plt.savefig('Line plot.jpeg')
plt.show()

# Use a bar chart to determine the highest scoring team
# Get goals scored by each team
team_goals = df_matches.groupby('team1')['score1'].sum() \
                + df_matches.groupby('team2')['score2'].sum() 

# Sort values in descending order
team_goals = team_goals.sort_values(ascending=False)

# Create bar chart
plt.bar(team_goals.index, team_goals.values, color='blue', width=0.7)

# Add title and label
plt.xlabel('Teams')
plt.ylabel('Goals Scored')
plt.xticks(rotation=90)
plt.title('Goals scored by each Team')

# Save and show plot
plt.savefig('Bar chart.jpeg')
plt.show()

# Use a pie chart to show goals scored by the top 5 highest scoring teams
# Get total goals for each team
team_goals = df_matches.groupby('team1')['score1'].sum() \
                    + df_matches.groupby('team2')['score2'].sum()

# Get the top 5 teams with the highest goals
top5_teams = team_goals.nlargest(5)

# Get percentage of goals scored by each top 5 team
total_top5 = top5_teams.sum()
percentage = (top5_teams / total_top5) * 100

# Create pie chart
plt.pie(percentage, labels=top5_teams.index, autopct='%d%%')
plt.title("% of Goals Scored by Top 5 Teams")

# Save and show plot
plt.savefig('Pie chart.jpeg')
plt.show()