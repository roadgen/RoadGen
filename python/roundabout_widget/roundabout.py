from TJunction_widget.tJunction import tJunction
from curve_widget.curve import Curve
from func.printAuto import printAutoInd
from func.widget import Widget
import math

class Roundabout(Widget):
    WidgetID = 1
    ID = 1  # junction id
    Start = (0, 0)  
    Width = 3.5
    R=0
    StartLaneID = 1  
    StartBoundaryID = 1  
    LaneNumber = 1
    BoundaryNumber = 1
    k = '+0' 
    Flag = ''  

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.Width = dict1.get('Width')
        self.R = dict1.get('R')
        self.StartLaneID = Widget.LaneID
        self.k = dict1.get('K')
        self.Type =dict1.get('Type')
        self.Flag = dict1.get('Flag')

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag
        Currents_info["Type"] = '双向实线双行道'
        Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 2))
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        if self.Flag == "双车道环岛":
            Next1 = dict()
            Next1['current'] = self.Flag + '_' + self.Type
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.Width * 4 + self.Width / 2 + self.R,
                        self.Start[1] + self.Width * 4 + self.Width / 2 + self.R)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            Next1['type'] = '双向实线双行道'
            Next1['lanes'] = [self.StartLaneID + 5, self.StartLaneID + 4]
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
            Next2['current'] = self.Flag + '_' + self.Type
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0],
                        self.Start[1] + self.Width * 8 + self.R * 2)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            Next2['type'] = '双向实线双行道'
            Next2['lanes'] = [self.StartLaneID + 17, self.StartLaneID + 16]
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
            endpoint = (self.Start[0] - self.R - self.Width * 3 - self.Width / 2,
                        self.Start[1] + self.R + self.Width * 3 + self.Width / 2)
            Next3['endpoint'] = self.roate_endpoints(endpoint)
            Next3['type'] = '双向实线双行道'
            Next3['lanes'] = [self.StartLaneID + 29, self.StartLaneID + 28]
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

    def roate_endpoints(self,point):
        if self.k == '+':
            return point
        if self.k == '+0': 
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi / 2)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi / 2)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi / 2)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi / 2)) + self.Start[1]))
            return x, y
        if self.k == '-':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi)) + self.Start[1]))
            return x, y
        if self.k == '-0':  
            x = float('{:.3f}'.format(
                (point[0] - self.Start[0]) * int(math.cos(math.pi * 1.5)) + (point[1] - self.Start[1]) * int(
                    math.sin(math.pi * 1.5)) + self.Start[0]))
            y = float('{:.3f}'.format(
                (point[1] - self.Start[1]) * int(math.cos(math.pi * 1.5)) - (point[0] - self.Start[0]) * int(
                    math.sin(math.pi * 1.5)) + self.Start[1]))
            return x, y
    
    def get_coveredArea(self):
        result=[]
        result1=[]
        if self.k=="-":
            point1=(self.Start[0]-self.Width*4-self.Width/2-self.R,self.Start[1])
            point2=(point1[0],self.Start[1]-8*self.Width-2*self.R)
            point3=(self.Start[0]+3*self.Width+self.Width/2+self.R,point2[1])
            point4=(point3[0],self.Start[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif self.k=="+":
            point1=(self.Start[0]-3*self.Width-self.Width/2-self.R,self.Start[1])
            point2=(point1[0]+8*self.Width+2*self.R,self.Start[1])
            point3=(point2[0],self.Start[1]+8*self.Width+2*self.R)
            point4=(point1[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif self.k=="+0":
            point1=(self.Start[0],self.Start[1]+3*self.Width+self.Width/2+self.R)
            point2=(self.Start[0],point1[1]+8*self.Width+2*self.R)
            point3=(self.Start[0]+8*self.Width+2*self.R,point2[1])
            point4=(point3[0],point1[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif self.k=="-0":
            point1=(self.Start[0],self.Start[1]-3*self.Width-self.Width/2-self.R)
            point2=(self.Start[0],point1[1]+8*self.Width+2*self.R)
            point3=(self.Start[0]-8*self.Width-2*self.R,point2[1])
            point4=(point3[0],point1[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        return result

    
    def generate_road(self, f):
        Widget.WidgetID -= 7
        if self.k == "+":

            Jdict1 = {
                'ID': 1,
                'Start': self.Start,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction1 = tJunction(Jdict1)
            tJunction1.generate_road(f)


            end1 = (self.Start[0] + self.Width * 2 + self.Width / 4, self.Start[1] + self.Width * 2 + self.Width / 4)
            start2 = end1

            Curve1 = {'Start': start2,
                     'W': self.Width,
                     'R': self.R,
                     'StartLaneID': 1,
                     'StartBoundaryID': 1,
                     'LaneNumber': 2,
                     'BoundaryNumber': 3,
                     'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                     'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                     'Function': '1/4Circle',
                     'Direction': 1,
                     'K': '+0',
                     'Flag': '单向双行道', }

            curve1 = Curve(Curve1)
            curve1.generate_road(f)

            end2 = (start2[0] + self.R, start2[1] + self.R)
            start3 = (end2[0] + self.Width * 2 + self.Width / 4, end2[1] + self.Width / 4 + self.Width)

            Jdict2 = {
                'ID': 2,
                'Start': start3,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction2 = tJunction(Jdict2)
            tJunction2.generate_road(f)

            end3 = (end2[0], end2[1] + self.Width * 3 + self.Width / 2)
            start4 = end3

            Curve2 = {'Start': start4,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+',
                      'Flag': '单向双行道', }

            curve2 = Curve(Curve2)
            curve2.generate_road(f)

            end4 = (start4[0] - self.R, start4[1] + self.R)

            start5 = (end4[0] - self.Width / 4 - self.Width, end4[1] + self.Width * 2 + self.Width / 4)

            Jdict3 = {
                'ID': 2,
                'Start': start5,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction3 = tJunction(Jdict3)
            tJunction3.generate_road(f)

            end5 = (end4[0] - self.Width * 3 - self.Width / 2, end4[1])
            start6 = end5

            Curve3 = {'Start': start6,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-0',
                      'Flag': '单向双行道', }

            curve3 = Curve(Curve3)
            curve3.generate_road(f)

            end6 = (start6[0] - self.R, start6[1] - self.R)
            start7 = (end6[0] - self.Width * 2 - self.Width / 4, end6[1] - self.Width / 4 - self.Width)

            Jdict4 = {
                'ID': 2,
                'Start': start7,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction4 = tJunction(Jdict4)
            tJunction4.generate_road(f)

            end7 = (end6[0], end6[1] - self.Width * 3 - self.Width / 2)
            start8 = end7

            Curve4 = {'Start': start8,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-',
                      'Flag': '单向双行道', }

            curve4 = Curve(Curve4)
            curve4.generate_road(f)


            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 20) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 20) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 21) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 21) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 19) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 19) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 18) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 18) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 32) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 32) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 33) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 33) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 31) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 31) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 30) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 30) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 44) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 44) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 45) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 45) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 43) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 43) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 42) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 42) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')

        elif self.k == "+0":
            Jdict1 = {
                'ID': 1,
                'Start': self.Start,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction1 = tJunction(Jdict1)
            tJunction1.generate_road(f)

            end1 = (self.Start[0] + self.Width * 2 + self.Width / 4, self.Start[1] - self.Width * 2 - self.Width / 4)
            start2 = end1

            Curve1 = {'Start': start2,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-',
                      'Flag': '单向双行道', }

            curve1 = Curve(Curve1)
            curve1.generate_road(f)

            end2 = (start2[0] + self.R, start2[1] -  self.R)

            start3 = (end2[0] + self.Width / 4 + self.Width, end2[1] - self.Width * 2 - self.Width / 4)

            Jdict2 = {
                'ID': 2,
                'Start': start3,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction2 = tJunction(Jdict2)
            tJunction2.generate_road(f)

            end3 = (end2[0] + self.Width * 3 + self.Width / 2, end2[1])
            start4 = end3

            Curve2 = {'Start': start4,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+0',
                      'Flag': '单向双行道', }

            curve2 = Curve(Curve2)
            curve2.generate_road(f)

            end4 = (start4[0] + self.R, start4[1] + self.R)

            start5 = (end4[0] + self.Width * 2 + self.Width / 4, end4[1] + self.Width / 4 + self.Width)

            Jdict3 = {
                'ID': 2,
                'Start': start5,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction3 = tJunction(Jdict3)
            tJunction3.generate_road(f)

            end5 = (end4[0], end4[1] + self.Width * 3 + self.Width / 2)
            start6 = end5

            Curve3 = {'Start': start6,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+',
                      'Flag': '单向双行道', }

            curve3 = Curve(Curve3)
            curve3.generate_road(f)

            end6 = (start6[0] - self.R, start6[1] + self.R)

            start7 = (end6[0] - self.Width / 4 - self.Width, end6[1] + self.Width * 2 + self.Width / 4)

            Jdict4 = {
                'ID': 2,
                'Start': start7,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction4 = tJunction(Jdict4)
            tJunction4.generate_road(f)

            end7 = (end6[0] - self.Width * 3 - self.Width / 2, end6[1])
            start8 = end7

            Curve4 = {'Start': start8,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-0',
                      'Flag': '单向双行道', }

            curve4 = Curve(Curve4)
            curve4.generate_road(f)



            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 20) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 20) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 21) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 21) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 19) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 19) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 18) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 18) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 32) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 32) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 33) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 33) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 31) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 31) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 30) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 30) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 44) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 44) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 45) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 45) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 43) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 43) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 42) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 42) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')
        elif self.k == "-":

            Jdict1 = {
                'ID': 1,
                'Start': self.Start,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction1 = tJunction(Jdict1)
            tJunction1.generate_road(f)

            end1 = (self.Start[0] - self.Width * 2 - self.Width / 4, self.Start[1] - self.Width * 2 - self.Width / 4)
            start2 = end1

            Curve1 = {'Start': start2,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-0',
                      'Flag': '单向双行道', }

            curve1 = Curve(Curve1)
            curve1.generate_road(f)

            end2 = (start2[0] - self.R, start2[1] -  self.R)

            start3 = (end2[0] - self.Width * 2 - self.Width / 4, end2[1] - self.Width / 4 - self.Width)

            Jdict2 = {
                'ID': 2,
                'Start': start3,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction2 = tJunction(Jdict2)
            tJunction2.generate_road(f)

            end3 = (end2[0], end2[1] - self.Width * 3 - self.Width / 2)
            start4 = end3

            Curve2 = {'Start': start4,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-',
                      'Flag': '单向双行道', }

            curve2 = Curve(Curve2)
            curve2.generate_road(f)

            end4 = (start4[0] + self.R, start4[1] - self.R)

            start5 = (end4[0] + self.Width / 4 + self.Width, end4[1] - self.Width * 2 - self.Width / 4)

            Jdict3 = {
                'ID': 2,
                'Start': start5,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction3 = tJunction(Jdict3)
            tJunction3.generate_road(f)

            end5 = (end4[0] + self.Width * 3 + self.Width / 2, end4[1])
            start6 = end5

            Curve3 = {'Start': start6,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+0',
                      'Flag': '单向双行道', }

            curve3 = Curve(Curve3)
            curve3.generate_road(f)

            end6 = (start6[0] + self.R, start6[1] + self.R)

            start7 = (end6[0] + self.Width * 2 + self.Width / 4, end6[1] + self.Width / 4 + self.Width)

            Jdict4 = {
                'ID': 2,
                'Start': start7,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction4 = tJunction(Jdict4)
            tJunction4.generate_road(f)

            end7 = (end6[0], end6[1] + self.Width * 3 + self.Width / 2)
            start8 = end7

            Curve4 = {'Start': start8,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+',
                      'Flag': '单向双行道', }

            curve4 = Curve(Curve4)
            curve4.generate_road(f)



            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 20) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 20) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 21) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 21) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 19) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 19) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 18) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 18) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 32) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 32) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 33) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 33) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 31) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 31) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 30) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 30) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 44) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 44) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 45) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 45) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 43) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 43) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 42) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 42) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')
        elif self.k == "-0":

            Jdict1 = {
                'ID': 1,
                'Start': self.Start,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction1 = tJunction(Jdict1)
            tJunction1.generate_road(f)

            end1 = (self.Start[0] - self.Width * 2 - self.Width / 4, self.Start[1] + self.Width * 2 + self.Width / 4)
            start2 = end1

            Curve1 = {'Start': start2,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+',
                      'Flag': '单向双行道', }

            curve1 = Curve(Curve1)
            curve1.generate_road(f)

            end2 = (start2[0] - self.R, start2[1] + self.R)

            start3 = (end2[0] - self.Width / 4 - self.Width, end2[1] + self.Width * 2 + self.Width / 4)

            Jdict2 = {
                'ID': 2,
                'Start': start3,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '-',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction2 = tJunction(Jdict2)
            tJunction2.generate_road(f)

            end3 = (end2[0] - self.Width * 3 - self.Width / 2, end2[1])
            start4 = end3

            Curve2 = {'Start': start4,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-0',
                      'Flag': '单向双行道', }

            curve2 = Curve(Curve2)
            curve2.generate_road(f)

            end4 = (start4[0] - self.R, start4[1] - self.R)

            start5 = (end4[0] - self.Width * 2 - self.Width / 4, end4[1] - self.Width / 4 - self.Width)

            Jdict3 = {
                'ID': 2,
                'Start': start5,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+0',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction3 = tJunction(Jdict3)
            tJunction3.generate_road(f)

            end5 = (end4[0], end4[1] - self.Width * 3 - self.Width / 2)
            start6 = end5

            Curve3 = {'Start': start6,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '-',
                      'Flag': '单向双行道', }

            curve3 = Curve(Curve3)
            curve3.generate_road(f)

            end6 = (start6[0] + self.R, start6[1] - self.R)

            start7 = (end6[0] + self.Width / 4 + self.Width, end6[1] - self.Width * 2 - self.Width / 4)

            Jdict4 = {
                'ID': 2,
                'Start': start7,
                'Width': self.Width,
                'OuterLaneNumber': [2, 2, 2],
                'InnerLaneNumber': 4,
                'BoundaryNumber': 16,
                'K': '+',
                'Flag': '双向双车道转同向双车道'
            }
            tJunction4 = tJunction(Jdict4)
            tJunction4.generate_road(f)

            end7 = (end6[0] + self.Width * 3 + self.Width / 2, end6[1])
            start8 = end7

            Curve4 = {'Start': start8,
                      'W': self.Width,
                      'R': self.R,
                      'StartLaneID': 1,
                      'StartBoundaryID': 1,
                      'LaneNumber': 2,
                      'BoundaryNumber': 3,
                      'TravelDirection': {'Lane1': 'Forward', 'Lane2': 'Forward'},
                      'LaneAssetType': {'Boundary1': 'SW', 'Boundary2': 'DW', 'Boundary3': 'SW'},
                      'Function': '1/4Circle',
                      'Direction': 1,
                      'K': '+0',
                      'Flag': '单向双行道', }

            curve4 = Curve(Curve4)
            curve4.generate_road(f)



            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 10) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 20) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 20) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 10) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 11) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 21) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 21) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 11) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 19) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 19) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 18) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 18) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 22) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 32) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 32) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 22) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 23) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 33) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 33) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 23) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 31) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 31) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 30) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 30) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 34) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 44) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 44) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 34) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 35) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 45) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 45) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 35) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 43) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 43) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 42) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 42) + '"));')

            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 46) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 8) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 8) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 46) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 47) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 9) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 9) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 47) + '"));')


