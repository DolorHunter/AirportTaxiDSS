# 将三万多台出租车分到各自的csv里
import pandas as pd

csv_dataT = pd.read_csv('data.csv')
print(csv_dataT)
# csv_data = csv_dataT.head(1000)
filterArr = []
# print(csv_data.shape)
# print(csv_data.__len__())

# print(csv_data)
print("pass")
print(csv_dataT["ID"])
road = []
index = 3483
for i in range(1348152, csv_dataT.__len__()-1):
        print(i)
        if csv_dataT["status"][i] == csv_dataT["status"][i+1]:
                road.append(csv_dataT.loc[i])
        else:
                road.append(csv_dataT.loc[i])
                fileName = "road/" + str(index) + ".csv"
                index = index+1
                df = pd.DataFrame(road, columns=["ID", "status", "time", "J", "W", "speed"])
                df.to_csv(fileName, index=False)
                road = []


print(csv_dataT.tail(5))
print(csv_dataT[csv_dataT["ID"].isin(["9025"])])





