import pandas as pd


def clean_data(matches, players, cups):
    # Cleaning Matches DataFrame
    matches['Datetime'] = pd.to_datetime(matches['Datetime'], errors='coerce')
    matches = matches.dropna(subset=['Datetime']).copy()
    matches['Datetime'] = matches['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    matches.fillna({
        'Home Team Name': 'Unknown',
        'Away Team Name': 'Unknown',
        'Home Team Goals': 0,
        'Away Team Goals': 0,
        'Win conditions': 'None',
        'Attendance': 0,
        'Half-time Home Goals': 0,
        'Half-time Away Goals': 0,
        'Referee': 'Unknown',
        'Assistant 1': 'Unknown',
        'Assistant 2': 'Unknown',
        'RoundID': 0,
        'MatchID': 0,
        'Home Team Initials': 'UNK',
        'Away Team Initials': 'UNK'
    }, inplace=True)

    matches.drop_duplicates(inplace=True)

    # Cleaning Players DataFrame
    players.fillna({
        'Coach Name': 'Unknown',
        'Line-up': 'Unknown',
        'Shirt Number': 0,
        'Player Name': 'Unknown',
        'Position': 'Unknown',
        'Event': 'None'
    }, inplace=True)

    # Merge players with matches to get the Year column
    players = players.merge(matches[['MatchID', 'Year']], how='left', on='MatchID')
    players.drop_duplicates(inplace=True)

    # Cleaning Cups DataFrame
    cups.fillna({
        'Country': 'Unknown',
        'Winner': 'Unknown',
        'Runners-Up': 'Unknown',
        'Third': 'Unknown',
        'Fourth': 'Unknown',
        'GoalsScored': 0,
        'QualifiedTeams': 0,
        'MatchesPlayed': 0,
        'Attendance': 0
    }, inplace=True)
    cups.drop_duplicates(inplace=True)

    return matches, players, cups
