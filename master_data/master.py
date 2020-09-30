from itertools import chain
import pandas as pd

df1 = pd.read_csv("/home/vikky/peekaboo/vikash/src/master_data/master_data.csv", index_col=0)
print(df1)

# FilterValue
list1 = df1.T.values.tolist()
s = [[str(e) for e in row] for row in list1]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]

flatten_list = list(chain.from_iterable(list1))
N = df1.size
df5 = pd.DataFrame(flatten_list, columns=["final_values"], index=range(1, N + 1))
ch = pd.DataFrame(df5)
c = len(df1.columns)
r = int(N / c)
chipset_id = []
benchmark_id = []

for a1 in range(c):
    for a2 in range(r):
        chipset_id.append(a1 + 1)

for b1 in range(c):
    for b2 in range(r):
        benchmark_id.append(b2 + 1)

# ch['id'] = id2
ch['chipset'] = chipset_id
ch['benchmark'] = benchmark_id
# ch['values'] = df5
ch.to_csv('FilterValue.csv', index=True)

# BenchmarkValue

df_benchmark = pd.read_csv("/home/vikky/peekaboo/vikash/src/master_data/master_data.csv")
cols = [0]
df_2 = df_benchmark[df_benchmark.columns[cols]]
ch1 = pd.DataFrame()
id = []
for a3 in range(r):
    id.append(a3 + 1)

ch1['id'] = id
ch1['benchmark_name'] = df_2
ch1.to_csv("benchmark.csv", index=False)

# ChipsetValue

df_chipset = pd.read_csv("/home/vikky/peekaboo/vikash/src/master_data/master_data.csv", index_col=0).T
col = [0]
df_3 = df_chipset[df_chipset.columns[col]]
ch2 = pd.DataFrame()
id1 = []
for a4 in range(c):
    id1.append(a4 + 1)

df_4 = pd.DataFrame(df_3.index.tolist())
ch2['id'] = id1
ch2['chipset_name'] = df_4

ch2.to_csv("chipset.csv", index=False)
