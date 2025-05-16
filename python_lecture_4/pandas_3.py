import pandas as pd
import numpy as np

def square(num):
    return num **2

Series1 = pd.Series(data = [1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])


squared_data = Series1.apply(square)

print(squared_data)