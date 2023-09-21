import pickle
from func.WidgetGraph import Node, WidgetGraph
import os


class GetBaseSimilarity:
    def __init__(self, graph_dir, graph_size):
        self.graph_dir = graph_dir
        self.graph_name = os.listdir(self.graph_dir)
        EdgesSimilarity = 0  # 边的总相似度
        NodesSimilarity = 0  # 点的总相似度
        EdgesDeSimilarity = 0  # 去重边的总相似度
        NodesDeSimilarity = 0  # 去重点的总相似度
        EdgesCurList = []
        NodesCurList = []
        CurList = []
        EdgesCurList.append(self.graph_dir + '/' + 'AGM' + str(1) + '.pkl')
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
        #         EdgeSimilarity = GraphBaseSimilarity(gsfile1, graph).EdgeSimilarity()  # 两个图边的相似度
        #         if EdgeSimilarity != 1:
        #             tmpcount += 1 #统计有效比较的次数
        #             tmpsum += EdgeSimilarity
        #         if EdgeSimilarity == 1:
        #             flag = 0  # 标识这个应该被剔除
        #             break
        #     #print(EdgesCurList)
        #     if flag == 1:  # 不需要被去重
        #         EdgesDeSimilarity += tmpsum
        #         edgecount += tmpcount #没被去除，此次为有效比较，加入count
        #         EdgesCurList.append(gsfile1)
        #     else:
        #         continue
        #         #print("重复，已被剔除...")
        # EdgesDeSizeV1 = len(EdgesCurList)
        # 点的去重相似度
        # for i in range(1,graph_size):
        #     flag = 1
        #     gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
        #     tmpsum = 0 #这一轮有可能要加上的相似度
        #     tmpcount = 0 #这一轮有可能要加上的比较次数
        #     for graph in NodesCurList:
        #         NodeSimilarity = GraphBaseSimilarity(gsfile1, graph).NodeSimilarity()
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
        # 计算不去重的相似度
        for i in range(0, graph_size + 1):
            for j in range(i + 1, graph_size + 1):
                gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
                gsfile2 = self.graph_dir + '/' + 'AGM' + str(j + 1) + '.pkl'
                # 边相似度===========
                EdgeSimilarity = GraphBaseSimilarity(gsfile1, gsfile2).EdgeSimilarity()  # 两条边间的相似度
                # 点相似度========
                NodeSimilarity = GraphBaseSimilarity(gsfile1, gsfile2).NodeSimilarity()
                EdgesSimilarity += EdgeSimilarity
                NodesSimilarity += NodeSimilarity

        # 按边和点相似度都为1来去重进行相似度计算
        CmpNodesSimilarity = 0
        CmpEdgesSimilarity = 0
        for i in range(1, graph_size):
            flag = 1
            gsfile1 = self.graph_dir + '/' + 'AGM' + str(i + 1) + '.pkl'
            for graph in CurList:
                NodeSimilarity = GraphBaseSimilarity(gsfile1, graph).NodeSimilarity()
                EdgeSimilarity = GraphBaseSimilarity(gsfile1, graph).EdgeSimilarity()
                if not (NodeSimilarity == 1 and EdgeSimilarity == 1):
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                CurList.append(gsfile1)
            else:
                # print("去重，被剔除...")
                continue
        CmpDeSize = len(CurList)  # 综合去重后的结果
        if CmpDeSize != graph_size: #计算去重后的相似度
            for i in range(0,CmpDeSize):
                for j in range(i+1,CmpDeSize):
                    NodeSimilarity = GraphBaseSimilarity(CurList[i], CurList[j]).NodeSimilarity()
                    EdgeSimilarity = GraphBaseSimilarity(CurList[i], CurList[j]).EdgeSimilarity()
                    CmpNodesSimilarity += NodeSimilarity
                    CmpEdgesSimilarity += EdgeSimilarity





        print("图的总数为 = ", graph_size)
        print("去重后图的个数为 = ", CmpDeSize)
        # print("·····································")
        # print("按边去重后图的个数为 = ", EdgesDeSizeV1)
        # print("去重后边的平均相似度 = ", EdgesDeSimilarity / edgecount)
        print("不去重边的平均相似度 = ", EdgesSimilarity / (graph_size * (graph_size - 1) / 2))
        # print("·····································")
        # print("按点去重后图的个数为 = ", NodesDeSizeV1)
        # print("去重后点的平均相似度 = ", NodesDeSimilarity / nodecount)
        print("不去重点的平均相似度 = ", NodesSimilarity / (graph_size * (graph_size - 1) / 2))
        # print("·····································")
        if graph_size == CmpDeSize:  # 说明没有去重，直接输出不去重的结果
            print("去重后边的平均相似度 = ", EdgesSimilarity / (graph_size * (graph_size - 1) / 2))
            print("去重后点的平均相似度 = ", NodesSimilarity / (graph_size * (graph_size - 1) / 2))
        else:
            print("去重后边平均相似度 = ", CmpEdgesSimilarity / (CmpDeSize*(CmpDeSize - 1)/2))
            print("去重后点平均相似度 = ", CmpNodesSimilarity / (CmpDeSize*(CmpDeSize - 1)/2))

        #         # 点相似度===========
        #         NodeSimilarity = GraphBaseSimilarity(gsfile1, gsfile2).NodeSimilarity()
        #         if NodeSimilarity != 1:
        #             NodesDeSimilarity += NodeSimilarity
        #             NodesSimilarity += NodeSimilarity  # 累加两两之间的点相似度
        #         else:
        #             NodesDeSizeV1 -= 1  # 点的相似度为 1，执行去重
        #             NodesSimilarity += 1  # 不去重的相似度 继续加1
        # print("图总数量 = ", graph_size)
        # print("按边去重后数量 = ", EdgesDeSizeV1)
        # print("按点去重后数量 = ", NodesDeSizeV1)
        # print("不去重边的平均相似度 = ", EdgesSimilarity / (graph_size*graph_size))
        # print("去重后边的平均相似财务系统上绑定自己的卡号度 = ", EdgesSimilarity)
        # print("不去重点的平均相似度 = ", NodesSimilarity / (graph_size*graph_size))
        # print("去重后点的平均相似度 = ", NodesSimilarity)

        # print(self.graph_name[i] + ' + ' + self.graph_name[j] + " 的边相似度 = ", Edgesimilarity)
        # print(self.graph_name[i] + ' + ' + self.graph_name[j] + " 的点相似度 = ", Nodesimilarity)
        # print("------------------------------")


