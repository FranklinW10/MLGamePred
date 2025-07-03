from pybaseball import statcast
import pandas as pd

# Step 1: Download data (small range to test first)
df = statcast(start_dt="2019-06-24", end_dt="2019-06-26")

# Step 2: Keep only rows where runs are finalized (end of game scoring)
df = df.dropna(subset=['home_score', 'away_score'])

# Step 3: Aggregate to game-level features
game_stats = df.groupby('game_pk').agg({
    'home_team': 'first',
    'away_team': 'first',
    'game_date': 'first',
    'home_score': 'max',
    'away_score': 'max',
    'release_speed': 'mean',
    'launch_speed': 'mean',
    'launch_angle': 'mean',
    'release_spin_rate': 'mean',
    'woba_value': 'mean',
}).reset_index()

# Step 4: Create a binary target (1 = home win, 0 = home loss)
game_stats['home_win'] = (game_stats['home_score'] > game_stats['away_score']).astype(int)

# Step 5: Preview results
print(game_stats.head())