
import sys
import time

from icecream import ic
import pandas as pd
import numpy as np

# measure use of pandas.DataFrame
start_time = time.time()

df = pd.DataFrame({
    "src": pd.Series(dtype="int"),
    "rel": pd.Series(dtype="int"),
    "dst": pd.Series(dtype="object"),
    "lit": pd.Series(dtype="bool"),
    "ctx": pd.Series(dtype="str"),
})

df.loc[0] = [ 4, 5, 3, True, "B" ]
df.loc[1] = [ 2, 3, 1, False, "A" ]
df.loc[2] = [ 3, 4, "wow", True, "A" ]
df.loc[3] = [ 1, 2, 3, True, "A" ]

ic(df)

for row in df.itertuples():
    ic(row)

rows = df.index[(df["src"] == 3) & (df["dst"] == "wow")]
ic(rows)
ic(rows[0])

millisec = (time.time() - start_time) * 1000.0
ic(millisec)

sys.exit(0)

x = np.empty(shape=[0, 1], dtype=object)
x = np.append(x, "foo")
x = np.append(x, "bar")
ic(x)
ic(x[0])

#np.array([ "foo", "bar" ])
ic(np.where(x == "bar"))
