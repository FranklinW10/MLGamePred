import os
import pandas as pd
import numpy as np
from pybaseball import batting_stats
START = 2005
END = 2025
batting = batting_stats(START, END, qual=200) #downloads data, qual is how many required abs

batting.to_csv("batting.csv")

#splis each player into differnet groups
#batting = batting.groupby("IDfg", group_keys = False).filter(lambda x: x.shape[0]>1)
#print(batting.head())

def next_season(player):
    player = player.sort_values("Season")
    player["Next_WAR"] = player["WAR"].shift(-1)
    return player
batting = batting.groupby("IDfg", group_keys=False).apply(next_season, include_group=False)
print(batting[["Name","Season","WAR","NextWar"]])


null_count = batting.isnull().sum()


