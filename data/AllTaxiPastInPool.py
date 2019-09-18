# 获取符合条件出租车的上下车点
import pandas as pd
import os
start = []
end = []
index1=0
fileNameS = "N_EndAtPool/" + str(0) + ".csv"
fileNameE = "startFromAirport/" + str(0) + ".csv"
for i in range(1 ,90000000):
    fileName = "road/" + str(i) + ".csv"


    if os.path.exists(fileName):
        csv_dataD = pd.read_csv(fileName)
        if csv_dataD['J'][csv_dataD.__len__()-1] <= 121.87 and csv_dataD['J'][csv_dataD.__len__()-1] >= 121.815 and csv_dataD['W'][csv_dataD.__len__()-1] <= 31.12 and csv_dataD['W'][csv_dataD.__len__()-1]>= 31.116:
                print(i)
                fileNameS = "N_RealInPool/" + str(index1) + ".csv"
                index1 = index1+1
                df = pd.DataFrame(csv_dataD, columns=["ID", "status", "time", "J", "W","speed"])
                df.to_csv(fileNameS, index=False)
