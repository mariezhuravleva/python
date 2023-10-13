import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_categories = data['whoAmI'].unique()

for category in unique_categories:
    data[category] = (data['whoAmI'] == category).astype(int)

data = data.drop('whoAmI', axis=1)

print(data.head())