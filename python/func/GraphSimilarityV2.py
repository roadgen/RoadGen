import pickle
from func.WidgetGraph import Node, WidgetGraph
import os


# 相似比较
class GetImproveSimilarity:
    def __init__(self, graph_dir, graph_size):
        self.graph_dir = graph_dir
        self.graph_name = os.listdir(self.graph_dir)
        self.graph_dir = graph_dir
        self.graph_name = os.listdir(self.graph_dir)
        EdgesSimilarity = 0  # 边的总相似度
        NodesSimilarity = 0  # 点的总相似度
        EdgesDeSimilarity = 0  # 去重边的总相似度
        NodesDeSimilarity = 0  # 去重点的总相似度
        EdgesCurList = []  # 用于计算
        NodesCurList = []
        CurList = []
        EdgesCurList.append(self.graph_dir + '/' + 'AGM' + str(1) + '.pkl')  # 先把第一幅图放进列表里面
        NodesCurList.append(self.graph_dir + '/' + 'AGM' + str(1) + '.pkl')
        CurList.append(self.graph_dir + '/' + 'AGM' + str(1) + '.pkl')
        edgecount = 0
        nodecount = 0
        # for i in range(1, graph_size):
        #     flag = 1  # 默认不重复
        #     gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
        #     tmpsum = 0  # 根据是否需要去重来决定是否要加上
        #     tmpcount = 0
        #     for graph in EdgesCurList:
        #         EdgeSimilarity = GraphSimilarity(gsfile1, graph).EdgeSimilarity()  # 两个图边的相似度
        #         if EdgeSimilarity != 1:
        #             tmpcount += 1  # 统计有效比较的次数
        #             tmpsum += EdgeSimilarity
        #         if EdgeSimilarity == 1:
        #             flag = 0  # 标识这个应该被剔除
        #             break
        #     if flag == 1:  # 不需要被去重
        #         EdgesDeSimilarity += tmpsum
        #         edgecount += tmpcount #没被去除，此次为有效比较，加入count
        #         EdgesCurList.append(gsfile1)
        #     else:
        #         continue
        # EdgesDeSizeV1 = len(EdgesCurList) # 列表大小即为按边去重后图的个数为

        # for i in range(1,graph_size):
        #     flag = 1
        #     gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
        #     tmpsum = 0  # 这一轮有可能要加上的相似度
        #     tmpcount = 0  # 这一轮有可能要加上的比较次数
        #     for graph in NodesCurList:
        #         NodeSimilarity = GraphSimilarity(gsfile1, graph).NodeSimilarity()
        #         if NodeSimilarity != 1:
        #             tmpcount += 1
        #             tmpsum += NodeSimilarity
        #         if NodeSimilarity == 1:
        #             flag = 0
        #             break
        #     if flag == 1: #不需要被剔除
        #         NodesDeSimilarity += tmpsum
        #         nodecount += tmpcount
        #         NodesCurList.append(gsfile1)
        #     else:
        #         continue
        # NodesDeSizeV1 = len(NodesCurList)
        for i in range(0, graph_size + 1):
            for j in range(i + 1, graph_size + 1):
                gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
                gsfile2 = self.graph_dir + '/' + 'AGM' + str(j + 1) + '.pkl'
                # 边相似度===========
                EdgeSimilarity = GraphSimilarity(gsfile1, gsfile2).EdgeSimilarity()  # 两条边间的相似度
                # 点相似度========
                NodeSimilarity = GraphSimilarity(gsfile1, gsfile2).NodeSimilarity()
                EdgesSimilarity += EdgeSimilarity
                NodesSimilarity += NodeSimilarity

        CmpNodesSimilarity = 0
        CmpEdgesSimilarity = 0
        Cmpcount = 0
        for i in range(1,graph_size):
            flag = 1
            gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
            for graph in CurList:
                NodeSimilarity = GraphSimilarity(gsfile1, graph).NodeSimilarity()
                EdgeSimilarity = GraphSimilarity(gsfile1, graph).EdgeSimilarity()
                if not (NodeSimilarity == 1 and EdgeSimilarity == 1):
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                CurList.append(gsfile1)
            else:
                #print("去重，被剔除...")
                continue
        CmpDeSize = len(CurList)
        if CmpDeSize != graph_size: #计算去重后的相似度
            for i in range(0,CmpDeSize):
                for j in range(i+1,CmpDeSize):
                    NodeSimilarity = GraphSimilarity(CurList[i], CurList[j]).NodeSimilarity()
                    EdgeSimilarity = GraphSimilarity(CurList[i], CurList[j]).EdgeSimilarity()
                    CmpNodesSimilarity += NodeSimilarity
                    CmpEdgesSimilarity += EdgeSimilarity



        print("图的总数为 = ", graph_size)
        print("去重后图的个数为 = ", CmpDeSize)
        #print("·····································")
        # print("按边去重后图的个数为 = ", EdgesDeSizeV1)
        # print("去重后边的平均相似度 = ", EdgesDeSimilarity / edgecount)
        print("不去重边的平均相似度 = ", EdgesSimilarity / (graph_size * (graph_size - 1) / 2))
        #print("·····································")
        # print("按点去重后图的个数为 = ", NodesDeSizeV1)
        # print("去重后点的平均相似度 = ", NodesDeSimilarity / nodecount)
        print("不去重点的平均相似度 = ", NodesSimilarity / (graph_size * (graph_size - 1) / 2))
        #print("·····································")
        if graph_size == CmpDeSize:
            print("去重后边的平均相似度 = ", EdgesSimilarity / (graph_size * (graph_size - 1) / 2))
            print("去重后点的平均相似度 = ", NodesSimilarity / (graph_size * (graph_size - 1) / 2))
        else:
            print("去重后边平均相似度 = ",CmpEdgesSimilarity / (CmpDeSize*(CmpDeSize - 1)/2))
            print("去重后点平均相似度 = ", CmpNodesSimilarity / (CmpDeSize*(CmpDeSize - 1)/2))

