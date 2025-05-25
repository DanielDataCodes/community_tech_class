#mergeing data sets with python

import pandas as pd

df1 = pd.DataFrame(
    {
        'PassengerId': ['1', '2', '3'],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25,30,35]

    }
)

df2 = pd.DataFrame(
    {
        'PassengerId': ['1','2','4'],
        'Ticket': ['A123', 'B456', 'C789'],
        'Fare': [72.5, 50.0, 100]
    }
)

df_combined = pd.merge(
    left = df1,
    right = df2,
    on = "PassengerId",
    how = "right"
)
print(df_combined)
