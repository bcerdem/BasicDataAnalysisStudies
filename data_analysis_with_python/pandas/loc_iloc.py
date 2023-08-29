############################################################
# iloc & loc
############################################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: Integer Base Selection

df.iloc[0:3]
df.iloc[0, 0]
df.iloc[0:3, 0:3]

# loc: Label Base Selection

df.loc[0:3]
df.loc[0:3, "age"]

col_names = ["age","embarked","alive"]
df.loc[0:3, col_names]