# 图相似性比较类
class GraphSimilarity:
    def __init__(self, file_dir1, file_dir2):
        self.file_dir1 = file_dir1  # 存图1的地址
        self.file_dir2 = file_dir2  # 存图2的地址
        self.data1 = []
        self.data2 = []
        with open(self.file_dir1, "rb") as f:
            self.data1 = pickle.load(f)
        with open(self.file_dir2, "rb") as f:
            self.data2 = pickle.load(f)

    def getData(self):
        return self.data1, self.data2

    def printData(self):
        print("Graph1\n", self.data1)
        print("Graph2\n", self.data2)

    def EdgeSimilarity(self):
        edgelist1 = self.data1.get_edges()
        edgelist2 = self.data2.get_edges()
        # print(edgelist1)
        # print(edgelist2)
        list1 = []
        list2 = []
        for i, edge in enumerate(edgelist1):
            if i % 2 == 0:
                if edge[0].type[0] > edge[1][0].type[0]:
                    newedge = (edge[1][0], edge[0])  # 无向边，统一顺序
                    list1.append(newedge)
                else:
                    list1.append((edge[0], edge[1][0]))
        # print(list1)
        for i, edge in enumerate(edgelist2):
            if i % 2 == 0:
                if edge[0].type[0] > edge[1][0].type[0]:  # 无向边，统一顺序
                    newedge = (edge[1][0], edge[0])
                    list2.append(newedge)
                else:
                    list2.append((edge[0], edge[1][0]))
        # print(list2)
        similarity = 0
        index_list1 = [[0] * (len(list1) + 2)] * (len(list1) + 2)
        index_list2 = [[0] * (len(list2) + 2)] * (len(list2) + 2)
        for edge1 in list1:  # 两层循环，先进行无向非对称性的判断
            for edge2 in list2:
                if CompareNode(edge1[0], edge2[0]) == True and CompareNode(edge1[1], edge2[1]) == True:  # 基本的两节点分别判断
                    # print("edge1 = ",edge1)
                    # print("edge2 = ",edge2)
                    # print("==========================")
                    # 相似配对成功，矩阵对应边置1
                    index_list1[edge1[0].id][edge1[1].id] = 1
                    index_list1[edge1[1].id][edge1[0].id] = 1
                    index_list2[edge2[0].id][edge2[1].id] = 1
                    index_list2[edge2[1].id][edge2[0].id] = 1
                    # 一个边最多只能和另一幅图的边相似一次
                    similarity += 1
                    break
                else:
                    continue
        # print(index_list1)
        # print(index_list2)
        Dlist1 = []  # 只存储有向标识为1的边
        Dlist2 = []
        for edge in edgelist1:
            if edge[1][1] == 1:
                Dlist1.append((edge[0], edge[1][0]))
            else:
                continue
        # print(Dlist1)
        for edge in edgelist2:
            if edge[1][1] == 1:
                Dlist2.append((edge[0], edge[1][0]))
            else:
                continue
        # print(Dlist2)
        # 此时Dlist1、Dlist2均存的是有向边信息，以此来判断特殊情况
        for edge1 in Dlist1:  # 特殊情况判断
            for edge2 in Dlist2:
                # print("edge1 = ",edge1)
                # print("edge2 = ", edge2)
                # print(index_list1[edge1[0].id][edge1[1].id])
                if index_list1[edge1[0].id][edge1[1].id] != 1 and index_list2[edge2[0].id][
                    edge2[1].id] != 1 and EdgeExceptionCompare(edge1, edge2):
                    similarity += 1
                else:
                    continue
        return (similarity * 2) / (len(list1) + len(list2))

    def NodeSimilarity(self):
        nodelist1 = self.data1.get_nodes()
        nodelist2 = self.data2.get_nodes()
        len1 = len(nodelist1)
        len2 = len(nodelist2)
        G1 = GraphNodeMsg(len1)
        G2 = GraphNodeMsg(len2)
        edgelist1 = self.data1.get_edges()
        edgelist2 = self.data2.get_edges()
        for edge in edgelist1:
            cur_id = edge[0].id
            G1.Nodelist[cur_id - 1].type = edge[0].type
            G1.Nodelist[cur_id - 1].flag = edge[0].flag
            G1.Nodelist[cur_id - 1].function = edge[0].function
            G1.Nodelist[cur_id - 1].direction = edge[0].direction
            G1.Nodelist[cur_id - 1].add_edge(
                [Node(0, edge[1][0].type, edge[1][0].flag, edge[1][0].function, edge[1][0].direction), edge[1][1]])
            # 存储边结点的时候不考虑ID，统一置为0
        # G1.printMsg()
        # print("-------------------------")
        for edge in edgelist2:
            cur_id = edge[0].id
            G2.Nodelist[cur_id - 1].type = edge[0].type
            G2.Nodelist[cur_id - 1].flag = edge[0].flag
            G2.Nodelist[cur_id - 1].function = edge[0].function
            G2.Nodelist[cur_id - 1].direction = edge[0].direction
            G2.Nodelist[cur_id - 1].add_edge(
                [Node(0, edge[1][0].type, edge[1][0].flag, edge[1][0].function, edge[1][0].direction), edge[1][1]])
            # 存储边结点的时候不考虑ID，统一置为0
        # G2.printMsg()
        # print("=====================================")
        similarity = 0
        index_list1 = [0] * (len(G1.Nodelist) + 1)  # 只能相似一次
        index_list2 = [0] * (len(G2.Nodelist) + 1)
        for node1 in G1.Nodelist:  # 无向比较
            for node2 in G2.Nodelist:
                # if CompareGraphNode(node1, node2):
                if CompareGraphNode(node1, node2) or NodeExceptionCompare(node1, node2):  # 比较两个不同图中两点的相似性 基本比较 + 特殊情况比较
                    if index_list1[node1.id] == 0 and index_list2[node2.id] == 0:
                        # print("相似的两个节点ID分别为：id1 = ",node1.id," id2 = ",node2.id)
                        index_list1[node1.id] = 1  # 只能相似一次
                        index_list2[node2.id] = 1
                        similarity += 1
                        break
        return similarity * 2 / (len(G1.Nodelist) + len(G2.Nodelist))
        # return similarity


