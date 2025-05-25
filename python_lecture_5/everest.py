#Everest merge exercise

import pandas as pd

expeditions = pd.read_csv("expeditions.csv")
members = pd.read_csv("members.csv")
peaks = pd.read_csv("peaks.csv")

e_p = pd.merge(
    left = expeditions,
    right = peaks,
    on = "peak_id",
    how = "inner"
)

epm = pd.merge(left = e_p, right = members, how = 'inner', on = ["expedition_id", "peak_id"])

print(epm)