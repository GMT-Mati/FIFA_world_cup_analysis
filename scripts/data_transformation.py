def transform_data(matches, players, cups):
    # Create a column for goal difference
    matches['GoalDifference'] = matches['Home Team Goals'] - matches['Away Team Goals']
    
    # Aggregate total goals per World Cup
    total_goals_per_cup = matches.groupby('Year')['Home Team Goals', 'Away Team Goals'].sum().reset_index()
    total_goals_per_cup['Total Goals'] = total_goals_per_cup['Home Team Goals'] + total_goals_per_cup['Away Team Goals']
    
    # Most successful teams
    winning_teams = cups[['Year', 'Winner']].groupby('Winner').count().reset_index()
    winning_teams.columns = ['Team', 'Number of Wins']
    
    return matches, total_goals_per_cup, winning_teams
