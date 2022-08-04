import pandas as pd

url = 'http://www.phrfne.org/page/handicapping/base_handicaps'
dfs = pd.read_html(url)
#grab the first table on the page
table = dfs[1]
#get only the columns we want
table = table[[0,2]]
#delete row 0, not part of the data
table = table.drop(0)

result_table = table.sort_values(by = [2])
result_table.to_html('index.html')
print(result_table)