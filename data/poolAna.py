import pandas as pd
import os
taxiWait_num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
index = 0
fileName = "DUresult/downAtpool.csv"
csv_dataD = pd.read_csv(fileName)
print(csv_dataD["time"])
for i in range(csv_dataD.__len__()):
    if csv_dataD["time"][i][10]==":":
        compare=csv_dataD["time"][i][9]
    else:
        compare=csv_dataD["time"][i][9:11]
    print(compare)
    for j in range(24):
        if int(compare) == j:
            taxiWait_num[j] = taxiWait_num[j]+1
            break
print(taxiWait_num)
