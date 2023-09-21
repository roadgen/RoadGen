from func.printAuto import printAutoInd
from func.widget import Widget
import sympy as sy
import math


class ULane(Widget):
    WidgetID = 1
    Start = (0, 0)  #  point
    LW = (20, 3.5)  # (length，width)
    DX = (10, 5)  # d:distance of two straight road，x:straight to circle。
    StartLaneID = 1  # start lane id
    StartBoundaryID = 1  # start boundary id
    LaneNumber = 1  
    BoundaryNumber = 1
    LaneAssetType = {}  
    k = '+0'  
    LaneType = 'Driving' 
    Diretction = 0  
    Flag = '' 

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.LW = dict1.get('LW')
        self.DX = dict1.get('DX')
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.LaneNumber = dict1.get('LaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        self.LaneAssetType = Widget.get_self_LaneAssetType(dict1.get('LaneAssetType'))
        self.k = dict1.get('K')
        self.Direction = dict1.get('Direction')
        self.Flag = dict1.get('Flag')
        self.Type = dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag
        Currents_info["CurrentLanes"] = []
        if self.LaneNumber == 3:  
            Currents_info["CurrentLanes"].extend([self.StartLaneID])
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 6:  
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1])
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 9:  
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self.StartLaneID + 2])
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 12:  
            Currents_info["CurrentLanes"].extend(
                [self.StartLaneID, self.StartLaneID + 1, self.StartLaneID + 2, self.StartLaneID + 3])
            Currents_info["Type"] = self.Flag
        if self.LaneNumber == 18:  
            Currents_info["CurrentLanes"].extend(
                [self.StartLaneID, self.StartLaneID + 1, self.StartLaneID + 2, self.StartLaneID + 3,
                 self.StartLaneID + 4, self.StartLaneID + 5])
            Currents_info["Type"] = self.Flag
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        if self.Direction == 0:
            endpoint = (self.Start[0],
                        self.Start[1] - (int(self.LaneNumber / 3) - 1) * 2 * self.LW[1] - self.DX[0])
        elif self.Direction == 1:
            endpoint = (self.Start[0],
                        self.Start[1] + self.DX[0])
        Next = dict()
        if self.k == '+0':
            Next['direction'] = '-0'
        elif self.k == '-0':
            Next['direction'] = '+0'
        elif self.k == '+':
            Next['direction'] = '-'
        elif self.k == '-':
            Next['direction'] = '+'

        Next['endpoint'] = self.roate_endpoints(endpoint)
        Next['type'] = self.Flag
        Next['lanes'] = list(range(self.StartLaneID + int(self.LaneNumber / 3),
                                   self.StartLaneID + int(self.LaneNumber / 3 * 2)))
        Next['current'] = self.Flag + '_' + self.Type
        Next['ID'] = self.WidgetID
        Nexts.append(Next)
        return Nexts

    def roate_endpoints(self, point):
        if self.k == '+0':
            return point
        if self.k == '-':  # rotate 90 degrees clockwise around the start.
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi / 2)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi / 2)) + self.Start[1]))
            return x, y
        if self.k == '-0':  # rotate 180 degrees clockwise around the start.
            x = float(
                '{:.3f}'.format((point[0] - self.Start[0]) * int(math.cos(math.pi)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi)) + self.Start[0]))
            y = float(
                '{:.3f}'.format((point[1] - self.Start[1]) * int(math.cos(math.pi)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi)) + self.Start[1]))
            return x, y
        if self.k == '+':  # rotate 270 degrees clockwise around the start.
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
        if self.k == '-':  # rotate 90 degrees clockwise around the start.
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
        if self.k == '-0':  # rotate 180 degrees clockwise around the start.
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
        if self.k == '+':  # rotate 270 degrees clockwise around the start.
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

    #return [[]]
    def get_coveredArea(self):
        result = []

        L = self.LW[0]
        W = self.LW[1]
        D = self.DX[0]
        X = self.DX[1]

        totalW = W
        if '单行道' in self.Flag:
            totalW = W
        if '双行道' in self.Flag:
            totalW = W * 2
        if '三行道' in self.Flag:
            totalW = 3 * W
        if '四车道' in self.Flag:
            totalW = 4 * W
        if '六车道' in self.Flag:
            totalW = 6 * W

        if self.Direction == 0:
            st1 = []
            st1_x1 = self.Start[0]
            st1_y1 = self.Start[1] + W / 2
            st1_x2 = st1_x1 + L
            st1_y2 = st1_y1 - totalW
            st1.append((st1_x1, st1_y1))
            st1.append((st1_x1, st1_y2))
            st1.append((st1_x2, st1_y2))
            st1.append((st1_x2, st1_y1))
            result.append(st1)

            st2 = []
            st2_x1 = st1_x1
            st2_x2 = st2_x1 + L
            st2_y1 = st1_y1 - totalW - D + W
            st2_y2 = st2_y1 - totalW
            st2.append((st2_x1, st2_y1))
            st2.append((st2_x1, st2_y2))
            st2.append((st2_x2, st2_y2))
            st2.append((st2_x2, st2_y1))
            result.append(st2)
            cle = []
            R = X / 2 + D * D / (8 * X)
            cle_x1 = st2_x2
            cle_x2 = cle_x1 + X - W / 2 + totalW
            cle_y1 = (st1_y1 + st2_y2) / 2 - R + W / 2 - totalW
            cle_y2 = (st1_y1 + st2_y2) / 2 + R - W / 2 + totalW
            cle.append((cle_x1, cle_y1))
            cle.append((cle_x1, cle_y2))
            cle.append((cle_x2, cle_y2))
            cle.append((cle_x2, cle_y1))
            result.append(cle)

        if self.Direction == 1:
            st1 = []
            st1_x1 = self.Start[0]
            st1_x2 = st1_x1 + L
            st1_y1 = self.Start[1] + W / 2
            st1_y2 = st1_y1 - totalW
            st1.append((st1_x1, st1_y1))
            st1.append((st1_x1, st1_y2))
            st1.append((st1_x2, st1_y2))
            st1.append((st1_x2, st1_y1))
            result.append(st1)

            st2 = []
            st2_x1 = st1_x1
            st2_x2 = st2_x1 + L
            st2_y1 = st1_y1 + D -W
            st2_y2 = st2_y1 + totalW
            st2.append((st2_x1,st2_y1))
            st2.append((st2_x2, st2_y1))
            st2.append((st2_x2, st2_y2))
            st2.append((st2_x1, st2_y2))
            result.append(st2)

            cle = []
            R = X / 2 + D * D / (8 * X)
            cle_x1 = st2_x2
            cle_x2 = cle_x1 + X - W/2 +totalW
            cle_y1 = (st1_y2 + st2_y2) /2 -R -totalW + W/2
            cle_y2 = (st1_y2 + st2_y2) /2 +R +totalW - W/2
            cle.append((cle_x1,cle_y1))
            cle.append((cle_x2,cle_y1))
            cle.append((cle_x2, cle_y2))
            cle.append((cle_x1, cle_y2))
            result.append(cle)

        finalresult = self.rotation(result)
        return finalresult


    def getlanepoint(self):
        flag = self.Flag
        pointlist = []
        # part1
        point1 = self.Start
        point2 = (self.Start[0] + self.LW[0] / 2, self.Start[1])
        point3 = (self.Start[0] + self.LW[0], self.Start[1])
        lane1 = [point1, point2, point3]
        pointlist.append(lane1)
        for i in range(int(self.LaneNumber / 3) - 1):
            point1 = (point1[0], point1[1] - self.LW[1])
            point2 = (point2[0], point2[1] - self.LW[1])
            point3 = (point3[0], point3[1] - self.LW[1])
            lane = [point1, point2, point3]
            pointlist.append(lane)
        # part2
        if self.Direction == 0:
            point1 = (self.Start[0] + self.LW[0],
                      self.Start[1] - (int(self.LaneNumber / 3) - 1) * 2 * self.LW[1] - self.DX[0])
            point2 = (self.Start[0] + self.LW[0] / 2,
                      self.Start[1] - (int(self.LaneNumber / 3) - 1) * 2 * self.LW[1] - self.DX[0])
            point3 = (self.Start[0],
                      self.Start[1] - (int(self.LaneNumber / 3) - 1) * 2 * self.LW[1] - self.DX[0])
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            for i in range(int(self.LaneNumber / 3) - 1):
                point1 = (point1[0], point1[1] + self.LW[1])
                point2 = (point2[0], point2[1] + self.LW[1])
                point3 = (point3[0], point3[1] + self.LW[1])
                lane = [point1, point2, point3]
                pointlist.append(lane)
            # part3
            i = 0
            k = int(self.LaneNumber / 3) - 1
            while (i < int(self.LaneNumber / 3) and k >= 0):
                j = i + int(self.LaneNumber / 3)
                point1 = pointlist[i][2]
                point2 = pointlist[j][0]
                point3 = (point1[0] + self.DX[1] + k * self.LW[1], (point1[1] + point2[1]) / 2)
                c = sy.Circle(sy.Point(point1), sy.Point(point2), sy.Point(point3))
                x, y = sy.symbols('x,y')
                eq = c.equation(x, y)
                lanelst = []
                for m in range(self.DX[1] + 1 + int((self.LaneNumber / 3 - 1 - i) * self.LW[1])):
                    a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
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
                    lanelst[m:m] = lst

                if len(lanelst) % 2 == 0:
                    l = point1[0] + self.DX[1] + (self.LaneNumber / 3 - 1 - i) * self.LW[1]
                    b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, l), y)]]
                    lanelst[int(len(lanelst) / 2):int(len(lanelst) / 2)] = [(l, b[0])]
                i += 1
                k -= 1
                pointlist.append(lanelst)
        else:
            point1 = (self.Start[0] + self.LW[0],
                      self.Start[1] + self.DX[0])
            point2 = (self.Start[0] + self.LW[0] / 2,
                      self.Start[1] + self.DX[0])
            point3 = (self.Start[0],
                      self.Start[1] + self.DX[0])
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            for i in range(int(self.LaneNumber / 3) - 1):
                point1 = (point1[0], point1[1] + self.LW[1])
                point2 = (point2[0], point2[1] + self.LW[1])
                point3 = (point3[0], point3[1] + self.LW[1])
                lane = [point1, point2, point3]
                pointlist.append(lane)
            # part3
            i = 0
            while (i < int(self.LaneNumber / 3)):
                j = i + int(self.LaneNumber / 3)
                point1 = pointlist[i][2]
                point2 = pointlist[j][0]
                point3 = (point1[0] + self.DX[1] + i * self.LW[1], (point1[1] + point2[1]) / 2)
                c = sy.Circle(sy.Point(point1), sy.Point(point2), sy.Point(point3))
                x, y = sy.symbols('x,y')
                eq = c.equation(x, y)
                lanelst = []
                for m in range(int(self.DX[1] + 1 + i * self.LW[1])):
                    a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
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
                    lanelst[m:m] = lst

                if len(lanelst) % 2 == 0:
                    l = point1[0] + self.DX[1] + i * self.LW[1]
                    b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, l), y)]]
                    lanelst[int(len(lanelst) / 2):int(len(lanelst) / 2)] = [(l, b[0])]
                i += 1
                pointlist.append(lanelst)

        pointlist = self.rotation(pointlist)
        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线双行道':
            pointlist = pointlist
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            pointlist[0].reverse()
            pointlist[2].reverse()
            pointlist[4].reverse()
        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[6].reverse()
        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            pointlist[12].reverse()
            pointlist[13].reverse()
            pointlist[14].reverse()

        return pointlist

    def getboundarypoint(self):
        pointlist = []
        flag = self.Flag
        # part1
        point1 = (self.Start[0], self.Start[1] + self.LW[1] / 2)
        point2 = (self.Start[0] + self.LW[0] / 2, self.Start[1] + self.LW[1] / 2)
        point3 = (self.Start[0] + self.LW[0], self.Start[1] + self.LW[1] / 2)
        lane1 = [point1, point2, point3]
        pointlist.append(lane1)
        for i in range(int(self.BoundaryNumber / 3) - 1):  
            point1 = (point1[0], point1[1] - self.LW[1])
            point2 = (point2[0], point2[1] - self.LW[1])
            point3 = (point3[0], point3[1] - self.LW[1])
            lane = [point1, point2, point3]
            pointlist.append(lane)

        # part2
        if self.Direction == 0:
            point1 = (self.Start[0] + self.LW[0],
                      self.Start[1] + self.LW[1] / 2 - ((int(self.BoundaryNumber / 3) - 1) * 2 - 1) * self.LW[1] -
                      self.DX[0])
            point2 = (self.Start[0] + self.LW[0] / 2,
                      self.Start[1] + self.LW[1] / 2 - ((int(self.BoundaryNumber / 3) - 1) * 2 - 1) * self.LW[1] -
                      self.DX[0])
            point3 = (self.Start[0],
                      self.Start[1] + self.LW[1] / 2 - ((int(self.BoundaryNumber / 3) - 1) * 2 - 1) * self.LW[1] -
                      self.DX[0])
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            for i in range(int(self.BoundaryNumber / 3) - 1):
                point1 = (point1[0], point1[1] + self.LW[1])
                point2 = (point2[0], point2[1] + self.LW[1])
                point3 = (point3[0], point3[1] + self.LW[1])
                lane = [point1, point2, point3]
                pointlist.append(lane)
            # part3
            i = 0
            k = int(self.BoundaryNumber / 3) - 1
            while (i < int(self.BoundaryNumber / 3) and k >= 0):
                j = i + int(self.BoundaryNumber / 3)
                point1 = pointlist[i][2]
                point2 = pointlist[j][0]
                point3 = (point1[0] + self.DX[1] + k * self.LW[1] - self.LW[1] / 2, (point1[1] + point2[1]) / 2)
                c = sy.Circle(sy.Point(point1), sy.Point(point2), sy.Point(point3))
                x, y = sy.symbols('x,y')
                eq = c.equation(x, y)
                lanelst = []
                for m in range(int(self.DX[1] + 1 + (self.BoundaryNumber / 3 - 1 - i) * self.LW[1] - self.LW[1] / 2)):
                    a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
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
                    lanelst[m:m] = lst

                if len(lanelst) % 2 == 0:
                    l = point1[0] + self.DX[1] + (self.BoundaryNumber / 3 - 1 - i) * self.LW[1] - self.LW[1] / 2
                    b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, l), y)]]
                    lanelst[int(len(lanelst) / 2):int(len(lanelst) / 2)] = [(l, b[0])]
                i += 1
                k -= 1
                pointlist.append(lanelst)
        else:
            point1 = (self.Start[0] + self.LW[0],
                      self.Start[1] - self.LW[1] / 2 + self.DX[0])
            point2 = (self.Start[0] + self.LW[0] / 2,
                      self.Start[1] - self.LW[1] / 2 + self.DX[0])
            point3 = (self.Start[0],
                      self.Start[1] - self.LW[1] / 2 + self.DX[0])
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            for i in range(int(self.BoundaryNumber / 3) - 1):
                point1 = (point1[0], point1[1] + self.LW[1])
                point2 = (point2[0], point2[1] + self.LW[1])
                point3 = (point3[0], point3[1] + self.LW[1])
                lane = [point1, point2, point3]
                pointlist.append(lane)
            # part3
            i = 0
            k = 0
            while (i < int(self.BoundaryNumber / 3)):
                j = i + int(self.BoundaryNumber / 3)
                point1 = pointlist[i][2]
                point2 = pointlist[j][0]
                point3 = (point1[0] + self.DX[1] + k * self.LW[1] - self.LW[1] / 2, (point1[1] + point2[1]) / 2)
                c = sy.Circle(sy.Point(point1), sy.Point(point2), sy.Point(point3))
                x, y = sy.symbols('x,y')
                eq = c.equation(x, y)
                lanelst = []
                for m in range(int(self.DX[1] + 1 + i * self.LW[1] - self.LW[1] / 2)):
                    a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point1[0] + m), y)]]
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
                    lanelst[m:m] = lst
                if len(lanelst) % 2 == 0:
                    l = point1[0] + self.DX[1] + i * self.LW[1] - self.LW[1] / 2
                    b = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, l), y)]]
                    lanelst[int(len(lanelst) / 2):int(len(lanelst) / 2)] = [(l, b[0])]
                i += 1
                k += 1
                pointlist.append(lanelst)

        pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线双行道':
            pointlist = pointlist
        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[6].reverse()
        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            pointlist[0].reverse()
            pointlist[4].reverse()
            pointlist[8].reverse()
        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[10].reverse()
            pointlist[11].reverse()
        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[2].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
            pointlist[14].reverse()
            pointlist[15].reverse()
            pointlist[16].reverse()

        return pointlist

    def PointtoString(self, lst):
        # [[(-1.5, 0), (-1.5, 5.0), (-1.5, 10)], [(1.5, 0), (1.5, 5.0), (1.5, 10)]] 变成 [-1.5 0;-1.5 5.0;-1.5 10],[1.5 0;1.5 5.0;1.5 10]的字符串
        lst = [str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def generate_road(self, f):

        Widget.LaneID += self.LaneNumber
        Widget.BoundaryID += self.BoundaryNumber
        Widget.WidgetID += 1

        flag = self.Flag
        # lane
        lanes = str(self.StartLaneID) + ':' + str(self.StartLaneID + self.LaneNumber - 1)
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a ULane wid')
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
        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线双行道':
            k = 0 
            for i in range(self.StartLaneID, self.StartLaneID + int(self.LaneNumber / 3)):
                printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k] + '",Alignment="Forward");')
                printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k + 1] + '",Alignment="Forward");')
                k = k + 1
            k += 1
            for i in range(self.StartLaneID + int(self.LaneNumber / 3),
                           self.StartLaneID + int(self.LaneNumber / 3 * 2)):
                printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k] + '",Alignment="Forward");')
                printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(i) + '),"' + laneboundaryidlist[
                    k + 1] + '",Alignment="Forward");')
                k = k + 1
            k += 1
            for i in range(self.StartLaneID + int(self.LaneNumber / 3 * 2), self.StartLaneID + self.LaneNumber):
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
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
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
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
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
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 8) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')
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
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 11) + '),"Boundary' + str(
                self.StartBoundaryID + 13) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 11) + '),"Boundary' + str(
                self.StartBoundaryID + 14) + '",Alignment="Forward");')
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
                self.StartBoundaryID + 16) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 13) + '),"Boundary' + str(
                self.StartBoundaryID + 15) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 14) + '),"Boundary' + str(
                self.StartBoundaryID + 17) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 14) + '),"Boundary' + str(
                self.StartBoundaryID + 16) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 15) + '),"Boundary' + str(
                self.StartBoundaryID + 17) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 15) + '),"Boundary' + str(
                self.StartBoundaryID + 18) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 16) + '),"Boundary' + str(
                self.StartBoundaryID + 18) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 16) + '),"Boundary' + str(
                self.StartBoundaryID + 19) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 17) + '),"Boundary' + str(
                self.StartBoundaryID + 19) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 17) + '),"Boundary' + str(
                self.StartBoundaryID + 20) + '",Alignment="Forward");')

        printAutoInd(f, '% Combine lanes')

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线双行道':
            for i in range(self.StartLaneID, self.StartLaneID + int(self.LaneNumber / 3)):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')
            for i in range(self.StartLaneID + int(self.LaneNumber / 3),
                           self.StartLaneID + int(self.LaneNumber / 3 * 2)):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + int(self.LaneNumber / 3 * 2), self.StartLaneID + self.LaneNumber):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')

        elif flag == '双向虚线双行道' or flag == '双向实线双行道' or flag == '双向虚实线双行道' or flag == '双向双实线双行道':
            for i in range(self.StartLaneID, self.StartLaneID + 1):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')
            for i in range(self.StartLaneID + 1, self.StartLaneID + 2):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')

            for i in range(self.StartLaneID + 2, self.StartLaneID + 3):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 3, self.StartLaneID + 4):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')

            for i in range(self.StartLaneID + 4, self.StartLaneID + 5):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 5, self.StartLaneID + 6):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')

        elif flag == '一前行虚白线虚黄线三行道' or flag == '一前行实白线虚黄线三行道' or flag == '一前行虚白线实黄线三行道' or flag == '一前行实白线实黄线三行道':
            for i in range(self.StartLaneID, self.StartLaneID + 2):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')
            for i in range(self.StartLaneID + 2, self.StartLaneID + 3):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')

            for i in range(self.StartLaneID + 3, self.StartLaneID + 5):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 5, self.StartLaneID + 6):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')

            for i in range(self.StartLaneID + 6, self.StartLaneID + 8):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 8, self.StartLaneID + 9):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')

        elif flag == '二前行虚黄线虚白线三行道' or flag == '二前行虚黄线实白线三行道' or flag == '二前行实黄线虚白线三行道' or flag == '二前行实黄线实白线三行道':
            for i in range(self.StartLaneID, self.StartLaneID + 1):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')
            for i in range(self.StartLaneID + 1, self.StartLaneID + 3):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')

            for i in range(self.StartLaneID + 3, self.StartLaneID + 4):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 4, self.StartLaneID + 6):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')

            for i in range(self.StartLaneID + 6, self.StartLaneID + 7):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 7, self.StartLaneID + 9):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')

        elif flag == '双黄实线虚虚四车道' or flag == '双黄实线实实四车道' or flag == '双黄实线虚实四车道' or flag == '双黄实线实虚四车道':
            for i in range(self.StartLaneID, self.StartLaneID + 2):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')
            for i in range(self.StartLaneID + 2, self.StartLaneID + 4):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')

            for i in range(self.StartLaneID + 4, self.StartLaneID + 6):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 6, self.StartLaneID + 8):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')

            for i in range(self.StartLaneID + 8, self.StartLaneID + 10):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 10, self.StartLaneID + 12):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')

        elif flag == '双实线虚虚虚虚六车道' or flag == '双实线实实实实六车道' or flag == '双实线虚虚实实六车道':
            for i in range(self.StartLaneID, self.StartLaneID + 3):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')
            for i in range(self.StartLaneID + 3, self.StartLaneID + 6):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3 * 2)) + '"));')

            for i in range(self.StartLaneID + 6, self.StartLaneID + 9):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 9, self.StartLaneID + 12):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i + int(self.LaneNumber / 3)) + '"));')

            for i in range(self.StartLaneID + 12, self.StartLaneID + 15):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')
            for i in range(self.StartLaneID + 15, self.StartLaneID + 18):
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3 * 2)) + '"));')
                printAutoInd(f, 'rrMap.Lanes(' + str(
                    i) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                    i - int(self.LaneNumber / 3)) + '"));')

        printAutoInd(f, '% End of this widget')