# 点相似测试函数
def NodeSimilarityTest(data1, data2):
    nodelist1 = data1.get_nodes()
    nodelist2 = data2.get_nodes()
    len1 = len(nodelist1)
    len2 = len(nodelist2)
    G1 = GraphNodeMsg(len1)
    G2 = GraphNodeMsg(len2)
    edgelist1 = data1.get_edges()
    edgelist2 = data2.get_edges()
    for edge in edgelist1:
        cur_id = edge[0].id
        G1.Nodelist[cur_id - 1].type = edge[0].type
        G1.Nodelist[cur_id - 1].flag = edge[0].flag
        G1.Nodelist[cur_id - 1].function = edge[0].function
        G1.Nodelist[cur_id - 1].direction = edge[0].direction
        G1.Nodelist[cur_id - 1].add_edge(
            [Node(0, edge[1][0].type, edge[1][0].flag, edge[1][0].function, edge[1][0].direction), edge[1][1]])
        # 存储边结点的时候不考虑ID，统一置为0
    # G1.printMsg()

    for edge in edgelist2:
        cur_id = edge[0].id
        G2.Nodelist[cur_id - 1].type = edge[0].type
        G2.Nodelist[cur_id - 1].flag = edge[0].flag
        G2.Nodelist[cur_id - 1].function = edge[0].function
        G2.Nodelist[cur_id - 1].direction = edge[0].direction
        G2.Nodelist[cur_id - 1].add_edge(
            [Node(0, edge[1][0].type, edge[1][0].flag, edge[1][0].function, edge[1][0].direction), edge[1][1]])
        # 存储边结点的时候不考虑ID，统一置为0
    # G2.printMsg()
    similarity = 0
    for node1 in G1.Nodelist:  # 无向比较
        for node2 in G2.Nodelist:
            if CompareGraphNode(node1, node2) or NodeExceptionCompare(node1, node2):  # 比较两个不同图中两点的相似性 基本比较 + 特殊情况比较
                similarity += 1


