import matplotlib.pyplot as plt
import seaborn as sns


def plot_total_goals(total_goals_per_cup):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Year', y='Total Goals', data=total_goals_per_cup)
    plt.title('Total Goals per World Cup')
    plt.xlabel('Year')
    plt.ylabel('Total Goals')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def plot_goal_difference_distribution(matches):
    plt.figure(figsize=(10, 6))
    sns.histplot(matches['GoalDifference'], bins=20, kde=True)
    plt.title('Goal Difference Distribution')
    plt.xlabel('Goal Difference')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_most_successful_teams(winning_teams):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Number of Wins', y='Winner', data=winning_teams, hue='Winner', dodge=False, palette='viridis')
    plt.title('Most Successful Teams in World Cup History')
    plt.xlabel('Number of Wins')
    plt.ylabel('Team')
    plt.legend([],[], frameon=False)
    plt.tight_layout()
    plt.show()


def plot_top_goal_scorers(players, year):
    # Use the correct column name for goals
    top_scorers = players[players['Year'] == year].groupby('Player Name')['Goals Scored'].sum().reset_index()
    top_scorers = top_scorers.sort_values(by='Goals Scored', ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Goals Scored', y='Player Name', data=top_scorers, palette='viridis')
    plt.title(f'Top 10 Goal Scorers in {year}')
    plt.xlabel('Goals Scored')
    plt.ylabel('Player Name')
    plt.tight_layout()
    plt.show()


def plot_goals_by_teams_over_time(matches):
    goals_by_team = matches.groupby(['Year', 'Home Team Name'])['Home Team Goals'].sum().reset_index()
    goals_by_team = goals_by_team.rename(columns={'Home Team Name': 'Team', 'Home Team Goals': 'Goals'})

    plt.figure(figsize=(14, 8))
    sns.lineplot(x='Year', y='Goals', hue='Team', data=goals_by_team)
    plt.title('Goals Scored by Teams Over Time')
    plt.xlabel('Year')
    plt.ylabel('Goals')
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    plt.show()


def plot_host_countries_performance(cups):
    host_performance = cups.groupby('Country')['Winner'].count().reset_index().rename(columns={'Winner': 'Wins'})

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Wins', y='Country', data=host_performance, orient='h')
    plt.title('Performance of Host Countries in World Cup')
    plt.xlabel('Wins')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()


def plot_average_goals_per_match(cups):
    cups['Average Goals per Match'] = cups['GoalsScored'] / cups['MatchesPlayed']

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Average Goals per Match', data=cups)
    plt.title('Average Goals per Match in Each World Cup')
    plt.xlabel('Year')
    plt.ylabel('Average Goals per Match')
    plt.tight_layout()
    plt.show()


def plot_match_results_heatmap(matches):
    results_pivot = matches.pivot_table(index='Home Team Name', columns='Away Team Name', values='Home Team Goals',
                                        aggfunc='count', fill_value=0)

    plt.figure(figsize=(12, 10))
    sns.heatmap(results_pivot, cmap='Blues', annot=True, fmt='d')
    plt.title('Heatmap of Match Results')
    plt.xlabel('Away Team')
    plt.ylabel('Home Team')
    plt.tight_layout()
    plt.show()
