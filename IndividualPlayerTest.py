import os
import pandas as pd
import numpy as np
from pybaseball import schedule_and_record
from pybaseball import  playerid_lookup
from pybaseball import statcast_batter
df = playerid_lookup("Arráez","Luis")


Arraezstats = statcast_batter('2025-06-23', '2025-06-24', 650333)

from pybaseball import schedule_and_record
data = schedule_and_record(2025, 'NYY')
data.loc[data.Date.str.contains("May 16"), :]
print(data)