# 边相似特殊情况判断
def EdgeExceptionCompare(edge1, edge2):
    exceptiontype = {"curve", "straightlane", "ulane"}
    # 判断边的组件是否都在 C U S这几个类型当中
    if not (edge1[0].type in exceptiontype and edge1[1].type in exceptiontype and edge2[0].type in exceptiontype and
            edge2[1].type in exceptiontype):
        return False

    typeset = set()
    typeset.add(edge1[0].type)
    typeset.add(edge1[1].type)
    typeset.add(edge2[0].type)
    typeset.add(edge2[1].type)
    if len(typeset) > 2 and (len(typeset) == 1 and edge1[0].type == "straightlane"):  # 如果类型数量大于2或者都是直线（非特殊情况算过了），也不可能相似
        return False

    # 判断车道数是否一致
    if edge1[0].flag[-3:] != edge2[0].flag[-3:]:
        return False

    # 以下为特殊情况
    # 1、 S - C
    if (edge1[0].type == "curve" and edge1[0].function == "1/4Circle" and edge1[0].type == "straightlane") and (
            edge2[0].type == "straightlane" and edge2[1].type == "curve" and edge2[1].function == "1/4Circle"):
        if edge1[0].direction + edge2[1].direction == 1:
            return True
        else:
            return False
    if (edge1[0].type == "straightlane" and edge1[1].type == "curve" and edge1[1].function == "1/4Circle") and (
            edge2[0].type == "curve" and edge2[0].function == "1/4Circle" and edge2[1].type == "straightlane"):
        if edge1[1].direction + edge2[0].direction == 1:
            return True
        else:
            return False

    # 2、S - U
    if (edge1[0].type == "ulane" and edge1[1].type == "straightlane") and (
            edge2[0].type == "straightlane" and edge2[1].type == "ulane"):
        if edge1[0].direction + edge2[1].direction == 1:
            return True
        else:
            return False

    if (edge1[0].type == "straightlane" and edge1[1].type == "ulane") and (
            edge2[0].type == "ulane" and edge2[1].type == "straightlane"):
        if edge1[1].direction + edge2[0].direction == 1:
            return True
        else:
            return False

    # 3、C - C  C0-C0 C1-C1
    if (edge1[0].type == "curve" and edge1[0].function == "1/4Circle" and edge1[1].type == "curve" and edge1[
        1].function == "1/4Circle") and (
            edge2[0].type == "curve" and edge2[0].function == "1/4Circle" and edge2[1].type == "curve" and edge2[
        1].function == "1/4Circle") and (edge1[0].direction == edge1[1].direction) and (
            edge2[0].direction == edge2[1].direction) and (edge1[0].direction != edge2[0].direction):
        return True

    # 4、C - U
    if (edge1[0].type == "curve" and edge1[0].function == "1/4Circle" and edge1[1].type == "ulane") and (
            edge2[0].type == "ulane" and edge2[1].type == "curve" and edge2[1].function == "1/4Circle"):
        if (edge1[0].direction, edge1[1].direction, edge2[0].direction, edge2[1].direction) in [(0, 0, 1, 1),
                                                                                                (0, 1, 0, 1),
                                                                                                (1, 1, 0, 0),
                                                                                                (1, 0, 1, 0)]:
            return True
        else:
            return False
    if (edge1[0].type == "ulane" and edge1[1].type == "curve" and edge1[1].function == "1/4Circle") and (
            edge2[0].type == "curve" and edge2[0].function == "1/4Circle" and edge2[1].type == "ulane"):
        if (edge1[0].direction, edge1[1].direction, edge2[0].direction, edge2[1].direction) in [(0, 0, 1, 1),
                                                                                                (0, 1, 0, 1),
                                                                                                (1, 1, 0, 0),
                                                                                                (1, 0, 1, 0)]:
            return True
        else:
            return False

    # 5、 U - U
    if (edge1[0].type == "ulane" and edge1[1].type == "ulane") and (
            edge2[0].type == "ulane" and edge2[1].type == "ulane"):
        if (edge1[0].direction, edge1[1].direction, edge2[0].direction, edge2[1].direction) in [(0, 0, 1, 1),
                                                                                                (0, 1, 0, 1),
                                                                                                (1, 1, 0, 0),
                                                                                                (1, 0, 1, 0)]:
            return True
        else:
            return False

    return False


