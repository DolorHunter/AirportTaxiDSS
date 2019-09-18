import pandas as pd
import os
flight_num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
index = 0
fileName = "flight.csv"
csv_dataD = pd.read_csv(fileName)
print(csv_dataD["时间段"])
for i in range(csv_dataD.__len__()-1):
    if csv_dataD["时间段"][i] != csv_dataD["时间段"][i+1]:
        flight_num[index] = flight_num[index] + 1
        index = index+1
    else:
        flight_num[index] = flight_num[index]+1
print(flight_num)        # 获得各时段内航班数量
for j in range(24):
    print('在第',j+1,'个时段的航班总数为:',flight_num[j])



