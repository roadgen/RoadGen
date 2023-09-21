# 行道变换组件的输入是一个字典{Start, W, StartLaneID, StartBoundaryID, LaneNumber, TravelDirection, LaneAssetType, K, Function, Flag}
# 不同小组件的起始点可能不同，具体需要参照LaneSwitchLibrary中的说明

# 为了方便拼接 后续可以在组件类中集成一个返回该组件结束位置的方法。
from func.printAuto import printAutoInd
from func.widget import Widget
import math


class LaneSwitch(Widget):
    WidgetID = 1
    Start = (0, 0) 
    W = 3.5 
    StartLaneID = 1  
    StartBoundaryID = 1 
    LaneNumber = 1  
    BoundaryNumber = 8
    LaneAssetType = {}  
    k = '+0'  
    LaneType = 'Driving' 
    Flag = ''  

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.W = dict1.get('W')
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.LaneNumber = dict1.get('LaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        self.LaneAssetType = Widget.get_self_LaneAssetType(dict1.get('LaneAssetType'))
        self.k = dict1.get('K')
        self.Flag = dict1.get('Flag')
        self.NextType = dict1.get('NextType')
        self.Type = dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag + '_laneswitch'
        Currents_info["CurrentLanes"] = []
        if self.Flag == '1*2左' or self.Flag == '1*2右':
            Currents_info["Type"] = '单行道'
            Currents_info["CurrentLanes"].append(self.StartLaneID)
        if self.Flag == '2*1左' or self.Flag == '2*1右':
            Currents_info["Type"] = '单向虚线双行道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 2))
        if self.Flag == '2*3左' or self.Flag == '2*3右':
            Currents_info["Type"] = '双向虚线双行道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 2))
        if self.Flag == '3*2左':
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 3))
        if self.Flag == '3*2右':
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 3))
        if self.Flag == '3*4右':
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 3))
        if self.Flag == '3*4左':
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 3))
        if self.Flag == '4*3左' or self.Flag == '4*3右' or self.Flag == '4*6':
            Currents_info["Type"] = '双黄实线虚虚四车道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 4))
        if self.Flag == '6*4':
            Currents_info["Type"] = '双实线虚虚虚虚六车道'
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 6))
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        Next = dict()
        if self.Flag == '1*2左':
            endpoint = (self.Start[0] + 30, self.Start[1] + self.W)
            Next['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 5))
        elif self.Flag == '1*2右':
            endpoint = (self.Start[0] + 30, self.Start[1])
            Next['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 5))
        elif self.Flag == '2*1左':
            endpoint = (self.Start[0] + 30, self.Start[1] - self.W)
            Next['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 5))
        elif self.Flag == '2*1右':
            endpoint = (self.Start[0] + 30, self.Start[1])
            Next['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 5))
        elif self.Flag == '2*3左':
            endpoint = (self.Start[0] + 30, self.Start[1] + self.W)
            Next['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 8))
        elif self.Flag == '2*3右':
            endpoint = (self.Start[0] + 30, self.Start[1])
            Next['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 8))
        elif self.Flag == '3*2左':
            endpoint = (self.Start[0] + 30, self.Start[1] - self.W)
            Next['lanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
        elif self.Flag == '3*2右':
            endpoint = (self.Start[0] + 30, self.Start[1])
            Next['lanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
        elif self.Flag == '3*4右':
            endpoint = (self.Start[0] + 30, self.Start[1])
            Next['lanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 11))
        elif self.Flag == '3*4左':
            endpoint = (self.Start[0] + 30, self.Start[1] + self.W)
            Next['lanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 11))
        elif self.Flag == '4*3左':
            endpoint = (self.Start[0] + 30, self.Start[1] - self.W)
            Next['lanes'] = list(range(self.StartLaneID + 8, self.StartLaneID + 11))
        elif self.Flag == '4*3右':
            endpoint = (self.Start[0] + 30, self.Start[1])
            Next['lanes'] = list(range(self.StartLaneID + 8, self.StartLaneID + 11))
        elif self.Flag == '4*6':
            endpoint = (self.Start[0] + 30, self.Start[1] + self.W)
            Next['lanes'] = list(range(self.StartLaneID + 10, self.StartLaneID + 16))
        elif self.Flag == '6*4':
            endpoint = (self.Start[0] + 30, self.Start[1] - self.W)
            Next['lanes'] = list(range(self.StartLaneID + 12, self.StartLaneID + 16))

        Next['endpoint'] = self.roate_endpoints(endpoint)
        Next['direction'] = self.k
        Next['type'] = self.NextType
        Next['current'] = self.Flag + '_' + self.Type
        Next['ID'] = self.WidgetID
        Nexts.append(Next)
        return Nexts

    def roate_endpoints(self, point):
        if self.k == '+0':
            return point
        if self.k == '-':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi / 2)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi / 2)) + self.Start[1]))
            return x, y
        if self.k == '-0':  
            x = float(
                '{:.3f}'.format((point[0] - self.Start[0]) * int(math.cos(math.pi)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi)) + self.Start[0]))
            y = float(
                '{:.3f}'.format((point[1] - self.Start[1]) * int(math.cos(math.pi)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi)) + self.Start[1]))
            return x, y
        if self.k == '+':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi * 1.5)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi * 1.5)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi * 1.5)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi * 1.5)) + self.Start[1]))
            return x, y

    def rotation(self, pointlist):
        if self.k == '+0':
            return pointlist
        if self.k == '-':  
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (j[1] - self.Start[1]) * int(
                            math.sin(math.pi / 2)) + self.Start[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (j[0] - self.Start[0]) * int(
                            math.sin(math.pi / 2)) + self.Start[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == '-0':  
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float(
                        '{:.3f}'.format((j[0] - self.Start[0]) * int(math.cos(math.pi)) + (j[1] - self.Start[1]) * int(
                            math.sin(math.pi)) + self.Start[0]))
                    y = float(
                        '{:.3f}'.format((j[1] - self.Start[1]) * int(math.cos(math.pi)) - (j[0] - self.Start[0]) * int(
                            math.sin(math.pi)) + self.Start[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == '+':  
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float('{:.3f}'.format(
                        (j[0] - self.Start[0]) * int(math.cos(math.pi * 1.5)) + (j[1] - self.Start[1]) * int(
                            math.sin(math.pi * 1.5)) + self.Start[0]))
                    y = float('{:.3f}'.format(
                        (j[1] - self.Start[1]) * int(math.cos(math.pi * 1.5)) - (j[0] - self.Start[0]) * int(
                            math.sin(math.pi * 1.5)) + self.Start[1]))
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        else:
            print('The function is wrong')

 
    def get_coveredArea(self):
        result=[]
        flag = self.Flag
        if flag == '1*2左':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2+self.W)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '1*2右' or flag == '2*1左' or flag == '2*1右':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '2*3左':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2+self.W)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '2*3右' or flag == '3*2左' or flag == '3*2右':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W*2)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '3*4右' or flag == '4*3左' or flag=='4*3右':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W*3)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag== '3*4左':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W*2)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2+self.W)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '4*6':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W*4)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2+self.W)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag== '6*4':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W*5)
            point2=(self.Start[0]+30,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        
        finalResult=self.rotation(result)
        return(finalResult)


    def getlanepoint(self):
        flag = self.Flag
        pointlist = []
        if flag == '1*2左':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point3[0] + 5, point3[1] + self.W / 2)
            point5 = (point3[0] + 10, point3[1] + self.W)
            lane2 = [point3, point4, point5]
            pointlist.append(lane2)
            point6 = (point3[0] + 5, point3[1])
            point7 = (point3[0] + 10, point3[1])
            lane3 = [point3, point6, point7]
            pointlist.append(lane3)
            point8 = (point5[0] + 5, point5[1])
            point9 = (point5[0] + 10, point5[1])
            lane4 = [point5, point8, point9]
            pointlist.append(lane4)
            point10 = (point7[0] + 5, point7[1])
            point11 = (point7[0] + 10, point7[1])
            lane5 = [point7, point10, point11]
            pointlist.append(lane5)

            pointlist = self.rotation(pointlist)

            return pointlist
        if flag == '1*2右':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point3[0] + 5, point3[1])
            point5 = (point3[0] + 10, point3[1])
            lane2 = [point3, point4, point5]
            pointlist.append(lane2)
            point6 = (point3[0] + 5, point3[1] - self.W / 2)
            point7 = (point3[0] + 10, point3[1] - self.W)
            lane3 = [point3, point6, point7]
            pointlist.append(lane3)
            point8 = (point5[0] + 5, point5[1])
            point9 = (point5[0] + 10, point5[1])
            lane4 = [point5, point8, point9]
            pointlist.append(lane4)
            point10 = (point7[0] + 5, point7[1])
            point11 = (point7[0] + 10, point7[1])
            lane5 = [point7, point10, point11]
            pointlist.append(lane5)

            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '2*1左':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + 5, point3[1] - self.W / 2)
            point8 = (point3[0] + 10, point3[1] - self.W)
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            point9 = (point6[0] + 5, point6[1])
            lane4 = [point6, point9, point8]
            pointlist.append(lane4)
            point10 = (point8[0] + 5, point8[1])
            point11 = (point8[0] + 10, point8[1])
            lane5 = [point8, point10, point11]
            pointlist.append(lane5)

            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '2*1右':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + 5, point3[1])
            point8 = (point3[0] + 10, point3[1])
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            point9 = (point6[0] + 5, point6[1] + self.W / 2)
            lane4 = [point6, point9, point8]
            pointlist.append(lane4)
            point10 = (point8[0] + 5, point8[1])
            point11 = (point8[0] + 10, point8[1])
            lane5 = [point8, point10, point11]
            pointlist.append(lane5)

            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '2*3左':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + 5, point3[1] + self.W / 2)
            point8 = (point3[0] + 10, point3[1] + self.W)
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            point9 = (point3[0] + 5, point3[1])
            point10 = (point3[0] + 10, point3[1])
            lane4 = [point3, point9, point10]
            pointlist.append(lane4)
            point11 = (point6[0] + 5, point6[1])
            point12 = (point6[0] + 10, point6[1])
            lane5 = [point6, point11, point12]
            pointlist.append(lane5)
            point13 = (point8[0] + 5, point8[1])
            point14 = (point8[0] + 10, point8[1])
            lane6 = [point8, point13, point14]
            pointlist.append(lane6)
            point15 = (point10[0] + 5, point10[1])
            point16 = (point10[0] + 10, point10[1])
            lane7 = [point10, point15, point16]
            pointlist.append(lane7)
            point17 = (point12[0] + 5, point12[1])
            point18 = (point12[0] + 10, point12[1])
            lane8 = [point12, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[2].reverse()
            pointlist[3].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()

            return pointlist
        if flag == '2*3右':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + 5, point3[1])
            point8 = (point3[0] + 10, point3[1])
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            point9 = (point6[0] + 5, point6[1])
            point10 = (point6[0] + 10, point6[1])
            lane4 = [point6, point9, point10]
            pointlist.append(lane4)
            point11 = (point6[0] + 5, point6[1] - self.W / 2)
            point12 = (point6[0] + 10, point6[1] - self.W)
            lane5 = [point6, point11, point12]
            pointlist.append(lane5)
            point13 = (point8[0] + 5, point8[1])
            point14 = (point8[0] + 10, point8[1])
            lane6 = [point8, point13, point14]
            pointlist.append(lane6)
            point15 = (point10[0] + 5, point10[1])
            point16 = (point10[0] + 10, point10[1])
            lane7 = [point10, point15, point16]
            pointlist.append(lane7)
            point17 = (point12[0] + 5, point12[1])
            point18 = (point12[0] + 10, point12[1])
            lane8 = [point12, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[2].reverse()
            pointlist[5].reverse()

            return pointlist
        if flag == '3*2左':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1] - self.W / 2)
            point11 = (point3[0] + 10, point3[1] - self.W)
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = [point6[0] + 5, point6[1]]
            lane5 = [point6, point12, point11]
            pointlist.append(lane5)
            point13 = (point9[0] + 5, point9[1])
            point14 = (point9[0] + 10, point9[1])
            lane6 = [point9, point13, point14]
            pointlist.append(lane6)
            point15 = (point11[0] + 5, point11[1])
            point16 = (point11[0] + 10, point11[1])
            lane7 = [point11, point15, point16]
            pointlist.append(lane7)
            point17 = (point14[0] + 5, point14[1])
            point18 = (point14[0] + 10, point14[1])
            lane8 = [point14, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[6].reverse()

            return pointlist
        if flag == '3*2右':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1])
            point11 = (point3[0] + 10, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + 5, point6[1])
            point13 = (point6[0] + 10, point6[1])
            lane5 = [point6, point12, point13]
            pointlist.append(lane5)
            point14 = (point9[0] + 5, point9[1] + self.W / 2)
            lane6 = [point9, point14, point13]
            pointlist.append(lane6)
            point15 = (point11[0] + 5, point11[1])
            point16 = (point11[0] + 10, point11[1])
            lane7 = [point11, point15, point16]
            pointlist.append(lane7)
            point17 = (point13[0] + 5, point13[1])
            point18 = (point13[0] + 10, point13[1])
            lane8 = [point13, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)

            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[6].reverse()
            return pointlist
        if flag == '3*4右':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1])
            point11 = (point3[0] + 10, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + 5, point6[1])
            point13 = (point6[0] + 10, point6[1])
            lane5 = [point6, point12, point13]
            pointlist.append(lane5)
            point14 = (point9[0] + 5, point9[1])
            point15 = (point9[0] + 10, point9[1])
            lane6 = [point9, point14, point15]
            pointlist.append(lane6)
            point16 = (point9[0] + 5, point9[1] - self.W / 2)
            point17 = (point9[0] + 10, point9[1] - self.W)
            lane7 = [point9, point16, point17]
            pointlist.append(lane7)
            point18 = (point11[0] + 5, point11[1])
            point19 = (point11[0] + 10, point11[1])
            lane8 = [point11, point18, point19]
            pointlist.append(lane8)
            point20 = (point13[0] + 5, point13[1])
            point21 = (point13[0] + 10, point13[1])
            lane9 = [point13, point20, point21]
            pointlist.append(lane9)
            point22 = (point15[0] + 5, point15[1])
            point23 = (point15[0] + 10, point15[1])
            lane10 = [point15, point22, point23]
            pointlist.append(lane10)
            point24 = (point17[0] + 5, point17[1])
            point25 = (point17[0] + 10, point17[1])
            lane11 = [point17, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()

            return pointlist
        if flag == '3*4左':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1] + self.W / 2)
            point11 = (point3[0] + 10, point3[1] + self.W)
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point3[0] + 5, point3[1])
            point13 = (point3[0] + 10, point3[1])
            lane5 = [point3, point12, point13]
            pointlist.append(lane5)
            point14 = (point6[0] + 5, point6[1])
            point15 = (point6[0] + 10, point6[1])
            lane6 = [point6, point14, point15]
            pointlist.append(lane6)
            point16 = (point9[0] + 5, point9[1])
            point17 = (point9[0] + 10, point9[1])
            lane7 = [point9, point16, point17]
            pointlist.append(lane7)
            point18 = (point11[0] + 5, point11[1])
            point19 = (point11[0] + 10, point11[1])
            lane8 = [point11, point18, point19]
            pointlist.append(lane8)
            point20 = (point13[0] + 5, point13[1])
            point21 = (point13[0] + 10, point13[1])
            lane9 = [point13, point20, point21]
            pointlist.append(lane9)
            point22 = (point15[0] + 5, point15[1])
            point23 = (point15[0] + 10, point15[1])
            lane10 = [point15, point22, point23]
            pointlist.append(lane10)
            point24 = (point17[0] + 5, point17[1])
            point25 = (point17[0] + 10, point17[1])
            lane11 = [point17, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()

            return pointlist
        if flag == '4*3左':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 3)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 3)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 3)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1] - self.W / 2)
            point14 = (point3[0] + 10, point3[1] - self.W)
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + 5, point6[1])
            lane6 = [point6, point15, point14]
            pointlist.append(lane6)
            point16 = (point9[0] + 5, point9[1])
            point17 = (point9[0] + 10, point9[1])
            lane7 = [point9, point16, point17]
            pointlist.append(lane7)
            point18 = (point12[0] + 5, point12[1])
            point19 = (point12[0] + 10, point12[1])
            lane8 = [point12, point18, point19]
            pointlist.append(lane8)
            point20 = (point14[0] + 5, point14[1])
            point21 = (point14[0] + 10, point14[1])
            lane9 = [point14, point20, point21]
            pointlist.append(lane9)
            point22 = (point17[0] + 5, point17[1])
            point23 = (point17[0] + 10, point17[1])
            lane10 = [point17, point22, point23]
            pointlist.append(lane10)
            point24 = (point19[0] + 5, point19[1])
            point25 = (point19[0] + 10, point19[1])
            lane11 = [point19, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[8].reverse()

            return pointlist
        if flag == '4*3右':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 3)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 3)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 3)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1])
            point14 = (point3[0] + 10, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + 5, point6[1])
            point16 = (point6[0] + 10, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            point17 = (point9[0] + 5, point9[1])
            point18 = (point9[0] + 10, point9[1])
            lane7 = [point9, point17, point18]
            pointlist.append(lane7)
            point19 = (point12[0] + 5, point12[1] + self.W / 2)
            lane8 = [point12, point19, point18]
            pointlist.append(lane8)
            point20 = (point14[0] + 5, point14[1])
            point21 = (point14[0] + 10, point14[1])
            lane9 = [point14, point20, point21]
            pointlist.append(lane9)
            point22 = (point16[0] + 5, point16[1])
            point23 = (point16[0] + 10, point16[1])
            lane10 = [point16, point22, point23]
            pointlist.append(lane10)
            point24 = (point18[0] + 5, point18[1])
            point25 = (point18[0] + 10, point18[1])
            lane11 = [point18, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
            return pointlist
        if flag == '4*6':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 3)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 3)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 3)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1] + self.W / 2)
            point14 = (point3[0] + 10, point3[1] + self.W)
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point3[0] + 5, point3[1])
            point16 = (point3[0] + 10, point3[1])
            lane6 = [point3, point15, point16]
            pointlist.append(lane6)
            point17 = (point6[0] + 5, point6[1])
            point18 = (point6[0] + 10, point6[1])
            lane7 = [point6, point17, point18]
            pointlist.append(lane7)
            point19 = (point9[0] + 5, point9[1])
            point20 = (point9[0] + 10, point9[1])
            lane8 = [point9, point19, point20]
            pointlist.append(lane8)
            point21 = (point12[0] + 5, point12[1])
            point22 = (point12[0] + 10, point12[1])
            lane9 = [point12, point21, point22]
            pointlist.append(lane9)
            point23 = (point12[0] + 5, point12[1] - self.W / 2)
            point24 = (point12[0] + 10, point12[1] - self.W)
            lane10 = [point12, point23, point24]
            pointlist.append(lane10)
            point25 = (point14[0] + 5, point14[1])
            point26 = (point14[0] + 10, point14[1])
            lane11 = [point14, point25, point26]
            pointlist.append(lane11)
            point27 = (point16[0] + 5, point16[1])
            point28 = (point16[0] + 10, point16[1])
            lane12 = [point16, point27, point28]
            pointlist.append(lane12)
            point29 = (point18[0] + 5, point18[1])
            point30 = (point18[0] + 10, point18[1])
            lane13 = [point18, point29, point30]
            pointlist.append(lane13)
            point31 = (point20[0] + 5, point20[1])
            point32 = (point20[0] + 10, point20[1])
            lane14 = [point20, point31, point32]
            pointlist.append(lane14)
            point33 = (point22[0] + 5, point22[1])
            point34 = (point22[0] + 10, point22[1])
            lane15 = [point22, point33, point34]
            pointlist.append(lane15)
            point35 = (point24[0] + 5, point24[1])
            point36 = (point24[0] + 10, point24[1])
            lane16 = [point24, point35, point36]
            pointlist.append(lane16)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[10].reverse()
            pointlist[11].reverse()
            pointlist[12].reverse()

            return pointlist
        if flag == '6*4':
            point1 = self.Start
            point2 = (self.Start[0] + 5, self.Start[1])
            point3 = (self.Start[0] + 10, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W * 2)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W * 2)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W * 2)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 3)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 3)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 3)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (self.Start[0], self.Start[1] - self.W * 4)
            point14 = (self.Start[0] + 5, self.Start[1] - self.W * 4)
            point15 = (self.Start[0] + 10, self.Start[1] - self.W * 4)
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (self.Start[0], self.Start[1] - self.W * 5)
            point17 = (self.Start[0] + 5, self.Start[1] - self.W * 5)
            point18 = (self.Start[0] + 10, self.Start[1] - self.W * 5)
            lane6 = [point16, point17, point18]
            pointlist.append(lane6)
            point19 = (point3[0] + 5, point3[1] - self.W / 2)
            point20 = (point3[0] + 10, point3[1] - self.W)
            lane7 = [point3, point19, point20]
            pointlist.append(lane7)
            point21 = (point6[0] + 5, point6[1])
            lane8 = [point6, point21, point20]
            pointlist.append(lane8)
            point22 = (point9[0] + 5, point9[1])
            point23 = (point9[0] + 10, point9[1])
            lane9 = [point9, point22, point23]
            pointlist.append(lane9)
            point24 = (point12[0] + 5, point12[1])
            point25 = (point12[0] + 10, point12[1])
            lane10 = [point12, point24, point25]
            pointlist.append(lane10)
            point26 = (point15[0] + 5, point15[1])
            point27 = (point15[0] + 10, point15[1])
            lane11 = [point15, point26, point27]
            pointlist.append(lane11)
            point28 = (point18[0] + 5, point18[1] + self.W / 2)
            lane12 = [point18, point28, point27]
            pointlist.append(lane12)
            point29 = (point20[0] + 5, point20[1])
            point30 = (point20[0] + 10, point20[1])
            lane13 = [point20, point29, point30]
            pointlist.append(lane13)
            point31 = (point23[0] + 5, point23[1])
            point32 = (point23[0] + 10, point23[1])
            lane14 = [point23, point31, point32]
            pointlist.append(lane14)
            point33 = (point25[0] + 5, point25[1])
            point34 = (point25[0] + 10, point25[1])
            lane15 = [point25, point33, point34]
            pointlist.append(lane15)
            point35 = (point27[0] + 5, point27[1])
            point36 = (point27[0] + 10, point27[1])
            lane16 = [point27, point35, point36]
            pointlist.append(lane16)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            pointlist[12].reverse()
            pointlist[13].reverse()
            return pointlist

    def getboundarypoint(self):
        flag = self.Flag
        pointlist = []
        if flag == '1*2左':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + 5, point3[1] + self.W / 2)
            point8 = (point3[0] + 10, point3[1] + self.W)
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            point9 = (point3[0] + 5, point3[1])
            point10 = (point3[0] + 10, point3[1])
            lane4 = [point3, point9, point10]
            pointlist.append(lane4)
            point11 = (point6[0] + 5, point6[1])
            point12 = (point6[0] + 10, point6[1])
            lane5 = [point6, point11, point12]
            pointlist.append(lane5)
            point13 = (point8[0] + 5, point8[1])
            point14 = (point8[0] + 10, point8[1])
            lane6 = [point8, point13, point14]
            pointlist.append(lane6)
            point15 = (point10[0] + 5, point10[1])
            point16 = (point10[0] + 10, point10[1])
            lane7 = [point10, point15, point16]
            pointlist.append(lane7)
            point17 = (point12[0] + 5, point12[1])
            point18 = (point12[0] + 10, point12[1])
            lane8 = [point12, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '1*2右':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + 5, point3[1])
            point8 = (point3[0] + 10, point3[1])
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            point9 = (point6[0] + 5, point6[1])
            point10 = (point6[0] + 10, point6[1])
            lane4 = [point6, point9, point10]
            pointlist.append(lane4)
            point11 = (point6[0] + 5, point6[1] - self.W / 2)
            point12 = (point6[0] + 10, point6[1] - self.W)
            lane5 = [point6, point11, point12]
            pointlist.append(lane5)
            point13 = (point8[0] + 5, point8[1])
            point14 = (point8[0] + 10, point8[1])
            lane6 = [point8, point13, point14]
            pointlist.append(lane6)
            point15 = (point10[0] + 5, point10[1])
            point16 = (point10[0] + 10, point10[1])
            lane7 = [point10, point15, point16]
            pointlist.append(lane7)
            point17 = (point12[0] + 5, point12[1])
            point18 = (point12[0] + 10, point12[1])
            lane8 = [point12, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '2*1左':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1] - self.W / 2)
            point11 = (point3[0] + 10, point3[1] - self.W)
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + 5, point6[1])
            lane5 = [point6, point12, point11]
            pointlist.append(lane5)
            point13 = (point9[0] + 5, point9[1])
            point14 = (point9[0] + 10, point9[1])
            lane6 = [point9, point13, point14]
            pointlist.append(lane6)
            point15 = (point11[0] + 5, point11[1])
            point16 = (point11[0] + 10, point11[1])
            lane7 = [point11, point15, point16]
            pointlist.append(lane7)
            point17 = (point14[0] + 5, point14[1])
            point18 = (point14[0] + 10, point14[1])
            lane8 = [point14, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '2*1右':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1])
            point11 = (point3[0] + 10, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + 5, point6[1])
            point13 = (point6[0] + 10, point6[1])
            lane5 = [point6, point12, point13]
            pointlist.append(lane5)
            point14 = (point9[0] + 10, point9[1] + self.W / 2)
            lane6 = [point9, point14, point13]
            pointlist.append(lane6)
            point15 = (point11[0] + 5, point11[1])
            point16 = (point11[0] + 10, point11[1])
            lane7 = [point11, point15, point16]
            pointlist.append(lane7)
            point17 = (point13[0] + 5, point13[1])
            point18 = (point13[0] + 10, point13[1])
            lane8 = [point13, point17, point18]
            pointlist.append(lane8)
            pointlist = self.rotation(pointlist)
            return pointlist
        if flag == '2*3左':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1] + self.W / 2)
            point11 = (point3[0] + 10, point3[1] + self.W)
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point3[0] + 5, point3[1])
            point13 = (point3[0] + 10, point3[1])
            lane5 = [point3, point12, point13]
            pointlist.append(lane5)
            point14 = (point6[0] + 5, point6[1])
            point15 = (point6[0] + 10, point6[1])
            lane6 = [point6, point14, point15]
            pointlist.append(lane6)
            point16 = (point9[0] + 5, point9[1])
            point17 = (point9[0] + 10, point9[1])
            lane7 = [point9, point16, point17]
            pointlist.append(lane7)
            point18 = (point11[0] + 5, point11[1])
            point19 = (point11[0] + 10, point11[1])
            lane8 = [point11, point18, point19]
            pointlist.append(lane8)
            point20 = (point13[0] + 5, point13[1])
            point21 = (point13[0] + 10, point13[1])
            lane9 = [point13, point20, point21]
            pointlist.append(lane9)
            point22 = (point15[0] + 5, point15[1])
            point23 = (point15[0] + 10, point15[1])
            lane10 = [point15, point22, point23]
            pointlist.append(lane10)
            point24 = (point17[0] + 5, point17[1])
            point25 = (point17[0] + 10, point17[1])
            lane11 = [point17, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()

            return pointlist
        if flag == '2*3右':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + 5, point3[1])
            point11 = (point3[0] + 10, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + 5, point6[1])
            point13 = (point6[0] + 10, point6[1])
            lane5 = [point6, point12, point13]
            pointlist.append(lane5)
            point14 = (point9[0] + 5, point9[1])
            point15 = (point9[0] + 10, point9[1])
            lane6 = [point9, point14, point15]
            pointlist.append(lane6)
            point16 = (point9[0] + 5, point9[1] - self.W / 2)
            point17 = (point9[0] + 10, point9[1] - self.W)
            lane7 = [point9, point16, point17]
            pointlist.append(lane7)
            point18 = (point11[0] + 5, point11[1])
            point19 = (point11[0] + 10, point11[1])
            lane8 = [point11, point18, point19]
            pointlist.append(lane8)
            point20 = (point13[0] + 5, point13[1])
            point21 = (point13[0] + 10, point13[1])
            lane9 = [point13, point20, point21]
            pointlist.append(lane9)
            point22 = (point15[0] + 5, point15[1])
            point23 = (point15[0] + 10, point15[1])
            lane10 = [point15, point22, point23]
            pointlist.append(lane10)
            point24 = (point17[0] + 5, point17[1])
            point25 = (point17[0] + 10, point17[1])
            lane11 = [point17, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[7].reverse()
            return pointlist
        if flag == '3*2左':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1] - self.W / 2)
            point14 = (point3[0] + 10, point3[1] - self.W)
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + 5, point6[1])
            lane6 = [point6, point15, point14]
            pointlist.append(lane6)
            point16 = (point9[0] + 5, point9[1])
            point17 = (point9[0] + 10, point9[1])
            lane7 = [point9, point16, point17]
            pointlist.append(lane7)
            point18 = (point12[0] + 5, point12[1])
            point19 = (point12[0] + 10, point12[1])
            lane8 = [point12, point18, point19]
            pointlist.append(lane8)
            point20 = (point14[0] + 5, point14[1])
            point21 = (point14[0] + 10, point14[1])
            lane9 = [point14, point20, point21]
            pointlist.append(lane9)
            point22 = (point17[0] + 5, point17[1])
            point23 = (point17[0] + 10, point17[1])
            lane10 = [point17, point22, point23]
            pointlist.append(lane10)
            point24 = (point19[0] + 5, point19[1])
            point25 = (point19[0] + 10, point19[1])
            lane11 = [point19, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[8].reverse()
            return pointlist
        if flag == '3*2右':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1])
            point14 = (point3[0] + 10, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + 5, point6[1])
            point16 = (point6[0] + 10, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            point17 = (point9[0] + 5, point9[1])
            point18 = (point9[0] + 10, point9[1])
            lane7 = [point9, point17, point18]
            pointlist.append(lane7)
            point19 = (point12[0] + 5, point12[1] + self.W / 2)
            lane8 = [point12, point19, point18]
            pointlist.append(lane8)
            point20 = (point14[0] + 5, point14[1])
            point21 = (point14[0] + 10, point14[1])
            lane9 = [point14, point20, point21]
            pointlist.append(lane9)
            point22 = (point16[0] + 5, point16[1])
            point23 = (point16[0] + 10, point16[1])
            lane10 = [point16, point22, point23]
            pointlist.append(lane10)
            point24 = (point18[0] + 5, point18[1])
            point25 = (point18[0] + 10, point18[1])
            lane11 = [point18, point24, point25]
            pointlist.append(lane11)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[4].reverse()
            pointlist[8].reverse()
            return pointlist
        if flag == '3*4右':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1])
            point14 = (point3[0] + 10, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + 5, point6[1])
            point16 = (point6[0] + 10, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            point17 = (point9[0] + 5, point9[1])
            point18 = (point9[0] + 10, point9[1])
            lane7 = [point9, point17, point18]
            pointlist.append(lane7)
            point19 = (point12[0] + 5, point12[1])
            point20 = (point12[0] + 10, point12[1])
            lane8 = [point12, point19, point20]
            pointlist.append(lane8)
            point21 = (point12[0] + 5, point12[1] - self.W / 2)
            point22 = (point12[0] + 10, point12[1] - self.W)
            lane9 = [point12, point21, point22]
            pointlist.append(lane9)
            point23 = (point14[0] + 5, point14[1])
            point24 = (point14[0] + 10, point14[1])
            lane10 = [point14, point23, point24]
            pointlist.append(lane10)
            point25 = (point16[0] + 5, point16[1])
            point26 = (point16[0] + 10, point16[1])
            lane11 = [point16, point25, point26]
            pointlist.append(lane11)
            point27 = (point18[0] + 5, point18[1])
            point28 = (point18[0] + 10, point18[1])
            lane12 = [point18, point27, point28]
            pointlist.append(lane12)
            point29 = (point20[0] + 5, point20[1])
            point30 = (point20[0] + 10, point20[1])
            lane13 = [point20, point29, point30]
            pointlist.append(lane13)
            point31 = (point22[0] + 5, point22[1])
            point32 = (point22[0] + 10, point22[1])
            lane14 = [point22, point31, point32]
            pointlist.append(lane14)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[9].reverse()
            pointlist[10].reverse()
            return pointlist
        if flag == '3*4左':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + 5, point3[1] + self.W / 2)
            point14 = (point3[0] + 10, point3[1] + self.W)
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point3[0] + 5, point3[1])
            point16 = (point3[0] + 10, point3[1])
            lane6 = [point3, point15, point16]
            pointlist.append(lane6)
            point17 = (point6[0] + 5, point6[1])
            point18 = (point6[0] + 10, point6[1])
            lane7 = [point6, point17, point18]
            pointlist.append(lane7)
            point19 = (point9[0] + 5, point9[1])
            point20 = (point9[0] + 10, point9[1])
            lane8 = [point9, point19, point20]
            pointlist.append(lane8)
            point21 = (point12[0] + 5, point12[1])
            point22 = (point12[0] + 10, point12[1])
            lane9 = [point12, point21, point22]
            pointlist.append(lane9)
            point23 = (point14[0] + 5, point14[1])
            point24 = (point14[0] + 10, point14[1])
            lane10 = [point14, point23, point24]
            pointlist.append(lane10)
            point25 = (point16[0] + 5, point16[1])
            point26 = (point16[0] + 10, point16[1])
            lane11 = [point16, point25, point26]
            pointlist.append(lane11)
            point27 = (point18[0] + 5, point18[1])
            point28 = (point18[0] + 10, point18[1])
            lane12 = [point18, point27, point28]
            pointlist.append(lane12)
            point29 = (point20[0] + 5, point20[1])
            point30 = (point20[0] + 10, point20[1])
            lane13 = [point20, point29, point30]
            pointlist.append(lane13)
            point31 = (point22[0] + 5, point22[1])
            point32 = (point22[0] + 10, point22[1])
            lane14 = [point22, point31, point32]
            pointlist.append(lane14)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[9].reverse()
            pointlist[10].reverse()
            return pointlist
        if flag == '4*3左':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (self.Start[0], self.Start[1] - self.W * 3.5)
            point14 = (self.Start[0] + 5, self.Start[1] - self.W * 3.5)
            point15 = (self.Start[0] + 10, self.Start[1] - self.W * 3.5)
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (point3[0] + 5, point3[1] - self.W / 2)
            point17 = (point3[0] + 10, point3[1] - self.W)
            lane6 = [point3, point16, point17]
            pointlist.append(lane6)
            point18 = (point6[0] + 5, point6[1])
            lane7 = [point6, point18, point17]
            pointlist.append(lane7)
            point19 = (point9[0] + 5, point9[1])
            point20 = (point9[0] + 10, point9[1])
            lane8 = [point9, point19, point20]
            pointlist.append(lane8)
            point21 = (point12[0] + 5, point12[1])
            point22 = (point12[0] + 10, point12[1])
            lane9 = [point12, point21, point22]
            pointlist.append(lane9)
            point23 = (point15[0] + 5, point15[1])
            point24 = (point15[0] + 10, point15[1])
            lane10 = [point15, point23, point24]
            pointlist.append(lane10)
            point25 = (point17[0] + 5, point17[1])
            point26 = (point17[0] + 10, point17[1])
            lane11 = [point17, point25, point26]
            pointlist.append(lane11)
            point27 = (point20[0] + 5, point20[1])
            point28 = (point20[0] + 10, point20[1])
            lane12 = [point20, point27, point28]
            pointlist.append(lane12)
            point29 = (point22[0] + 5, point22[1])
            point30 = (point22[0] + 10, point22[1])
            lane13 = [point22, point29, point30]
            pointlist.append(lane13)
            point31 = (point24[0] + 5, point24[1])
            point32 = (point24[0] + 10, point24[1])
            lane14 = [point24, point31, point32]
            pointlist.append(lane14)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[10].reverse()
            return pointlist
        if flag == '4*3右':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (self.Start[0], self.Start[1] - self.W * 3.5)
            point14 = (self.Start[0] + 5, self.Start[1] - self.W * 3.5)
            point15 = (self.Start[0] + 10, self.Start[1] - self.W * 3.5)
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (point3[0] + 5, point3[1])
            point17 = (point3[0] + 10, point3[1])
            lane6 = [point3, point16, point17]
            pointlist.append(lane6)
            point18 = (point6[0] + 5, point6[1])
            point19 = (point6[0] + 10, point6[1])
            lane7 = [point6, point18, point19]
            pointlist.append(lane7)
            point20 = (point9[0] + 5, point9[1])
            point21 = (point9[0] + 10, point9[1])
            lane8 = [point9, point20, point21]
            pointlist.append(lane8)
            point22 = (point12[0] + 5, point12[1])
            point23 = (point12[0] + 10, point12[1])
            lane9 = [point12, point22, point23]
            pointlist.append(lane9)
            point24 = (point15[0] + 5, point15[1] + self.W / 2)
            lane10 = [point15, point24, point23]
            pointlist.append(lane10)
            point25 = (point17[0] + 5, point17[1])
            point26 = (point17[0] + 10, point17[1])
            lane11 = [point17, point25, point26]
            pointlist.append(lane11)
            point27 = (point19[0] + 5, point19[1])
            point28 = (point19[0] + 10, point19[1])
            lane12 = [point19, point27, point28]
            pointlist.append(lane12)
            point29 = (point21[0] + 5, point21[1])
            point30 = (point21[0] + 10, point21[1])
            lane13 = [point21, point29, point30]
            pointlist.append(lane13)
            point31 = (point23[0] + 5, point23[1])
            point32 = (point23[0] + 10, point23[1])
            lane14 = [point23, point31, point32]
            pointlist.append(lane14)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[10].reverse()
            pointlist[11].reverse()
            return pointlist
        if flag == '4*6':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (self.Start[0], self.Start[1] - self.W * 3.5)
            point14 = (self.Start[0] + 5, self.Start[1] - self.W * 3.5)
            point15 = (self.Start[0] + 10, self.Start[1] - self.W * 3.5)
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (point3[0] + 5, point3[1] + self.W / 2)
            point17 = (point3[0] + 10, point3[1] + self.W)
            lane6 = [point3, point16, point17]
            pointlist.append(lane6)
            point18 = (point3[0] + 5, point3[1])
            point19 = (point3[0] + 10, point3[1])
            lane7 = [point3, point18, point19]
            pointlist.append(lane7)
            point20 = (point6[0] + 5, point6[1])
            point21 = (point6[0] + 10, point6[1])
            lane8 = [point6, point20, point21]
            pointlist.append(lane8)
            point22 = (point9[0] + 5, point9[1])
            point23 = (point9[0] + 10, point9[1])
            lane9 = [point9, point22, point23]
            pointlist.append(lane9)
            point24 = (point12[0] + 5, point12[1])
            point25 = (point12[0] + 10, point12[1])
            lane10 = [point12, point24, point25]
            pointlist.append(lane10)
            point26 = (point15[0] + 5, point15[1])
            point27 = (point15[0] + 10, point15[1])
            lane11 = [point15, point26, point27]
            pointlist.append(lane11)
            point28 = (point15[0] + 5, point15[1] - self.W / 2)
            point29 = (point15[0] + 10, point15[1] - self.W)
            lane12 = [point15, point28, point29]
            pointlist.append(lane12)
            point30 = (point17[0] + 5, point17[1])
            point31 = (point17[0] + 10, point17[1])
            lane13 = [point17, point30, point31]
            pointlist.append(lane13)
            point32 = (point19[0] + 5, point19[1])
            point33 = (point19[0] + 10, point19[1])
            lane14 = [point19, point32, point33]
            pointlist.append(lane14)
            point34 = (point21[0] + 5, point21[1])
            point35 = (point21[0] + 10, point21[1])
            lane15 = [point21, point34, point35]
            pointlist.append(lane15)
            point36 = (point23[0] + 5, point23[1])
            point37 = (point23[0] + 10, point23[1])
            lane16 = [point23, point36, point37]
            pointlist.append(lane16)
            point38 = (point25[0] + 5, point25[1])
            point39 = (point25[0] + 10, point25[1])
            lane17 = [point25, point38, point39]
            pointlist.append(lane17)
            point40 = (point27[0] + 5, point27[1])
            point41 = (point27[0] + 10, point27[1])
            lane18 = [point27, point40, point41]
            pointlist.append(lane18)
            point42 = (point29[0] + 5, point29[1])
            point43 = (point29[0] + 10, point29[1])
            lane19 = [point29, point42, point43]
            pointlist.append(lane19)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[12].reverse()
            pointlist[13].reverse()
            pointlist[14].reverse()
            return pointlist
        if flag == '6*4':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (self.Start[0] + 5, self.Start[1] + self.W / 2)
            point3 = (self.Start[0] + 10, self.Start[1] + self.W / 2)
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (self.Start[0], self.Start[1] - self.W / 2)
            point5 = (self.Start[0] + 5, self.Start[1] - self.W / 2)
            point6 = (self.Start[0] + 10, self.Start[1] - self.W / 2)
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (self.Start[0], self.Start[1] - self.W / 2 - self.W)
            point8 = (self.Start[0] + 5, self.Start[1] - self.W / 2 - self.W)
            point9 = (self.Start[0] + 10, self.Start[1] - self.W / 2 - self.W)
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (self.Start[0], self.Start[1] - self.W * 2.5)
            point11 = (self.Start[0] + 5, self.Start[1] - self.W * 2.5)
            point12 = (self.Start[0] + 10, self.Start[1] - self.W * 2.5)
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (self.Start[0], self.Start[1] - self.W * 3.5)
            point14 = (self.Start[0] + 5, self.Start[1] - self.W * 3.5)
            point15 = (self.Start[0] + 10, self.Start[1] - self.W * 3.5)
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (self.Start[0], self.Start[1] - self.W * 4.5)
            point17 = (self.Start[0] + 5, self.Start[1] - self.W * 4.5)
            point18 = (self.Start[0] + 10, self.Start[1] - self.W * 4.5)
            lane6 = [point16, point17, point18]
            pointlist.append(lane6)
            point19 = (self.Start[0], self.Start[1] - self.W * 5.5)
            point20 = (self.Start[0] + 5, self.Start[1] - self.W * 5.5)
            point21 = (self.Start[0] + 10, self.Start[1] - self.W * 5.5)
            lane7 = [point19, point20, point21]
            pointlist.append(lane7)
            point22 = (point3[0] + 5, point3[1] - self.W / 2)
            point23 = (point3[0] + 10, point3[1] - self.W)
            lane8 = [point3, point22, point23]
            pointlist.append(lane8)
            point24 = (point6[0] + 5, point6[1])
            lane9 = [point6, point24, point23]
            pointlist.append(lane9)
            point25 = (point9[0] + 5, point9[1])
            point26 = (point9[0] + 10, point9[1])
            lane10 = [point9, point25, point26]
            pointlist.append(lane10)
            point27 = (point12[0] + 5, point12[1])
            point28 = (point12[0] + 10, point12[1])
            lane11 = [point12, point27, point28]
            pointlist.append(lane11)
            point29 = (point15[0] + 5, point15[1])
            point30 = (point15[0] + 10, point15[1])
            lane12 = [point15, point29, point30]
            pointlist.append(lane12)
            point31 = (point18[0] + 5, point18[1])
            point32 = (point18[0] + 10, point18[1])
            lane13 = [point18, point31, point32]
            pointlist.append(lane13)
            point33 = (point21[0] + 5, point21[1] + self.W / 2)
            lane14 = [point21, point33, point32]
            pointlist.append(lane14)
            point34 = (point23[0] + 5, point23[1])
            point35 = (point23[0] + 10, point23[1])
            lane15 = [point23, point34, point35]
            pointlist.append(lane15)
            point36 = (point26[0] + 5, point26[1])
            point37 = (point26[0] + 10, point26[1])
            lane16 = [point26, point36, point37]
            pointlist.append(lane16)
            point38 = (point28[0] + 5, point28[1])
            point39 = (point28[0] + 10, point28[1])
            lane17 = [point28, point38, point39]
            pointlist.append(lane17)
            point40 = (point30[0] + 5, point30[1])
            point41 = (point30[0] + 10, point30[1])
            lane18 = [point30, point40, point41]
            pointlist.append(lane18)
            point42 = (point32[0] + 5, point32[1])
            point43 = (point32[0] + 10, point32[1])
            lane19 = [point32, point42, point43]
            pointlist.append(lane19)
            pointlist = self.rotation(pointlist)

            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
            pointlist[14].reverse()
            pointlist[15].reverse()
            return pointlist

    def PointtoString(self, lst):
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def generate_road(self, f):
        Widget.LaneID += self.LaneNumber
        Widget.BoundaryID += self.BoundaryNumber
        Widget.WidgetID += 1
        # lane
        lanes = str(self.StartLaneID) + ':' + str(self.StartLaneID + self.LaneNumber - 1)  # 当前组件涉及到的lane
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a LaneSwitch widget')
        printAutoInd(f, '% Set the lanes.')
        for lane in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
            printAutoInd(f, 'rrMap.Lanes(' + str(lane) + ') = roadrunner.hdmap.Lane();')
        laneidlist = []
        for i in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
            laneidlist.append('Lane' + str(i))
        laneid = ','.join(['"' + i + '"' for i in laneidlist])
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').ID] = deal(' + laneid + ');')
        lanepointlist = self.getlanepoint()
        lanepointstring = self.PointtoString(lanepointlist)
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').Geometry] = deal(' + lanepointstring + ');')
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').TravelDirection] = deal("Forward");')
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
        boundarypointlist = self.getboundarypoint()
        boundarypointstring = self.PointtoString(boundarypointlist)
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').Geometry] = deal(' + boundarypointstring + ');')
     
        parametricattributelist = []
        for laneboundary in laneboundaryidlist:
            s = self.LaneAssetType.setdefault(laneboundary, 'SW')
            parametricattributelist.append(s)
        laneassetlist = []
        for i in parametricattributelist:
            if i == 'SW':
                laneassetlist.append('markingAttribSW')
            if i == 'SY':
                laneassetlist.append('markingAttribSY')
            if i == 'DW':
                laneassetlist.append('markingAttribDW')
            if i == 'DY':
                laneassetlist.append('markingAttribDY')
            if i == 'DSW':
                laneassetlist.append('markingAttribDSW')
            if i == 'DSY':
                laneassetlist.append('markingAttribDSY')
            if i == 'SDW':
                laneassetlist.append('markingAttribSDW')
            if i == 'SDY':
                laneassetlist.append('markingAttribSDY')
        laneasset = ','.join(laneassetlist)
        printAutoInd(f, '[rrMap.LaneBoundaries(' + boundaries + ').ParametricAttributes] = deal(' + laneasset + ');')
       
        printAutoInd(f, '% Associate lanes and lane boundaries.')
        if self.Flag == '1*2左':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
        elif self.Flag == '1*2右':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
        elif self.Flag == '2*1左':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
        elif self.Flag == '2*1右':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
        elif self.Flag == '2*3左':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '2*3右':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '3*2左':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '3*2右':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '3*4右':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
        elif self.Flag == '3*4左':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
        elif self.Flag == '4*3左':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
        elif self.Flag == '4*3右':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
        elif self.Flag == '4*6':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 11) + '),"Boundary' + str(
                self.StartBoundaryID + 14) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 11) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 12) + '),"Boundary' + str(
                self.StartBoundaryID + 15) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 12) + '),"Boundary' + str(
                self.StartBoundaryID + 14) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 13) + '),"Boundary' + str(
                self.StartBoundaryID + 15) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 13) + '),"Boundary' + str(
                self.StartBoundaryID + 16) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 14) + '),"Boundary' + str(
                self.StartBoundaryID + 16) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 14) + '),"Boundary' + str(
                self.StartBoundaryID + 17) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 15) + '),"Boundary' + str(
                self.StartBoundaryID + 17) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 15) + '),"Boundary' + str(
                self.StartBoundaryID + 18) + '",Alignment="Forward");')
        elif self.Flag == '6*4':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 9) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 10) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 11) + '),"Boundary' + str(
                self.StartBoundaryID + 12) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 11) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 12) + '),"Boundary' + str(
                self.StartBoundaryID + 15) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 12) + '),"Boundary' + str(
                self.StartBoundaryID + 14) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 13) + '),"Boundary' + str(
                self.StartBoundaryID + 16) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 13) + '),"Boundary' + str(
                self.StartBoundaryID + 15) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 14) + '),"Boundary' + str(
                self.StartBoundaryID + 16) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 14) + '),"Boundary' + str(
                self.StartBoundaryID + 17) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 15) + '),"Boundary' + str(
                self.StartBoundaryID + 17) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 15) + '),"Boundary' + str(
                self.StartBoundaryID + 18) + '",Alignment="Forward");')
        # 关联lane的前继和后继
        printAutoInd(f, '% Combine lanes')
        if self.Flag == '1*2左':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '1*2右':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '2*1左':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
        elif self.Flag == '2*1右':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '2*3左':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
        elif self.Flag == '2*3右':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
        elif self.Flag == '3*2左':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
        elif self.Flag == '3*2右':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
        elif self.Flag == '3*4右':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
        elif self.Flag == '3*4左':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
        elif self.Flag == '4*3左':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
        elif self.Flag == '4*3右':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
        elif self.Flag == '4*6':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 12) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 13) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 14) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 15) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 12) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 13) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 14) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 15) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
        elif self.Flag == '6*4':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 12) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 12) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 13) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 14) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 15) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 15) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 12) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 13) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 14) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 15) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')

        printAutoInd(f, '% End of this widget')
