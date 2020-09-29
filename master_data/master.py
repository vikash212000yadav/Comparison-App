import pandas as pd
df1 = pd.read_csv("/home/vikky/peekaboo/vikash/src/master_data/master_data.csv")
print(df1)
df2 = df1.loc["Antutu 7":, :]
print(df2)
print(df2.to_csv('benchmark.csv', index=True))