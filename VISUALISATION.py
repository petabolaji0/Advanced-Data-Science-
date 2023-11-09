# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:35:18 2023
@author: Peter Adedeji
"""

# Import standard math and graphics library
import pandas as pd
import matplotlib.pyplot as plt


def cummualative_team_goals(team1_goals, team2_goals):
    """
    define a function to calculate cumulative sum of goals scored during
    the tournamnent.
    """
    # Import data from a csv file
    df_matches = pd.read_csv('wc_matches.csv')

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

    # Set x-axis limit
    plt.xlim(0, 63)

    # Save and show plot
    plt.savefig('Lineplot.jpg')
    plt.show()
    return(team1_goals, team2_goals)


# Create a line plot for cummulative goals of Team 1 vs Team 2
cummualative_team_goals('team1_goals', 'team2_goals')


def total_goals(team_goals):
    """
    define a function to calculate the total goals scored by each country at
    the tournament.
    """
    # Import data from a csv file
    df_matches = pd.read_csv('wc_matches.csv')

    team_goals = df_matches.groupby('team1')['score1'].sum() \
        + df_matches.groupby('team2')['score2'].sum()

    # Sort values in descending order
    team_goals = team_goals.sort_values(ascending=False)

    # Create bar chart
    plt.bar(team_goals.index, team_goals.values, color='blue', width=0.7)

    # Add title and label
    plt.xlabel('Countries')
    plt.ylabel('Goals Scored')
    plt.xticks(rotation=90)
    plt.title('Goals scored by each Country')

    # Save and show plot
    plt.savefig('Barchart.jpg')
    plt.show()
    return(team_goals)


# Use a bar chart to show goals scored by each country
total_goals('team_goals')


def top5_team_goals(team_goals):
    """
    define a function to determine the top 5 teams with the highest goals
    """
    # Import data from a csv file
    df_matches = pd.read_csv('wc_matches.csv')

    team_goals = df_matches.groupby('team1')['score1'].sum() \
        + df_matches.groupby('team2')['score2'].sum()

    # top 5 team with highest goals
    top5_teams = team_goals.nlargest(5)

    # Get percentage of goals scored by each top 5 team
    total_top5 = top5_teams.sum()
    percentage = (top5_teams / total_top5) * 100

    # Create pie chart
    plt.pie(percentage, labels=top5_teams.index, autopct='%d%%')

    # Add title
    plt.title("% of Goals Scored by Top 5 Teams")

    # Save and show plot
    plt.savefig('Piechart.jpg')
    plt.show()
    return(team_goals)


# Use a pie chart to show goals scored by the top 5 highest scoring teams
top5_team_goals('team_goals')
