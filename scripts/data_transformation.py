import pandas as pd


def transform_data(matches, players, cups):
    # Total goals per cup
    total_goals_per_cup = matches.groupby('Year')[['Home Team Goals', 'Away Team Goals']].sum().reset_index()
    total_goals_per_cup['Total Goals'] = total_goals_per_cup['Home Team Goals'] + total_goals_per_cup['Away Team Goals']

    # Most successful teams (using cups data)
    winning_teams = cups['Winner'].value_counts().reset_index()
    winning_teams.columns = ['Winner', 'Number of Wins']

    # Goal difference calculation
    matches['GoalDifference'] = abs(matches['Home Team Goals'] - matches['Away Team Goals'])

    # Calculate goals scored by players
    players['Goals Scored'] = players['Event'].apply(lambda x: str(x).count('G'))
    players['Yellow Cards'] = players['Event'].apply(lambda x: str(x).count('Y'))
    players['Red Cards'] = players['Event'].apply(lambda x: str(x).count('R'))

    # Calculate average goals per match
    cups['Average Goals per Match'] = cups['GoalsScored'] / cups['MatchesPlayed']

    return matches, total_goals_per_cup, winning_teams, cups
