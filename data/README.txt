road 文件夹
存放的是从元数据中提取的大部分出租车轨迹

截图文件夹
存放与论文撰写相关的截图与配图

经过蓄车池排队的轨迹（计算数据）  文件夹
如其名，从出租车轨迹中筛选经过蓄车池的轨迹

上下车点获取 文件夹
存放着从元数据中获取的所有上车点和下车点

途经机场的所有轨迹 文件夹
存放着从出租车轨迹中晒选出来的经过机场区的轨迹

airportArriveAna.py
python程序，用于从轨迹中提取到达出发层的轨迹并分析

airportLeaveAns.py
python程序，用于从轨迹中提取从到达层出发的轨迹的轨迹并分析

AllTaxiPastInPool.py
python程序，用于从源数据中提取有经过蓄车池的出租车  

AllTaxiPastInPool.csv
提取完成的出租车数据

flightAna.py
用于分析航班以提炼航班密度

Filter_pool.py
过滤器，用于筛选经过蓄车池的轨迹   

infoGet.py
信息获取，用于获取经过蓄车池的轨迹

ModelGraph.mxd
arcmap生成地图文件，用于数据点集可视化

poolAna.py
用于分析蓄车池中不同时段的车辆数

split.py
用于从源数据中将每一辆车的数据单独剥离出来形成文件

upAndDownAtPool.py
获取在蓄车池的上车点和下车点

upAndDownInAp.py
获取在到达层和出发层的上下车点  

waitInpool.py
获取蓄车池的上车点和下车点（分开）

上海浦东国际机场航班详情.xls
航班源数据

所有下车点.csv
存放所有下车点数据

所有上车点.csv
存放所有上车点数据

源数据
存档最原始的获取数据