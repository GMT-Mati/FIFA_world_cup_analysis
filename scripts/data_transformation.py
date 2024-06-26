def transform_data(matches, players, cups):
    # Calculate Goal Difference
    matches['GoalDifference'] = abs(matches['Home Team Goals'] - matches['Away Team Goals'])

    # Total goals per cup
    total_goals_per_cup = matches.groupby('Year')[['Home Team Goals', 'Away Team Goals']].sum().reset_index()
    total_goals_per_cup['Total Goals'] = total_goals_per_cup['Home Team Goals'] + total_goals_per_cup['Away Team Goals']

    # Winning teams
    winning_teams = cups[['Year', 'Winner']].value_counts().reset_index(name='Number of Wins')
    winning_teams.rename(columns={'Winner': 'Team'}, inplace=True)

    return matches, total_goals_per_cup, winning_teams
