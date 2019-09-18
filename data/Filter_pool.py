# 将符合条件的出租车筛选出来
import pandas as pd
import os
for i in range(10322, 32011):

    fileName = "divide/"+str(i)+".csv"
    if os.path.exists(fileName):
        csv_dataD = pd.read_csv(fileName)
        for j in range(1,csv_dataD.__len__()-1):
            if csv_dataD['J'][j]<=121.81 and csv_dataD['J'][j]>=121.785 and csv_dataD['W'][j]<=31.159 and csv_dataD['W'][j]>=31.14:
                print(csv_dataD)
                fileName2 = "validAirport/" + str(i) + ".csv"
                df = pd.DataFrame(csv_dataD,columns=["ID", "status", "time", "J", "W"])
                df.to_csv(fileName2, index=False)
                break













