import pandas as pd
import numpy as np

Series1 = pd.Series(data = [1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
Series2 = pd.Series(data =[6, 7, 8, 9, 10], index = ['a', 'b', 'c', 'd', 'e'])

print(Series1 + Series2)
print(Series1 - Series2)
print(Series1 * Series2)
print(Series1 / Series2)