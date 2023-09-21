class ConnectorQueue:
    def __init__(self):
        self.list = []

    # 入队
    def enqueue(self, item):
        self.list.append(item)

    # 出队
    def dequeue(self):
        a = self.list[0]
        self.list.pop(0)
        return a

    # 判断是否为空
    def isempty(self):
        return len(self.list) == 0

    # 队列长度
    def length(self):
        return len(self.list)

    # 打印队列
    def print_queue(self):
        print(self.list)

    # 从队头元素开始打印队列
    def print_element(self):
        for i in self.list:
            print(i)