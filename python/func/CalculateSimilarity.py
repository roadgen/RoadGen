from func.GraphSimilarity import GetBaseSimilarity
from func.GraphSimilarityV2 import GetImproveSimilarity


def calculatesimilarity():
    four_random_h1 = [100,118,98,122,110]
    four_count_h1 = [73,94,78,89,104]
    four_random_h2 = [198,222,218,221,200]
    four_count_h2 = [182,168,171,179,196]
    four_random_h3 = [302,340,330,305,302]
    four_count_h3 = [267,263,264,271,281]
    four_random_h4 = [437,465,437,433,429]
    four_count_h4 = [349,352,352,379,387]
    four_random_h5 = [534,593,559,566,535]
    four_count_h5 = [446,443,438,465,478]
    four_random_h6 = [659,703,666,673,647]
    four_count_h6 = [522,526,526,557,576]
    four_random_h7 = [764,805,773,797,762]
    four_count_h7 = [612,621,619,636,661]
    four_random_h8 = [864,901,856,910,875]
    four_count_h8 = [701,695,704,730,748]
    four_random_h9 = [983,1024,949,999,984]
    four_count_h9 = [786,778,805,820,835]
    four_random_h10 = [1078,1140,1037,1104,1095]
    four_count_h10 = [885,880,888,893,921]
    four_random_h11 = [1218,1247,1132,1181,1209]
    four_count_h11 = [990,954,972,982,1022]
    four_random_h12 = [1341,1347,1221,1285,1327]
    four_count_h12 = [1065,1051,1051,1084,1119]
    four_random_h13 = [1430,1459,1341,1375,1448]
    four_count_h13 = [1161,1140,1135,1180,1197]
    four_random_h14 = [1542,1552,1439,1470,1581]
    four_count_h14 = [1251,1238,1221,1278,1288]
    four_random_h15 = [1649,1652,1523,1566,1685]
    four_count_h15 = [1332,1329,1321,1369,1377]
    four_random_h16 = [1783,1769,1637,1663,1780]
    four_count_h16 = [1430,1408,1421,1466,1454]
    four_random_h17 = [1900,1866,1746,1797,1874]
    four_count_h17 = [1523,1506,1492,1564,1547]
    four_random_h18 = [1993,1983,1859,1899,1968]
    four_count_h18 = [1614,1596,1574,1662,1653]
    four_random_h19 = [2100,2090,1990,2014,2077]
    four_count_h19 = [1699,1680,1668,1744,1735]
    four_random_h20 = [2222,2216,2075,2114,2193]
    four_count_h20 = [1794,1774,1758,1824,1830]
    four_random_h21 = [2329,2336,2186,2215,2317]
    four_count_h21 = [1870,1865,1849,1914,1925]
    four_random_h22 = [2446,2447,2303,2343,2450]
    four_count_h22 = [1963,1949,1937,1914,2009]
    four_random_h23 = [2547,2564,2412,2343,2538]
    four_count_h23 = [2066,2043,2032,2106,2090]
    four_random_h24 = [2620,2658,2518,2530,2663]
    four_count_h24 = [2150,2120,2130,2180,2185]
    
    
    
    lab0_random = [16,36,61,120,386]
    lab1_random = [16,37,69,132,435]
    lab2_random = [14,35,61,102,455]
    lab3_random = [14,32,59,106,510]
    lab4_random = [15,36,61,120,701]





    lab0_count = [14,26,40,53,69]
    lab1_count = [13,26,39,51,87]
    lab2_count = [14,27,41,55,76]
    lab3_count = [14,27,42,56,69]
    lab4_count = [14,27,39,52,73]
        
    
    

    
    
    RandomStr = "four_random_h"
    CountStr = "four_count_h"

    

    graph_dir0 = "./graph" #第0组
    graph_dir1 = "./1graph" 
    graph_dir2 = "./2graph"
    graph_dir3 = "./3graph"
    graph_dir4 = "./4graph"


    graphList = [graph_dir0,graph_dir1,graph_dir2,graph_dir3,graph_dir4]

    for i in range(1,6):
        if i == 1:
            print("使用50组件相似度结果:============================================")
        if i == 2:
            print("使用100组件相似度结果:============================================")
        if i == 3:
            print("使用150组件相似度结果:============================================")
        if i == 4:
            print("使用200组件相似度结果:============================================")
        if i == 5:
            print("使用243组件相似度结果:============================================")
        for j in range(0,5):
            print("第",j,"组结果:---------------------")
            print("random-base相似度")
            GetBaseSimilarity(graphList[j], eval("lab"+ str(j)+"_random")[i-1])
            
            print("\n")
            print("random-improve相似度")
            GetImproveSimilarity(graphList[j], eval("lab"+ str(j)+"_random")[i-1])
            print("\n")
            print("count-base相似度")
            GetBaseSimilarity(graphList[j], eval("lab"+ str(j)+"_count")[i-1])
            print("\n")
            print("count-improve相似度")
            GetImproveSimilarity(graphList[j], eval("lab"+ str(j)+"_count\n")[i-1])
            print("\n\n")
            
        print("\n\n\n")
        
    
    # for index in range(24,25):
    #     print(index,"小时结果")
    #     print("=======================================================================================")
    #     for i, (e1, e2) in enumerate(zip(eval(RandomStr + str(index)), eval(CountStr + str(index)))):
    #         print("第 ", i, " 组的实验结果为：--------------------------------------------------")
    #         print("random-V1相似度判断方法结果")
    #         GetBaseSimilarity(graphList[i], e1)
    #         print("random-V2相似度判断方法结果")
    #         GetImproveSimilarity(graphList[i], e1)
    #         print("\n")
    #         print("countBased-V1相似度判断方法结果")
    #         GetBaseSimilarity(graphList[i] + "2", e2)
    #         print("countBased-V2相似度判断方法结果")
    #         GetImproveSimilarity(graphList[i] + "2", e2)
    #         print("\n\n\n")
        
    
    
    
  