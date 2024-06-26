def transform_data(matches, players, cups):
    # Calculate total goals per cup
    matches['Total Goals'] = matches['Home Team Goals'] + matches['Away Team Goals']
    total_goals_per_cup = matches.groupby('Year')['Total Goals'].sum().reset_index()

    # Calculate most successful teams
    winning_teams = cups.groupby('Winner').size().reset_index(name='Number of Wins')
    winning_teams = winning_teams.sort_values(by='Number of Wins', ascending=False)

    return matches, total_goals_per_cup, winning_teams
