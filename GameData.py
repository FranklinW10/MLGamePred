from pybaseball import statcast
import pandas as pd

# Get all games on a specific date
data = statcast(start_dt="2024-05-16", end_dt="2024-05-16")

# Group by unique games
grouped = data.groupby(['game_date', 'game_pk', 'home_team', 'away_team'])

# Get final scores
scores = grouped[['home_score', 'away_score']].max().reset_index()

print(scores)