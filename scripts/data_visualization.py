import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_goals(total_goals_per_cup):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Year', y='Total Goals', data=total_goals_per_cup, palette='viridis', hue='Year', dodge=False)
    plt.legend([],[], frameon=False)
    plt.title('Total Goals per World Cup')
    plt.xlabel('Year')
    plt.ylabel('Total Goals')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_most_successful_teams(winning_teams):
    top_winning_teams = winning_teams.head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Number of Wins', y='Winner', data=top_winning_teams, palette='viridis', hue='Winner', dodge=False)
    plt.legend([],[], frameon=False)
    plt.title('Most Successful Teams in World Cup History')
    plt.xlabel('Number of Wins')
    plt.ylabel('Team')
    plt.tight_layout()
    plt.show()

def plot_goal_difference_distribution(matches):
    matches['Goal Difference'] = matches['Home Team Goals'] - matches['Away Team Goals']
    plt.figure(figsize=(12, 6))
    sns.histplot(matches['Goal Difference'], bins=20, kde=True, color='purple')
    plt.title('Goal Difference Distribution')
    plt.xlabel('Goal Difference')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_top_goal_scorers(players, year):
    if 'Goals Scored' not in players.columns:
        print(f"Column 'Goals Scored' not found in the players DataFrame.")
        return
    top_scorers = players[players['Year'] == year].groupby('Player Name')['Goals Scored'].sum().reset_index()
    top_scorers = top_scorers.sort_values(by='Goals Scored', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Goals Scored', y='Player Name', data=top_scorers, palette='viridis', hue='Player Name', dodge=False)
    plt.legend([],[], frameon=False)
    plt.title(f'Top Goal Scorers in {year} World Cup')
    plt.xlabel('Goals Scored')
    plt.ylabel('Player')
    plt.tight_layout()
    plt.show()

def plot_goals_by_teams_over_time(matches):
    team_goals = matches.groupby(['Year', 'Home Team Name'])['Home Team Goals'].sum().reset_index()
    team_goals = team_goals.rename(columns={'Home Team Name': 'Team', 'Home Team Goals': 'Goals'})
    away_goals = matches.groupby(['Year', 'Away Team Name'])['Away Team Goals'].sum().reset_index()
    away_goals = away_goals.rename(columns={'Away Team Name': 'Team', 'Away Team Goals': 'Goals'})
    total_goals = pd.concat([team_goals, away_goals]).groupby(['Year', 'Team']).sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Year', y='Goals', hue='Team', data=total_goals, palette='tab20', marker='o')
    plt.title('Goals by Teams Over Time')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_host_countries_performance(cups):
    host_performance = cups[['Country', 'Winner', 'Year']].copy()
    host_performance['Host Wins'] = (host_performance['Country'] == host_performance['Winner']).astype(int)
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Year', y='Host Wins', hue='Country', data=host_performance)
    plt.title('Performance of Host Countries')
    plt.xlabel('Year')
    plt.ylabel('Host Wins')
    plt.tight_layout()
    plt.show()

def plot_average_goals_per_match(cups):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Year', y='Average Goals per Match', data=cups, palette='viridis', hue='Year', dodge=False)
    plt.legend([],[], frameon=False)
    plt.title('Average Goals per Match in World Cups')
    plt.xlabel('Year')
    plt.ylabel('Average Goals per Match')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_match_results_heatmap(matches):
    match_results = matches.pivot_table(index='Home Team Name', columns='Away Team Name', values='Home Team Goals', aggfunc='count')
    plt.figure(figsize=(14, 10))
    sns.heatmap(match_results, cmap='viridis', annot=True, fmt='.1f', linewidths=.5)
    plt.title('Match Results Heatmap')
    plt.tight_layout()
    plt.show()
