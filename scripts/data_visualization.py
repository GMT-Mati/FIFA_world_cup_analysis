import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_goals(total_goals_per_cup):
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Year', y='Total Goals', data=total_goals_per_cup)
    plt.title('Total Goals per World Cup')
    plt.xlabel('Year')
    plt.ylabel('Total Goals')
    plt.show()

def plot_most_successful_teams(winning_teams):
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Number of Wins', y='Team', data=winning_teams.sort_values(by='Number of Wins', ascending=False))
    plt.title('Most Successful Teams in World Cup History')
    plt.xlabel('Number of Wins')
    plt.ylabel('Team')
    plt.show()

def plot_goal_difference_distribution(matches):
    plt.figure(figsize=(14, 7))
    sns.histplot(matches['GoalDifference'], bins=20, kde=True)
    plt.title('Distribution of Goal Differences in World Cup Matches')
    plt.xlabel('Goal Difference')
    plt.ylabel('Frequency')
    plt.show()
