import pandas as pd


def load_data():
    matches = pd.read_csv('../data/WorldCupMatches.csv')
    players = pd.read_csv('../data/WorldCupPlayers.csv')
    cups = pd.read_csv('../data/WorldCups.csv')
    return matches, players, cups
