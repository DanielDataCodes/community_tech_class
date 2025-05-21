#Titanic lesson 2 Confidence Interval
#MEthod chaining
import pandas as pd
import numpy as np

titanic = pd.read_csv("titanic.csv")

titanic_summary = titanic.query("Survived == 1")\
        .groupby("Pclass")["Fare"]\
        .describe()\
        .reset_index()\
        .rename(columns={
            "count": "n"})\
        .assign(
            sqrt_n = lambda x: np.sqrt(x["n"]),
            standard_error = lambda x: x["std"]/np.sqrt(x["n"]),
            upper_ci = lambda x: x['mean']+1.96*x['standard_error'],
            lower_ci = lambda x: x['mean']-1.96*x['standard_error']
        )\
        .to_csv("titanic_summary.csv", index=False)
print(titanic_summary)