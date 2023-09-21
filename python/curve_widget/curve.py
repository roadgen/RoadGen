from func.printAuto import printAutoInd
from func.widget import Widget
import sympy as sy
import math
from math import factorial

from matplotlib.pyplot import plot


class Curve(Widget):
    WidgetID = 1
    Start = (0, 0)  
    CurveSet = (0, 100)
    ControlPoint = []
    W = 3.5  
    R = 5  
    StartLaneID = 1  
    StartBoundaryID = 1  
    LaneNumber = 1  
    BoundaryNumber = 1
    
    LaneAssetType = {}  
    k = '+0'  
    LaneType = 'Driving'  
    Direction = 0  # 0: direction change to right, 1: direction change to left, 2 no change
    Function = '1/4Circle'
    Flag = ''  

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.CurveSet = dict1.setdefault('CurveSet', (0, 100))
        self.ControlPoint = dict1.setdefault('ControlPoint', [])
        self.W = dict1.get('W')
        self.R = dict1.setdefault('R', 10)
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.LaneNumber = dict1.get('LaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        # self.TravelDirection = Widget.get_self_TravelDirection(dict1.get('TravelDirection'))
        self.LaneAssetType = Widget.get_self_LaneAssetType(dict1.get('LaneAssetType'))
        self.k = dict1.get('K')
        self.Function = dict1.get('Function')
        self.Direction = dict1.get('Direction')
        self.Flag = dict1.get('Flag')
        self.Type =dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag
        Currents_info["CurrentLanes"] = []
        if self.LaneNumber == 1:  # 单行道，直接返回StartLaneID
            Currents_info["CurrentLanes"].append(self.StartLaneID)
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 2:  # 双行道，返回两条LaneID信息
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1])
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 3:  # 三行道，返回三条LaneID信息
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self.StartLaneID + 2])
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 4:  # 四车道，返回四条LaneID信息
            Currents_info["CurrentLanes"].extend(
                [self.StartLaneID, self.StartLaneID + 1, self.StartLaneID + 2, self.StartLaneID + 4])
            Currents_info["Type"] = self.Flag
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        Next = dict()
        if self.Function == '1/4Circle':
            if self.Direction == 0:
                r = self.R + self.W * (self.LaneNumber - 1)
                p = (float('{:.3f}'.format(self.Start[0] + r)),
                     float('{:.3f}'.format(self.Start[1] - self.R - self.W * (self.LaneNumber - 1))))
                endpoint = p
                if self.k == '+0':
                    Next['direction'] = '-'
                elif self.k == '-0':
                    Next['direction'] = '+'
                elif self.k == '+':
                    Next['direction'] = '+0'
                elif self.k == '-':
                    Next['direction'] = '-0'
            else:
                center = (self.Start[0], self.Start[1] + self.R)
                point1 = self.Start
                p = (float('{:.3f}'.format(point1[0] + self.R)), float('{:.3f}'.format(point1[1] + self.R)))
                endpoint = p
                if self.k == '+0':
                    Next['direction'] = '+'
                elif self.k == '-0':
                    Next['direction'] = '-'
                elif self.k == '+':
                    Next['direction'] = '-0'
                elif self.k == '-':
                    Next['direction'] = '+0'
        elif self.Function == 'S':
            if self.Direction == 0:
                point1 = self.Start
                center2 = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) * 2 - self.R * 3)
                r2 = self.R
                c2 = sy.Circle(center2, r2)
                x, y = sy.symbols('x,y')
                eq2 = c2.equation(x, y)
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point1[0]), y)]]
                a = sorted(a)
                endpoint = (point1[0], a[0])
            else:
                point1 = self.Start
                center2 = (self.Start[0], self.Start[1] + self.W * (self.LaneNumber - 1) + self.R * 3)
                r2 = self.R + self.W * (self.LaneNumber - 1)
                c2 = sy.Circle(center2, r2)
                x, y = sy.symbols('x,y')
                eq2 = c2.equation(x, y)
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point1[0]), y)]]
                a = sorted(a)
                endpoint = (point1[0], a[1])

            Next['direction'] = self.k
        elif self.Function == 'Bezier':
            if self.Direction == 0:
                endpoint = (self.Start[0] + self.CurveSet[1], self.Start[1] - self.CurveSet[0])
            elif self.Direction == 1:
                endpoint = (self.Start[0] + self.CurveSet[1], self.Start[1] + self.CurveSet[0])
            elif self.Direction == 2:
                endpoint = (self.Start[0] + self.CurveSet[1], self.Start[1])
            Next['direction'] = self.k

        Next['endpoint'] = self.roate_endpoints(endpoint)
        Next['type'] = self.Flag
        Next['lanes'] = list(range(self.StartLaneID, self.StartLaneID + self.LaneNumber))
        Next['ID'] = self.WidgetID
        Next['current'] = self.Flag + self.Function + '_' + self.Type
        Nexts.append(Next)
        return Nexts


    def get_coveredArea(self):
        result=[]
        if self.Function=='1/4Circle':
            result1=[]
            if self.Direction == 0:
                point1=(self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) - self.R) #center
                point2=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2,self.Start[1] - self.W * (self.LaneNumber - 1) - self.R)
                point3=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2,self.Start[1]+self.W/2)
                point4=(self.Start[0],self.Start[1]+self.W/2)
                result1.append(point1)
                result1.append(point2)
                result1.append(point3)
                result1.append(point4)
                result.append(result1)
            elif self.Direction == 1:
                point1=(self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) - self.W/2) 
                point2=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2,self.Start[1] - self.W * (self.LaneNumber - 1) - self.W/2)
                point3=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2,self.Start[1] + self.R)
                point4=(self.Start[0], self.Start[1] + self.R) #center
                result1.append(point1)
                result1.append(point2)
                result1.append(point3)
                result1.append(point4)
                result.append(result1)
            finalResult = self.rotation(result)
            return finalResult
        elif self.Function=='S':
            result1=[]
            result2=[]
            if self.Direction == 0:
                point1 = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1)*2 - self.R*2-self.W/2)
                point2=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2, self.Start[1] - self.W * (self.LaneNumber - 1)*2 - self.R*2-self.W/2)
                point3=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2,self.Start[1] + self.W/2)
                point4=(self.Start[0], self.Start[1] + self.W/2)
                result1.append(point1)
                result1.append(point2)
                result1.append(point3)
                result1.append(point4)
                result.append(result1)

                point5=(self.Start[0],point1[1]+self.W*self.LaneNumber)
                point6=(self.Start[0]-self.W * (self.LaneNumber - 1) - self.R-self.W/2,point5[1])
                point7=(self.Start[0]-self.W * (self.LaneNumber - 1) - self.R-self.W/2,point5[1]-self.W*(self.LaneNumber*2-1)-self.R*2)
                point8=(self.Start[0],point7[1])
                result2.append(point5)
                result2.append(point6)
                result2.append(point7)
                result2.append(point8)
                result.append(result2)
            elif self.Direction == 1:
                point1=(self.Start[0],self.Start[1]- self.W * (self.LaneNumber - 1) - self.W/2)
                point2=(self.Start[0]+self.W * (self.LaneNumber - 1) + self.R+self.W/2,point1[1])
                point3=(point2[0],self.Start[1]+self.R*2+self.W/2+self.W * (self.LaneNumber - 1))
                point4=(self.Start[0],point3[1])
                result1.append(point1)
                result1.append(point2)
                result1.append(point3)
                result1.append(point4)
                result.append(result1)

                point5=(self.Start[0],point4[1]-self.W*self.LaneNumber)
                point6=(self.Start[0],point5[1]+self.W*(self.LaneNumber*2-1)+self.R*2)
                point7=(self.Start[0]-self.W * (self.LaneNumber - 1) - self.R-self.W/2,point6[1])
                point8=(point7[0],point5[1])
                result2.append(point5)
                result2.append(point6)
                result2.append(point7)
                result2.append(point8)
                result.append(result2)
            finalResult=self.rotation(result)
            return finalResult
        elif self.Function=="Bezier":
            result1=[]
            boundarylist=self.getboundarypoint()
            x=[]
            y=[]
            for boundary in boundarylist:
                for point in boundary:
                    x.append(point[0])
                    y.append(point[1])
            point1=(min(x),min(y))
            point2=(max(x),point1[1])
            point3=(point2[0],max(y))
            point4=(point1[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
            return (result)
       

    def roate_endpoints(self,point):
        if self.k == '+0':
            return point
        if self.k == '-':  # 绕start顺时针旋转90度
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi / 2)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi / 2)) + self.Start[1]))
            return x, y
        if self.k == '-0':  # 绕start顺时针旋转180度
            x = float(
                '{:.3f}'.format((point[0] - self.Start[0]) * int(math.cos(math.pi)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi)) + self.Start[0]))
            y = float(
                '{:.3f}'.format((point[1] - self.Start[1]) * int(math.cos(math.pi)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi)) + self.Start[1]))
            return x, y
        if self.k == '+':  # 绕start顺时针旋转270度
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
        if self.k == '-':  # 绕start顺时针旋转90度
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
        if self.k == '-0':  # 绕start顺时针旋转180度
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
        if self.k == '+':  # 绕start顺时针旋转270度
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

    def bezier(self, lst):  # x轴方向
        N = len(lst)
        n = N - 1
        px = []
        py = []
        p = lst[-1][0]
        num = 1 / p
        for T in range(int(p) + 1):
            t = T * num
            x, y = 0, 0
            for i in range(N):
                B = factorial(n) * t ** i * (1 - t) ** (n - i) / (factorial(i) * factorial(n - i))
                x += lst[i][0] * B
                y += lst[i][1] * B
            px.append(round(x, 3))
            py.append(round(y, 3))


        lst0 = list(zip(px, py))
        lst0.append(lst[-1])
 

        return lst0

    def getlanepoint(self):
        function = self.Function
        flag = self.Flag
        pointlist = []
        if function == '1/4Circle':
            if self.Direction == 0:
                center = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) - self.R)
                point1 = self.Start
                r = self.R + self.W * (self.LaneNumber - 1)
                for i in range(self.LaneNumber):
                    c = sy.Circle(sy.Point(center), r)
                    x, y = sy.symbols('x,y')
                    eq = c.equation(x, y)
                    lanelist = []
                    for m in range(int(r) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        if len(a) == 2:
                            lanelist.append((point1[0] + m, a[1]))
                        else:
                            lanelist.append((point1[0] + m, a[0]))
                    # p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + r), y)]]
                    # p = (point1[0] + r, p[0])
                    p = (float('{:.3f}'.format(self.Start[0] + r)),
                         float('{:.3f}'.format(self.Start[1] - self.R - self.W * (self.LaneNumber - 1))))
                    if p not in lanelist:
                        lanelist.append(p)
                    pointlist.append(lanelist)
                    r -= self.W
                    point1 = (point1[0], point1[1] - self.W)
                pointlist = self.rotation(pointlist)
            elif self.Direction == 1:
                center = (self.Start[0], self.Start[1] + self.R)
                point1 = self.Start
                r = self.R
                for i in range(self.LaneNumber):
                    c = sy.Circle(sy.Point(center), r)
                    x, y = sy.symbols('x,y')
                    eq = c.equation(x, y)
                    lanelist = []
                    for m in range(int(r) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        if len(a) == 2:
                            lanelist.append((point1[0] + m, a[0]))
                        else:
                            lanelist.append((point1[0] + m, a[0]))
                    # p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + r), y)]]
                    # p = (point1[0] + r, p[0])
                    p = (float('{:.3f}'.format(point1[0] + r)), float('{:.3f}'.format(point1[1] + self.R)))
                    if p not in lanelist:
                        lanelist.append(p)
                    pointlist.append(lanelist)
                    r += self.W
                pointlist = self.rotation(pointlist)

        elif function == 'S':
            if self.Direction == 0:
                point1 = self.Start
                center1 = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) - self.R)
                center2 = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) * 2 - self.R * 3)
                r1 = self.R + self.W * (self.LaneNumber - 1)
                r2 = self.R
                for i in range(self.LaneNumber):
                    c1 = sy.Circle(center1, r1)
                    x, y = sy.symbols('x,y')
                    eq1 = c1.equation(x, y)
                    lanelst1 = []
                    for m in range(int(r1) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] + m, a[1])
                            lst.append(p1)
                            p2 = (point1[0] + m, a[0])
                            lst.append(p2)
                        else:
                            p = (point1[0] + m, a[0])
                            lst.append(p)
                        lanelst1[m:m] = lst
                    if len(lanelst1) % 2 == 0:
                        l = point1[0] + r1
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, l), y)]]
                        lanelst1[int(len(lanelst1) / 2):int(len(lanelst1) / 2)] = [(l, b[0])]
                    c2 = sy.Circle(center2, r2)
                    x, y = sy.symbols('x,y')
                    eq2 = c2.equation(x, y)
                    lanelst2 = []
                    for m in range(int(r2) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point1[0] - m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] - m, a[1])
                            lst.append(p1)
                            p2 = (point1[0] - m, a[0])
                            lst.append(p2)
                        else:
                            p = (point1[0] - m, a[0])
                            lst.append(p)
                        lanelst2[m:m] = lst
                    if len(lanelst2) % 2 == 0:
                        l = point1[0] - r2
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, l), y)]]
                        lanelst2[int(len(lanelst2) / 2):int(len(lanelst2) / 2)] = [(l, b[0])]
                    lanelst = lanelst1[:-1] + lanelst2
                    pointlist.append(lanelst)
                    r1 -= self.W
                    r2 += self.W
                pointlist = self.rotation(pointlist)

            elif self.Direction == 1:
                point1 = self.Start
                center1 = (self.Start[0], self.Start[1] + self.R)
                center2 = (self.Start[0], self.Start[1] + self.W * (self.LaneNumber - 1) + self.R * 3)
                r1 = self.R
                r2 = self.R + self.W * (self.LaneNumber - 1)
                for i in range(self.LaneNumber):
                    c1 = sy.Circle(center1, r1)
                    x, y = sy.symbols('x,y')
                    eq1 = c1.equation(x, y)
                    lanelst1 = []
                    for m in range(int(r1) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] + m, a[0])
                            lst.append(p1)
                            p2 = (point1[0] + m, a[1])
                            lst.append(p2)
                        else:
                            p = (point1[0] + m, a[0])
                            lst.append(p)
                        lanelst1[m:m] = lst
                    if len(lanelst1) % 2 == 0:
                        l = point1[0] + r1
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, l), y)]]
                        lanelst1[int(len(lanelst1) / 2):int(len(lanelst1) / 2)] = [(l, b[0])]
                    c2 = sy.Circle(center2, r2)
                    x, y = sy.symbols('x,y')
                    eq2 = c2.equation(x, y)
                    lanelst2 = []
                    for m in range(int(r2) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point1[0] - m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] - m, a[0])
                            lst.append(p1)
                            p2 = (point1[0] - m, a[1])
                            lst.append(p2)
                        else:
                            p = (point1[0] - m, a[0])
                            lst.append(p)
                        lanelst2[m:m] = lst
                    if len(lanelst2) % 2 == 0:
                        l = point1[0] - r2
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, l), y)]]
                        lanelst2[int(len(lanelst2) / 2):int(len(lanelst2) / 2)] = [(l, b[0])]
                    lanelst = lanelst1[:-1] + lanelst2
                    pointlist.append(lanelst)
                    r1 += self.W
                    r2 -= self.W
                pointlist = self.rotation(pointlist)


        elif function == 'Bezier':
            if self.Direction == 0:
                pointS = self.Start
                pointE = (self.Start[0] + self.CurveSet[1], self.Start[1] - self.CurveSet[0])
                lanelst = [pointS]
                lanelst = lanelst + self.ControlPoint
                lanelst.append(pointE)
                for i in range(self.LaneNumber):
                    lst = self.bezier(lanelst)
                    pointlist.append(lst)
                    lanelst = [(i[0], i[1] - self.W) for i in lanelst]

                pointlist = self.rotation(pointlist)

            elif self.Direction == 1:
                pointS = self.Start
                # print('start:')
                # print(pointS)
                pointE = (self.Start[0] + self.CurveSet[1], self.Start[1] + self.CurveSet[0])
                # print(pointE)
                lanelst = [pointS]
                lanelst = lanelst + self.ControlPoint
                lanelst.append(pointE)
                # print(lanelst)
                for i in range(self.LaneNumber):
                    lst = self.bezier(lanelst)
                    pointlist.append(lst)
                    lanelst = [(i[0], i[1] - self.W) for i in lanelst]

                # print(pointlist)

                pointlist = self.rotation(pointlist)
                # print(pointlist)

            elif self.Direction == 2:
                pointS = self.Start
                pointE = (self.Start[0] + self.CurveSet[1], self.Start[1])
                lanelst = [pointS]
                lanelst = lanelst + self.ControlPoint
                lanelst.append(pointE)
                for i in range(self.LaneNumber):
                    lst = self.bezier(lanelst)
                    pointlist.append(lst)
                    lanelst = [(i[0], i[1] - self.W) for i in lanelst]

                pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线双行道':
            pointlist = pointlist
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            pointlist[0].reverse()
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            pointlist[0].reverse()
        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()

        return pointlist

    def getboundarypoint(self):
        function = self.Function
        flag = self.Flag
        pointlist = []
        if function == '1/4Circle':
            if self.Direction == 0:
                center = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) - self.R)
                point1 = (self.Start[0], self.Start[1] + self.W / 2)
                r = self.R + self.W * (self.LaneNumber - 1) + self.W / 2
                for i in range(self.BoundaryNumber):
                    c = sy.Circle(sy.Point(center), r)
                    x, y = sy.symbols('x,y')
                    eq = c.equation(x, y)
                    lanelist = []
                    for m in range(int(r) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        if len(a) == 2:
                            lanelist.append((point1[0] + m, a[1]))
                        else:
                            lanelist.append((point1[0] + m, a[0]))
                    # p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + r), y)]]
                    # p = (point1[0] + r, p[0])
                    p = (float('{:.3f}'.format(self.Start[0] + r)),
                         float('{:.3f}'.format(self.Start[1] - self.R - self.W * (self.LaneNumber - 1))))
                    if p not in lanelist:
                        lanelist.append(p)
                    pointlist.append(lanelist)
                    r = r - self.W
                    point1 = (point1[0], point1[1] - self.W)
                pointlist = self.rotation(pointlist)

            elif self.Direction == 1:
                center = (self.Start[0], self.Start[1] + self.R)
                point1 = (self.Start[0], self.Start[1] - self.W / 2)
                r = self.R - self.W / 2
                for i in range(self.BoundaryNumber):
                    c = sy.Circle(sy.Point(center), r)
                    x, y = sy.symbols('x,y')
                    eq = c.equation(x, y)
                    lanelist = []
                    for m in range(int(r) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        if len(a) == 2:
                            lanelist.append((point1[0] + m, a[0]))
                        else:
                            lanelist.append((point1[0] + m, a[0]))
                    # p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + r), y)]]
                    # p = (point1[0] + r, p[0])
                    p = (float('{:.3f}'.format(self.Start[0] + r)), float('{:.3f}'.format(self.Start[1] + self.R)))
                    if p not in lanelist:
                        lanelist.append(p)
                    pointlist.append(lanelist)
                    r += self.W
                    point1 = (point1[0], point1[1] - self.W)
                pointlist = self.rotation(pointlist)


        elif function == 'S':
            if self.Direction == 0:
                point1 = (self.Start[0], self.Start[1] + self.W / 2)
                center1 = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) - self.R)
                center2 = (self.Start[0], self.Start[1] - self.W * (self.LaneNumber - 1) * 2 - self.R * 3)
                r1 = self.R + self.W * (self.LaneNumber - 1) + self.W / 2
                r2 = self.R - self.W / 2
                for i in range(self.BoundaryNumber):
                    c1 = sy.Circle(center1, r1)
                    x, y = sy.symbols('x,y')
                    eq1 = c1.equation(x, y)
                    lanelst1 = []
                    for m in range(int(r1) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] + m, a[1])
                            lst.append(p1)
                            p2 = (point1[0] + m, a[0])
                            lst.append(p2)
                        else:
                            p = (point1[0] + m, a[0])
                            lst.append(p)
                        lanelst1[m:m] = lst
                    if len(lanelst1) % 2 == 0:
                        l = point1[0] + r1
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, l), y)]]
                        lanelst1[int(len(lanelst1) / 2):int(len(lanelst1) / 2)] = [(l, b[0])]
                    c2 = sy.Circle(center2, r2)
                    x, y = sy.symbols('x,y')
                    eq2 = c2.equation(x, y)
                    lanelst2 = []
                    for m in range(int(r2) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point1[0] - m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] - m, a[1])
                            lst.append(p1)
                            p2 = (point1[0] - m, a[0])
                            lst.append(p2)
                        else:
                            p = (point1[0] - m, a[0])
                            lst.append(p)
                        lanelst2[m:m] = lst
                    if len(lanelst2) % 2 == 0:
                        l = point1[0] - r2
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, l), y)]]
                        lanelst2[int(len(lanelst2) / 2):int(len(lanelst2) / 2)] = [(l, b[0])]
                    lanelst = lanelst1[:-1] + lanelst2
                    pointlist.append(lanelst)
                    r1 -= self.W
                    r2 += self.W
                pointlist = self.rotation(pointlist)

            elif self.Direction == 1:
                point1 = (self.Start[0], self.Start[1] + self.W / 2)
                center1 = (self.Start[0], self.Start[1] + self.R)
                center2 = (self.Start[0], self.Start[1] + self.W * (self.LaneNumber - 1) + self.R * 3)
                r1 = self.R - self.W / 2
                r2 = self.R + self.W * (self.LaneNumber - 1) + self.W / 2
                for i in range(self.BoundaryNumber):
                    c1 = sy.Circle(center1, r1)
                    x, y = sy.symbols('x,y')
                    eq1 = c1.equation(x, y)
                    lanelst1 = []
                    for m in range(int(r1) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point1[0] + m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] + m, a[0])
                            lst.append(p1)
                            p2 = (point1[0] + m, a[1])
                            lst.append(p2)
                        else:
                            p = (point1[0] + m, a[0])
                            lst.append(p)
                        lanelst1[m:m] = lst
                    if len(lanelst1) % 2 == 0:
                        l = point1[0] + r1
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, l), y)]]
                        lanelst1[int(len(lanelst1) / 2):int(len(lanelst1) / 2)] = [(l, b[0])]
                    c2 = sy.Circle(center2, r2)
                    x, y = sy.symbols('x,y')
                    eq2 = c2.equation(x, y)
                    lanelst2 = []
                    for m in range(int(r2) + 1):
                        a = [float(k) for k in
                             ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point1[0] - m), y)]]
                        a = sorted(a)
                        lst = []
                        if len(a) == 2:
                            p1 = (point1[0] - m, a[0])
                            lst.append(p1)
                            p2 = (point1[0] - m, a[1])
                            lst.append(p2)
                        else:
                            p = (point1[0] - m, a[0])
                            lst.append(p)
                        lanelst2[m:m] = lst
                    if len(lanelst2) % 2 == 0:
                        l = point1[0] - r2
                        b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, l), y)]]
                        lanelst2[int(len(lanelst2) / 2):int(len(lanelst2) / 2)] = [(l, b[0])]
                    lanelst = lanelst1[:-1] + lanelst2
                    pointlist.append(lanelst)
                    r1 += self.W
                    r2 -= self.W
                pointlist = self.rotation(pointlist)


        elif function == 'Bezier':
            if self.Direction == 0:
                pointS = (self.Start[0], self.Start[1] + self.W / 2)
                pointE = (pointS[0] + self.CurveSet[1], pointS[1] - self.CurveSet[0])
                lanelst = [pointS]
                lanelst = lanelst + [(i[0], i[1] + self.W / 2) for i in self.ControlPoint]
                lanelst.append(pointE)
                for i in range(self.BoundaryNumber):
                    lst = self.bezier(lanelst)
                    pointlist.append(lst)
                    lanelst = [(i[0], i[1] - self.W) for i in lanelst]
                pointlist = self.rotation(pointlist)

            elif self.Direction == 1:
                pointS = (self.Start[0], self.Start[1] + self.W / 2)
                pointE = (pointS[0] + self.CurveSet[1], pointS[1] + self.CurveSet[0])
                lanelst = [pointS]
                lanelst = lanelst + [(i[0], i[1] + self.W / 2) for i in self.ControlPoint]
                lanelst.append(pointE)
                for i in range(self.BoundaryNumber):
                    lst = self.bezier(lanelst)
                    pointlist.append(lst)
                    lanelst = [(i[0], i[1] - self.W) for i in lanelst]
                pointlist = self.rotation(pointlist)

            elif self.Direction == 2:
                pointS = (self.Start[0], self.Start[1] + self.W / 2)
                pointE = (pointS[0] + self.CurveSet[1], pointS[1])
                lanelst = [pointS]
                lanelst = lanelst + [(i[0], i[1] + self.W / 2) for i in self.ControlPoint]
                lanelst.append(pointE)
                for i in range(self.BoundaryNumber):
                    lst = self.bezier(lanelst)
                    pointlist.append(lst)
                    lanelst = [(i[0], i[1] - self.W) for i in lanelst]
                pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线双行道':
            pointlist = pointlist
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            pointlist[0].reverse()
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            pointlist[0].reverse()
        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()

        return pointlist

    def PointtoString(self, lst):
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def generate_road(self, f):
        Widget.LaneID += self.LaneNumber
        Widget.BoundaryID += self.BoundaryNumber
        Widget.WidgetID += 1

        flag = self.Flag
        # lane
        lanes = str(self.StartLaneID) + ':' + str(self.StartLaneID + self.LaneNumber - 1)  # 当前组件涉及到的lane
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a Curve widget')
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
            self.StartBoundaryID + self.BoundaryNumber - 1) 
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
        k = 0  

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线线双行道':
            for i in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
                printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k] + '",Alignment="Forward");')
                printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k + 1] + '",Alignment="Forward");')
                k = k + 1
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
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

        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
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

        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
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

        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
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
