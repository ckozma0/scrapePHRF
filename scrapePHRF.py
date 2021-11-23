import pandas as pd

url = 'http://www.phrfne.org/page/handicapping/base_handicaps'
dfs = pd.read_html(url)
table = dfs[2]
columns = table[[0,2]]
columns = columns.drop(0)
print(columns)