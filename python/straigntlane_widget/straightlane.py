

from func.printAuto import printAutoInd
from func.widget import Widget
import math


class StraightLane(Widget):
    WidgetID = 1
    Start = (0, 0)  
    LW = (10, 3.5)  
    StartLaneID = 1  
    LaneNumber = 1  
    BoundaryNumber = 1
    LaneAssetType = {}  
    k = '+0'  
    LaneType = 'Driving'  
    Flag = '' 

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.LW = dict1.get('LW')
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.LaneNumber = dict1.get('LaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        self.LaneAssetType = Widget.get_self_LaneAssetType(dict1.get('LaneAssetType'))
        self.k = dict1.get('K')
        self.Flag = dict1.get('Flag')
        self.Type = dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        CurrentFlag = self.Flag
        Currents_info["CurrentLanes"] = []  
        Currents_info["Flag"] = CurrentFlag  
        if self.BoundaryNumber == 2:  
            Currents_info["CurrentLanes"].append(self.StartLaneID)
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 3:  
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1])
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 4:  
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self
                                                 .StartLaneID + 2])
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 5: 
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self
                                                 .StartLaneID + 2, self.StartLaneID + 3])
            Currents_info["Type"] = self.Flag
        if self.BoundaryNumber == 7: 
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1, self
                                                 .StartLaneID + 2, self.StartLaneID + 3, self.StartLaneID + 4,
                                                  self.StartLaneID + 5])
            Currents_info["Type"] = self.Flag
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        endpoint = (self.Start[0] + self.LW[0], self.Start[1])
        Next = dict()
        Next['direction'] = self.k
        Next['endpoint'] = self.roate_endpoints(endpoint)
        Next['type'] = self.Flag
        Next['lanes'] = list(range(self.StartLaneID, self.StartLaneID + self.LaneNumber))
        Next['current'] = self.Flag + '_' + self.Type
        Next['ID'] = self.WidgetID
        Nexts.append(Next)
        return Nexts
    
    def get_coveredArea(self):
        result=[]
        point1=(self.Start[0],self.Start[1]-self.LW[1]*(self.LaneNumber-1)-self.LW[1]/2)
        point2=(self.Start[0]+self.LW[0],self.Start[1]-self.LW[1]*(self.LaneNumber-1)-self.LW[1]/2)
        point3=(self.Start[0]+self.LW[0],self.Start[1]+self.LW[1]/2)
        point4=(self.Start[0],self.Start[1]+self.LW[1]/2)
        result.append(point1)
        result.append(point2)
        result.append(point3)
        result.append(point4)

        tmp=[result]
        finalResult=self.rotation(tmp)
        return (finalResult)

    
    def roate_endpoints(self,point):
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

    def getlanepoint(self):
        pointlist = []
        flag = self.Flag

        point1 = self.Start
        point2 = (self.Start[0] + self.LW[0] / 2, self.Start[1])
        point3 = (self.Start[0] + self.LW[0], self.Start[1])
        lane1 = [point1, point2, point3]
        pointlist.append(lane1)
        for i in range(self.LaneNumber - 1):
            point1 = (point1[0], point1[1] - self.LW[1])
            point2 = (point2[0], point2[1] - self.LW[1])
            point3 = (point3[0], point3[1] - self.LW[1])
            lane = [point1, point2, point3]
            pointlist.append(lane)
        pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向虚线双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道' or flag == '单向实线线双行道':
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
        pointlist = []
        flag = self.Flag

        point1 = (self.Start[0], self.Start[1] + self.LW[1] / 2)
        point2 = (self.Start[0] + self.LW[0] / 2, self.Start[1] + self.LW[1] / 2)
        point3 = (self.Start[0] + self.LW[0], self.Start[1] + self.LW[1] / 2)
        lane1 = [point1, point2, point3]
        pointlist.append(lane1)
        for i in range(self.LaneNumber):  
            point1 = (point1[0], point1[1] - self.LW[1])
            point2 = (point2[0], point2[1] - self.LW[1])
            point3 = (point3[0], point3[1] - self.LW[1])
            lane = [point1, point2, point3]
            pointlist.append(lane)

        pointlist = self.rotation(pointlist)

        if flag == '单行道' or flag == '单向双行道' or flag == '单向虚实线双行道' or flag == '单向双实线双行道':
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
        lanes = str(self.StartLaneID) + ':' + str(self.StartLaneID + self.LaneNumber - 1)  
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a StraightRoad widget.')
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
        boundaries = str(self.StartBoundaryID) + ':' + str(self.StartBoundaryID + self.LaneNumber)  # 直线道路组件车道边界数=车道数+1
        printAutoInd(f, '% Set the lane boundaries.')
        for boundary in range(self.StartBoundaryID, self.StartBoundaryID + self.LaneNumber + 1):
            printAutoInd(f, 'rrMap.LaneBoundaries(' + str(boundary) + ') = roadrunner.hdmap.LaneBoundary();')
        laneboundaryidlist = []
        for i in range(self.StartBoundaryID, self.StartBoundaryID + self.LaneNumber + 1):
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

        printAutoInd(f, '% End of this widget')
