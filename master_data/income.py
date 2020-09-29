import pandas as pd
df1 = pd.read_csv("/home/vikky/peekaboo/vikash/src/master_data/income_data.csv")
print(df1)
df2 = df1.set_index("State")
