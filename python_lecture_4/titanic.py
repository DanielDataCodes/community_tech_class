import pandas as pd

titanic = pd.read_csv('titanic.csv')

mask = (
    titanic['Pclass'].isin([1,2]) &
    titanic['Age'].notnull() & (titanic['Age'] >= 18) &
    (titanic ['Sex'] == 'female') &
    (titanic['Fare'] >= 20) & (titanic['Fare'] <= 80) &
    (titanic['Embarked'] == 'S') &
    (titanic['Survived'] == 1)

)

print(titanic[mask])