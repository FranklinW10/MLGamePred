
import pandas as pd

from pybaseball import schedule_and_record
from pybaseball import  playerid_lookup
from pybaseball import statcast_batter

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

# Regression models
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Metrics / evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Saving / loading models
import joblib

df = playerid_lookup("Raleigh","Cal")


pitch_physics_cols = [

    'balls', 'strikes', 'outs_when_up', 'home_score_diff',

    'release_speed', 'effective_speed',
    
    # Release Point
    'release_pos_x', 'release_pos_y', 'release_pos_z', 'release_extension', 'arm_angle',
    
    # Spin
    'release_spin_rate', 'spin_axis',
    
    # Movement / Break
    'pfx_x', 'pfx_z',
    
    # Ball Flight (kinematics & acceleration)
    'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az',
    
    
    # Plate location (optional, still physics)
    'plate_x', 'plate_z',
    
    # Target variable
    'delta_run_exp'
]

player_df = playerid_lookup("Arráez", "Luis")
player_id = player_df['key_mlbam'].values[0]

Arraezstats = statcast_batter('2025-03-30', '2025-10-01', player_id)

Arraezstats1 = Arraezstats.tail(10000)




last_3000_pitches = Arraezstats1[pitch_physics_cols].copy()

data_clean = last_3000_pitches.dropna()

data_clean.to_csv("pitch_physics_deltaRE.csv", index=False)
print(data_clean.head())