# 点相似特殊情况判断
def NodeExceptionCompare(node1, node2):
    if not (node1.type == node2.type and node1.flag[-3:] == node2.flag[-3:] and node1.type in (
            "curve", "ulane", "straightlane") and len(node1.edge) == len(node2.edge)):
        return False
    for node in (node1.edge + node2.edge):  # 如果有不属于 C U S的组件，直接返回False
        if node[0].type not in ("curve", "ulane", "straightlane"):
            return False
    type = node1.type
    # # S - C - S
    # if type == "curve" and node1.function == node2.function and node1.function == "1/4Circle" and node1.direction != node2.direction and len(
    #         node1.edge) == 2:
    #     typelist = []
    #     for node in (node1.edge + node2.edge):
    #         typelist.append(node[0].type[0])
    #     if typelist == ["s", "s", "s", "s"]:
    #         return True
    #
    # # S - U - S
    # if type == "ulane" and node1.direction != node2.direction and len(node1.edge) == 2:
    #     typelist = []
    #     for node in (node1.edge + node2.edge):
    #         typelist.append(node[0].type[0])
    #     if typelist == ["s", "s", "s", "s"]:
    #         return True
    #
    # # C - U - C
    # if type == "ulane" and node1.direction != node2.direction and len(node1.edge) == 2:
    #     if node1.edge[0][0].type == "curve" and node1.edge[0][0].function == "1/4Circle" and node1.edge[1][0].type == "curve" and node1.edge[1][0].function == "1/4Circle" and node2.edge[0][0].type == "curve" and node2.edge[0][0].function == "1/4Circle" and node2.edge[1][0].type == "curve" and node1.edge[1][0].function == "1/4Circle":
    #         if node1.edge[-2].direction != node2.edge[-2].direction and node1.edge[-1].direction != node2.edge[-1].direction: # 同向有向边的方向需要相反
    #             return True
    #     return False
    # # U - C - U
    # if type == "curve" and node1.function == "1/4Circle" and len(node1.edge) == 2 and node1.direction != node2.direction:
    #     if node1.edge[0][0].type == "ulane" and node1.edge[1][0].type == "ulane" and node2.edge[0][0].type == "ulane" and node2.edge[1][0].type == "ulane":
    #         if node1.edge[-2].direction != node2.edge[-2].direction and node1.edge[-1].direction != node2.edge[-1].direction: # 同向有向边的方向需要相反

    #             return True

    # U - S
    # U - S
    # if type == "ulane" and node1.direction != node2.direction and len(node1.edge) == 1:
    #     if node1.edge[0][0].type == node2.edge[0][0].type and node1.edge[0][0].type == "straightlane" and node1.edge[0][
    #         1] != node2.edge[0][1]:
    #         return True
    # # C - S
    # if type == "curve" and node1.function == "1/4Circle" and node2.function == "1/4Circle" and len(node1.edge) == 1:
    #     if node1.edge[0][0].type == "straightlane" and node2.edge[0][0].type == "straightlane" and node1.edge[0][1] != \
    #             node2.edge[0][1]:
    #         return True

    # C - C - C
    if TypeJudge(node1, node2):
        if len(node1.edge) == 2:  # 连接了两个组件情况
            if NodeReverseJudge(node1.edge[0][0], node2.edge[1][0]) and NodeReverseJudge(node1.edge[1][0],  # 判断方向相反
                                                                                         node2.edge[0][0]):
                #print("X - X - X类相似")
                return True
        if len(node1.edge) == 1 and node1.edge[0][1] != node2.edge[0][1]:  # 如果是只连接了一个组件的结点，则连接的方向需要反向
            if NodeReverseJudge(node1.edge[0][0], node2.edge[0][0]):  # 判断方向相反
                #print("X - X类相似")
                return True
    return False


