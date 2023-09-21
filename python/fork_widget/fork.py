from func.printAuto import printAutoInd
from func.widget import Widget
import sympy as sy
import math


class Fork(Widget):
    WidgetID = 1
    Start = (0, 0)  
    W = 3.5  
    R = 5  # radius
    StartLaneID = 1 
    StartBoundaryID = 1  
    LaneNumber = 1  
    BoundaryNumber = 1
    
    LaneAssetType = {} 
    k = '+0'  
    LaneType = 'Driving'  
    Flag = ''  

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.Start = dict1.get('Start')
        self.W = dict1.get('W')
        self.R = dict1.get('R')
        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.LaneNumber = dict1.get('LaneNumber')
        self.BoundaryNumber = dict1.get('BoundaryNumber')
        # self.TravelDirection = Widget.get_self_TravelDirection(dict1.get('TravelDirection'))
        self.LaneAssetType = Widget.get_self_LaneAssetType(dict1.get('LaneAssetType'))
        self.k = dict1.get('K')
        self.Flag = dict1.get('Flag')
        self.Type = dict1.get('Type')

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag
        Currents_info["CurrentLanes"] = []
        SingleList = ['单车道右弯曲并入单向双车道', '单车道右弯曲并入双向双车道', '单车道右弯曲并入二前行三车道',
                      '单车道右弯曲并入一前行三车道', '单车道右弯曲并入四车道', '单车道左弯曲并入单向双车道']
        DoubleList1 = ['单向双车道右弯曲并入四车道', '单向双车道右弯曲岔路', '单向双车道右弯曲并入二前行三车道']

        DoubleList2 = ['双向双车道右弯曲并入一前行三车道', '双向双车道左弯曲并入二前行三车道', '双向双车道右弯曲岔路']
        TripleList1 = ['一前行三车道左弯曲并入四车道', '一前行三车道右弯曲岔路', '一前行三车道左右弯曲岔路']
        TripleList2 = ['二前行三车道右弯曲并入四车道', '二前行三车道一右弯曲岔路', '二前行三车道二右弯曲岔路',
                       '二前行三车道左右弯曲岔路']
        QuadrupleList = ['四车道一右弯曲岔路', '四车道二右弯曲岔路', '四车道左右弯曲岔路']
        if self.Flag in SingleList:  # 单车道，直接返回StartLaneID
            Currents_info["CurrentLanes"].extend([self.StartLaneID])
            Currents_info["Type"] = '单行道'
        if self.Flag == '单向双车道右弯曲并入二前行三车道' or self.Flag == '单向双车道右弯曲并入四车道':
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1])
            Currents_info["Type"] = '单向虚线双行道'
        if self.Flag == '双向双车道右弯曲并入一前行三车道' or self.Flag == '双向双车道左弯曲并入二前行三车道' or self.Flag == '双向双车道右弯曲岔路':
            Currents_info["CurrentLanes"].extend([self.StartLaneID, self.StartLaneID + 1])
            Currents_info["Type"] = '双向实线双行道'
        if self.Flag == '二前行三车道右弯曲并入四车道' or self.Flag == '二前行三车道一右弯曲岔路' or self.Flag == '二前行三车道二右弯曲岔路' or self.Flag == '二前行三车道左右弯曲岔路':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID,self.StartLaneID+3))
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
        if self.Flag == '一前行三车道左弯曲并入四车道' or self.Flag == '一前行三车道右弯曲岔路' or self.Flag == '一前行三车道左右弯曲岔路':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 3))
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
        if self.Flag == '单向双车道右弯曲岔路':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID,self.StartLaneID+2))
            Currents_info["Type"] = '单向实线双行道'
        if self.Flag == '四车道一右弯曲岔路' or self.Flag == '四车道二右弯曲岔路' or self.Flag == '四车道左右弯曲岔路':
            Currents_info["CurrentLanes"] = list(range(self.StartLaneID, self.StartLaneID + 4))
            Currents_info["Type"] = '双黄实线虚虚四车道'
        return Currents_info

    def get_Nexts(self):
        flag = self.Flag
        Nexts = []
        if flag == '单车道右弯曲并入单向双车道':
            Next = dict()
            endpoint = (self.Start[0] + self.R + self.W, self.Start[1] - self.R * 2)
            Next['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next['direction'] = '-'
            elif self.k == '-0':
                Next['direction'] = '+'
            elif self.k == '+':
                Next['direction'] = '+0'
            elif self.k == '-':
                Next['direction'] = '-0'
            Next['type'] = '单向虚线双行道'
            Next['lanes'] = list(range(self.StartLaneID + 1, self.StartLaneID + 3))[::-1]
            Next['current'] = self.Flag + '_fork'
            Next['ID'] = self.WidgetID
            Nexts.append(Next)
        elif flag == '单车道右弯曲并入双向双车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W, self.Start[1] - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '双向实线双行道'
            Next1['lanes'] = list(range(self.StartLaneID + 1, self.StartLaneID + 3))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W, self.Start[1] - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 4))
            Nexts.append(Next2)
        elif flag == '单车道右弯曲并入二前行三车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '二前行实黄线虚白线三行道'
            Next1['lanes'] = list(range(self.StartLaneID + 1, self.StartLaneID + 4))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W, self.Start[1] - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '双向实线双行道'
            Next2['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '单车道右弯曲并入一前行三车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '一前行虚白线实黄线三行道'
            Next1['lanes'] = list(range(self.StartLaneID + 1, self.StartLaneID + 4))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W, self.Start[1] - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '单向虚线双行道'
            Next2['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '单车道右弯曲并入四车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 3, self.Start[1] - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '双黄实线虚虚四车道'
            Next1['lanes'] = list(range(self.StartLaneID + 1, self.StartLaneID + 5))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W, self.Start[1] - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '二前行实黄线虚白线三行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 8))
            Nexts.append(Next2)
        elif flag == '单车道左弯曲并入单向双车道':
            Next = dict()
            Next['current'] = self.Flag + '_fork'
            Next['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R, self.Start[1] + self.R * 2)
            Next['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next['direction'] = '+'
            elif self.k == '-0':
                Next['direction'] = '-'
            elif self.k == '+':
                Next['direction'] = '-0'
            elif self.k == '-':
                Next['direction'] = '+0'
            Next['type'] = '单向虚线双行道'
            Next['lanes'] = list(range(self.StartLaneID + 1, self.StartLaneID + 3))
            Nexts.append(Next)
        elif flag == '单向双车道右弯曲并入二前行三车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.W - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '二前行实黄线虚白线三行道'
            Next1['lanes'] = list(range(self.StartLaneID + 2, self.StartLaneID + 5))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.W - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '双向双车道右弯曲并入一前行三车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.W - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '一前行虚白线实黄线三行道'
            Next1['lanes'] = list(range(self.StartLaneID + 2, self.StartLaneID + 5))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.W - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '单向双车道右弯曲并入四车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 3, self.Start[1] - self.W - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '双黄实线虚虚四车道'
            Next1['lanes'] = list(range(self.StartLaneID + 2, self.StartLaneID + 6))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 2, self.Start[1] - self.W - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '单向虚线双行道'
            Next2['lanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
            Nexts.append(Next2)
        elif flag == '双向双车道左弯曲并入二前行三车道':
            Next = dict()
            Next['current'] = self.Flag + '_fork'
            Next['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R, self.Start[1] + self.R * 2)
            Next['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next['direction'] = '+'
            elif self.k == '-0':
                Next['direction'] = '-'
            elif self.k == '+':
                Next['direction'] = '-0'
            elif self.k == '-':
                Next['direction'] = '+0'
            Next['type'] = '二前行实黄线虚白线三行道'
            Next['lanes'] = list(range(self.StartLaneID + 2, self.StartLaneID + 5))
            Nexts.append(Next)
        elif flag == '二前行三车道右弯曲并入四车道':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 3, self.Start[1] - self.W * 2 - self.R * 2)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '-'
            elif self.k == '-0':
                Next1['direction'] = '+'
            elif self.k == '+':
                Next1['direction'] = '+0'
            elif self.k == '-':
                Next1['direction'] = '-0'
            Next1['type'] = '双黄实线虚虚四车道'
            Next1['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 7))[::-1]
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R + self.W * 3, self.Start[1] - self.W * 2 - self.R + 30)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '+'
            elif self.k == '-0':
                Next2['direction'] = '-'
            elif self.k == '+':
                Next2['direction'] = '-0'
            elif self.k == '-':
                Next2['direction'] = '+0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 8))
            Nexts.append(Next2)
        elif flag == '一前行三车道左弯曲并入四车道':
            Next = dict()
            Next['current'] = self.Flag + '_fork'
            Next['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R, self.Start[1] + self.R * 2)
            Next['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next['direction'] = '+'
            elif self.k == '-0':
                Next['direction'] = '-'
            elif self.k == '+':
                Next['direction'] = '-0'
            elif self.k == '-':
                Next['direction'] = '+0'
            Next['type'] = '双黄实线虚虚四车道'
            Next['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 7))
            Nexts.append(Next)
        elif flag == '单向双车道右弯曲岔路':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1])
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '+0'
            elif self.k == '-0':
                Next1['direction'] = '-0'
            elif self.k == '+':
                Next1['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Next1['type'] = '单行道'
            Next1['lanes'] = list(range(self.StartLaneID + 2, self.StartLaneID + 3))
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 4))
            Nexts.append(Next2)
        elif flag == '双向双车道右弯曲岔路':
            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 4))
            Nexts.append(Next2)
        elif flag == '一前行三车道右弯曲岔路':
            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 2 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '二前行三车道一右弯曲岔路':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1])
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '+0'
            elif self.k == '-0':
                Next1['direction'] = '-0'
            elif self.k == '+':
                Next1['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Next1['type'] = '双向实线双行道'
            Next1['lanes'] = list(range(self.StartLaneID + 3, self.StartLaneID + 5))
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 2 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '二前行三车道二右弯曲岔路':
            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2 + self.W, self.Start[1] - self.W * 2 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单向虚线双行道'
            Next2['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '一前行三车道左右弯曲岔路':
            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 2 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 6))
            Nexts.append(Next2)
        elif flag == '二前行三车道左右弯曲岔路':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '+0'
            elif self.k == '-0':
                Next1['direction'] = '-0'
            elif self.k == '+':
                Next1['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Next1['type'] = '单行道'
            Next1['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 5))
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 2 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 6))
            Nexts.append(Next2)

        elif flag == '四车道一右弯曲岔路':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1])
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '+0'
            elif self.k == '-0':
                Next1['direction'] = '-0'
            elif self.k == '+':
                Next1['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Next1['type'] = '一前行虚白线实黄线三行道'
            Next1['lanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 7))
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 3 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 8))
            Nexts.append(Next2)
        elif flag == '四车道二右弯曲岔路':
            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 3 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单向虚线双行道'
            Next2['lanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
            Nexts.append(Next2)
        elif flag == '四车道左右弯曲岔路':
            Next1 = dict()
            Next1['current'] = self.Flag + '_fork'
            Next1['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W)
            Next1['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next1['direction'] = '+0'
            elif self.k == '-0':
                Next1['direction'] = '-0'
            elif self.k == '+':
                Next1['direction'] = '+'
            elif self.k == '-':
                Next1['direction'] = '-'
            Next1['type'] = '双向实线双行道'
            Next1['lanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 7))
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_fork'
            Next2['ID'] = self.WidgetID
            endpoint = (self.Start[0] + self.R * 2, self.Start[1] - self.W * 3 - self.R)
            Next2['endpoint'] = self.roate_endpoints(endpoint)
            if self.k == '+0':
                Next2['direction'] = '-'
            elif self.k == '-0':
                Next2['direction'] = '+'
            elif self.k == '+':
                Next2['direction'] = '+0'
            elif self.k == '-':
                Next2['direction'] = '-0'
            Next2['type'] = '单行道'
            Next2['lanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 8))
            Nexts.append(Next2)

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
        flag=self.Flag
        result=[]
        if flag == '单车道右弯曲并入单向双车道' or flag == '单车道右弯曲并入双向双车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.R*2)
            point2=(self.Start[0]+self.R+self.W/2+self.W,point1[1])
            point3=(point2[0],point2[1]+self.R+30)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '单车道右弯曲并入二前行三车道' or flag == '单车道右弯曲并入一前行三车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.R*2)
            point2=(self.Start[0]+self.R+self.W/2+self.W*2,point1[1])
            point3=(point2[0],point2[1]+self.R+30)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '单车道右弯曲并入四车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.R*2)
            point2=(self.Start[0]+self.R+self.W/2+self.W*3,point1[1])
            point3=(point2[0],point2[1]+self.R+30)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '单车道左弯曲并入单向双车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]+self.R*2)
            point2=(self.Start[0],point1[1]-self.R-30)
            point3=(self.Start[0]+self.R+self.W/2+self.W,point2[1])
            point4=(point3[0],point1[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '单向双车道右弯曲并入二前行三车道' or flag == '双向双车道右弯曲并入一前行三车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.R*2-self.W)
            point2=(self.Start[0]+self.R+self.W/2+self.W*2,point1[1])
            point3=(point2[0],point2[1]+self.R+30)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '单向双车道右弯曲并入四车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.R*2-self.W)
            point2=(self.Start[0]+self.R+self.W/2+self.W*3,point1[1])
            point3=(point2[0],point2[1]+self.R+30)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '双向双车道左弯曲并入二前行三车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]+self.R*2)
            point2=(self.Start[0],point1[1]-self.R-30)
            point3=(self.Start[0]+self.R+self.W/2+self.W*2,point2[1])
            point4=(point3[0],point1[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '二前行三车道右弯曲并入四车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.R*2-self.W*2)
            point2=(self.Start[0]+self.R+self.W/2+self.W*3,point1[1])
            point3=(point2[0],point2[1]+self.R+30)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '一前行三车道左弯曲并入四车道':
            result1=[]
            point1=(self.Start[0],self.Start[1]+self.R*2)
            point2=(self.Start[0],point1[1]-self.R-30)
            point3=(self.Start[0]+self.R+self.W/2+self.W*3,point2[1])
            point4=(point3[0],point1[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)
        elif flag == '单向双车道右弯曲岔路' or flag == '双向双车道右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2)
            point2=(self.Start[0]+self.R*2,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(self.Start[0],self.Start[1]-self.W-self.R)
            point6=(self.Start[0]+self.R*2+self.W/2,point5[1])
            point7=(point6[0],self.Start[1]-self.W/2)
            point8=(self.Start[0],point7[1])
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)
        elif flag == '一前行三车道右弯曲岔路' or flag == '二前行三车道一右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W)
            point2=(self.Start[0]+self.R*2,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(self.Start[0],self.Start[1]-self.W*2-self.R)
            point6=(self.Start[0]+self.R*2+self.W/2,point5[1])
            point7=(point6[0],self.Start[1]-self.W/2-self.W)
            point8=(self.Start[0],point7[1])
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)
        elif flag == '二前行三车道二右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2)
            point2=(self.Start[0]+self.R*2,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(self.Start[0],self.Start[1]-self.W*2-self.R)
            point6=(self.Start[0]+self.R*2+self.W/2+self.W,point5[1])
            point7=(point6[0],self.Start[1]-self.W/2)
            point8=(self.Start[0],point7[1])
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)
        elif flag == '一前行三车道左右弯曲岔路' or flag =='二前行三车道左右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2)
            point2=(self.Start[0]+self.R*2+self.W/2,point1[1])
            point3=(point2[0],self.Start[1]+self.R)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(point1[0],point1[1]-self.W)
            point6=(point1[0]+self.R*2,point5[1])
            point7=(point6[0],point1[1])
            point8=point1
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)

            result3=[]
            point9=(self.Start[0],point5[1]-self.W/2-self.R)
            point10=(point2[0],point9[1])
            point11=(point10[0],point5[1])
            point12=point5
            result3.append(point9)
            result3.append(point10)
            result3.append(point11)
            result3.append(point12)
            result.append(result3)
        elif flag == '四车道一右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W*2)
            point2=(self.Start[0]+self.R*2,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(self.Start[0],point1[1]-self.W/2-self.R)
            point6=(self.Start[0]+self.R*2+self.W/2,point5[1])
            point7=(point6[0],point1[1])
            point8=point1
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)
        elif flag == '四车道二右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2-self.W)
            point2=(self.Start[0]+self.R*2,point1[1])
            point3=(point2[0],self.Start[1]+self.W/2)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(self.Start[0],self.Start[1]-self.W*3-self.R)
            point6=(self.Start[0]+self.R*2+self.W/2+self.W,point5[1])
            point7=(point6[0],point1[1])
            point8=point1
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)
        elif flag == '四车道左右弯曲岔路':
            result1=[]
            point1=(self.Start[0],self.Start[1]-self.W/2)
            point2=(self.Start[0]+self.R*2+self.W/2,point1[1])
            point3=(point2[0],self.Start[1]+self.R)
            point4=(self.Start[0],point3[1])
            result1.append(point1)
            result1.append(point2)
            result1.append(point3)
            result1.append(point4)
            result.append(result1)

            result2=[]
            point5=(point1[0],point1[1]-self.W*2)
            point6=(point1[0]+self.R*2,point5[1])
            point7=(point6[0],point1[1])
            point8=point1
            result2.append(point5)
            result2.append(point6)
            result2.append(point7)
            result2.append(point8)
            result.append(result2)

            result3=[]
            point9=(self.Start[0],point5[1]-self.W/2-self.R)
            point10=(point2[0],point9[1])
            point11=(point10[0],point5[1])
            point12=point5
            result3.append(point9)
            result3.append(point10)
            result3.append(point11)
            result3.append(point12)
            result.append(result3)

        finalResult=self.rotation(result)
        return(finalResult)

    def getlanepoint(self):
        flag = self.Flag
        pointlist = []
        if flag == '单车道右弯曲并入单向双车道' or flag == '单车道右弯曲并入双向双车道':
            point = self.Start
            center = (point[0], point[1] - self.R)
            c = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq = c.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point[0] + m, a[1]))
                else:
                    lanelist.append((point[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + self.R), y)]]
            p = (point[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            point4 = (point1[0] + self.W, point1[1])
            point5 = (point1[0] + self.W, point1[1] - self.R / 2)
            point6 = (point1[0] + self.W, point1[1] - self.R)
            lane3 = [point4, point5, point6]
            pointlist.append(lane3)
            point7 = (point4[0], point4[1] + 15)
            point8 = (point4[0], point4[1] + 30)
            lane4 = [point8, point7, point4]
            pointlist.append(lane4)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单车道右弯曲并入二前行三车道' or flag == '单车道右弯曲并入一前行三车道':
            point = self.Start
            center = (point[0], point[1] - self.R)
            c = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq = c.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point[0] + m, a[1]))
                else:
                    lanelist.append((point[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + self.R), y)]]
            p = (point[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            point4 = (point1[0] + self.W, point1[1])
            point5 = (point1[0] + self.W, point1[1] - self.R / 2)
            point6 = (point1[0] + self.W, point1[1] - self.R)
            lane3 = [point4, point5, point6]
            pointlist.append(lane3)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point4[0] + self.W, point4[1] - self.R / 2)
            point9 = (point4[0] + self.W, point4[1] - self.R)
            lane4 = [point7, point8, point9]
            pointlist.append(lane4)
            point10 = (point4[0], point4[1] + 15)
            point11 = (point4[0], point4[1] + 30)
            lane5 = [point11, point10, point4]
            pointlist.append(lane5)
            point12 = (point7[0], point7[1] + 15)
            point13 = (point7[0], point7[1] + 30)
            lane6 = [point13, point12, point7]
            pointlist.append(lane6)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单车道右弯曲并入四车道':
            point = self.Start
            center = (point[0], point[1] - self.R)
            c = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq = c.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point[0] + m, a[1]))
                else:
                    lanelist.append((point[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + self.R), y)]]
            p = (point[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            point4 = (point1[0] + self.W, point1[1])
            point5 = (point1[0] + self.W, point1[1] - self.R / 2)
            point6 = (point1[0] + self.W, point1[1] - self.R)
            lane3 = [point4, point5, point6]
            pointlist.append(lane3)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point4[0] + self.W, point4[1] - self.R / 2)
            point9 = (point4[0] + self.W, point4[1] - self.R)
            lane4 = [point7, point8, point9]
            pointlist.append(lane4)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point7[0] + self.W, point7[1] - self.R / 2)
            point12 = (point7[0] + self.W, point7[1] - self.R)
            lane5 = [point10, point11, point12]
            pointlist.append(lane5)
            point13 = (point4[0], point4[1] + 15)
            point14 = (point4[0], point4[1] + 30)
            lane6 = [point14, point13, point4]
            pointlist.append(lane6)
            point15 = (point7[0], point7[1] + 15)
            point16 = (point7[0], point7[1] + 30)
            lane7 = [point16, point15, point7]
            pointlist.append(lane7)
            point17 = (point10[0], point10[1] + 15)
            point18 = (point10[0], point10[1] + 30)
            lane8 = [point18, point17, point10]
            pointlist.append(lane8)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单车道左弯曲并入单向双车道':
            point = self.Start
            center = (point[0], point[1] + self.R)
            c = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq = c.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point[0] + m, a[0]))
                else:
                    lanelist.append((point[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq.subs(x, point[0] + self.R), y)]]
            p = (point[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] + self.R / 2)
            point3 = (point1[0], point1[1] + self.R)
            lane2 = [point1, point2, point3]
            pointlist.append(lane2)
            point4 = (point1[0] + self.W, point1[1])
            point5 = (point1[0] + self.W, point1[1] + self.R / 2)
            point6 = (point1[0] + self.W, point1[1] + self.R)
            lane3 = [point4, point5, point6]
            pointlist.append(lane3)
            point7 = (point4[0], point4[1] - 15)
            point8 = (point4[0], point4[1] - 30)
            lane4 = [point8, point7, point4]
            pointlist.append(lane4)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单向双车道右弯曲并入二前行三车道' or flag == '双向双车道右弯曲并入一前行三车道':
            p1 = self.Start
            p2 = (self.Start[0], self.Start[1] - self.W)
            center = (self.Start[0], p2[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W), y)]]
            p = (p1[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R), y)]]
            p = (p2[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point7[0], point7[1] + 15)
            point11 = (point7[0], point7[1] + 30)
            lane6 = [point11, point10, point7]
            pointlist.append(lane6)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单向双车道右弯曲并入四车道':
            p1 = self.Start
            p2 = (self.Start[0], self.Start[1] - self.W)
            center = (self.Start[0], p2[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W), y)]]
            p = (p1[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R), y)]]
            p = (p2[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point10[0], point10[1] - self.R / 2)
            point12 = (point10[0], point10[1] - self.R)
            lane6 = [point10, point11, point12]
            pointlist.append(lane6)
            point13 = (point7[0], point7[1] + 15)
            point14 = (point7[0], point7[1] + 30)
            lane7 = [point14, point13, point7]
            pointlist.append(lane7)
            point15 = (point10[0], point10[1] + 15)
            point16 = (point10[0], point10[1] + 30)
            lane8 = [point16, point15, point10]
            pointlist.append(lane8)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '双向双车道左弯曲并入二前行三车道':
            p1 = self.Start
            p2 = (self.Start[0], self.Start[1] - self.W)
            center = (self.Start[0], p1[1] + self.R)
            c1 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[0]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R), y)]]
            p = (p1[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[0]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W), y)]]
            p = (p2[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] + self.R / 2)
            point3 = (point1[0], point1[1] + self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] + self.R / 2]
            point6 = [point4[0], point4[1] + self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] + self.R / 2)
            point9 = (point7[0], point7[1] + self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point7[0], point7[1] - 15)
            point11 = (point7[0], point7[1] - 30)
            lane6 = [point11, point10, point7]
            pointlist.append(lane6)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '二前行三车道右弯曲并入四车道':
            p1 = self.Start
            p2 = (self.Start[0], self.Start[1] - self.W)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W)
            center = (self.Start[0], p3[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W + self.W), y)]]
            p = (p1[0] + self.R + self.W + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W), y)]]
            p = (p2[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[1]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R), y)]]
            p = (p3[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane4 = [point1, point2, point3]
            pointlist.append(lane4)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane5 = [point4, point5, point6]
            pointlist.append(lane5)
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane6 = [point7, point8, point9]
            pointlist.append(lane6)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point10[0], point10[1] - self.R / 2)
            point12 = (point10[0], point10[1] - self.R)
            lane7 = [point10, point11, point12]
            pointlist.append(lane7)
            point13 = (point10[0], point10[1] + 15)
            point14 = (point10[0], point10[1] + 30)
            lane8 = [point14, point13, point10]
            pointlist.append(lane8)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '一前行三车道左弯曲并入四车道':
            p1 = self.Start
            p2 = (self.Start[0], self.Start[1] - self.W)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W)
            center = (self.Start[0], p1[1] + self.R)
            c1 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[0]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R), y)]]
            p = (p1[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[0]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W), y)]]
            p = (p2[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R + self.W + self.W)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R + self.W + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[0]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R + self.W + self.W), y)]]
            p = (p3[0] + self.R + self.W + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] + self.R / 2)
            point3 = (point1[0], point1[1] + self.R)
            lane4 = [point1, point2, point3]
            pointlist.append(lane4)
            point5 = [point4[0], point4[1] + self.R / 2]
            point6 = [point4[0], point4[1] + self.R]
            lane5 = [point4, point5, point6]
            pointlist.append(lane5)
            point8 = (point7[0], point7[1] + self.R / 2)
            point9 = (point7[0], point7[1] + self.R)
            lane6 = [point7, point8, point9]
            pointlist.append(lane6)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point10[0], point10[1] + self.R / 2)
            point12 = (point10[0], point10[1] + self.R)
            lane7 = [point10, point11, point12]
            pointlist.append(lane7)
            point13 = (point10[0], point10[1] - 15)
            point14 = (point10[0], point10[1] - 30)
            lane8 = [point14, point13, point10]
            pointlist.append(lane8)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单向双车道右弯曲岔路' or flag == '双向双车道右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point3[0] + self.R / 2, point3[1])
            point8 = (point3[0] + self.R, point3[1])
            lane3 = [point3, point7, point8]
            pointlist.append(lane3)
            center = (point6[0], point6[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[1]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + self.R), y)]]
            p = (point6[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '一前行三车道右弯曲岔路' or flag == '二前行三车道一右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + self.R / 2, point3[1])
            point11 = (point3[0] + self.R, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + self.R / 2, point6[1])
            point13 = (point6[0] + self.R, point6[1])
            lane5 = [point6, point12, point13]
            pointlist.append(lane5)
            center = (point9[0], point9[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + self.R), y)]]
            p = (point9[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '二前行三车道二右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + self.R / 2, point3[1])
            point11 = (point3[0] + self.R, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append((lane4))
            center = (point9[0], point9[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + self.R + self.W), y)]]
            p = (point9[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            c2 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + self.R), y)]]
            p = (point9[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '一前行三车道左右弯曲岔路' or flag == '二前行三车道左右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            center1 = (point3[0], point3[1] + self.R)
            c1 = sy.Circle(sy.Point(center1), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point3[0] + m, a[0]))
                else:
                    lanelist.append((point3[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point3[0] + self.R), y)]]
            p = (point3[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            point10 = (point6[0] + self.R / 2, point6[1])
            point11 = (point6[0] + self.R, point6[1])
            lane5 = [point6, point10, point11]
            pointlist.append(lane5)
            center2 = (point9[0], point9[1] - self.R)
            c2 = sy.Circle(sy.Point(center2), self.R)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + self.R), y)]]
            p = (point9[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '四车道一右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + self.R / 2, point3[1])
            point14 = (point3[0] + self.R, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + self.R / 2, point6[1])
            point16 = (point6[0] + self.R, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            point17 = (point9[0] + self.R / 2, point9[1])
            point18 = (point9[0] + self.R, point9[1])
            lane7 = [point9, point17, point18]
            pointlist.append(lane7)
            center = (point12[0], point12[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + self.R), y)]]
            p = (point12[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '四车道二右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + self.R / 2, point3[1])
            point14 = (point3[0] + self.R, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + self.R / 2, point6[1])
            point16 = (point6[0] + self.R, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            center = (point12[0], point12[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + self.R + self.W), y)]]
            p = (point12[0] + self.R + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            c2 = sy.Circle(sy.Point(center), self.R)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + self.R), y)]]
            p = (point12[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '四车道左右弯曲岔路':
            point1 = self.Start
            point2 = (self.Start[0] + self.R / 2, self.Start[1])
            point3 = (self.Start[0] + self.R, self.Start[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            center1 = (point3[0], point3[1] + self.R)
            c1 = sy.Circle(sy.Point(center1), self.R)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point3[0] + m, a[0]))
                else:
                    lanelist.append((point3[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point3[0] + self.R), y)]]
            p = (point3[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            point13 = (point6[0] + self.R / 2, point6[1])
            point14 = (point6[0] + self.R, point6[1])
            lane6 = [point6, point13, point14]
            pointlist.append(lane6)
            point15 = (point9[0] + self.R / 2, point9[1])
            point16 = (point9[0] + self.R, point9[1])
            lane7 = [point9, point15, point16]
            pointlist.append(lane7)
            center2 = (point12[0], point12[1] - self.R)
            c2 = sy.Circle(sy.Point(center2), self.R)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            lanelist = []
            for m in range(int(self.R) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + self.R), y)]]
            p = (point12[0] + self.R, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

    def getboundarypoint(self):
        flag = self.Flag
        pointlist = []
        if flag == '单车道右弯曲并入单向双车道' or flag == '单车道右弯曲并入双向双车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            center = (self.Start[0], self.Start[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W / 2), y)]]
            p = (p1[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R - self.W / 2), y)]]
            p = (p2[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point4[0], point4[1] + 15)
            point11 = (point4[0], point4[1] + 30)
            lane6 = [point11, point10, point4]
            pointlist.append(lane6)
            point12 = (point7[0], point7[1] + 15)
            point13 = (point7[0], point7[1] + 30)
            lane7 = [point13, point12, point7]
            pointlist.append(lane7)
            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单车道右弯曲并入二前行三车道' or flag == '单车道右弯曲并入一前行三车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            center = (self.Start[0], self.Start[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W / 2), y)]]
            p = (p1[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R - self.W / 2), y)]]
            p = (p2[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point7[0] + self.W, point7[1] - self.R / 2)
            point12 = (point7[0] + self.W, point7[1] - self.R)
            lane6 = [point10, point11, point12]
            pointlist.append(lane6)
            point13 = (point4[0], point4[1] + 15)
            point14 = (point4[0], point4[1] + 30)
            lane7 = [point14, point13, point4]
            pointlist.append(lane7)
            point15 = (point7[0], point7[1] + 15)
            point16 = (point7[0], point7[1] + 30)
            lane8 = [point16, point15, point7]
            pointlist.append(lane8)
            point17 = (point10[0], point10[1] + 15)
            point18 = (point10[0], point10[1] + 30)
            lane9 = [point18, point17, point10]
            pointlist.append(lane9)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单车道右弯曲并入四车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            center = (self.Start[0], self.Start[1] - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W / 2), y)]]
            p = (p1[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R - self.W / 2), y)]]
            p = (p2[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point7[0] + self.W, point7[1] - self.R / 2)
            point12 = (point7[0] + self.W, point7[1] - self.R)
            lane6 = [point10, point11, point12]
            pointlist.append(lane6)
            point13 = (point10[0] + self.W, point10[1])
            point14 = (point10[0] + self.W, point10[1] - self.R / 2)
            point15 = (point10[0] + self.W, point10[1] - self.R)
            lane7 = [point13, point14, point15]
            pointlist.append(lane7)
            point16 = (point4[0], point4[1] + 15)
            point17 = (point4[0], point4[1] + 30)
            lane8 = [point17, point16, point4]
            pointlist.append(lane8)
            point18 = (point7[0], point7[1] + 15)
            point19 = (point7[0], point7[1] + 30)
            lane9 = [point19, point18, point9]
            pointlist.append(lane9)
            point20 = (point10[0], point10[1] + 15)
            point21 = (point10[0], point10[1] + 30)
            lane10 = [point21, point20, point10]
            pointlist.append(lane10)
            point22 = (point13[0], point13[1] + 15)
            point23 = (point13[0], point13[1] + 30)
            lane11 = [point23, point22, point13]
            pointlist.append(lane11)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单车道左弯曲并入单向双车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            center = (self.Start[0], self.Start[1] + self.R)
            c1 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[0]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R - self.W / 2), y)]]
            p = (p1[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[0]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W / 2), y)]]
            p = (p2[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] + self.R / 2)
            point3 = (point1[0], point1[1] + self.R)
            lane3 = [point1, point2, point3]
            pointlist.append(lane3)
            point5 = [point4[0], point4[1] + self.R / 2]
            point6 = [point4[0], point4[1] + self.R]
            lane4 = [point4, point5, point6]
            pointlist.append(lane4)
            point7 = (point4[0] + self.W, point4[1])
            point8 = (point7[0], point7[1] + self.R / 2)
            point9 = (point7[0], point7[1] + self.R)
            lane5 = [point7, point8, point9]
            pointlist.append(lane5)
            point10 = (point4[0], point4[1] - 15)
            point11 = (point4[0], point4[1] - 30)
            lane6 = [point11, point10, point4]
            pointlist.append(lane6)
            point12 = (point7[0], point7[1] - 15)
            point13 = (point7[0], point7[1] - 30)
            lane7 = [point13, point12, point7]
            pointlist.append(lane7)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单向双车道右弯曲并入二前行三车道' or flag == '双向双车道右弯曲并入一前行三车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W / 2)
            center = (self.Start[0], self.Start[1] - self.R - self.W)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W / 2 + self.W), y)]]
            p = (p1[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W / 2), y)]]
            p = (p2[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[1]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R - self.W / 2), y)]]
            p = (p3[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane4 = [point1, point2, point3]
            pointlist.append(lane4)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane5 = [point4, point5, point6]
            pointlist.append(lane5)
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane6 = [point7, point8, point9]
            pointlist.append(lane6)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point7[0] + self.W, point7[1] - self.R / 2)
            point12 = (point7[0] + self.W, point7[1] - self.R)
            lane7 = [point10, point11, point12]
            pointlist.append(lane7)
            point13 = (point7[0], point7[1] + 15)
            point14 = (point7[0], point7[1] + 30)
            lane8 = [point14, point13, point7]
            pointlist.append(lane8)
            point15 = (point10[0], point10[1] + 15)
            point16 = (point10[0], point10[1] + 30)
            lane9 = [point16, point15, point10]
            pointlist.append(lane9)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单向双车道右弯曲并入四车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W / 2)
            center = (self.Start[0], self.Start[1] - self.R - self.W)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R + self.W / 2 + self.W), y)]]
            p = (p1[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W / 2), y)]]
            p = (p2[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[1]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R - self.W / 2), y)]]
            p = (p3[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane4 = [point1, point2, point3]
            pointlist.append(lane4)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane5 = [point4, point5, point6]
            pointlist.append(lane5)
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane6 = [point7, point8, point9]
            pointlist.append(lane6)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point7[0] + self.W, point7[1] - self.R / 2)
            point12 = (point7[0] + self.W, point7[1] - self.R)
            lane7 = [point10, point11, point12]
            pointlist.append(lane7)
            point13 = (point10[0] + self.W, point10[1])
            point14 = (point13[0], point13[1] - self.R / 2)
            point15 = (point13[0], point13[1] - self.R)
            lane8 = [point13, point14, point15]
            pointlist.append(lane8)
            point16 = (point7[0], point7[1] + 15)
            point17 = (point7[0], point7[1] + 30)
            lane9 = [point17, point16, point7]
            pointlist.append(lane9)
            point18 = (point10[0], point10[1] + 15)
            point19 = (point10[0], point10[1] + 30)
            lane10 = [point19, point18, point10]
            pointlist.append(lane10)
            point20 = (point13[0], point13[1] + 15)
            point21 = (point13[0], point13[1] + 30)
            lane11 = [point21, point20, point13]
            pointlist.append(lane11)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '双向双车道左弯曲并入二前行三车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W / 2)
            center = (self.Start[0], self.Start[1] + self.R)
            c1 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[0]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R - self.W / 2), y)]]
            p = (p1[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[0]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W / 2), y)]]
            p = (p2[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[0]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R + self.W / 2 + self.W), y)]]
            p = (p3[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] + self.R / 2)
            point3 = (point1[0], point1[1] + self.R)
            lane4 = [point1, point2, point3]
            pointlist.append(lane4)
            point5 = [point4[0], point4[1] + self.R / 2]
            point6 = [point4[0], point4[1] + self.R]
            lane5 = [point4, point5, point6]
            pointlist.append(lane5)
            point8 = (point7[0], point7[1] + self.R / 2)
            point9 = (point7[0], point7[1] + self.R)
            lane6 = [point7, point8, point9]
            pointlist.append(lane6)
            point10 = (point7[0] + self.W, point7[1])
            point11 = (point7[0] + self.W, point7[1] + self.R / 2)
            point12 = (point7[0] + self.W, point7[1] + self.R)
            lane7 = [point10, point11, point12]
            pointlist.append(lane7)
            point13 = (point7[0], point7[1] - 15)
            point14 = (point7[0], point7[1] - 30)
            lane8 = [point14, point13, point7]
            pointlist.append(lane8)
            point15 = (point10[0], point10[1] - 15)
            point16 = (point10[0], point10[1] - 30)
            lane9 = [point16, point15, point10]
            pointlist.append(lane9)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '二前行三车道右弯曲并入四车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W / 2)
            p4 = (self.Start[0], self.Start[1] - self.W - self.W / 2 - self.W)
            center = (self.Start[0], self.Start[1] - self.R - self.W - self.W)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2 + self.W + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[1]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in
                                    sy.solve(eq1.subs(x, p1[0] + self.R + self.W / 2 + self.W + self.W), y)]]
            p = (p1[0] + self.R + self.W / 2 + self.W + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point10 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[1]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W / 2 + self.W), y)]]
            p = (p2[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[1]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R + self.W / 2), y)]]
            p = (p3[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c4 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq4 = c4.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, p4[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[1]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, p4[0] + self.R - self.W / 2), y)]]
            p = (p4[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] - self.R / 2)
            point3 = (point1[0], point1[1] - self.R)
            lane5 = [point1, point2, point3]
            pointlist.append(lane5)
            point5 = [point4[0], point4[1] - self.R / 2]
            point6 = [point4[0], point4[1] - self.R]
            lane6 = [point4, point5, point6]
            pointlist.append(lane6)
            point8 = (point7[0], point7[1] - self.R / 2)
            point9 = (point7[0], point7[1] - self.R)
            lane7 = [point7, point8, point9]
            pointlist.append(lane7)
            point11 = (point10[0], point10[1] - self.R / 2)
            point12 = (point10[0], point10[1] - self.R)
            lane8 = [point10, point11, point12]
            pointlist.append(lane8)
            point13 = (point10[0] + self.W, point10[1])
            point14 = (point13[0], point13[1] - self.R / 2)
            point15 = (point13[0], point13[1] - self.R)
            lane9 = [point13, point14, point15]
            pointlist.append(lane9)
            point16 = (point10[0], point10[1] + 15)
            point17 = (point10[0], point10[1] + 30)
            lane10 = [point17, point16, point10]
            pointlist.append(lane10)
            point18 = (point13[0], point13[1] + 15)
            point19 = (point13[0], point13[1] + 30)
            lane11 = [point19, point18, point13]
            pointlist.append(lane11)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '一前行三车道左弯曲并入四车道':
            p1 = (self.Start[0], self.Start[1] + self.W / 2)
            p2 = (self.Start[0], self.Start[1] - self.W / 2)
            p3 = (self.Start[0], self.Start[1] - self.W - self.W / 2)
            p4 = (self.Start[0], self.Start[1] - self.W - self.W / 2 - self.W)
            center = (self.Start[0], self.Start[1] + self.R)
            c1 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p1[0] + m, a[0]))
                else:
                    lanelist.append((p1[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, p1[0] + self.R - self.W / 2), y)]]
            p = (p1[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point1 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p2[0] + m, a[0]))
                else:
                    lanelist.append((p2[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, p2[0] + self.R + self.W / 2), y)]]
            p = (p2[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point4 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[0]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, p3[0] + self.R + self.W / 2 + self.W), y)]]
            p = (p3[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point7 = (lanelist[-1])
            pointlist.append(lanelist)
            lanelist = []
            c4 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W + self.W)
            x, y = sy.symbols('x,y')
            eq4 = c4.equation(x, y)
            for m in range(int(self.R + self.W / 2 + self.W + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, p4[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((p3[0] + m, a[0]))
                else:
                    lanelist.append((p3[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in
                                    sy.solve(eq4.subs(x, p4[0] + self.R + self.W / 2 + self.W + self.W), y)]]
            p = (p4[0] + self.R + self.W / 2 + self.W + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            point10 = (lanelist[-1])
            pointlist.append(lanelist)
            point2 = (point1[0], point1[1] + self.R / 2)
            point3 = (point1[0], point1[1] + self.R)
            lane5 = [point1, point2, point3]
            pointlist.append(lane5)
            point5 = [point4[0], point4[1] + self.R / 2]
            point6 = [point4[0], point4[1] + self.R]
            lane6 = [point4, point5, point6]
            pointlist.append(lane6)
            point8 = (point7[0], point7[1] + self.R / 2)
            point9 = (point7[0], point7[1] + self.R)
            lane7 = [point7, point8, point9]
            pointlist.append(lane7)
            point11 = (point10[0], point10[1] + self.R / 2)
            point12 = (point10[0], point10[1] + self.R)
            lane8 = [point10, point11, point12]
            pointlist.append(lane8)
            point13 = (point10[0] + self.W, point10[1])
            point14 = (point13[0], point13[1] + self.R / 2)
            point15 = (point13[0], point13[1] + self.R)
            lane9 = [point13, point14, point15]
            pointlist.append(lane9)
            point16 = (point10[0], point10[1] - 15)
            point17 = (point10[0], point10[1] - 30)
            lane10 = [point17, point16, point10]
            pointlist.append(lane10)
            point18 = (point13[0], point13[1] - 15)
            point19 = (point13[0], point13[1] - 30)
            lane11 = [point19, point18, point13]
            pointlist.append(lane11)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '单向双车道右弯曲岔路' or flag == '双向双车道右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point3[0] + self.R / 2, point3[1])
            point11 = (point3[0] + self.R, point3[1])
            lane4 = [point3, point10, point11]
            pointlist.append(lane4)
            point12 = (point6[0] + self.R / 2, point6[1])
            point13 = (point6[0] + self.R, point6[1])
            lane5 = [point6, point12, point13]
            pointlist.append(lane5)
            center = (point6[0], point6[1] - self.W / 2 - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[1]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + self.R + self.W / 2), y)]]
            p = (point6[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[1]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point6[0] + self.R - self.W / 2), y)]]
            p = (point6[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '一前行三车道右弯曲岔路' or flag == '二前行三车道一右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + self.R / 2, point3[1])
            point14 = (point3[0] + self.R, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + self.R / 2, point6[1])
            point16 = (point6[0] + self.R, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            point17 = (point9[0] + self.R / 2, point9[1])
            point18 = (point9[0] + self.R, point9[1])
            lane7 = [point9, point17, point18]
            pointlist.append(lane7)
            center = (point9[0], point9[1] - self.W / 2 - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + self.R + self.W / 2), y)]]
            p = (point9[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + self.R - self.W / 2), y)]]
            p = (point9[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '二前行三车道二右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point3[0] + self.R / 2, point3[1])
            point14 = (point3[0] + self.R, point3[1])
            lane5 = [point3, point13, point14]
            pointlist.append(lane5)
            point15 = (point6[0] + self.R / 2, point6[1])
            point16 = (point6[0] + self.R, point6[1])
            lane6 = [point6, point15, point16]
            pointlist.append(lane6)
            center = (point9[0], point9[1] - self.W / 2 - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in
                                    sy.solve(eq1.subs(x, point9[0] + self.R + self.W / 2 + self.W), y)]]
            p = (point9[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point9[0] + self.R + self.W / 2), y)]]
            p = (point9[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point9[0] + self.R - self.W / 2), y)]]
            p = (point9[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '一前行三车道左右弯曲岔路' or flag == '二前行三车道左右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            center1 = (point6[0], point6[1] + self.W / 2 + self.R)
            c1 = sy.Circle(sy.Point(center1), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[0]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + self.R - self.W / 2), y)]]
            p = (point6[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            c2 = sy.Circle(sy.Point(center1), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[0]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point6[0] + self.R + self.W / 2), y)]]
            p = (point6[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            point13 = (point6[0] + self.R / 2, point6[1])
            point14 = (point6[0] + self.R, point6[1])
            lane7 = [point6, point13, point14]
            pointlist.append(lane7)
            point15 = (point9[0] + self.R / 2, point9[1])
            point16 = (point9[0] + self.R, point9[1])
            lane8 = [point9, point15, point16]
            pointlist.append(lane8)
            center2 = (point9[0], point9[1] - self.W / 2 - self.R)
            c3 = sy.Circle(sy.Point(center2), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point9[0] + self.R + self.W / 2), y)]]
            p = (point9[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            c4 = sy.Circle(sy.Point(center2), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq4 = c4.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, point9[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point9[0] + m, a[1]))
                else:
                    lanelist.append((point9[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, point9[0] + self.R - self.W / 2), y)]]
            p = (point9[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '四车道一右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point10[0], point10[1] - self.W)
            point14 = (point13[0] + self.R / 2, point13[1])
            point15 = (point13[0] + self.R, point13[1])
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (point3[0] + self.R / 2, point3[1])
            point17 = (point3[0] + self.R, point3[1])
            lane6 = [point3, point16, point17]
            pointlist.append(lane6)
            point18 = (point6[0] + self.R / 2, point6[1])
            point19 = (point6[0] + self.R, point6[1])
            lane7 = [point6, point18, point19]
            pointlist.append(lane7)
            point20 = (point9[0] + self.R / 2, point9[1])
            point21 = (point9[0] + self.R, point9[1])
            lane8 = [point9, point20, point21]
            pointlist.append(lane8)
            point22 = (point12[0] + self.R / 2, point12[1])
            point23 = (point12[0] + self.R, point12[1])
            lane9 = [point12, point22, point23]
            pointlist.append(lane9)
            center = (point12[0], point12[1] - self.W / 2 - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + self.R + self.W / 2), y)]]
            p = (point12[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + self.R - self.W / 2), y)]]
            p = (point12[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '四车道二右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point10[0], point10[1] - self.W)
            point14 = (point13[0] + self.R / 2, point13[1])
            point15 = (point13[0] + self.R, point13[1])
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            point16 = (point3[0] + self.R / 2, point3[1])
            point17 = (point3[0] + self.R, point3[1])
            lane6 = [point3, point16, point17]
            pointlist.append(lane6)
            point18 = (point6[0] + self.R / 2, point6[1])
            point19 = (point6[0] + self.R, point6[1])
            lane7 = [point6, point18, point19]
            pointlist.append(lane7)
            point20 = (point9[0] + self.R / 2, point9[1])
            point21 = (point9[0] + self.R, point9[1])
            lane8 = [point9, point20, point21]
            pointlist.append(lane8)
            center = (point12[0], point12[1] - self.W / 2 - self.R)
            c1 = sy.Circle(sy.Point(center), self.R + self.W / 2 + self.W)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2 + self.W) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in
                                    sy.solve(eq1.subs(x, point12[0] + self.R + self.W / 2 + self.W), y)]]
            p = (point12[0] + self.R + self.W / 2 + self.W, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c2 = sy.Circle(sy.Point(center), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point12[0] + self.R + self.W / 2), y)]]
            p = (point12[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            lanelist = []
            c3 = sy.Circle(sy.Point(center), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point12[0] + self.R - self.W / 2), y)]]
            p = (point12[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

        if flag == '四车道左右弯曲岔路':
            point1 = (self.Start[0], self.Start[1] + self.W / 2)
            point2 = (point1[0] + self.R / 2, point1[1])
            point3 = (point1[0] + self.R, point1[1])
            lane1 = [point1, point2, point3]
            pointlist.append(lane1)
            point4 = (point1[0], point1[1] - self.W)
            point5 = (point4[0] + self.R / 2, point4[1])
            point6 = (point4[0] + self.R, point4[1])
            lane2 = [point4, point5, point6]
            pointlist.append(lane2)
            point7 = (point4[0], point4[1] - self.W)
            point8 = (point7[0] + self.R / 2, point7[1])
            point9 = (point7[0] + self.R, point7[1])
            lane3 = [point7, point8, point9]
            pointlist.append(lane3)
            point10 = (point7[0], point7[1] - self.W)
            point11 = (point10[0] + self.R / 2, point10[1])
            point12 = (point10[0] + self.R, point10[1])
            lane4 = [point10, point11, point12]
            pointlist.append(lane4)
            point13 = (point10[0], point10[1] - self.W)
            point14 = (point13[0] + self.R / 2, point13[1])
            point15 = (point13[0] + self.R, point13[1])
            lane5 = [point13, point14, point15]
            pointlist.append(lane5)
            center1 = (point6[0], point6[1] + self.W / 2 + self.R)
            c1 = sy.Circle(sy.Point(center1), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq1 = c1.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[0]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq1.subs(x, point6[0] + self.R - self.W / 2), y)]]
            p = (point6[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            c2 = sy.Circle(sy.Point(center1), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq2 = c2.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point6[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point6[0] + m, a[0]))
                else:
                    lanelist.append((point6[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq2.subs(x, point6[0] + self.R + self.W / 2), y)]]
            p = (point6[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            point16 = (point6[0] + self.R / 2, point6[1])
            point17 = (point6[0] + self.R, point6[1])
            lane8 = [point6, point16, point17]
            pointlist.append(lane8)
            point18 = (point9[0] + self.R / 2, point9[1])
            point19 = (point9[0] + self.R, point9[1])
            lane9 = [point9, point18, point19]
            pointlist.append(lane9)
            point20 = (point12[0] + self.R / 2, point12[1])
            point21 = (point12[0] + self.R, point12[1])
            lane10 = [point12, point20, point21]
            pointlist.append(lane10)
            center2 = (point12[0], point12[1] - self.W / 2 - self.R)
            c3 = sy.Circle(sy.Point(center2), self.R + self.W / 2)
            x, y = sy.symbols('x,y')
            eq3 = c3.equation(x, y)
            lanelist = []
            for m in range(int(self.R + self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq3.subs(x, point12[0] + self.R + self.W / 2), y)]]
            p = (point12[0] + self.R + self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)
            c4 = sy.Circle(sy.Point(center2), self.R - self.W / 2)
            x, y = sy.symbols('x,y')
            eq4 = c4.equation(x, y)
            lanelist = []
            for m in range(int(self.R - self.W / 2) + 1):
                a = [float(k) for k in ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, point12[0] + m), y)]]
                a = sorted(a)
                if len(a) == 2:
                    lanelist.append((point12[0] + m, a[1]))
                else:
                    lanelist.append((point12[0] + m, a[0]))
            p = [float(k) for k in
                 ['{:.3f}'.format(i.evalf()) for i in sy.solve(eq4.subs(x, point12[0] + self.R - self.W / 2), y)]]
            p = (point12[0] + self.R - self.W / 2, p[0])
            if p not in lanelist:
                lanelist.append(p)
            pointlist.append(lanelist)

            pointlist = self.rotation(pointlist)
            return pointlist

    def fixlane(self, pointlist):
        flag = self.Flag
        if flag == '单车道右弯曲并入单向双车道':
            return pointlist
        elif flag == '单车道右弯曲并入双向双车道':
            pointlist[2].reverse()
            pointlist[3].reverse()
            return pointlist
        elif flag == '单车道右弯曲并入二前行三车道':
            pointlist[3].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '单车道右弯曲并入一前行三车道':
            pointlist[2].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '单车道右弯曲并入四车道':
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            return pointlist
        elif flag == '单车道左弯曲并入单向双车道':
            return pointlist
        elif flag == '单向双车道右弯曲并入二前行三车道':
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '双向双车道右弯曲并入一前行三车道':
            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '单向双车道右弯曲并入四车道':
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            return pointlist
        elif flag == '双向双车道左弯曲并入二前行三车道':
            pointlist[0].reverse()
            pointlist[2].reverse()
            return pointlist
        elif flag == '二前行三车道右弯曲并入四车道':
            pointlist[0].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            return pointlist
        elif flag == '一前行三车道左弯曲并入四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            return pointlist
        elif flag == '单向双车道右弯曲岔路':
            return pointlist
        elif flag == '双向双车道右弯曲岔路':
            pointlist[0].reverse()
            pointlist[2].reverse()
            return pointlist
        elif flag == '一前行三车道右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            return pointlist
        elif flag == '二前行三车道一右弯曲岔路':
            pointlist[0].reverse()
            pointlist[3].reverse()
            return pointlist
        elif flag == '二前行三车道二右弯曲岔路':
            pointlist[0].reverse()
            pointlist[3].reverse()
            return pointlist
        elif flag == '一前行三车道左右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            return pointlist
        elif flag == '二前行三车道左右弯曲岔路':
            pointlist[0].reverse()
            pointlist[3].reverse()
            return pointlist
        elif flag == '四车道一右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '四车道二右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '四车道左右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist

    def fixboundary(self, pointlist):
        flag = self.Flag
        if flag == '单车道右弯曲并入单向双车道':
            return pointlist
        elif flag == '单车道右弯曲并入双向双车道':
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            return pointlist
        elif flag == '单车道右弯曲并入二前行三车道':
            pointlist[5].reverse()
            pointlist[8].reverse()
            return pointlist
        elif flag == '单车道右弯曲并入一前行三车道':
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            return pointlist
        elif flag == '单车道右弯曲并入四车道':
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[9].reverse()
            pointlist[10].reverse()
            return pointlist
        elif flag == '单车道左弯曲并入单向双车道':
            return pointlist
        elif flag == '单向双车道右弯曲并入二前行三车道':
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            return pointlist
        elif flag == '双向双车道右弯曲并入一前行三车道':
            pointlist[0].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            return pointlist
        elif flag == '单向双车道右弯曲并入四车道':
            pointlist[6].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
            pointlist[10].reverse()
            return pointlist
        elif flag == '双向双车道左弯曲并入二前行三车道':
            pointlist[0].reverse()
            pointlist[3].reverse()
            return pointlist
        elif flag == '二前行三车道右弯曲并入四车道':
            pointlist[0].reverse()
            pointlist[7].reverse()
            pointlist[8].reverse()
            pointlist[9].reverse()
            pointlist[10].reverse()
            return pointlist
        elif flag == '一前行三车道左弯曲并入四车道':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '单向双车道右弯曲岔路':
            return pointlist
        elif flag == '双向双车道右弯曲岔路':
            pointlist[0].reverse()
            pointlist[3].reverse()
            pointlist[4].reverse()
            return pointlist
        elif flag == '一前行三车道右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            return pointlist
        elif flag == '二前行三车道一右弯曲岔路':
            pointlist[0].reverse()
            pointlist[4].reverse()
            return pointlist
        elif flag == '二前行三车道二右弯曲岔路':
            pointlist[0].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '一前行三车道左右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            return pointlist
        elif flag == '二前行三车道左右弯曲岔路':
            pointlist[0].reverse()
            pointlist[4].reverse()
            pointlist[5].reverse()
            return pointlist
        elif flag == '四车道一右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            return pointlist
        elif flag == '四车道二右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
            return pointlist
        elif flag == '四车道左右弯曲岔路':
            pointlist[0].reverse()
            pointlist[1].reverse()
            pointlist[5].reverse()
            pointlist[6].reverse()
            pointlist[7].reverse()
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
        # lane
        lanes = str(self.StartLaneID) + ':' + str(self.StartLaneID + self.LaneNumber - 1)  # 当前组件涉及到的lane
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a Fork widget')
        printAutoInd(f, '% Set the lanes.')
        for lane in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
            printAutoInd(f, 'rrMap.Lanes(' + str(lane) + ') = roadrunner.hdmap.Lane();')
        laneidlist = []
        for i in range(self.StartLaneID, self.StartLaneID + self.LaneNumber):
            laneidlist.append('Lane' + str(i))
        laneid = ','.join(['"' + i + '"' for i in laneidlist])
        printAutoInd(f, '[rrMap.Lanes(' + lanes + ').ID] = deal(' + laneid + ');')
        lanepointlist = self.fixlane(self.getlanepoint())
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
        boundarypointlist = self.fixboundary(self.getboundarypoint())
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
        if self.Flag == '单车道右弯曲并入单向双车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
        elif self.Flag == '单车道右弯曲并入双向双车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
        elif self.Flag == '单车道右弯曲并入二前行三车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '单车道右弯曲并入一前行三车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Backward");')
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
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '单车道右弯曲并入四车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '单车道左弯曲并入单向双车道':
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
        elif self.Flag == '单向双车道右弯曲并入二前行三车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '双向双车道右弯曲并入一前行三车道':
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
                self.StartBoundaryID + 4) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '单向双车道右弯曲并入四车道':
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 1) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 1) + '),"Boundary' + str(
                self.StartBoundaryID + 2) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 2) + '),"Boundary' + str(
                self.StartBoundaryID + 3) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 4) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
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
        elif self.Flag == '双向双车道左弯曲并入二前行三车道':
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
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '二前行三车道右弯曲并入四车道':
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
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '一前行三车道左弯曲并入四车道':
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
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '单向双车道右弯曲岔路':
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
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
        elif self.Flag == '双向双车道右弯曲岔路':
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
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 3) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
        elif self.Flag == '一前行三车道右弯曲岔路':
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
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 5) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '二前行三车道一右弯曲岔路':
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
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '二前行三车道二右弯曲岔路':
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
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
        elif self.Flag == '一前行三车道左右弯曲岔路':
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
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
        elif self.Flag == '二前行三车道左右弯曲岔路':
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
                self.StartBoundaryID + 6) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 4) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
        elif self.Flag == '四车道一右弯曲岔路':
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
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '四车道二右弯曲岔路':
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
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
        elif self.Flag == '四车道左右弯曲岔路':
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
                self.StartBoundaryID + 8) + '",Alignment="Backward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 5) + '),"Boundary' + str(
                self.StartBoundaryID + 7) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 8) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 6) + '),"Boundary' + str(
                self.StartBoundaryID + 9) + '",Alignment="Forward");')
            printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 10) + '",Alignment="Forward");')
            printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.StartLaneID + 7) + '),"Boundary' + str(
                self.StartBoundaryID + 11) + '",Alignment="Forward");')

       
        printAutoInd(f, '% Combine lanes')
        if self.Flag == '单车道右弯曲并入单向双车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '单车道右弯曲并入双向双车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '单车道右弯曲并入二前行三车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
        elif self.Flag == '单车道右弯曲并入一前行三车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
        elif self.Flag == '单车道右弯曲并入四车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
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
        elif self.Flag == '单车道左弯曲并入单向双车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '单向双车道右弯曲并入二前行三车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
        elif self.Flag == '双向双车道右弯曲并入一前行三车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
        elif self.Flag == '单向双车道右弯曲并入四车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
        elif self.Flag == '双向双车道左弯曲并入二前行三车道':
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
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
        elif self.Flag == '二前行三车道右弯曲并入四车道':
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 5) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 1) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 4) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 2) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
        elif self.Flag == '一前行三车道左弯曲并入四车道':
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
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 7) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 6) + '"));')
        elif self.Flag == '单向双车道右弯曲岔路':
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
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
        elif self.Flag == '双向双车道右弯曲岔路':
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
                self.StartLaneID + 3) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
        elif self.Flag == '一前行三车道右弯曲岔路':
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
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '二前行三车道一右弯曲岔路':
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
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '二前行三车道二右弯曲岔路':
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
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '一前行三车道左右弯曲岔路':
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
                self.StartLaneID + 4) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '二前行三车道左右弯曲岔路':
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
                self.StartLaneID + 4) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 5) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
        elif self.Flag == '四车道一右弯曲岔路':
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
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
        elif self.Flag == '四车道二右弯曲岔路':
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
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')
        elif self.Flag == '四车道左右弯曲岔路':
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
                self.StartLaneID + 5) + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 1) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 6) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 2) + '"));')
            printAutoInd(f, 'rrMap.Lanes(' + str(
                self.StartLaneID + 7) + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane' + str(
                self.StartLaneID + 3) + '"));')

        printAutoInd(f, '% End of this widget')
