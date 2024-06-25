def clean_data(matches, players, cups):
    # Drop missing values
    matches.dropna(inplace=True)
    players.dropna(inplace=True)
    cups.dropna(inplace=True)
    
    # Convert date columns to datetime
    matches['Datetime'] = pd.to_datetime(matches['Datetime'])
    
    # Remove duplicates
    matches.drop_duplicates(inplace=True)
    players.drop_duplicates(inplace=True)
    cups.drop_duplicates(inplace=True)
    
    return matches, players, cups
