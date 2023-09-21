import math

from func.printAuto import printAutoInd
from func.widget import Widget
from ArcLane_widget.arcLane import ArcLane
from Intersection_widget.straightLaneConnection import StraightLaneConnection


class Intersection(Widget):
    WidgetID = 1
    ID = 1  
    Start = (0, 0) 
    Width = 3.5
    StartLaneID = 1 
    StartBoundaryID = 1  
    OuterLaneNumber = [1, 1, 1, 1]  
    InnerLaneNumber = 1  
    BoundaryNumber = 1
    k = '+0'  
    Flag = ''  
    GeometryPoints = []  

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.ID = Widget.JunctionID
        self.Start1 = dict1.get('Start')
        self.Width = dict1.get('Width')
        self.Start = (self.Start1[0], self.Start1[1] + self.Width / 2)
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.OuterLaneNumber = dict1.get('OuterLaneNumber')
        self.InnerLaneNumber = dict1.get('InnerLaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        self.k = dict1.get('K')
        self.Flag = dict1.get('Flag')
        self.GeometryPoints = self.getGeometryPoints()
        self.Type = dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag
        Currents_info["CurrentLanes"] = []
        if self.Flag == '双向双车道十字路口':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID + 12, self.StartLaneID + 14))
            Currents_info["Type"] = '双向实线双行道'
        if self.Flag == '四车道十字路口':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID + 12, self.StartLaneID + 16))
            Currents_info["Type"] = '双黄实线虚实四车道'
        if self.Flag == '六车道十字路口':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID + 12, self.StartLaneID + 18))
            Currents_info["Type"] = '双实线虚虚实实六车道'
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        edgelist = self.getEdgePoint()
        if self.Flag == '双向双车道十字路口':
            Next1 = dict()
            Next1['current'] = self.Flag + '_' + self.Type
            Next1['ID'] = self.WidgetID
            endpoint = (float('{:.3f}'.format(edgelist[1][1][0] + self.Width / 2)), edgelist[1][1][1])
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            Next1['type'] = '双向实线双行道'
            Next1['lanes'] = [self.StartLaneID + 15, self.StartLaneID + 14]
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_intersection'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width + self.Width * 2)))
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            Next2['type'] = '双向实线双行道'
            Next2['lanes'] = [self.StartLaneID + 16, self.StartLaneID + 17]
            if self.k == '+0':
                Next2['direction'] = '+0'
            elif self.k == '-0':
                Next2['direction'] = '-0'
            elif self.k == '+':
                Next2['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Nexts.append(Next2)

            Next3 = dict()
            Next3['current'] = self.Flag + '_intersection'
            Next3['ID'] = self.WidgetID
            endpoint = (float('{:.3f}'.format(edgelist[0][0][0] - self.Width / 2)), edgelist[0][0][1])
            Next3['endpoint'] = self.roate_endpoints(endpoint)
            Next3['type'] = '双向实线双行道'
            Next3['lanes'] = [self.StartLaneID + 19, self.StartLaneID + 18]
            if self.k == '+0':
                Next3['direction'] = '+'
            elif self.k == '-0':
                Next3['direction'] = '-'
            elif self.k == '+':
                Next3['direction'] = '-0'
            elif self.k == '-':
                Next3['direction'] = '+0'
            Nexts.append(Next3)
        elif self.Flag == '四车道十字路口':
            Next1 = dict()
            Next1['current'] = self.Flag + '_intersection'
            Next1['ID'] = self.WidgetID
            endpoint = (float('{:.3f}'.format(edgelist[3][1][0] + self.Width / 2)), edgelist[3][1][1])
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            Next1['type'] = '双黄实线虚实四车道'
            Next1['lanes'] = [self.StartLaneID + 19, self.StartLaneID + 18, self.StartLaneID + 17,
                              self.StartLaneID + 16]
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_intersection'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width + self.Width * 4)))
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            Next2['type'] = '双黄实线虚实四车道'
            Next2['lanes'] = [self.StartLaneID + 20, self.StartLaneID + 21, self.StartLaneID + 22,
                              self.StartLaneID + 23]
            if self.k == '+0':
                Next2['direction'] = '+0'
            elif self.k == '-0':
                Next2['direction'] = '-0'
            elif self.k == '+':
                Next2['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Nexts.append(Next2)

            Next3 = dict()
            Next3['current'] = self.Flag + '_intersection'
            Next3['ID'] = self.WidgetID
            endpoint = (float('{:.3f}'.format(edgelist[0][0][0] - self.Width / 2)), edgelist[0][0][1])
            Next3['endpoint'] = self.roate_endpoints(endpoint)
            Next3['type'] = '双黄实线虚实四车道'
            Next3['lanes'] = [self.StartLaneID + 27, self.StartLaneID + 26, self.StartLaneID + 25,
                              self.StartLaneID + 24]
            if self.k == '+0':
                Next3['direction'] = '+'
            elif self.k == '-0':
                Next3['direction'] = '-'
            elif self.k == '+':
                Next3['direction'] = '-0'
            elif self.k == '-':
                Next3['direction'] = '+0'
            Nexts.append(Next3)
        elif self.Flag == '六车道十字路口':
            Next1 = dict()
            Next1['current'] = self.Flag + '_intersection'
            Next1['ID'] = self.WidgetID
            endpoint = (float('{:.3f}'.format(edgelist[5][1][0] + self.Width / 2)), edgelist[5][1][1])
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            Next1['type'] = '双实线虚虚实实六车道'
            Next1['lanes'] = [self.StartLaneID + 23, self.StartLaneID + 22, self.StartLaneID + 21,
                              self.StartLaneID + 20, self.StartLaneID + 19, self.StartLaneID + 18]
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_intersection'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width + self.Width * 6)))
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            Next2['type'] = '双实线虚虚实实六车道'
            Next2['lanes'] = [self.StartLaneID + 24, self.StartLaneID + 25, self.StartLaneID + 26,
                              self.StartLaneID + 27, self.StartLaneID + 18, self.StartLaneID + 29]
            if self.k == '+0':
                Next2['direction'] = '+0'
            elif self.k == '-0':
                Next2['direction'] = '-0'
            elif self.k == '+':
                Next2['direction'] = '+'
            elif self.k == '-':
                Next2['direction'] = '-'
            Nexts.append(Next2)

            Next3 = dict()
            Next3['current'] = self.Flag + '_' + self.Type
            Next3['ID'] = self.WidgetID
            endpoint = (float('{:.3f}'.format(edgelist[0][0][0] - self.Width / 2)), edgelist[0][0][1])
            Next3['endpoint'] = self.roate_endpoints(endpoint)
            Next3['type'] = '双实线虚虚实实六车道'
            Next3['lanes'] = [self.StartLaneID + 35, self.StartLaneID + 34, self.StartLaneID + 33,
                              self.StartLaneID + 32, self.StartLaneID + 31, self.StartLaneID + 30]
            if self.k == '+0':
                Next3['direction'] = '+'
            elif self.k == '-0':
                Next3['direction'] = '-'
            elif self.k == '+':
                Next3['direction'] = '-0'
            elif self.k == '-':
                Next3['direction'] = '+0'
            Nexts.append(Next3)
        return Nexts

    def get_coveredArea(self):
        edgePoints = self.getEdgePoint()
        result = []
        point1 = (float("{:.3f}".format(edgePoints[0][0][0] - self.Width / 2)),
                  float("{:.3f}".format(edgePoints[0][0][1] - self.Width / 2 * 2 - self.Width / 4)))
        point2 = (float("{:.3f}".format(edgePoints[0][1][0] + self.Width / 2)),
                  float("{:.3f}".format(edgePoints[0][1][1] - self.Width / 2 * 2 - self.Width / 4)))
        point3 = (float("{:.3f}".format(edgePoints[-1][1][0] + self.Width / 2)),
                  float("{:.3f}".format(edgePoints[-1][1][1] + self.Width / 2 * 2 + self.Width / 4)))
        point4 = (float("{:.3f}".format(edgePoints[-1][0][0] - self.Width / 2)),
                  float("{:.3f}".format(edgePoints[-1][0][1] + self.Width / 2 * 2 + self.Width / 4)))

        result.append(point1)
        result.append(point2)
        result.append(point3)
        result.append(point4)

        tmp = [result]
        finalResult = self.rotation(tmp)
        return (finalResult)

    def roate_endpoints(self, point):
        if self.k == '+':
            return point
        if self.k == '+0':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start1[0]) * int(math.cos(math.pi / 2)) + (point[1] - self.Start1[1]) * int(
                    math.sin(math.pi / 2)) + self.Start1[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start1[1]) * int(math.cos(math.pi / 2)) - (point[0] - self.Start1[0]) * int(
                    math.sin(math.pi / 2)) + self.Start1[1]))
            return x, y
        if self.k == '-':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start1[0]) * int(math.cos(math.pi)) + (point[1] - self.Start1[1]) * int(
                    math.sin(math.pi)) + self.Start1[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start1[1]) * int(math.cos(math.pi)) - (point[0] - self.Start1[0]) * int(
                    math.sin(math.pi)) + self.Start1[1]))
            return x, y
        if self.k == '-0':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start1[0]) * int(math.cos(math.pi * 1.5)) + (point[1] - self.Start1[1]) * int(
                    math.sin(math.pi * 1.5)) + self.Start1[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start1[1]) * int(math.cos(math.pi * 1.5)) - (point[0] - self.Start1[0]) * int(
                    math.sin(math.pi * 1.5)) + self.Start1[1]))
            return x, y

    def rotation(self, pointlist):
        if self.k == '+':
            return pointlist
        if self.k == '+0':  
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start1[0]) * int(math.cos(math.pi / 2)) + (j[1] - self.Start1[1]) * int(
                            math.sin(math.pi / 2)) + self.Start1[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start1[1]) * int(math.cos(math.pi / 2)) - (j[0] - self.Start1[0]) * int(
                            math.sin(math.pi / 2)) + self.Start1[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == '-':  
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start1[0]) * int(math.cos(math.pi)) + (j[1] - self.Start1[1]) * int(
                            math.sin(math.pi)) + self.Start1[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start1[1]) * int(math.cos(math.pi)) - (j[0] - self.Start1[0]) * int(
                            math.sin(math.pi)) + self.Start1[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == '-0':  
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start1[0]) * int(math.cos(math.pi * 1.5)) + (j[1] - self.Start1[1]) * int(
                            math.sin(math.pi * 1.5)) + self.Start1[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start1[1]) * int(math.cos(math.pi * 1.5)) - (j[0] - self.Start1[0]) * int(
                            math.sin(math.pi * 1.5)) + self.Start1[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        else:
            print('The function is wrong')

    def PointtoString(self, lst):
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def getGeometryPoints(self):
        pointlist = []
        # if self.k=='+':
        start = (
            float("{:.3f}".format(self.Start[0] - self.Width / 2 - self.Width / 4)),
            self.Start[1],
        )
        pointlist.append(start)
        pointlist.append(
            (
                float(
                    "{:.3f}".format(
                        start[0] + self.Width * self.OuterLaneNumber[0] + self.Width / 2
                    )
                ),
                start[1],
            )
        )
        pointlist.append(
            (
                float(
                    "{:.3f}".format(
                        start[0] + self.Width * self.OuterLaneNumber[0] + self.Width / 2
                    )
                ),
                start[1] + self.Width * self.OuterLaneNumber[1] + self.Width / 2,
            )
        )
        pointlist.append(
            (
                start[0],
                float(
                    "{:.3f}".format(
                        start[1] + self.Width * self.OuterLaneNumber[1] + self.Width / 2
                    )
                ),
            )
        )
        result = []
        result.append(pointlist)
        return result

    def getEdgePoint(self):
        edgelist = []
        for i in range(self.OuterLaneNumber[1]):
            tmp = []
            tmp.append((float('{:.3f}'.format(self.Start[0] - self.Width / 2 - self.Width / 4)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 4 + self.Width * (2 * i + 1) / 2))))
            tmp.append((float('{:.3f}'.format(
                self.Start[0] + self.Width / 2 + self.Width * (self.OuterLaneNumber[0] - 1) + self.Width / 4)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 4 + self.Width * (2 * i + 1) / 2))))

            edgelist.append(tmp)
        return (edgelist)

    def getLaneInfoList(self):
        laneInfolist = []

        lanelist = []
        boundarylist = []
        indexes = []
        laneObjects = []

        directions = []
        successors = []
        predecessors = []
        alignment = []
        flag = self.Flag
        edgelist = self.getEdgePoint()

        if flag == "双向双车道十字路口":
            # turn right1
            dict1 = {
                'ID': self.StartLaneID,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width)), self.Start[1]),
                'End': edgelist[0][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID,
                'BoundaryId2': self.StartBoundaryID + 1,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '+0',
                'Flag': '上右转'
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
           
            alignment.append(['Forward', 'Forward'])
            # turn left1
            dict2 = {
                'ID': self.StartLaneID + 1,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width)), self.Start[1]),
                'End': edgelist[1][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 2,
                'BoundaryId2': self.StartBoundaryID + 3,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '-0',
                'Flag': '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(['Forward', 'Forward'])
            # turn right2
            dict3 = {
                'ID': self.StartLaneID + 2,
                'Start': edgelist[1][1],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 2))),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 4,
                'BoundaryId2': self.StartBoundaryID + 5,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '+',
                'Flag': '左右转'
            }
            # print(dict1)
            tmpArc3 = ArcLane(dict3)
            lanelist.append(tmpArc3.lanePoints)
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            
            alignment.append(['Forward', 'Forward'])
            # turn left2
            dict4 = {
                'ID': self.StartLaneID + 3,
                'Start': edgelist[1][1],
                'End': self.Start,
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID,
                'BoundaryId2': self.StartBoundaryID + 6,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '-',
                'Flag': '左左转'
            }
            # print(dict1)
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            # boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((0, 6))
            laneObjects.append(tmpArc4)
            
            alignment.append(['Backward', 'Forward'])

            # turn right3
            dict5 = {
                'ID': self.StartLaneID + 4,
                'Start': (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 2))),
                'End': edgelist[1][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 7,
                'BoundaryId2': self.StartBoundaryID + 8,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '-0',
                'Flag': '下右转'
            }
            tmpArc5 = ArcLane(dict5)
            lanelist.append(tmpArc5.lanePoints)
            boundarylist.append(tmpArc5.boundaryPoints[0])
            boundarylist.append(tmpArc5.boundaryPoints[1])
            directions.append(tmpArc5.TravelDirection)
            indexes.append((7, 8))
            laneObjects.append(tmpArc5)
            alignment.append(['Forward', 'Forward'])
            # turn left3
            dict6 = {
                'ID': self.StartLaneID + 5,
                'Start': (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 2))),
                'End': edgelist[0][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 4,
                'BoundaryId2': self.StartBoundaryID + 9,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '+0',
                'Flag': '下左转'
            }
            tmpArc6 = ArcLane(dict6)
            lanelist.append(tmpArc6.lanePoints)
            # boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc6.boundaryPoints[1])
            directions.append(tmpArc6.TravelDirection)
            indexes.append((4, 9))
            laneObjects.append(tmpArc6)
            alignment.append(['Backward', 'Forward'])

            # turn right4
            dict7 = {
                'ID': self.StartLaneID + 6,
                'Start': edgelist[0][0],
                'End': self.Start,
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 2,
                'BoundaryId2': self.StartBoundaryID + 10,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '-',
                'Flag': '右右转'
            }
            tmpArc7 = ArcLane(dict7)
            lanelist.append(tmpArc7.lanePoints)
            # boundarylist.append(tmpArc7.boundaryPoints[0])
            boundarylist.append(tmpArc7.boundaryPoints[1])
            directions.append(tmpArc7.TravelDirection)
            indexes.append((2, 10))
            laneObjects.append(tmpArc7)
            alignment.append(['Backward', 'Forward'])
            # turn left4
            dict8 = {
                'ID': self.StartLaneID + 7,
                'Start': edgelist[0][0],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 2))),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 7,
                'BoundaryId2': self.StartBoundaryID + 11,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '+',
                'Flag': '右左转'
            }
            tmpArc8 = ArcLane(dict8)
            lanelist.append(tmpArc8.lanePoints)
            # boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc8.boundaryPoints[1])
            directions.append(tmpArc8.TravelDirection)
            indexes.append((7, 11))
            laneObjects.append(tmpArc8)
            alignment.append(['Backward', 'Forward'])

            # straight1
            dict9 = {
                'ID': self.StartLaneID + 8,
                'Start': edgelist[0][0],
                'End': edgelist[0][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 12,  # 共用
                'BoundaryId2': self.StartBoundaryID + 13,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '+0',
                'Flag': '左至右'
            }
            tmpStraight1 = StraightLaneConnection(dict9)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((12, 13))
            laneObjects.append(tmpStraight1)
            alignment.append(['Forward', 'Forward'])

            # straight2
            dict10 = {
                'ID': self.StartLaneID + 9,
                'Start': edgelist[1][1],
                'End': edgelist[1][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 12,  # reuse
                'BoundaryId2': self.StartBoundaryID + 14,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '-0',
                'Flag': '右至左'
            }
            tmpStraight2 = StraightLaneConnection(dict10)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((12, 14))
            laneObjects.append(tmpStraight2)
            alignment.append(['Backward', 'Forward'])

            # straight3
            dict11 = {
                'ID': self.StartLaneID + 10,
                'Start': (self.Start[0], self.Start[1] + self.Width / 2 + self.Width * 2),
                'End': self.Start,
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 16,  # 共用
                'BoundaryId2': self.StartBoundaryID + 15,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '-',
                'Flag': '上至下'
            }
            tmpStraight3 = StraightLaneConnection(dict11)
            lanelist.append(tmpStraight3.lanePoints)
            # boundarylist.append(tmpStraight3.boundaryPoints[0])
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((16, 15))
            laneObjects.append(tmpStraight3)
            alignment.append(['Backward', 'Forward'])

            # straight4
            dict12 = {
                'ID': self.StartLaneID + 11,
                'Start': (self.Start[0] + self.Width, self.Start[1]),
                'End': (self.Start[0] + self.Width, self.Start[1] + self.Width / 2 + self.Width * 2),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 16,  # reuse
                'BoundaryId2': self.StartBoundaryID + 17,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '+',
                'Flag': '下至上'
            }
            tmpStraight4 = StraightLaneConnection(dict12)
            tmpBoundarys = []
            # tmpBoundarys.append(tmpStraight3.boundaryPoints[0])
            # tmpBoundarys.append(tmpStraight4.boundaryPoints[1])
            # tmpStraight4.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[0])
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append(tmpStraight4.TravelDirection)
            indexes.append((16, 17))
            laneObjects.append(tmpStraight4)
            alignment.append(['Forward', 'Forward'])

            # outer road
            # major direction1
            lane1 = [self.Start, (self.Start[0], self.Start[1] - self.Width / 4),
                     (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            lanelist.append(lane1)
            boundary1 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2, self.Start[1])]
            boundary2 = [(self.Start[0] - self.Width / 2, self.Start[1]),
                         (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:8
            indexes.append((18, 19))
            directions.append("Forward")
            
            successors.append((10, 12))
            predecessors.append((12, 10))
            successors.append((6, 12))
            predecessors.append((12, 6))
            successors.append((3, 12))
            predecessors.append((12, 3))
            alignment.append(['Backward', 'Forward'])

            # major direction2
            lane2 = [(float("{:.3f}".format(self.Start[0] + self.Width)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                     (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                     (self.Start[0] + self.Width, self.Start[1])]
            lanelist.append(lane2)
            boundary3 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2 + self.Width, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2 + self.Width, self.Start[1])]
            boundarylist.append(boundary3)
            indexes.append((18, 20))
            directions.append("Forward")
            successors.append((13, 11))
            predecessors.append((11, 13))
            successors.append((13, 0))
            predecessors.append((0, 13))
            successors.append((13, 1))
            predecessors.append((1, 13))
            alignment.append(['Forward', 'Forward'])

            # right road1
            lane3 = [edgelist[0][1], (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                     (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)), edgelist[0][1][1])]
            lanelist.append(lane3)
            boundary4 = [(edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                         (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1] + self.Width / 2),
                         (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)))]
            boundary5 = [(edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                         (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1] - self.Width / 2),
                         (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)))]
            boundarylist.append(boundary4)  # reuse id:10
            boundarylist.append(boundary5)
            indexes.append((21, 22))
            directions.append("Forward")
            successors.append((8, 14))
            predecessors.append((14, 8))
            successors.append((0, 14))
            predecessors.append((14, 0))
            successors.append((5, 14))
            predecessors.append((14, 5))
            alignment.append(['Forward', 'Forward'])

            # right road2
            lane4 = [(float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)), edgelist[1][1][1]),
                     (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]), edgelist[1][1]]
            lanelist.append(lane4)
            boundary6 = [(float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2))),
                         (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1] + self.Width / 2),
                         (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2)]
            boundarylist.append(boundary6)  
            indexes.append((21, 23))
            directions.append("Forward")
            successors.append((15, 9))
            predecessors.append((9, 15))
            successors.append((15, 2))
            predecessors.append((2, 15))
            successors.append((15, 3))
            predecessors.append((3, 15))
            alignment.append(['Backward', 'Forward'])

            # upper1
            lane5 = [(self.Start[0],
                      float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 2))),
                     (self.Start[0], self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 4),
                     (self.Start[0], self.Start[1] + self.Width / 2 + self.Width * 2)]
            lanelist.append(lane5)
            boundary7 = [(self.Start[0] + self.Width / 2, self.Start[1] + self.Width / 2 + self.Width * 2),
                         (self.Start[0] + self.Width / 2,
                          self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 2)))]
            boundary8 = [(float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 2))),
                         (self.Start[0] - self.Width / 2,
                          self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 4),
                         (self.Start[0] - self.Width / 2, self.Start[1] + self.Width / 2 + self.Width * 2)]
            boundarylist.append(boundary7)
            boundarylist.append(boundary8)
            indexes.append((24, 25))
            directions.append("Forward")
            successors.append((16, 10))
            predecessors.append((10, 16))
            successors.append((16, 4))
            predecessors.append((4, 16))
            successors.append((16, 5))
            predecessors.append((5, 16))
            alignment.append(['Backward', 'Forward'])
            # upper2
            lane6 = [(self.Start[0] + self.Width, self.Start[1] + self.Width / 2 + self.Width * 2),
                     (self.Start[0] + self.Width, self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 4),
                     (float("{:.3f}".format(self.Start[0] + self.Width)),
                      float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 2)))]
            lanelist.append(lane6)
            boundary9 = [
                (self.Start[0] + self.Width + self.Width / 2, self.Start[1] + self.Width / 2 + self.Width * 2),
                (self.Start[0] + self.Width + self.Width / 2,
                 self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 4),
                (float("{:.3f}".format(self.Start[0] + self.Width + self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 2 + self.Width / 2)))]
            boundarylist.append(boundary9)
            indexes.append((24, 26))
            directions.append("Forward")
            successors.append((11, 17))
            predecessors.append((17, 11))
            successors.append((2, 17))
            predecessors.append((17, 2))
            successors.append((2, 17))
            predecessors.append((17, 2))
            successors.append((7, 17))
            predecessors.append((17, 7))
            alignment.append(['Forward', 'Forward'])

            # left road1
            lane7 = [edgelist[1][0], (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                     (float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)), edgelist[1][0][1])]
            lanelist.append(lane7)
            boundary10 = [(float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2))),
                          (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1] - self.Width / 2),
                          (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2)]
            boundary11 = [(edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
                          (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1] + self.Width / 2),
                          (float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)))]
            boundarylist.append(boundary10)
            boundarylist.append(boundary11)  # reuse,id:14
            indexes.append((27, 28))
            directions.append("Forward")
            successors.append((1, 18))
            predecessors.append((18, 1))
            successors.append((9, 18))
            predecessors.append((18, 9))
            successors.append((4, 18))
            predecessors.append((18, 4))
            alignment.append(['Backward', 'Forward'])

            # left road2
            lane8 = [(float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)), edgelist[0][0][1]),
                     (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]), edgelist[0][0]]
            lanelist.append(lane8)
            boundary12 = [(float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2))),
                          (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1] - self.Width / 2),
                          (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2)]
            boundarylist.append(boundary12)  
            indexes.append((27, 29))
            directions.append("Forward")
            successors.append((19, 8))
            predecessors.append((8, 19))
            successors.append((19, 7))
            predecessors.append((7, 19))
            successors.append((19, 6))
            predecessors.append((6, 19))
            alignment.append(['Forward', 'Forward'])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return (laneInfolist)
        if flag == "四车道十字路口":
            # turn right1
            dict1 = {
                'ID': self.StartLaneID,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width * 3)), self.Start[1]),
                'End': edgelist[0][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID,
                'BoundaryId2': self.StartBoundaryID + 1,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '+0',
                'Flag': '上右转'
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(['Forward', 'Forward'])
            # turn left1
            dict2 = {
                'ID': self.StartLaneID + 1,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width * 2)), self.Start[1]),
                'End': edgelist[2][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 2,
                'BoundaryId2': self.StartBoundaryID + 3,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '-0',
                'Flag': '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(['Forward', 'Forward'])
            # turn right2
            dict3 = {
                'ID': self.StartLaneID + 2,
                'Start': edgelist[3][1],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width * 3)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 4))),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 4,
                'BoundaryId2': self.StartBoundaryID + 5,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '+',
                'Flag': '左右转'
            }
            # print(dict1)
            tmpArc3 = ArcLane(dict3)
            lanelist.append(tmpArc3.lanePoints)
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            
            alignment.append(['Forward', 'Forward'])
            # turn left2
            dict4 = {
                'ID': self.StartLaneID + 3,
                'Start': edgelist[2][1],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width)), self.Start[1]),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 6,
                'BoundaryId2': self.StartBoundaryID + 7,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '-',
                'Flag': '左左转'
            }
            # print(dict1)
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            
            alignment.append(['Forward', 'Forward'])

            # turn right3
            dict5 = {
                'ID': self.StartLaneID + 4,
                'Start': (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 4))),
                'End': edgelist[3][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 8,
                'BoundaryId2': self.StartBoundaryID + 9,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '-0',
                'Flag': '下右转'
            }
            tmpArc5 = ArcLane(dict5)
            lanelist.append(tmpArc5.lanePoints)
            boundarylist.append(tmpArc5.boundaryPoints[0])
            boundarylist.append(tmpArc5.boundaryPoints[1])
            directions.append(tmpArc5.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpArc5)
            alignment.append(['Forward', 'Forward'])
            # turn left3
            dict6 = {
                'ID': self.StartLaneID + 5,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width)),
                          float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 4))),
                'End': edgelist[1][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 10,
                'BoundaryId2': self.StartBoundaryID + 11,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '+0',
                'Flag': '下左转'
            }
            tmpArc6 = ArcLane(dict6)
            lanelist.append(tmpArc6.lanePoints)
            boundarylist.append(tmpArc6.boundaryPoints[0])
            boundarylist.append(tmpArc6.boundaryPoints[1])
            directions.append(tmpArc6.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpArc6)
            alignment.append(['Forward', 'Forward'])

            # turn right4
            dict7 = {
                'ID': self.StartLaneID + 6,
                'Start': edgelist[0][0],
                'End': self.Start,
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 12,
                'BoundaryId2': self.StartBoundaryID + 13,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '-',
                'Flag': '右右转'
            }
            tmpArc7 = ArcLane(dict7)
            lanelist.append(tmpArc7.lanePoints)
            boundarylist.append(tmpArc7.boundaryPoints[0])
            boundarylist.append(tmpArc7.boundaryPoints[1])
            directions.append(tmpArc7.TravelDirection)
            indexes.append((12, 13))
            laneObjects.append(tmpArc7)
            alignment.append(['Forward', 'Forward'])
            # turn left4
            dict8 = {
                'ID': self.StartLaneID + 7,
                'Start': edgelist[1][0],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width * 2)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 4))),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 14,
                'BoundaryId2': self.StartBoundaryID + 15,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '+',
                'Flag': '右左转'
            }
            tmpArc8 = ArcLane(dict8)
            lanelist.append(tmpArc8.lanePoints)
            boundarylist.append(tmpArc8.boundaryPoints[0])
            boundarylist.append(tmpArc8.boundaryPoints[1])
            directions.append(tmpArc8.TravelDirection)
            indexes.append((14, 15))
            laneObjects.append(tmpArc8)
            alignment.append(['Forward', 'Forward'])

            # straight1
            dict9 = {
                'ID': self.StartLaneID + 8,
                'Start': edgelist[1][0],
                'End': edgelist[1][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 16,  # 共用
                'BoundaryId2': self.StartBoundaryID + 17,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '+0',
                'Flag': '左至右'
            }
            tmpStraight1 = StraightLaneConnection(dict9)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((16, 17))
            laneObjects.append(tmpStraight1)
            alignment.append(['Forward', 'Forward'])

            # straight2
            dict10 = {
                'ID': self.StartLaneID + 9,
                'Start': edgelist[2][1],
                'End': edgelist[2][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 16,  # reuse
                'BoundaryId2': self.StartBoundaryID + 18,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '-0',
                'Flag': '右至左'
            }
            tmpStraight2 = StraightLaneConnection(dict10)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((16, 18))
            laneObjects.append(tmpStraight2)
            alignment.append(['Backward', 'Forward'])

            # straight3
            dict11 = {
                'ID': self.StartLaneID + 10,
                'Start': (self.Start[0] + self.Width, self.Start[1] + self.Width / 2 + self.Width * 4),
                'End': (self.Start[0] + self.Width, self.Start[1]),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 20,  # 共用
                'BoundaryId2': self.StartBoundaryID + 19,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '-',
                'Flag': '上至下'
            }
            tmpStraight3 = StraightLaneConnection(dict11)
            lanelist.append(tmpStraight3.lanePoints)
            # boundarylist.append(tmpStraight3.boundaryPoints[0])
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((20, 19))
            laneObjects.append(tmpStraight3)
            alignment.append(['Backward', 'Forward'])

            # straight4
            dict12 = {
                'ID': self.StartLaneID + 11,
                'Start': (self.Start[0] + self.Width * 2, self.Start[1]),
                'End': (self.Start[0] + self.Width * 2, self.Start[1] + self.Width / 2 + self.Width * 4),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 20,  # reuse
                'BoundaryId2': self.StartBoundaryID + 21,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '+',
                'Flag': '下至上'
            }
            tmpStraight4 = StraightLaneConnection(dict12)
            tmpBoundarys = []
            # tmpBoundarys.append(tmpStraight3.boundaryPoints[0])
            # tmpBoundarys.append(tmpStraight4.boundaryPoints[1])
            # tmpStraight4.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[0])
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append(tmpStraight4.TravelDirection)
            indexes.append((20, 21))
            laneObjects.append(tmpStraight4)
            alignment.append(['Forward', 'Forward'])

            # outer road
            # major direction1
            lane1 = [self.Start, (self.Start[0], self.Start[1] - self.Width / 4),
                     (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            lanelist.append(lane1)
            boundary1 = [(self.Start[0] + self.Width / 2, self.Start[1]),
                         (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            boundary2 = [(self.Start[0] - self.Width / 2, self.Start[1]),
                         (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:8
            indexes.append((22, 23))
            directions.append("Forward")
            
            successors.append((6, 12))
            predecessors.append((12, 6))
            alignment.append(['Forward', 'Forward'])

            # major direction2
            lane2 = [(self.Start[0] + self.Width, self.Start[1]),
                     (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                     (float("{:.3f}".format(self.Start[0] + self.Width)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            lanelist.append(lane2)
            indexes.append((24, 22))
            directions.append("Forward")
            successors.append((3, 13))
            predecessors.append((13, 3))
            successors.append((10, 13))
            predecessors.append((13, 10))
            alignment.append(['Backward', 'Forward'])
            # major direction3
            lane3 = [(float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                     (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                     (self.Start[0] + self.Width * 2, self.Start[1])]
            lanelist.append(lane3)
            boundary3 = [(float("{:.3f}".format(self.Start[0] - self.Width / 2 + self.Width * 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] - self.Width / 2 + self.Width * 2, self.Start[1] - self.Width / 4),
                         (self.Start[0] - self.Width / 2 + self.Width * 2, self.Start[1])]
            boundary4 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1])]
            boundarylist.append(boundary3)
            boundarylist.append(boundary4)
            indexes.append((24, 25))
            directions.append("Forward")
            successors.append((14, 1))
            predecessors.append((1, 14))
            successors.append((14, 11))
            predecessors.append((11, 14))
            alignment.append(['Forward', 'Forward'])
            # major direction4
            lane4 = [(float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                     (self.Start[0] + self.Width * 3, self.Start[1] - self.Width / 4),
                     (self.Start[0] + self.Width * 3, self.Start[1])]
            lanelist.append(lane4)
            boundary5 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 3)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1])]
            boundarylist.append(boundary5)
            indexes.append((25, 26))
            directions.append("Forward")
            successors.append((15, 0))
            predecessors.append((0, 15))
            alignment.append(['Forward', 'Forward'])

            # right1
            lane5 = [(edgelist[0][1][0], edgelist[0][1][1]),
                     (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                     (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)), edgelist[0][1][1])]
            lanelist.append(lane5)
            boundary6 = [(edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                         (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1] + self.Width / 2),
                         (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)))]
            boundary7 = [(edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                         (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1] - self.Width / 2),
                         (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)))]
            boundarylist.append(boundary6)
            boundarylist.append(boundary7)
            indexes.append((27, 28))
            directions.append("Forward")
            successors.append((0, 16))
            predecessors.append((16, 0))
            alignment.append(['Forward', 'Forward'])
            # right2
            lane6 = [(edgelist[1][1][0], edgelist[1][1][1]),
                     (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                     (float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)), edgelist[1][1][1])]
            lanelist.append(lane6)
            boundary8 = [(edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                         (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1] + self.Width / 2),
                         (float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)))]
            boundarylist.append(boundary8)
            indexes.append((29, 27))
            directions.append("Forward")
            successors.append((5, 17))
            predecessors.append((17, 5))
            successors.append((8, 17))
            predecessors.append((17, 8))
            alignment.append(['Forward', 'Forward'])
            # right3
            lane7 = [(float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)), edgelist[2][1][1]),
                     (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                     (edgelist[2][1][0], edgelist[2][1][1])]
            lanelist.append(lane7)
            boundary9 = [(float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2))),
                         (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1] + self.Width / 2),
                         (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2)]
            boundarylist.append(boundary9)
            indexes.append((29, 30))
            directions.append("Forward")
            successors.append((18, 3))
            predecessors.append((3, 18))
            successors.append((18, 9))
            predecessors.append((9, 18))
            alignment.append(['Backward', 'Forward'])
            # right4
            lane8 = [(float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)), edgelist[3][1][1]),
                     (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                     (edgelist[3][1][0], edgelist[3][1][1])]
            lanelist.append(lane8)
            boundary10 = [(float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                           float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2))),
                          (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1] + self.Width / 2),
                          (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2)]
            boundarylist.append(boundary10)
            indexes.append((30, 31))
            directions.append("Forward")
            successors.append((19, 2))
            predecessors.append((2, 19))
            alignment.append(['Forward', 'Forward'])
            # upper1
            lane9 = [(self.Start[0],
                      float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2))),
                     (self.Start[0], self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                     (self.Start[0], self.Start[1] + self.Width * 4 + self.Width / 2)]
            lanelist.append(lane9)
            boundary11 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                           float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2))),
                          (self.Start[0] + self.Width / 2,
                           self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                          (self.Start[0] + self.Width / 2, self.Start[1] + self.Width * 4 + self.Width / 2)]
            boundary12 = [(float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                           float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2))),
                          (self.Start[0] - self.Width / 2,
                           self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                          (self.Start[0] - self.Width / 2, self.Start[1] + self.Width * 4 + self.Width / 2)]
            boundarylist.append(boundary11)
            boundarylist.append(boundary12)
            indexes.append((32, 33))
            directions.append("Forward")
            successors.append((20, 4))
            predecessors.append((4, 20))
            alignment.append(['Forward', 'Forward'])
            # upper2
            lane10 = [(float("{:.3f}".format(self.Start[0] + self.Width)),
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2))),
                      (self.Start[0] + self.Width, self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                      (self.Start[0] + self.Width, self.Start[1] + self.Width * 4 + self.Width / 2)]
            lanelist.append(lane10)
            indexes.append((34, 32))
            directions.append("Forward")
            successors.append((21, 5))
            predecessors.append((5, 21))
            successors.append((21, 10))
            predecessors.append((10, 21))
            alignment.append(['Backward', 'Forward'])
            # upper3
            lane11 = [(self.Start[0] + self.Width * 2, self.Start[1] + self.Width * 4 + self.Width / 2),
                      (
                      self.Start[0] + self.Width * 2, self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                      (float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2)))]
            lanelist.append(lane11)
            boundary13 = [
                (self.Start[0] + self.Width * 2 - self.Width / 2, self.Start[1] + self.Width * 4 + self.Width / 2),
                (self.Start[0] + self.Width * 2 - self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 2 - self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2)))]
            boundary14 = [
                (self.Start[0] + self.Width * 2 + self.Width / 2, self.Start[1] + self.Width * 4 + self.Width / 2),
                (self.Start[0] + self.Width * 2 + self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 2 + self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2)))]
            boundarylist.append(boundary13)
            boundarylist.append(boundary14)
            indexes.append((34, 35))
            directions.append("Forward")
            successors.append((7, 22))
            predecessors.append((22, 7))
            successors.append((11, 22))
            predecessors.append((22, 11))
            alignment.append(['Forward', 'Forward'])
            # upper4
            lane12 = [(self.Start[0] + self.Width * 3, self.Start[1] + self.Width * 4 + self.Width / 2),
                      (
                      self.Start[0] + self.Width * 3, self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                      (float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2)))]
            lanelist.append(lane12)
            boundary15 = [
                (self.Start[0] + self.Width * 3 + self.Width / 2, self.Start[1] + self.Width * 4 + self.Width / 2),
                (self.Start[0] + self.Width * 3 + self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 4 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 3 + self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 4 + self.Width / 2)))]
            boundarylist.append(boundary15)
            indexes.append((35, 36))
            directions.append("Forward")
            successors.append((2, 23))
            predecessors.append((23, 2))
            alignment.append(['Forward', 'Forward'])
            # left1
            lane13 = [(edgelist[3][0][0], edgelist[3][0][1]),
                      (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                      (float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)), edgelist[3][0][1])]
            lanelist.append(lane13)
            boundary16 = [(edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                          (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1] - self.Width / 2),
                          (float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)))]
            boundary17 = [(edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                          (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1] + self.Width / 2),
                          (float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)))]
            boundarylist.append(boundary16)
            boundarylist.append(boundary17)
            indexes.append((37, 38))
            directions.append("Forward")
            successors.append((4, 24))
            predecessors.append((24, 4))
            alignment.append(['Forward', 'Forward'])
            # left2
            lane14 = [(edgelist[2][0][0], edgelist[2][0][1]),
                      (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                      (float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)), edgelist[2][0][1])]
            lanelist.append(lane14)
            indexes.append((39, 37))
            directions.append("Forward")
            successors.append((1, 25))
            predecessors.append((25, 1))
            successors.append((9, 25))
            predecessors.append((25, 9))
            alignment.append(['Backward', 'Forward'])
            # left3
            lane15 = [(float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)), edgelist[1][0][1]),
                      (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                      (edgelist[1][0][0], edgelist[1][0][1])]
            lanelist.append(lane15)
            boundary18 = [(float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2))),
                          (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1] + self.Width / 2),
                          (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2)]
            boundary19 = [(float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2))),
                          (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1] - self.Width / 2),
                          (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2)]
            boundarylist.append(boundary18)
            boundarylist.append(boundary19)
            indexes.append((39, 40))
            directions.append("Forward")
            successors.append((26, 7))
            predecessors.append((7, 26))
            successors.append((26, 8))
            predecessors.append((8, 26))
            alignment.append(['Forward', 'Forward'])
            # right4
            lane16 = [(float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)), edgelist[0][0][1]),
                      (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                      (edgelist[0][0][0], edgelist[0][0][1])]
            lanelist.append(lane16)
            boundary20 = [(float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2))),
                          (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1] - self.Width / 2),
                          (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2)]
            boundarylist.append(boundary20)
            indexes.append((40, 41))
            directions.append("Forward")
            successors.append((27, 6))
            predecessors.append((6, 27))
            alignment.append(['Forward', 'Forward'])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return (laneInfolist)
        if flag == "六车道十字路口":
            # turn right1
            dict1 = {
                'ID': self.StartLaneID,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width * 5)), self.Start[1]),
                'End': edgelist[0][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID,
                'BoundaryId2': self.StartBoundaryID + 1,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '+0',
                'Flag': '上右转'
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(['Forward', 'Forward'])
            # turn left1
            dict2 = {
                'ID': self.StartLaneID + 1,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width * 3)), self.Start[1]),
                'End': edgelist[3][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 2,
                'BoundaryId2': self.StartBoundaryID + 3,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '-0',
                'Flag': '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(['Forward', 'Forward'])
            # turn right2
            dict3 = {
                'ID': self.StartLaneID + 2,
                'Start': edgelist[5][1],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width * 5)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 6))),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 4,
                'BoundaryId2': self.StartBoundaryID + 5,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '+',
                'Flag': '左右转'
            }
            # print(dict1)
            tmpArc3 = ArcLane(dict3)
            lanelist.append(tmpArc3.lanePoints)
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            
            alignment.append(['Forward', 'Forward'])
            # turn left2
            dict4 = {
                'ID': self.StartLaneID + 3,
                'Start': edgelist[3][1],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width * 2)), self.Start[1]),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 6,
                'BoundaryId2': self.StartBoundaryID + 7,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '-',
                'Flag': '左左转'
            }
            # print(dict1)
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            
            alignment.append(['Forward', 'Forward'])

            # turn right3
            dict5 = {
                'ID': self.StartLaneID + 4,
                'Start': (self.Start[0], float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 6))),
                'End': edgelist[5][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 8,
                'BoundaryId2': self.StartBoundaryID + 9,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '-0',
                'Flag': '下右转'
            }
            tmpArc5 = ArcLane(dict5)
            lanelist.append(tmpArc5.lanePoints)
            boundarylist.append(tmpArc5.boundaryPoints[0])
            boundarylist.append(tmpArc5.boundaryPoints[1])
            directions.append(tmpArc5.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpArc5)
            alignment.append(['Forward', 'Forward'])
            # turn left3
            dict6 = {
                'ID': self.StartLaneID + 5,
                'Start': (float('{:.3f}'.format(self.Start[0] + self.Width * 2)),
                          float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 6))),
                'End': edgelist[2][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 10,
                'BoundaryId2': self.StartBoundaryID + 11,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '+0',
                'Flag': '下左转'
            }
            tmpArc6 = ArcLane(dict6)
            lanelist.append(tmpArc6.lanePoints)
            boundarylist.append(tmpArc6.boundaryPoints[0])
            boundarylist.append(tmpArc6.boundaryPoints[1])
            directions.append(tmpArc6.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpArc6)
            alignment.append(['Forward', 'Forward'])

            # turn right4
            dict7 = {
                'ID': self.StartLaneID + 6,
                'Start': edgelist[0][0],
                'End': self.Start,
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 12,
                'BoundaryId2': self.StartBoundaryID + 13,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '-',
                'Flag': '右右转'
            }
            tmpArc7 = ArcLane(dict7)
            lanelist.append(tmpArc7.lanePoints)
            boundarylist.append(tmpArc7.boundaryPoints[0])
            boundarylist.append(tmpArc7.boundaryPoints[1])
            directions.append(tmpArc7.TravelDirection)
            indexes.append((12, 13))
            laneObjects.append(tmpArc7)
            alignment.append(['Forward', 'Forward'])
            # turn left4
            dict8 = {
                'ID': self.StartLaneID + 7,
                'Start': edgelist[2][0],
                'End': (float('{:.3f}'.format(self.Start[0] + self.Width * 3)),
                        float('{:.3f}'.format(self.Start[1] + self.Width / 2 + self.Width * 6))),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 14,
                'BoundaryId2': self.StartBoundaryID + 15,
                'Direction': 1,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '+',
                'Flag': '右左转'
            }
            tmpArc8 = ArcLane(dict8)
            lanelist.append(tmpArc8.lanePoints)
            boundarylist.append(tmpArc8.boundaryPoints[0])
            boundarylist.append(tmpArc8.boundaryPoints[1])
            directions.append(tmpArc8.TravelDirection)
            indexes.append((14, 15))
            laneObjects.append(tmpArc8)
            alignment.append(['Forward', 'Forward'])

            # straight1
            dict9 = {
                'ID': self.StartLaneID + 8,
                'Start': edgelist[1][0],
                'End': edgelist[1][1],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 16,  # 共用
                'BoundaryId2': self.StartBoundaryID + 17,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+0',
                'k1': '+0',
                'Flag': '左至右'
            }
            tmpStraight1 = StraightLaneConnection(dict9)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((16, 17))
            laneObjects.append(tmpStraight1)
            alignment.append(['Forward', 'Forward'])

            # straight2
            dict10 = {
                'ID': self.StartLaneID + 9,
                'Start': edgelist[4][1],
                'End': edgelist[4][0],
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 18,  # reuse
                'BoundaryId2': self.StartBoundaryID + 19,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-0',
                'k1': '-0',
                'Flag': '右至左'
            }
            tmpStraight2 = StraightLaneConnection(dict10)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((18, 19))
            laneObjects.append(tmpStraight2)
            alignment.append(['Forward', 'Forward'])

            # straight3
            dict11 = {
                'ID': self.StartLaneID + 10,
                'Start': (self.Start[0] + self.Width, self.Start[1] + self.Width / 2 + self.Width * 6),
                'End': (self.Start[0] + self.Width, self.Start[1]),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 20,  # 共用
                'BoundaryId2': self.StartBoundaryID + 21,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '-',
                'k1': '-',
                'Flag': '上至下'
            }
            tmpStraight3 = StraightLaneConnection(dict11)
            lanelist.append(tmpStraight3.lanePoints)
            boundarylist.append(tmpStraight3.boundaryPoints[0])
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((20, 21))
            laneObjects.append(tmpStraight3)
            alignment.append(['Forward', 'Forward'])

            # straight4
            dict12 = {
                'ID': self.StartLaneID + 11,
                'Start': (self.Start[0] + self.Width * 4, self.Start[1]),
                'End': (self.Start[0] + self.Width * 4, self.Start[1] + self.Width / 2 + self.Width * 6),
                'Width': self.Width,
                'BoundaryId1': self.StartBoundaryID + 22,  # reuse
                'BoundaryId2': self.StartBoundaryID + 23,
                'Direction': 0,
                'TravelDirection': 'Forward',
                'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'SW'},
                'LaneType': 'Driving',
                'k': '+',
                'k1': '+',
                'Flag': '下至上'
            }
            tmpStraight4 = StraightLaneConnection(dict12)
            lanelist.append(tmpStraight4.lanePoints)
            boundarylist.append(tmpStraight4.boundaryPoints[0])
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append(tmpStraight4.TravelDirection)
            indexes.append((22, 23))
            laneObjects.append(tmpStraight4)
            alignment.append(['Forward', 'Forward'])

            # outer road
            # major direction1
            lane1 = [self.Start, (self.Start[0], self.Start[1] - self.Width / 4),
                     (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            lanelist.append(lane1)
            boundary1 = [(self.Start[0] + self.Width / 2, self.Start[1]),
                         (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            boundary2 = [(self.Start[0] - self.Width / 2, self.Start[1]),
                         (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:8
            indexes.append((24, 25))
            directions.append("Forward")
            
            successors.append((6, 12))
            predecessors.append((12, 6))
            alignment.append(['Forward', 'Forward'])

            # major direction2
            lane2 = [(self.Start[0] + self.Width, self.Start[1]),
                     (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                     (float("{:.3f}".format(self.Start[0] + self.Width)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            boundary3 = [(self.Start[0] + self.Width + self.Width / 2, self.Start[1]),
                         (self.Start[0] + self.Width + self.Width / 2, self.Start[1] - self.Width / 4),
                         (float("{:.3f}".format(self.Start[0] + self.Width + self.Width / 2)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            lanelist.append(lane2)
            boundarylist.append(boundary3)
            indexes.append((26, 24))
            directions.append("Forward")
            successors.append((10, 13))
            predecessors.append((13, 10))
            alignment.append(['Forward', 'Forward'])
            # major direction3
            lane3 = [(self.Start[0] + self.Width * 2, self.Start[1]),
                     (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                     (float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2)))]
            lanelist.append(lane3)
            indexes.append((27, 26))
            directions.append("Forward")
            successors.append((3, 14))
            predecessors.append((14, 3))
            alignment.append(['Backward', 'Forward'])
            # major direction4
            lane4 = [(float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                     (self.Start[0] + self.Width * 3, self.Start[1] - self.Width / 4),
                     (self.Start[0] + self.Width * 3, self.Start[1])]
            lanelist.append(lane4)
            boundary4 = [(float("{:.3f}".format(self.Start[0] - self.Width / 2 + self.Width * 3)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] - self.Width / 2 + self.Width * 3, self.Start[1] - self.Width / 4),
                         (self.Start[0] - self.Width / 2 + self.Width * 3, self.Start[1])]
            boundary5 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 3)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1])]
            boundarylist.append(boundary4)
            boundarylist.append(boundary5)
            indexes.append((27, 28))
            directions.append("Forward")
            successors.append((15, 1))
            predecessors.append((1, 15))
            alignment.append(['Forward', 'Forward'])
            # major direction5
            lane5 = [(float("{:.3f}".format(self.Start[0] + self.Width * 4)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                     (self.Start[0] + self.Width * 4, self.Start[1] - self.Width / 4),
                     (self.Start[0] + self.Width * 4, self.Start[1])]
            lanelist.append(lane5)
            boundary6 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 4)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2 + self.Width * 4, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2 + self.Width * 4, self.Start[1])]
            boundarylist.append(boundary6)
            indexes.append((28, 29))
            directions.append("Forward")
            successors.append((16, 11))
            predecessors.append((11, 16))
            alignment.append(['Forward', 'Forward'])
            # major direction6
            lane6 = [(float("{:.3f}".format(self.Start[0] + self.Width * 5)),
                      float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                     (self.Start[0] + self.Width * 5, self.Start[1] - self.Width / 4),
                     (self.Start[0] + self.Width * 5, self.Start[1])]
            lanelist.append(lane6)
            boundary7 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 5)),
                          float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                         (self.Start[0] + self.Width / 2 + self.Width * 5, self.Start[1] - self.Width / 4),
                         (self.Start[0] + self.Width / 2 + self.Width * 5, self.Start[1])]
            boundarylist.append(boundary7)
            indexes.append((29, 30))
            directions.append("Forward")
            successors.append((17, 0))
            predecessors.append((0, 17))
            alignment.append(['Forward', 'Forward'])

            # right1
            lane7 = [(edgelist[0][1][0], edgelist[0][1][1]),
                     (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                     (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)), edgelist[0][1][1])]
            lanelist.append(lane7)
            boundary8 = [(edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                         (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1] + self.Width / 2),
                         (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)))]
            boundary9 = [(edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                         (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1] - self.Width / 2),
                         (float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                          float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)))]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)
            indexes.append((31, 32))
            directions.append("Forward")
            successors.append((0, 18))
            predecessors.append((18, 0))
            alignment.append(['Forward', 'Forward'])
            # right2
            lane8 = [(edgelist[1][1][0], edgelist[1][1][1]),
                     (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                     (float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)), edgelist[1][1][1])]
            lanelist.append(lane8)
            boundary10 = [(edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                          (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1] + self.Width / 2),
                          (float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                           float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)))]
            boundarylist.append(boundary10)
            indexes.append((33, 31))
            directions.append("Forward")
            successors.append((8, 19))
            predecessors.append((19, 8))
            alignment.append(['Forward', 'Forward'])
            # right3
            lane9 = [(edgelist[2][1][0], edgelist[2][1][1]),
                     (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                     (float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)), edgelist[2][1][1])]
            lanelist.append(lane9)
            boundary11 = [(edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
                          (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1] + self.Width / 2),
                          (float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                           float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)))]
            boundarylist.append(boundary11)
            indexes.append((34, 33))
            directions.append("Forward")
            successors.append((5, 20))
            predecessors.append((20, 5))
            alignment.append(['Forward', 'Forward'])
            # right4
            lane10 = [(float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)), edgelist[3][1][1]),
                      (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                      (edgelist[3][1][0], edgelist[3][1][1])]
            lanelist.append(lane10)
            boundary12 = [(float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                           float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2))),
                          (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1] + self.Width / 2),
                          (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2)]
            boundarylist.append(boundary12)
            indexes.append((34, 35))
            directions.append("Forward")
            successors.append((21, 3))
            predecessors.append((3, 21))
            alignment.append(['Backward', 'Forward'])
            # right5
            lane11 = [(float("{:.3f}".format(edgelist[4][1][0] + self.Width / 2)), edgelist[4][1][1]),
                      (edgelist[4][1][0] + self.Width / 4, edgelist[4][1][1]),
                      (edgelist[4][1][0], edgelist[4][1][1])]
            lanelist.append(lane11)
            boundary13 = [(float("{:.3f}".format(edgelist[4][1][0] + self.Width / 2)),
                           float("{:.3f}".format(edgelist[4][1][1] + self.Width / 2))),
                          (edgelist[4][1][0] + self.Width / 4, edgelist[4][1][1] + self.Width / 2),
                          (edgelist[4][1][0], edgelist[4][1][1] + self.Width / 2)]
            boundarylist.append(boundary13)
            indexes.append((35, 36))
            directions.append("Forward")
            successors.append((22, 9))
            predecessors.append((9, 22))
            alignment.append(['Forward', 'Forward'])
            # right6
            lane12 = [(float("{:.3f}".format(edgelist[5][1][0] + self.Width / 2)), edgelist[5][1][1]),
                      (edgelist[5][1][0] + self.Width / 4, edgelist[5][1][1]),
                      (edgelist[5][1][0], edgelist[5][1][1])]
            lanelist.append(lane12)
            boundary14 = [(float("{:.3f}".format(edgelist[5][1][0] + self.Width / 2)),
                           float("{:.3f}".format(edgelist[5][1][1] + self.Width / 2))),
                          (edgelist[5][1][0] + self.Width / 4, edgelist[5][1][1] + self.Width / 2),
                          (edgelist[5][1][0], edgelist[5][1][1] + self.Width / 2)]
            boundarylist.append(boundary14)
            indexes.append((36, 37))
            directions.append("Forward")
            successors.append((23, 2))
            predecessors.append((2, 23))
            alignment.append(['Forward', 'Forward'])

            # upper1
            lane13 = [(self.Start[0],
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2))),
                      (self.Start[0], self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                      (self.Start[0], self.Start[1] + self.Width * 6 + self.Width / 2)]
            lanelist.append(lane13)
            boundary15 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                           float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2))),
                          (self.Start[0] + self.Width / 2,
                           self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                          (self.Start[0] + self.Width / 2, self.Start[1] + self.Width * 6 + self.Width / 2)]
            boundary16 = [(float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                           float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2))),
                          (self.Start[0] - self.Width / 2,
                           self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                          (self.Start[0] - self.Width / 2, self.Start[1] + self.Width * 6 + self.Width / 2)]
            boundarylist.append(boundary15)
            boundarylist.append(boundary16)
            indexes.append((38, 39))
            directions.append("Forward")
            successors.append((24, 4))
            predecessors.append((4, 24))
            alignment.append(['Forward', 'Forward'])
            # upper2
            lane14 = [(float("{:.3f}".format(self.Start[0] + self.Width)),
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2))),
                      (self.Start[0] + self.Width, self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                      (self.Start[0] + self.Width, self.Start[1] + self.Width * 6 + self.Width / 2)]
            boundary17 = [(float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                           float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2))),
                          (self.Start[0] + self.Width / 2 + self.Width,
                           self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                          (
                          self.Start[0] + self.Width / 2 + self.Width, self.Start[1] + self.Width * 6 + self.Width / 2)]
            lanelist.append(lane14)
            boundarylist.append(boundary17)
            indexes.append((40, 38))
            directions.append("Forward")
            successors.append((25, 10))
            predecessors.append((10, 25))
            alignment.append(['Forward', 'Forward'])
            # upper3
            lane15 = [(float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2))),
                      (
                      self.Start[0] + self.Width * 2, self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                      (self.Start[0] + self.Width * 2, self.Start[1] + self.Width * 6 + self.Width / 2)]
            lanelist.append(lane15)
            indexes.append((41, 40))
            directions.append("Forward")
            successors.append((26, 5))
            predecessors.append((5, 26))
            alignment.append(['Backward', 'Forward'])
            # upper4
            lane16 = [(self.Start[0] + self.Width * 3, self.Start[1] + self.Width * 6 + self.Width / 2),
                      (
                      self.Start[0] + self.Width * 3, self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                      (float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                       float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            lanelist.append(lane16)
            boundary18 = [
                (self.Start[0] + self.Width * 3 - self.Width / 2, self.Start[1] + self.Width * 6 + self.Width / 2),
                (self.Start[0] + self.Width * 3 - self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 3 - self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            boundary19 = [
                (self.Start[0] + self.Width * 3 + self.Width / 2, self.Start[1] + self.Width * 6 + self.Width / 2),
                (self.Start[0] + self.Width * 3 + self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 3 + self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            boundarylist.append(boundary18)
            boundarylist.append(boundary19)
            indexes.append((41, 42))
            directions.append("Forward")
            successors.append((7, 27))
            predecessors.append((27, 7))
            alignment.append(['Forward', 'Forward'])
            # upper5
            lane17 = [(self.Start[0] + self.Width * 4, self.Start[1] + self.Width * 6 + self.Width / 2),
                      (
                          self.Start[0] + self.Width * 4,
                          self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                      (
                          float("{:.3f}".format(self.Start[0] + self.Width * 4)),
                          float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            lanelist.append(lane17)
            boundary20 = [
                (self.Start[0] + self.Width * 4 + self.Width / 2, self.Start[1] + self.Width * 6 + self.Width / 2),
                (self.Start[0] + self.Width * 4 + self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 4 + self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            boundarylist.append(boundary20)
            indexes.append((42, 43))
            directions.append("Forward")
            successors.append((11, 28))
            predecessors.append((28, 11))
            alignment.append(['Forward', 'Forward'])
            # upper6
            lane18 = [(self.Start[0] + self.Width * 5, self.Start[1] + self.Width * 6 + self.Width / 2),
                      (
                          self.Start[0] + self.Width * 5,
                          self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                      (
                          float("{:.3f}".format(self.Start[0] + self.Width * 5)),
                          float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            lanelist.append(lane18)
            boundary21 = [
                (self.Start[0] + self.Width * 5 + self.Width / 2, self.Start[1] + self.Width * 6 + self.Width / 2),
                (self.Start[0] + self.Width * 5 + self.Width / 2,
                 self.Start[1] + self.Width / 4 + self.Width * 6 + self.Width / 2),
                (float("{:.3f}".format(self.Start[0] + self.Width * 5 + self.Width / 2)),
                 float("{:.3f}".format(self.Start[1] + self.Width / 2 + self.Width * 6 + self.Width / 2)))]
            boundarylist.append(boundary21)
            indexes.append((43, 44))
            directions.append("Forward")
            successors.append((2, 29))
            predecessors.append((29, 2))
            alignment.append(['Forward', 'Forward'])

            # left1
            lane19 = [(edgelist[5][0][0], edgelist[5][0][1]),
                      (edgelist[5][0][0] - self.Width / 4, edgelist[5][0][1]),
                      (float("{:.3f}".format(edgelist[5][0][0] - self.Width / 2)), edgelist[5][0][1])]
            lanelist.append(lane19)
            boundary22 = [(edgelist[5][0][0], edgelist[5][0][1] - self.Width / 2),
                          (edgelist[5][0][0] - self.Width / 4, edgelist[5][0][1] - self.Width / 2),
                          (float("{:.3f}".format(edgelist[5][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[5][0][1] - self.Width / 2)))]
            boundary23 = [(edgelist[5][0][0], edgelist[5][0][1] + self.Width / 2),
                          (edgelist[5][0][0] - self.Width / 4, edgelist[5][0][1] + self.Width / 2),
                          (float("{:.3f}".format(edgelist[5][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[5][0][1] + self.Width / 2)))]
            boundarylist.append(boundary22)
            boundarylist.append(boundary23)
            indexes.append((45, 46))
            directions.append("Forward")
            successors.append((4, 30))
            predecessors.append((30, 4))
            alignment.append(['Forward', 'Forward'])
            # left2
            lane20 = [(edgelist[4][0][0], edgelist[4][0][1]),
                      (edgelist[4][0][0] - self.Width / 4, edgelist[4][0][1]),
                      (float("{:.3f}".format(edgelist[4][0][0] - self.Width / 2)), edgelist[4][0][1])]
            boundary24 = [(edgelist[4][0][0], edgelist[4][0][1] - self.Width / 2),
                          (edgelist[4][0][0] - self.Width / 4, edgelist[4][0][1] - self.Width / 2),
                          (float("{:.3f}".format(edgelist[4][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[4][0][1] - self.Width / 2)))]
            lanelist.append(lane20)
            boundarylist.append(boundary24)
            indexes.append((47, 45))
            directions.append("Forward")
            successors.append((9, 31))
            predecessors.append((31, 9))
            alignment.append(['Forward', 'Forward'])
            # left3
            lane21 = [(edgelist[3][0][0], edgelist[3][0][1]),
                      (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                      (float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)), edgelist[3][0][1])]
            lanelist.append(lane21)
            indexes.append((48, 47))
            directions.append("Forward")
            successors.append((1, 32))
            predecessors.append((32, 1))
            alignment.append(['Backward', 'Forward'])
            # right4
            lane22 = [(float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)), edgelist[2][0][1]),
                      (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                      (edgelist[2][0][0], edgelist[2][0][1])]
            lanelist.append(lane22)
            boundary25 = [(float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2))),
                          (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1] + self.Width / 2),
                          (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2)]
            boundary26 = [(float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2))),
                          (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1] - self.Width / 2),
                          (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2)]
            boundarylist.append(boundary25)
            boundarylist.append(boundary26)
            indexes.append((48, 49))
            directions.append("Forward")
            successors.append((33, 7))
            predecessors.append((7, 33))
            alignment.append(['Forward', 'Forward'])
            # right5
            lane23 = [(float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)), edgelist[1][0][1]),
                      (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                      (edgelist[1][0][0], edgelist[1][0][1])]
            lanelist.append(lane23)
            boundary27 = [(float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2))),
                          (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1] - self.Width / 2),
                          (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2)]
            boundarylist.append(boundary27)
            indexes.append((49, 50))
            directions.append("Forward")
            successors.append((34, 8))
            predecessors.append((8, 34))
            alignment.append(['Forward', 'Forward'])
            # right6
            lane24 = [(float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)), edgelist[0][0][1]),
                      (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                      (edgelist[0][0][0], edgelist[0][0][1])]
            lanelist.append(lane24)
            boundary28 = [(float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                           float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2))),
                          (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1] - self.Width / 2),
                          (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2)]
            boundarylist.append(boundary28)
            indexes.append((50, 51))
            directions.append("Forward")
            successors.append((35, 6))
            predecessors.append((6, 35))
            alignment.append(['Forward', 'Forward'])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return (laneInfolist)

    def generate_road(self, f):
        Widget.LaneID += sum(self.OuterLaneNumber) + self.InnerLaneNumber
        Widget.BoundaryID += self.BoundaryNumber
        Widget.JunctionID += 1
        Widget.WidgetID += 1

        lanes = str(self.StartLaneID) + ':' + str(
            self.StartLaneID + sum(self.OuterLaneNumber) + self.InnerLaneNumber + - 1)  # 当前组件涉及到的lane
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a T-Junction widget.')
        for lane in range(self.StartLaneID, self.StartLaneID + sum(self.OuterLaneNumber) + self.InnerLaneNumber):
            printAutoInd(f, 'rrMap.Lanes(' + str(lane) + ') = roadrunner.hdmap.Lane();')
        laneidlist = []
        for i in range(self.StartLaneID, self.StartLaneID + sum(self.OuterLaneNumber) + self.InnerLaneNumber):
            laneidlist.append('Lane' + str(i))
        laneid = ','.join(['"' + i + '"' for i in laneidlist])
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').ID] = deal(' + laneid + ');')

        laneInfoList = self.getLaneInfoList()
        lanepointlist = self.rotation(laneInfoList[0])
        boundarypointlist = self.rotation(laneInfoList[1])
        indexes = laneInfoList[2]
        directions = laneInfoList[3]
        successors = laneInfoList[4]
        predecessors = laneInfoList[5]
        alignment = laneInfoList[6]

        lanepointstring = self.PointtoString(lanepointlist)
        boundarypointstring = self.PointtoString(boundarypointlist)

        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').Geometry] = deal(' + lanepointstring + ');')

        traveldirectionlist = []
        for direction in directions:
            traveldirectionlist.append(direction)
        traveldirection = ','.join(['"' + i + '"' for i in traveldirectionlist])
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').TravelDirection] = deal(' + traveldirection + ');')
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').LaneType] = deal("Driving");')

        # boundary
        boundaries = str(self.StartBoundaryID) + ':' + str(
            self.StartBoundaryID + self.BoundaryNumber - 1)  # 组件车道边界数=laneassettype字典的大小。
        printAutoInd(f, '% Set the lane boundaries.')
        for boundary in range(self.StartBoundaryID, self.StartBoundaryID + self.BoundaryNumber):
            printAutoInd(f, 'rrMap.LaneBoundaries(' + str(boundary) + ') = roadrunner.hdmap.LaneBoundary();')
        laneboundaryidlist = []
        for i in range(self.StartBoundaryID, self.StartBoundaryID + self.BoundaryNumber):
            laneboundaryidlist.append('Boundary' + str(i))
        boundaryid = ','.join(['"' + i + '"' for i in laneboundaryidlist])
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').ID] = deal(' + boundaryid + ');')
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').Geometry] = deal(' + boundarypointstring + ');')
  
        if self.Flag == '双向双车道十字路口':
            idlst = [self.StartLaneID + 19, self.StartLaneID + 18, self.StartLaneID + 20,
                     self.StartLaneID + 23, self.StartLaneID + 22, self.StartLaneID + 21,
                     self.StartLaneID + 25, self.StartLaneID + 24, self.StartLaneID + 26,
                     self.StartLaneID + 29, self.StartLaneID + 27, self.StartLaneID + 28]
            assertlst = ['SW', 'SY', 'SW',
                         'SW', 'SY', 'SW',
                         'SW', 'SY', 'SW',
                         'SW', 'SY', 'SW', ]

        elif self.Flag == '四车道十字路口':
            idlst = [self.StartLaneID + 23, self.StartLaneID + 22, self.StartLaneID + 24, self.StartLaneID + 25,
                     self.StartLaneID + 26,
                     self.StartLaneID + 31, self.StartLaneID + 30, self.StartLaneID + 29, self.StartLaneID + 27,
                     self.StartLaneID + 28,
                     self.StartLaneID + 33, self.StartLaneID + 32, self.StartLaneID + 34, self.StartLaneID + 35,
                     self.StartLaneID + 36,
                     self.StartLaneID + 41, self.StartLaneID + 40, self.StartLaneID + 39, self.StartLaneID + 37,
                     self.StartLaneID + 38, ]
            assertlst = ['SW', 'DW', 'SDY', 'SW', 'SW',
                         'SW', 'DW', 'SDY', 'SW', 'SW',
                         'SW', 'DW', 'SDY', 'SW', 'SW',
                         'SW', 'DW', 'SDY', 'SW', 'SW', ]
        elif self.Flag == '六车道十字路口':
            idlst = [self.StartLaneID + 25, self.StartLaneID + 24, self.StartLaneID + 26, self.StartLaneID + 27,
                     self.StartLaneID + 28, self.StartLaneID + 29, self.StartLaneID + 30,
                     self.StartLaneID + 37, self.StartLaneID + 36, self.StartLaneID + 35, self.StartLaneID + 34,
                     self.StartLaneID + 33, self.StartLaneID + 31, self.StartLaneID + 32,
                     self.StartLaneID + 39, self.StartLaneID + 38, self.StartLaneID + 40, self.StartLaneID + 41,
                     self.StartLaneID + 42, self.StartLaneID + 43, self.StartLaneID + 44,
                     self.StartLaneID + 51, self.StartLaneID + 50, self.StartLaneID + 49, self.StartLaneID + 48,
                     self.StartLaneID + 47, self.StartLaneID + 45, self.StartLaneID + 46, ]
            assertlst = ['SW', 'DW', 'DW', 'SDY', 'DW', 'DW', 'SW',
                         'SW', 'DW', 'DW', 'SDY', 'DW', 'DW', 'SW',
                         'SW', 'DW', 'DW', 'SDY', 'DW', 'DW', 'SW',
                         'SW', 'DW', 'DW', 'SDY', 'DW', 'DW', 'SW', ]
        for id in range(len(idlst)):
            if assertlst[id] == 'SW':
                a = 'markingAttribSW'
            if assertlst[id] == 'SY':
                a = 'markingAttribSY'
            if assertlst[id] == 'DW':
                a = 'markingAttribDW'
            if assertlst[id] == 'DY':
                a = 'markingAttribDY'
            if assertlst[id] == 'DSW':
                a = 'markingAttribDSW'
            if assertlst[id] == 'DSY':
                a = 'markingAttribDSY'
            if assertlst[id] == 'SDW':
                a = 'markingAttribSDW'
            if assertlst[id] == 'SDY':
                a = 'markingAttribSDY'
            printAutoInd(f, '[rrMap.LaneBoundaries(' + str(idlst[id]) + ':' + str(
                idlst[id]) + ').ParametricAttributes] = deal(' + a + ');')

        
        printAutoInd(f, '% Associate lanes and lane boundaries.')
        for i in range(len(laneidlist)):
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + i) + '),"Boundary' + str(
                self.StartBoundaryID + indexes[i][0]) + '",Alignment="' + alignment[i][0] + '");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + i) + '),"Boundary' + str(
                self.StartBoundaryID + indexes[i][1]) + '",Alignment="' + alignment[i][1] + '");')

       
        for i in range(len(successors)):
            # rrMap.Lanes(3).Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane4"));
            printAutoInd(f, 'rrMap.Lanes(' + str(self.StartLaneID + successors[i][
                0]) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="' +
                         laneidlist[successors[i][1]] + '"));')

        for i in range(len(predecessors)):
            printAutoInd(f, 'rrMap.Lanes(' + str(self.StartLaneID + predecessors[i][
                0]) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="' +
                         laneidlist[predecessors[i][1]] + '"));')

        # junction definition
        printAutoInd(f, '% junction definition')
        printAutoInd(f, 'rrMap.Junctions(' + str(self.ID) + ') = roadrunner.hdmap.Junction();')

        geoPoints = self.getGeometryPoints()
        # print(geoPoints)
        geoPoints1 = self.rotation(geoPoints)
        geoPointsStr = self.PointtoString([geoPoints1])
        printAutoInd(f, 'polygon=roadrunner.hdmap.Polygon("ExteriorRing",deal(' + geoPointsStr + '));')
        printAutoInd(f, 'multipolygon=roadrunner.hdmap.MultiPolygon("Polygons",polygon);')
        printAutoInd(f, '[rrMap.Junctions(' + str(self.ID) + ':' + str(self.ID) + ').Geometry]=multipolygon;')
        tmpStr = 'roadrunner.hdmap.Reference("ID","' + laneidlist[0] + '")'
        for i in range(1, self.InnerLaneNumber):
            tmpStr += ',roadrunner.hdmap.Reference("ID","' + laneidlist[i] + '")'
        printAutoInd(f, 'rrMap.Junctions(' + str(self.ID) + ').Lanes=deal([' + tmpStr + ']);')

