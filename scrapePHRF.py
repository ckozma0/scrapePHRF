import pandas as pd

url = 'http://www.phrfne.org/page/handicapping/base_handicaps'
dfs = pd.read_html(url)
#grab the third table on the page
table = dfs[2]
#get only the columns we want
columns = table[[0,2]]
#delete row 0, not part of the data
columns = columns.drop(0)

print(columns)