# 判断两个点本身是否满足对称性特殊情况的条件函数
def TypeJudge(node1, node2):
    type = node1.type  # 已经提前满足了type、flag一致，无需再次判断
    if type == "straightlane":  # straightlane 直接返回true
        return True
    if type == "ulane" and node1.direction != node2.direction:  # ulane只需方向相反即可
        return True
    if type == "curve" and node1.function == "1/4Circle" and node2.function == "1/4Circle" and node1.direction != node2.direction:
        return True  # curve需要满足方向相反且均为1/4圆
    return False


# 判断两个结点是否是同类反向
def NodeReverseJudge(node1, node2):
    if not (node1.type == node2.type and node1.flag[-3:] == node1.flag[-3:]):  # 先进行type与flag的判断
        return False
    if node1.type == "ulane" and node1.direction != node2.direction:
        return True
    if node1.type == "straightlane":
        return True
    if node1.type == "curve" and node1.function == node2.function and node1.function == "1/4Circle" and node1.direction != node2.direction:
        return True
    return False


# 判断不同图两个结点的相似性
def CompareGraphNode(node1, node2):
    if not CompareNode(node1, node2):  # 要比较的结点本身得相似，在比较其连接的边的情况
        return False
    else:
        if len(node1.edge) != len(node2.edge):  # 如果边的个数不一致
            return False
        else:
            for nextNode1, nextNode2 in zip(node1.edge, node2.edge):  # 同步遍历，依次对比
                if not CompareNode(nextNode1[0], nextNode2[0]):
                    return False
                else:
                    continue
            return True


# 判断每个结点是否相似
# 根据组件类型进行相似判断的函数
def CompareNode(node1, node2):
    # if node1.type == node2 and node1.flag == node2.flag:
    #     type = node1.type
    #     if type in ("intersection", "laneswitch", "roundabout", "tJunction", "fork"):
    #         return True
    #     else:  # 以下三类需要补充特殊情况 之后补充
    #         if type in ("curve", "ulane", "straightlane"):
    #             if node1.function == node2.function and node1.direction == node2.direction:
    #                 return True
    #             else:
    #                 return False
    if node1.type == node2.type:  # 第一步判断type，必须一致
        type = node1.type
        if type in ("intersection", "laneswitch", "roundabout", "tJunction", "fork"):  # 这几种组件，必须保证type和flag完全一致才视为相似
            if node1.flag == node2.flag:
                # print("node1.flag = ", node1.flag)
                # print("node2.flag = ", node2.flag)
                return True
        else:
            if node1.flag[-3:] == node2.flag[-3:]:  # 利用切片找出车道数是否一直，车道数一致则视为flag一致
                if type == "straightlane":
                    return True
                if type == "ulane":
                    if node1.direction == node2.direction:
                        return True
                if type == "curve":
                    if node1.direction == node2.direction and node1.function == node2.function:
                        return True
    return False


# 比较结点相似度时的Node数据结构
class NodeMsg:
    def __init__(self, id, type, flag, function, direction):
        self.id = id
        self.flag = flag
        self.type = type
        self.function = function
        self.direction = direction
        self.edge = []

    def add_edge(self, type):
        self.edge.append(type)

    def __str__(self):
        return f"Node(ID={self.id}, Type='{self.type}' flag = {self.flag} function = {self.function} direction = {self.direction}  Edge = '{self.edge}')"


# 比较结点相似度时的Graph数据结构
class GraphNodeMsg:
    def __init__(self, size):
        self.Nodelist = []
        self.size = size
        for i in range(size):
            tmpnode = NodeMsg(i + 1, "unknown", "unknown", "unknown", "unknown")
            self.Nodelist.append(tmpnode)

    def printMsg(self):
        for i in range(self.size):
            print(self.Nodelist[i])