class GraphBaseSimilarity:
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
        list1 = []
        list2 = []
        for i, edge in enumerate(edgelist1):
            if i % 2 == 0:
                list1.append(edge[0].type[0] + "-" + edge[1][0].type[0])
                # print(edge[0].type[0],edge[1][0].type[0]
            else:
                continue
        # print(list1)
        # print("=============")
        new_list1 = []
        for edge in list1:  # 把边顺序归一
            if edge[0] > edge[-1]:
                edge = edge[::-1]
            new_list1.append(edge)
        # print(new_list1)
        for i, edge in enumerate(edgelist2):
            if i % 2 == 0:
                list2.append(edge[0].type[0] + "-" + edge[1][0].type[0])
            else:
                continue
        new_list2 = []
        for edge in list2:
            if edge[0] > edge[-1]:
                edge = edge[::-1]
            new_list2.append(edge)
        count = len(new_list1) + len(new_list2)
        # print(new_list1)
        # print(new_list2)
        similar = 0
        for edge in new_list1:
            if edge in new_list2:
                similar = similar + 1
            else:
                continue
        similarity = 2 * similar / count
        return similarity

    def NodeSimilarity(self):
        nodelist1 = self.data1.get_nodes()
        nodelist2 = self.data2.get_nodes()
        len1 = len(nodelist1)
        len2 = len(nodelist2)
        G1 = GraphNodeMsg(len1)
        # G1.printMsg()
        G2 = GraphNodeMsg(len2)
        edgelist1 = self.data1.get_edges()
        edgelist2 = self.data2.get_edges()
        # print(edgelist1)
        for edge in edgelist1:
            # print(edge)
            cur_id = edge[0].id
            cur_type = edge[0].type
            G1.Nodelist[cur_id - 1].type = cur_type
            G1.Nodelist[cur_id - 1].add_edge(Node(0, edge[1][0].type, 1, 1, 1))
            # 存储边结点的时候不考虑ID，统一置为0
        # G1.printMsg()
        #
        for edge in edgelist2:
            cur_id = edge[0].id
            cur_type = edge[0].type
            G2.Nodelist[cur_id - 1].type = cur_type
            G2.Nodelist[cur_id - 1].add_edge(Node(0, edge[1][0].type, 1, 1, 1))
        # G2.printMsg()
        similarity = CompareGraphNode(G1, G2).comparenode()
        # print(similarity)
        # print("结点相似度 = ", similarity / len1)
        return similarity * 2 / (len1 + len2)


class CompareGraphNode:
    def __init__(self, G1, G2):
        self.G2 = G2
        self.G1 = G1

    def comparenode(self):
        similarity = 0
        for node1 in self.G1.Nodelist:
            for node2 in self.G2.Nodelist:
                if self.similar(node1, node2):
                    similarity += 1
        return similarity

    def similar(self, node1, node2):
        if node1.type == node2.type and len(node1.edge) == len(node2.edge):
            strnode1 = ""
            for node in node1.edge:
                strnode1 = strnode1 + node.type[0]
            strnode1 = ''.join(sorted(strnode1))
            # print(strnode1)
            strnode2 = ""
            for node in node2.edge:
                strnode2 = strnode2 + node.type[0]
            strnode2 = ''.join(sorted(strnode2))
            if strnode1 == strnode2:
                return True
            else:
                return False
        return False


# 比较结点相似度时的Node数据结构
class NodeMsg:
    def __init__(self, type, id):
        self.id = id
        self.type = type
        self.edge = []

    def add_edge(self, type):
        self.edge.append(type)

    def __str__(self):
        return f"Node(ID={self.id}, Type='{self.type}' Edge = '{self.edge}')"


# 比较结点相似度时的Graph数据结构
class GraphNodeMsg:
    def __init__(self, size):
        self.Nodelist = []
        self.size = size
        for i in range(size):
            tmpnode = NodeMsg("unknown", i + 1)
            self.Nodelist.append(tmpnode)

    def printMsg(self):
        for i in range(self.size):
            print(self.Nodelist[i])
        print("============================================")
