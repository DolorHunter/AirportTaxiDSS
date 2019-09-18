import pandas as pd

csv_data = pd.read_csv('data.csv')
# csv_data = csv_dataT.head(1000)
filterArr = []
print(csv_data.shape)
print(csv_data.__len__())
