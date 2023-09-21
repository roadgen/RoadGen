class Node:
    def __init__(self, id, type, flag, function, direction):
        self.id = id
        self.type = type
        self.flag = flag
        self.function = function
        self.direction = direction

    def __repr__(self):
        return f"Node(ID={self.id}, Type='{self.type}',flag = {self.flag} function={self.function},direction={self.direction})"
        # return f"Node(ID={self.id}, Type='{self.type}')"





class WidgetGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, id, type, flag, function, direction):
        if id not in self.nodes:
            node = Node(id, type, flag, function, direction)
            self.nodes[id] = node
            self.edges[node] = []

    def add_edge(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            node1 = self.nodes[id1]
            node2 = self.nodes[id2]
            if [node2, 1] not in self.edges[node1]:
                self.edges[node1].append([node2,1])
            if [node1, 0] not in self.edges[node2]:  # 如果是有向图，这行可以去掉
                self.edges[node2].append([node1,0])

    def get_nodes(self):
        return list(self.nodes.values())

    def get_edges(self):
        return [(k, v) for k in self.edges for v in self.edges[k]]

    def __str__(self):
        result = "Nodes:\n"
        result += ", ".join(str(node) for node in self.nodes.values())
        result += "\nEdges:\n"
        result += ", ".join(f"{str(k)} -> {str(v)}" for k in self.edges for v in self.edges[k])
        return result


#
# G = WidgetGraph()
# n1 = Node(1,'a','1','1','1')
# G.add_node(1,'a','1','1','1')
# n2 = Node(2,'b','1','1','1')
# G.add_node(2,'b','1','1','1')
# n3 = Node(3,'a','1','1','1')
# G.add_node(3,'a','1','1','1')
# G.add_edge(1,2)
# G.add_edge(3,1)
# # print(G.get_nodes())
# print(G)