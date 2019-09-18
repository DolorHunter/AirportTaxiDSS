# 获取符合条件出租车的上下车点
import pandas as pd
import os
start = []
end = []
index1=73
fileNameS = "N_EndAtPool/" + str(0) + ".csv"
fileNameE = "startFromAirport/" + str(0) + ".csv"
for i in range(26819 , 90000000):
    fileName = "road/" + str(i) + ".csv"


    if os.path.exists(fileName):
        csv_dataD = pd.read_csv(fileName)
        for j in range(1,csv_dataD.__len__()-1):
            if csv_dataD['J'][j] <= 121.87 and csv_dataD['J'][j] >= 121.815 and csv_dataD['W'][j] <= 31.12 and csv_dataD['W'][j]>= 31.116:
                print(i)
                fileNameS = "N_EndAtPool/" + str(index1) + ".csv"
                index1 = index1+1
                df = pd.DataFrame(csv_dataD, columns=["ID", "status", "time", "J", "W","speed"])
                df.to_csv(fileNameS, index=False)
                break

