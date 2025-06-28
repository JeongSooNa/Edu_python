import pandas as pd

raw = pd.read_excel("js.xlsx", header=None)

print(raw.index)

