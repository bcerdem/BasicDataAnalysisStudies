import pandas as pd

series = pd.Series([1,2,3])

series**2

###
import pandas as pd
dict = {"Paris": [10], "Berlin": [20]}

pd.DataFrame(dict)

###

import pandas as pd
import numpy as np

df = pd.DataFrame(data= np.random.randint(1,10, size=(2,3)),
                  columns=["var1","var2","var3"])

df[(df.var1 <= 5)][["var2","var3"]]

df.loc[(df.var1 <= 5), ["var2", "var3"]]