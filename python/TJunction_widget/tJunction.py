from func.printAuto import printAutoInd
from func.widget import Widget
from ArcLane_widget.arcLane import ArcLane
from TJunction_widget.straightLaneConnection import StraightLaneConnection

# import StraightLaneConncetion
import sympy as sy
import math


class tJunction(Widget):
    WidgetID = 1
    ID = 1  # junction id
    Start = (0, 0) 
    Width = 3.5
    StartLaneID = 1 
    StartBoundaryID = 1 
    
    OuterLaneNumber = [1, 1, 1]  #lane numbers of 3 directions.major\right\left
    InnerLaneNumber = 1 
    BoundaryNumber = 1
    k = "+0" 
    Flag = "" 
    GeometryPoints = [] 

    def __init__(self, dict1):
        self.WidgetID = Widget.WidgetID
        self.ID = Widget.JunctionID
        self.Width = dict1.get("Width")

        self.k = dict1.get("K")
        self.Start1 = dict1.get("Start")
        self.Start = (self.Start1[0], self.Start1[1] + self.Width / 2)

        self.StartLaneID = Widget.LaneID
        self.StartBoundaryID = Widget.BoundaryID
        self.OuterLaneNumber = dict1.get("OuterLaneNumber")
        self.InnerLaneNumber = dict1.get("InnerLaneNumber")
        self.BoundaryNumber = dict1.get("BoundaryNumber")
        self.Flag = dict1.get("Flag")
        self.GeometryPoints = self.getGeometryPoints()

    def get_Currents(self):
        Currents_info = {}
        Currents_info["Flag"] = self.Flag
        Currents_info["CurrentLanes"] = []
        if self.Flag == '单向车道转双向双车道':
            Currents_info['CurrentLanes'].append(self.StartLaneID + 4)
            Currents_info["Type"] = '单行道'
        if self.Flag == '单向车道转双向三车道一':
            Currents_info['CurrentLanes'].append(self.StartLaneID + 5)
            Currents_info["Type"] = '单行道'
        if self.Flag == '单向车道转双向三车道二':
            Currents_info['CurrentLanes'].append(self.StartLaneID + 5)
            Currents_info["Type"] = '单行道'
        if self.Flag == '单向车道转双向四车道':
            Currents_info['CurrentLanes'].append(self.StartLaneID + 6)
            Currents_info["Type"] = '单行道'
        if self.Flag == '同向双车道转双向双车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 4, self.StartLaneID + 6))
            Currents_info["Type"] = '单向实线双行道'
        if self.Flag == '同向双车道转双向三车道一':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 7))
            Currents_info["Type"] = '单向实线双行道'
        if self.Flag == '同向双车道转双向三车道二':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 5, self.StartLaneID + 7))
            Currents_info["Type"] = '单向实线双行道'
        if self.Flag == '同向双车道转双向四车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
            Currents_info["Type"] = '单向实线双行道'
        if self.Flag == '双向双车道转双向双车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
            Currents_info["Type"] = '双向实线双行道'
        if self.Flag == '双向双车道转双向三车道一':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 9))
            Currents_info["Type"] = '双向实线双行道'
        if self.Flag == '双向双车道转双向三车道二':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 9))
            Currents_info["Type"] = '双向实线双行道'
        if self.Flag == '双向双车道转双向四车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 8, self.StartLaneID + 10))
            Currents_info["Type"] = '双向实线双行道'
        if self.Flag == '双向三车道一转双向双车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 9))
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
        if self.Flag == '双向三车道一转双向三车道一':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 10))
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
        if self.Flag == '双向三车道一转双向三车道二':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 10))
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
        if self.Flag == '双向三车道一转双向四车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 8, self.StartLaneID + 11))
            Currents_info["Type"] = '一前行虚白线实黄线三行道'
        if self.Flag == '双向三车道二转双向双车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 9))
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
        if self.Flag == '双向三车道二转双向三车道一':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 10))
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
        if self.Flag == '双向三车道二转双向三车道二':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 10))
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
        if self.Flag == '双向三车道二转双向四车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 8, self.StartLaneID + 11))
            Currents_info["Type"] = '二前行实黄线虚白线三行道'
        if self.Flag == '双向四车道转双向双车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 10))
            Currents_info["Type"] = '双黄实线虚实四车道'
        if self.Flag == '双向四车道转双向三车道一':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 11))
            Currents_info["Type"] = '双黄实线虚实四车道'
        if self.Flag == '双向四车道转双向三车道二':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 7, self.StartLaneID + 11))
            Currents_info["Type"] = '双黄实线虚实四车道'
        if self.Flag == '双向四车道转双向四车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 8, self.StartLaneID + 12))
            Currents_info["Type"] = '双黄实线虚实四车道'
        if self.Flag == '双向双车道转同向双车道':
            Currents_info['CurrentLanes'] = list(range(self.StartLaneID + 6, self.StartLaneID + 8))
            Currents_info["Type"] = '双向实线双行道'
        return Currents_info

    def get_Nexts(self):
        Nexts = []
        edgelist = self.getEdgePoint()

        if self.Flag == "单向车道转双向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 6, self.StartLaneID + 5]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 8, self.StartLaneID + 7]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "单向车道转双向三车道一":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "二前行实黄线虚白线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 8,
                self.StartLaneID + 7,
                self.StartLaneID + 6,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "二前行实黄线虚白线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 11,
                self.StartLaneID + 10,
                self.StartLaneID + 9,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "单向车道转双向三车道二":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "一前行虚白线实黄线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 8,
                self.StartLaneID + 7,
                self.StartLaneID + 6,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "一前行虚白线实黄线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 11,
                self.StartLaneID + 10,
                self.StartLaneID + 9,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "单向车道转双向四车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                edgelist[3][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双黄实线虚实四车道"
            Next1["lanes"] = [
                self.StartLaneID + 10,
                self.StartLaneID + 9,
                self.StartLaneID + 8,
                self.StartLaneID + 7,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双黄实线虚实四车道"
            Next2["lanes"] = [
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
                self.StartLaneID + 11,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "同向双车道转双向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 7, self.StartLaneID + 6]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 9, self.StartLaneID + 8]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "同向双车道转双向三车道一":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "二前行实黄线虚白线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 9,
                self.StartLaneID + 8,
                self.StartLaneID + 7,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "二前行实黄线虚白线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "同向双车道转双向三车道二":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "一前行虚白线实黄线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 9,
                self.StartLaneID + 8,
                self.StartLaneID + 7,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "一前行虚白线实黄线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "同向双车道转双向四车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                edgelist[3][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双黄实线虚实四车道"
            Next1["lanes"] = [
                self.StartLaneID + 11,
                self.StartLaneID + 10,
                self.StartLaneID + 9,
                self.StartLaneID + 8,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双黄实线虚实四车道"
            Next2["lanes"] = [
                self.StartLaneID + 15,
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向双车道转双向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 9, self.StartLaneID + 8]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 11, self.StartLaneID + 10]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向双车道转同向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "单向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 9, self.StartLaneID + 8]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "单向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 11, self.StartLaneID + 10]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向双车道转双向三车道一":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "二前行实黄线虚白线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 11,
                self.StartLaneID + 10,
                self.StartLaneID + 9,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "二前行实黄线虚白线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向双车道转双向三车道二":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "一前行虚白线实黄线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 11,
                self.StartLaneID + 10,
                self.StartLaneID + 9,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "一前行虚白线实黄线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向双车道转双向四车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                edgelist[3][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双黄实线虚实四车道"
            Next1["lanes"] = [
                self.StartLaneID + 13,
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双黄实线虚实四车道"
            Next2["lanes"] = [
                self.StartLaneID + 17,
                self.StartLaneID + 16,
                self.StartLaneID + 15,
                self.StartLaneID + 14,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道一转双向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 10, self.StartLaneID + 9]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 12, self.StartLaneID + 11]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道一转双向三车道一":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "二前行实黄线虚白线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "二前行实黄线虚白线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 15,
                self.StartLaneID + 14,
                self.StartLaneID + 13,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道一转双向三车道二":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "一前行虚白线实黄线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "一前行虚白线实黄线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 15,
                self.StartLaneID + 14,
                self.StartLaneID + 13,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道一转双向四车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                edgelist[3][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双黄实线虚实四车道"
            Next1["lanes"] = [
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
                self.StartLaneID + 11,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双黄实线虚实四车道"
            Next2["lanes"] = [
                self.StartLaneID + 18,
                self.StartLaneID + 17,
                self.StartLaneID + 16,
                self.StartLaneID + 15,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道二转双向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 10, self.StartLaneID + 9]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 12, self.StartLaneID + 11]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道二转双向三车道一":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "二前行实黄线虚白线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "二前行实黄线虚白线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 15,
                self.StartLaneID + 14,
                self.StartLaneID + 13,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道二转双向三车道二":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "一前行虚白线实黄线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 12,
                self.StartLaneID + 11,
                self.StartLaneID + 10,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "一前行虚白线实黄线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 15,
                self.StartLaneID + 14,
                self.StartLaneID + 13,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向三车道二转双向四车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                edgelist[3][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双黄实线虚实四车道"
            Next1["lanes"] = [
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
                self.StartLaneID + 11,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双黄实线虚实四车道"
            Next2["lanes"] = [
                self.StartLaneID + 18,
                self.StartLaneID + 17,
                self.StartLaneID + 16,
                self.StartLaneID + 15,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向四车道转双向双车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                edgelist[1][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双向实线双行道"
            Next1["lanes"] = [self.StartLaneID + 11, self.StartLaneID + 10]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双向实线双行道"
            Next2["lanes"] = [self.StartLaneID + 13, self.StartLaneID + 12]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向四车道转双向三车道一":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "二前行实黄线虚白线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 13,
                self.StartLaneID + 12,
                self.StartLaneID + 11,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "二前行实黄线虚白线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 16,
                self.StartLaneID + 15,
                self.StartLaneID + 14,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向四车道转双向三车道二":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                edgelist[2][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "一前行虚白线实黄线三行道"
            Next1["lanes"] = [
                self.StartLaneID + 13,
                self.StartLaneID + 12,
                self.StartLaneID + 11,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "一前行虚白线实黄线三行道"
            Next2["lanes"] = [
                self.StartLaneID + 16,
                self.StartLaneID + 15,
                self.StartLaneID + 14,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)
        elif self.Flag == "双向四车道转双向四车道":
            Next1 = dict()
            Next1['current'] = self.Flag + '_tjunction'
            Next1['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                edgelist[3][1][1],
            )
            Next1["endpoint"] = self.roate_endpoints(endpoint)
            Next1["type"] = "双黄实线虚实四车道"
            Next1["lanes"] = [
                self.StartLaneID + 15,
                self.StartLaneID + 14,
                self.StartLaneID + 13,
                self.StartLaneID + 12,
            ]
            if self.k == "+0":
                Next1["direction"] = "-"
            elif self.k == "-0":
                Next1["direction"] = "+"
            elif self.k == "+":
                Next1["direction"] = "+0"
            elif self.k == "-":
                Next1["direction"] = "-0"
            Nexts.append(Next1)

            Next2 = dict()
            Next2['current'] = self.Flag + '_tjunction'
            Next2['ID'] = self.WidgetID
            endpoint = (
                float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                edgelist[0][0][1],
            )
            Next2["endpoint"] = self.roate_endpoints(endpoint)
            Next2["type"] = "双黄实线虚实四车道"
            Next2["lanes"] = [
                self.StartLaneID + 19,
                self.StartLaneID + 18,
                self.StartLaneID + 17,
                self.StartLaneID + 16,
            ]
            if self.k == "+0":
                Next2["direction"] = "+"
            elif self.k == "-0":
                Next2["direction"] = "-"
            elif self.k == "+":
                Next2["direction"] = "-0"
            elif self.k == "-":
                Next2["direction"] = "+0"
            Nexts.append(Next2)

        return Nexts
    
    def get_coveredArea(self):
        edgePoints=self.getEdgePoint()
        result=[]
        point1=(float("{:.3f}".format(edgePoints[0][0][0]-self.Width/2)),float("{:.3f}".format(edgePoints[0][0][1]-self.Width/2*2-self.Width/4)))
        point2=(float("{:.3f}".format(edgePoints[0][1][0]+self.Width/2)),float("{:.3f}".format(edgePoints[0][1][1]-self.Width/2*2-self.Width/4)))
        point3=(float("{:.3f}".format(edgePoints[-1][1][0]+self.Width/2)),float("{:.3f}".format(edgePoints[-1][1][1]+self.Width/2)))
        point4=(float("{:.3f}".format(edgePoints[-1][0][0]-self.Width/2)),float("{:.3f}".format(edgePoints[-1][0][1]+self.Width/2)))
        
        result.append(point1)
        result.append(point2)
        result.append(point3)
        result.append(point4)

        tmp=[result]
        finalResult=self.rotation(tmp)
        return(finalResult)

    def roate_endpoints(self, point):
        if self.k == "+":
            return point
        if self.k == "+0":  # rotate 90 degrees clockwise around the start.
            x = float(
                "{:.3f}".format(
                    (point[0] - self.Start1[0]) * int(math.cos(math.pi / 2))
                    + (point[1] - self.Start1[1]) * int(math.sin(math.pi / 2))
                    + self.Start1[0]
                )
            )
            y = float(
                "{:.3f}".format(
                    (point[1] - self.Start1[1]) * int(math.cos(math.pi / 2))
                    - (point[0] - self.Start1[0]) * int(math.sin(math.pi / 2))
                    + self.Start1[1]
                )
            )
            return x, y
        if self.k == "-":  # rotate 180 degrees clockwise around the start.
            x = float(
                "{:.3f}".format(
                    (point[0] - self.Start1[0]) * int(math.cos(math.pi))
                    + (point[1] - self.Start1[1]) * int(math.sin(math.pi))
                    + self.Start1[0]
                )
            )
            y = float(
                "{:.3f}".format(
                    (point[1] - self.Start1[1]) * int(math.cos(math.pi))
                    - (point[0] - self.Start1[0]) * int(math.sin(math.pi))
                    + self.Start1[1]
                )
            )
            return x, y
        if self.k == "-0":  # rotate 270 degrees clockwise around the start.
            x = float(
                "{:.3f}".format(
                    (point[0] - self.Start1[0]) * int(math.cos(math.pi * 1.5))
                    + (point[1] - self.Start1[1]) * int(math.sin(math.pi * 1.5))
                    + self.Start1[0]
                )
            )
            y = float(
                "{:.3f}".format(
                    (point[1] - self.Start1[1]) * int(math.cos(math.pi * 1.5))
                    - (point[0] - self.Start1[0]) * int(math.sin(math.pi * 1.5))
                    + self.Start1[1]
                )
            )
            return x, y

    def rotation(self, pointlist):
        if self.k == "+":
            return pointlist
        if self.k == "+0": 
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float(
                        "{:.3f}".format(
                            (j[0] - self.Start1[0]) * int(math.cos(math.pi / 2))
                            + (j[1] - self.Start1[1]) * int(math.sin(math.pi / 2))
                            + self.Start1[0]
                        )
                    )
                    y = float(
                        "{:.3f}".format(
                            (j[1] - self.Start1[1]) * int(math.cos(math.pi / 2))
                            - (j[0] - self.Start1[0]) * int(math.sin(math.pi / 2))
                            + self.Start1[1]
                        )
                    )
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == "-": 
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float(
                        "{:.3f}".format(
                            (j[0] - self.Start1[0]) * int(math.cos(math.pi))
                            + (j[1] - self.Start1[1]) * int(math.sin(math.pi))
                            + self.Start1[0]
                        )
                    )
                    y = float(
                        "{:.3f}".format(
                            (j[1] - self.Start1[1]) * int(math.cos(math.pi))
                            - (j[0] - self.Start1[0]) * int(math.sin(math.pi))
                            + self.Start1[1]
                        )
                    )
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        if self.k == "-0": 
            lst1 = []
            for i in pointlist:
                lst0 = []
                for j in i:
                    x = float(
                        "{:.3f}".format(
                            (j[0] - self.Start1[0]) * int(math.cos(math.pi * 1.5))
                            + (j[1] - self.Start1[1]) * int(math.sin(math.pi * 1.5))
                            + self.Start1[0]
                        )
                    )
                    y = float(
                        "{:.3f}".format(
                            (j[1] - self.Start1[1]) * int(math.cos(math.pi * 1.5))
                            - (j[0] - self.Start1[0]) * int(math.sin(math.pi * 1.5))
                            + self.Start1[1]
                        )
                    )
                    lst0.append((x, y))
                lst1.append(lst0)
            return lst1
        else:
            print("The function is wrong")

    def PointtoString(self, lst):
        lst = [
            str(i)
            .replace(",", "")
            .replace(") (", ";")
            .replace("(", "")
            .replace(")", "")
            for i in lst
        ]
        string = ",".join(lst)
        return string

    def getGeometryPoints(self):
        pointlist = []
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

    # #return list[[]]
    def getEdgePoint(self):
        edgelist = []
        for i in range(self.OuterLaneNumber[1]):
            tmp = []
            tmp.append(
                (
                    float(
                        "{:.3f}".format(self.Start[0] - self.Width / 2 - self.Width / 4)
                    ),
                    float(
                        "{:.3f}".format(
                            self.Start[1]
                            + self.Width / 4
                            + self.Width * (2 * i + 1) / 2
                        )
                    ),
                )
            )
            tmp.append(
                (
                    float(
                        "{:.3f}".format(
                            self.Start[0]
                            + self.Width / 2
                            + self.Width * (self.OuterLaneNumber[0] - 1)
                            + self.Width / 4
                        )
                    ),
                    float(
                        "{:.3f}".format(
                            self.Start[1]
                            + self.Width / 4
                            + self.Width * (2 * i + 1) / 2
                        )
                    ),
                )
            )

            edgelist.append(tmp)

        return edgelist

    # return list[]。1\lanelist，2\boundarylist。
    # 3\arclanelist。4\straightconnectionlist。
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
        # print(edgelist)

        if flag == "单向车道转双向双车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": self.Start,
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])

            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  # reuse
                "BoundaryId2": self.StartBoundaryID + 6,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])

            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            # indexes.append((6,4))
            indexes.append((4, 6))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            #outer road
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)
            indexes.append((7, 8))
            directions.append("Forward")

            # eg:0 is successor of 4
            successors.append((4, 0))
            predecessors.append((0, 4))
            predecessors.append((1, 4))
            alignment.append(["Forward", "Forward"])

            #id+5
            lane2 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary3)  # reuse id:9
            boundarylist.append(boundary4)
            indexes.append((9, 10))
            directions.append("Forward")
            successors.append((2, 5))
            predecessors.append((5, 2))
            successors.append((0, 5))
            predecessors.append((5, 0))
            alignment.append(["Forward", "Forward"])

            # id+6
            lane3 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lane3.reverse()
            lanelist.append(lane3)
            boundary5 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            boundary5.reverse()
            boundarylist.append(boundary5)  
            indexes.append((9, 11))
            directions.append("Forward")
            successors.append((6, 3))
            predecessors.append((3, 6))
            alignment.append(["Backward", "Forward"])

            # id+7
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lane4.reverse()
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundary6.reverse()
            boundarylist.append(boundary6)
            boundarylist.append(boundary7)  # reuse,id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))

            successors.append((1, 7))
            predecessors.append((7, 1))
            alignment.append(["Backward", "Forward"])

            # id+8
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane5)
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)  
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((8, 2))
            predecessors.append((2, 8))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "单向车道转双向三车道一":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": self.Start,
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 4,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((6, 4))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict5)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction id：startLaneID+5
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)
            indexes.append((8, 9))
            directions.append("Forward")
            
            successors.append((5, 0))
            # successors.append((4,1))
            predecessors.append((0, 5))
            predecessors.append((1, 5))
            alignment.append(["Forward", "Forward"])

            # right road1 id +6
            lane2 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary3)  # reuse id:10
            boundarylist.append(boundary4)
            indexes.append((10, 11))
            directions.append("Forward")
            successors.append((2, 6))
            predecessors.append((6, 2))
            successors.append((0, 6))
            predecessors.append((6, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +7
            lane3 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary5 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary5)  # reuse id:12
            # boundarylist.append(boundary4)
            indexes.append((12, 10))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # right road3 id+8
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane4)
            boundarylist.append(boundary6)
            indexes.append((12, 13))
            directions.append("Forward")
            successors.append((8, 4))
            predecessors.append((4, 8))
            alignment.append(["Backward", "Forward"])

            # left road1 id+9
            lane5 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane5)
            boundary7 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary7)
            boundarylist.append(boundary8)  # reuse,id:15
            indexes.append((15, 14))
            directions.append("Forward")
            successors.append((4, 9))
            predecessors.append((9, 4))

            successors.append((1, 9))
            predecessors.append((9, 1))
            alignment.append(["Backward", "Forward"])

            # left road2 id+10
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane6)
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary9)  # reuse id:16
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((10, 3))
            predecessors.append((3, 10))
            alignment.append(["Forward", "Forward"])

            # left road3 id+11
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((11, 2))
            predecessors.append((2, 11))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "单向车道转双向三车道二":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": self.Start,
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 6,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((4, 6))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # straight3
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict5)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[1])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight3)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction id：startLaneID+5
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)
            indexes.append((8, 9))
            directions.append("Forward")
            
            successors.append((5, 0))
            predecessors.append((0, 5))
            predecessors.append((1, 5))
            alignment.append(["Forward", "Forward"])

            # right road1 id +6
            lane2 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary3)  # reuse id:10
            boundarylist.append(boundary4)
            indexes.append((10, 11))
            directions.append("Forward")
            successors.append((2, 6))
            predecessors.append((6, 2))
            successors.append((0, 6))
            predecessors.append((6, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +7
            lane3 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane3)
            boundary5 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary5)  # reuse id:12
            # boundarylist.append(boundary4)
            indexes.append((10, 12))
            directions.append("Forward")
            successors.append((7, 3))
            predecessors.append((3, 7))
            alignment.append(["Backward", "Forward"])

            # right road3 id+8
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane4)
            boundarylist.append(boundary6)
            indexes.append((12, 13))
            directions.append("Forward")
            successors.append((8, 4))
            predecessors.append((4, 8))
            alignment.append(["Forward", "Forward"])

            # left road1 id+9
            lane5 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane5)
            boundary7 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary7)
            boundarylist.append(boundary8)  # reuse,id:15
            indexes.append((15, 14))
            directions.append("Forward")
            successors.append((4, 9))
            predecessors.append((9, 4))
            alignment.append(["Forward", "Forward"])

            # left road2 id+10
            lane6 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary9)  # reuse id:16
            indexes.append((16, 15))
            directions.append("Forward")
            successors.append((3, 10))
            predecessors.append((10, 3))
            successors.append((1, 10))
            predecessors.append((10, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+11
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((11, 2))
            predecessors.append((2, 11))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "单向车道转双向四车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": self.Start,
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 4,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((6, 4))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict5)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # straight4
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[3][1],
                "End": edgelist[3][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 7,  
                "BoundaryId2": self.StartBoundaryID + 8,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight4 = StraightLaneConnection(dict6)
            tmpBoundarys2 = []
            tmpBoundarys2.append(tmpStraight3.boundaryPoints[1])
            tmpBoundarys2.append(tmpStraight4.boundaryPoints[1])
            tmpStraight4.setBoundaryPoints(tmpBoundarys2)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append("Forward")
            indexes.append((7, 8))
            laneObjects.append(tmpStraight4)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction id：startLaneID+6
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)
            indexes.append((9, 10))
            directions.append("Forward")
            left road
            successors.append((6, 0))
            predecessors.append((0, 6))
            predecessors.append((1, 6))
            alignment.append(["Forward", "Forward"])

            # right road1 id +7 
            lane2 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary3)  # reuse id:11
            boundarylist.append(boundary4)
            indexes.append((11, 12))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            successors.append((0, 7))
            predecessors.append((7, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +8 to right
            lane3 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary5 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary5)  # reuse id:13
            # boundarylist.append(boundary4)
            indexes.append((13, 11))
            directions.append("Forward")
            successors.append((3, 8))
            predecessors.append((8, 3))
            alignment.append(["Forward", "Forward"])

            # right road3 id+9 to left
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane4)
            boundarylist.append(boundary6)  # reuse id:14
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((9, 4))
            predecessors.append((4, 9))
            alignment.append(["Backward", "Forward"])

            # right road4 id+10 to left
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    edgelist[3][1][1],
                ),
                (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                edgelist[3][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[3][1][0] + self.Width / 4,
                    edgelist[3][1][1] + self.Width / 2,
                ),
                (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)  # reuse id:15
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((10, 5))
            predecessors.append((5, 10))
            alignment.append(["Forward", "Forward"])

            # left road1 id+11 to left
            lane6 = [
                edgelist[3][0],
                (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    edgelist[3][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:17
            indexes.append((17, 16))
            directions.append("Forward")
            successors.append((5, 11))
            predecessors.append((11, 5))
            alignment.append(["Forward", "Forward"])

            # left road2 id+12 to left
            lane7 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:18
            indexes.append((18, 17))
            directions.append("Forward")
            successors.append((4, 12))
            predecessors.append((12, 4))
            successors.append((1, 12))
            predecessors.append((12, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+13 to right
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:19
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((13, 3))
            predecessors.append((3, 13))
            alignment.append(["Forward", "Forward"])

            # left road4 id+14 to right
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((14, 2))
            predecessors.append((2, 14))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "同向双车道转双向双车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            # laneIdList.append(tmpArc2.ID)
            # boundaryIdList.append(tmpArc2.BoundaryId1)
            # boundaryIdList.append(tmpArc2.BoundaryId2)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])

            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  # reuse
                "BoundaryId2": self.StartBoundaryID + 6,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])

            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((4, 6))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+4
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:8
            indexes.append((7, 8))
            directions.append("Forward")
            
            successors.append((4, 1))
            # predecessors.append((0,4))
            predecessors.append((1, 4))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+5
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((8, 9))
            directions.append("Forward")
            successors.append((5, 0))
            predecessors.append((0, 5))
            alignment.append(["Forward", "Forward"])

            # right road1，id+6
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:10
            boundarylist.append(boundary5)
            indexes.append((10, 11))
            directions.append("Forward")
            successors.append((2, 6))
            predecessors.append((6, 2))
            successors.append((0, 6))
            predecessors.append((6, 0))
            alignment.append(["Forward", "Forward"])

            # right road2，id+7
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary6)  
            indexes.append((10, 12))
            directions.append("Forward")
            successors.append((7, 3))
            predecessors.append((3, 7))
            alignment.append(["Backward", "Forward"])

            # left road1，id+8
            lane5 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane5)
            boundary7 = [
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary7)
            boundarylist.append(boundary8)  # reuse,id:14
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((3, 8))
            predecessors.append((8, 3))
            successors.append((1, 8))
            predecessors.append((8, 1))
            alignment.append(["Backward", "Forward"])

            # left road2，id+9
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane6)
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary9)  
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 2))
            predecessors.append((2, 9))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "同向双车道转双向三车道一":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 4,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((6, 4))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict5)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction id：startLaneID+5
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:9
            indexes.append((8, 9))
            directions.append("Forward")
            successors.append((5, 1))
            predecessors.append((1, 5))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+6
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((9, 10))
            directions.append("Forward")
            successors.append((6, 0))
            predecessors.append((0, 6))
            alignment.append(["Forward", "Forward"])

            # right road1 id +7
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:11
            boundarylist.append(boundary5)
            indexes.append((11, 12))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            successors.append((0, 7))
            predecessors.append((7, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +8
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:13
            # boundarylist.append(boundary4)
            indexes.append((13, 11))
            directions.append("Forward")
            successors.append((3, 8))
            predecessors.append((8, 3))
            alignment.append(["Forward", "Forward"])

            # right road3 id+9
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((9, 4))
            predecessors.append((4, 9))
            alignment.append(["Backward", "Forward"])

            # left road1 id+10
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:16
            indexes.append((16, 15))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((1, 10))
            predecessors.append((10, 1))
            alignment.append(["Backward", "Forward"])

            # left road2 id+11
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:17
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((11, 3))
            predecessors.append((3, 11))
            alignment.append(["Forward", "Forward"])

            # left road3 id+12
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((12, 2))
            predecessors.append((2, 12))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "同向双车道转双向三车道二":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 6,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((4, 6))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # straight3
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict5)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[1])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight3)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction id：startLaneID+5
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)
            indexes.append((8, 9))
            directions.append("Forward")
            successors.append((5, 1))
            predecessors.append((1, 5))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+6
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((9, 10))
            directions.append("Forward")
            successors.append((6, 0))
            predecessors.append((0, 6))
            alignment.append(["Forward", "Forward"])

            # right road1 id +7
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:11
            boundarylist.append(boundary5)
            indexes.append((11, 12))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            successors.append((0, 7))
            predecessors.append((7, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +8
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:13
            # boundarylist.append(boundary4)
            indexes.append((11, 13))
            directions.append("Forward")
            successors.append((8, 3))
            predecessors.append((3, 8))
            alignment.append(["Backward", "Forward"])

            # right road3 id+9
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((9, 4))
            predecessors.append((4, 9))
            alignment.append(["Forward", "Forward"])

            # left road1 id+10
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:16
            indexes.append((16, 15))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            alignment.append(["Forward", "Forward"])

            # left road2 id+11
            lane7 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:17
            indexes.append((17, 16))
            directions.append("Forward")
            successors.append((3, 11))
            predecessors.append((11, 3))
            successors.append((1, 11))
            predecessors.append((11, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+12
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((12, 2))
            predecessors.append((2, 12))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "同向双车道转双向四车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            # print(dict1)
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": self.Start,
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # straight1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict3)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 4,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict4)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((6, 4))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict5)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # straight4
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[3][1],
                "End": edgelist[3][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 7,  
                "BoundaryId2": self.StartBoundaryID + 8,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight4 = StraightLaneConnection(dict6)
            tmpBoundarys2 = []
            tmpBoundarys2.append(tmpStraight3.boundaryPoints[1])
            tmpBoundarys2.append(tmpStraight4.boundaryPoints[1])
            tmpStraight4.setBoundaryPoints(tmpBoundarys2)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append("Forward")
            indexes.append((7, 8))
            laneObjects.append(tmpStraight4)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction id：startLaneID+6
            lane1 = [
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
                (self.Start[0], self.Start[1] - self.Width / 4),
                self.Start,
            ]
            lanelist.append(lane1)
            boundary1 = [
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] - self.Width / 2, self.Start[1]),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)
            indexes.append((9, 10))
            directions.append("Forward")
            successors.append((6, 1))
            predecessors.append((1, 6))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+7
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((10, 11))
            directions.append("Forward")
            successors.append((7, 0))
            predecessors.append((0, 7))
            alignment.append(["Forward", "Forward"])

            # right road1 id +8 to right
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:12
            boundarylist.append(boundary5)
            indexes.append((12, 13))
            directions.append("Forward")
            successors.append((2, 8))
            predecessors.append((8, 2))
            successors.append((0, 8))
            predecessors.append((8, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +9 to right
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:14
            # boundarylist.append(boundary4)
            indexes.append((14, 12))
            directions.append("Forward")
            successors.append((3, 9))
            predecessors.append((9, 3))
            alignment.append(["Forward", "Forward"])

            # right road3 id+10 to left
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)  # reuse id:15
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((10, 4))
            predecessors.append((4, 10))
            alignment.append(["Backward", "Forward"])

            # right road4 id+11 to left
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    edgelist[3][1][1],
                ),
                (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                edgelist[3][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[3][1][0] + self.Width / 4,
                    edgelist[3][1][1] + self.Width / 2,
                ),
                (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((11, 5))
            predecessors.append((5, 11))
            alignment.append(["Forward", "Forward"])

            # left road1 id+12 to left
            lane7 = [
                edgelist[3][0],
                (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    edgelist[3][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary9 = [
                (edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)),
                ),
            ]
            boundary10 = [
                (edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary9)
            boundarylist.append(boundary10)  # reuse,id:18
            indexes.append((18, 17))
            directions.append("Forward")
            successors.append((5, 12))
            predecessors.append((12, 5))
            alignment.append(["Forward", "Forward"])

            # left road2 id+13 to left
            lane8 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:19
            indexes.append((19, 18))
            directions.append("Forward")
            successors.append((4, 13))
            predecessors.append((13, 4))
            successors.append((1, 13))
            predecessors.append((13, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+14 to right
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)  # reuse id:20
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((14, 3))
            predecessors.append((3, 14))
            alignment.append(["Forward", "Forward"])

            # left road4 id+15 to right
            lane10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane10)
            boundary13 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary13)
            indexes.append((20, 21))
            directions.append("Forward")
            successors.append((15, 2))
            predecessors.append((2, 15))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向双车道转双向双车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,  # reuse id:0
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,  # reuse id:2
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[1][1],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,  # reuse id:0
                "BoundaryId2": self.StartBoundaryID + 4,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            lanelist.append(tmpArc3.lanePoints)
            boundarylist.append(tmpArc3.boundaryPoints[1])
            tmpArc3.boundaryPoints[0] = tmpArc1.boundaryPoints[0]
            directions.append(tmpArc3.TravelDirection)
            indexes.append((0, 4))
            laneObjects.append(tmpArc3)
            alignment.append(("Backward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,  # reuse id:2
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[1])
            tmpArc4.boundaryPoints[0] = tmpArc2.boundaryPoints[0]
            directions.append(tmpArc4.TravelDirection)
            indexes.append((2, 5))
            laneObjects.append(tmpArc4)
            alignment.append(("Backward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  # reuse
                "BoundaryId2": self.StartBoundaryID + 8,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((6, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+6 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:10
            indexes.append((10, 9))
            directions.append("Forward")
            successors.append((2, 6))
            predecessors.append((6, 2))
            successors.append((3, 6))
            predecessors.append((6, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+7  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((10, 11))
            directions.append("Forward")
            successors.append((7, 0))
            predecessors.append((0, 7))
            predecessors.append((1, 7))
            alignment.append(["Backward", "Forward"])

            # right road1，id+8
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:12
            boundarylist.append(boundary5)
            indexes.append((12, 13))
            directions.append("Forward")
            successors.append((4, 8))
            predecessors.append((8, 4))
            successors.append((0, 8))
            predecessors.append((8, 0))
            alignment.append(["Forward", "Forward"])

            # right road2，id+9
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary6)  
            indexes.append((12, 14))
            directions.append("Forward")
            successors.append((9, 5))
            predecessors.append((5, 9))
            predecessors.append((2, 9))
            alignment.append(["Backward", "Forward"])

            # left road1，id+10
            lane5 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane5)
            boundary7 = [
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary7)
            boundarylist.append(boundary8)  # reuse,id:16
            indexes.append((16, 15))
            directions.append("Forward")
            successors.append((5, 10))
            predecessors.append((10, 5))
            successors.append((1, 10))
            predecessors.append((10, 1))
            alignment.append(["Backward", "Forward"])

            # left road2，id+11
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane6)
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary9)  
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((11, 4))
            predecessors.append((4, 11))
            predecessors.append((3, 11))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向双车道转同向双车道":  
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                # 'Start':(11.37,41.88),
                # 'End':(13.995,44.505),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,  # reuse id:0
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }

            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])
            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,  # reuse id:0
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            lanelist.append(tmpArc3.lanePoints)
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            # tmpArc3.boundaryPoints[0] = tmpArc1.boundaryPoints[0]
            directions.append(tmpArc3.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,  
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,  # reuse
                "BoundaryId2": self.StartBoundaryID + 4,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((6, 4))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+6 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width / 2, self.Start[1]),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:10
            indexes.append((8, 7))
            directions.append("Forward")
            successors.append((1, 4))
            predecessors.append((4, 1))

            alignment.append(["Backward", "Forward"])

            # major direction2 id：+7  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((8, 9))
            directions.append("Forward")
            successors.append((5, 0))
            predecessors.append((0, 5))
            alignment.append(["Forward", "Forward"])

            # right road1，id+8
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:12
            boundarylist.append(boundary5)
            indexes.append((10, 11))
            directions.append("Forward")
            successors.append((0, 6))
            predecessors.append((6, 0))
            successors.append((2, 6))
            predecessors.append((6, 2))
            alignment.append(["Forward", "Forward"])

            # right road2，id+9
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary6)  
            indexes.append((12, 10))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # left road1，id+10
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane5)
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary7)
            boundarylist.append(boundary8)  # reuse,id:16
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((8, 3))
            predecessors.append((3, 8))
            alignment.append(["Forward", "Forward"])

            # left road2，id+11
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane6)
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary9)  
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 1))
            predecessors.append((1, 9))
            successors.append((9, 2))
            predecessors.append((2, 9))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向双车道转双向三车道一":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": self.Start,
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction id：startLaneID+7 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((8, 0))
            predecessors.append((0, 8))
            predecessors.append((1, 8))
            alignment.append(["Backward", "Forward"])

            # right road1 id +9
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:15
            boundarylist.append(boundary5)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((4, 9))
            predecessors.append((9, 4))
            successors.append((0, 9))
            predecessors.append((9, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +10
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary6)  # reuse id:17
            indexes.append((17, 15))
            directions.append("Forward")
            successors.append((5, 10))
            predecessors.append((10, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+11
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((11, 6))
            predecessors.append((6, 11))
            predecessors.append((2, 11))
            alignment.append(["Backward", "Forward"])

            # left road1 id+12
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:20
            indexes.append((20, 19))
            directions.append("Forward")
            successors.append((6, 12))
            predecessors.append((12, 6))
            successors.append((1, 12))
            predecessors.append((12, 1))
            alignment.append(["Backward", "Forward"])

            # left road2 id+13
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:21
            indexes.append((20, 21))
            directions.append("Forward")
            successors.append((13, 5))
            predecessors.append((5, 13))
            alignment.append(["Forward", "Forward"])

            # left road3 id+14
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((21, 22))
            directions.append("Forward")
            successors.append((14, 4))
            predecessors.append((4, 14))
            predecessors.append((3, 14))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向双车道转双向三车道二":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": self.Start,
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # '左下转'
            }
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,
                "BoundaryId2": self.StartBoundaryID + 10,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((8, 10))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[1])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction id：startLaneID+7 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((8, 0))
            predecessors.append((0, 8))
            predecessors.append((1, 8))
            alignment.append(["Backward", "Forward"])

            # right road1 id +9
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:15
            boundarylist.append(boundary5)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((4, 9))
            predecessors.append((9, 4))
            successors.append((0, 9))
            predecessors.append((9, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +10
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary6)  # reuse id:17
            indexes.append((15, 17))
            directions.append("Forward")
            successors.append((10, 5))
            predecessors.append((5, 10))
            alignment.append(["Backward", "Forward"])

            # right road3 id+11
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((11, 6))
            predecessors.append((6, 11))
            predecessors.append((2, 11))
            alignment.append(["Forward", "Forward"])

            # left road1 id+12
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:20
            indexes.append((20, 19))
            directions.append("Forward")
            successors.append((6, 12))
            predecessors.append((12, 6))
            successors.append((1, 12))
            predecessors.append((12, 1))
            alignment.append(["Forward", "Forward"])

            # left road2 id+13
            lane7 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:21
            indexes.append((21, 20))
            directions.append("Forward")
            successors.append((5, 13))
            predecessors.append((13, 5))
            alignment.append(["Backward", "Forward"])

            # left road3 id+14
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((21, 22))
            directions.append("Forward")
            successors.append((14, 4))
            predecessors.append((4, 14))
            predecessors.append((3, 14))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向双车道转双向四车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            ，变上右转
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": self.Start,
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # '左下转'
            }
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # straight4
            dict8 = {
                "ID": self.StartLaneID + 7,
                "Start": edgelist[3][1],
                "End": edgelist[3][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 11,  
                "BoundaryId2": self.StartBoundaryID + 12,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight4 = StraightLaneConnection(dict8)
            tmpBoundarys2 = []
            tmpBoundarys2.append(tmpStraight3.boundaryPoints[1])
            tmpBoundarys2.append(tmpStraight4.boundaryPoints[1])
            tmpStraight4.setBoundaryPoints(tmpBoundarys2)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append("Forward")
            indexes.append((11, 12))
            laneObjects.append(tmpStraight4)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction id：startLaneID+8 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:14
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((2, 8))
            predecessors.append((8, 2))
            successors.append((3, 8))
            predecessors.append((8, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+9
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 0))
            predecessors.append((0, 9))
            predecessors.append((1, 9))
            alignment.append(["Backward", "Forward"])

            # right road1 id +10 to right
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:16
            boundarylist.append(boundary5)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((0, 10))
            predecessors.append((10, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +11 to right
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:18
            indexes.append((18, 16))
            directions.append("Forward")
            successors.append((5, 11))
            predecessors.append((11, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+12 to left
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)  # reuse id:19
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((12, 6))
            predecessors.append((6, 12))
            predecessors.append((2, 12))
            alignment.append(["Backward", "Forward"])

            # right road4 id+13 to left
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    edgelist[3][1][1],
                ),
                (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                edgelist[3][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[3][1][0] + self.Width / 4,
                    edgelist[3][1][1] + self.Width / 2,
                ),
                (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((13, 7))
            predecessors.append((7, 13))
            alignment.append(["Forward", "Forward"])

            # left road1 id+14 to left
            lane7 = [
                edgelist[3][0],
                (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    edgelist[3][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary9 = [
                (edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)),
                ),
            ]
            boundary10 = [
                (edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary9)
            boundarylist.append(boundary10)  # reuse,id:22
            indexes.append((22, 21))
            directions.append("Forward")
            successors.append((7, 14))
            predecessors.append((14, 7))
            alignment.append(["Forward", "Forward"])

            # left road2 id+15 to left
            lane8 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:23
            indexes.append((23, 22))
            directions.append("Forward")
            successors.append((6, 15))
            predecessors.append((15, 6))
            successors.append((1, 15))
            predecessors.append((15, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+16 to right
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)  # reuse id:24
            indexes.append((23, 24))
            directions.append("Forward")
            successors.append((16, 5))
            predecessors.append((5, 16))
            alignment.append(["Forward", "Forward"])

            # left road4 id+17 to right
            lane10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane10)
            boundary13 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary13)
            indexes.append((24, 25))
            directions.append("Forward")
            successors.append((17, 4))
            predecessors.append((3, 17))
            predecessors.append((4, 17))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向三车道一转双向双车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,  # reuse id:0
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            ，变成下右转
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[1][0],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "下右转",  # '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lane = list(reversed(tmpArc2.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc2.boundaryPoints[0]))
            right = list(reversed(tmpArc2.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[1][1],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 0,
                "BoundaryId2": self.StartBoundaryID + 4,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            lanelist.append(tmpArc3.lanePoints)
            # boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            tmpArc3.boundaryPoints[0] = tmpArc1.boundaryPoints[0]
            directions.append(tmpArc3.TravelDirection)
            indexes.append((0, 4))
            laneObjects.append(tmpArc3)
            alignment.append(("Backward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 5,
                "BoundaryId2": self.StartBoundaryID + 6,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((5, 6))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 7,  
                "BoundaryId2": self.StartBoundaryID + 8,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((7, 8))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 7,  # reuse
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((7, 9))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+6 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:11
            indexes.append((11, 10))
            directions.append("Forward")
            successors.append((3, 6))
            predecessors.append((6, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+7  to down
            lane2 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary3)
            indexes.append((12, 11))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to up
            lane3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary4)
            indexes.append((12, 13))
            directions.append("Forward")
            successors.append((8, 0))
            predecessors.append((0, 8))
            predecessors.append((1, 8))
            alignment.append(["Backward", "Forward"])

            # right road1，id+9
            lane4 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary6 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary5)  # reuse id:14
            boundarylist.append(boundary6)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((4, 9))
            predecessors.append((9, 4))
            successors.append((0, 9))
            predecessors.append((9, 0))
            alignment.append(["Forward", "Forward"])

            # right road2，id+10
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane5)
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary7)  
            indexes.append((14, 16))
            directions.append("Forward")
            successors.append((10, 5))
            predecessors.append((5, 10))
            predecessors.append((2, 10))
            alignment.append(["Backward", "Forward"])

            # left road1，id+11
            lane6 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:18
            indexes.append((18, 17))
            directions.append("Forward")
            successors.append((5, 11))
            predecessors.append((11, 5))
            successors.append((1, 11))
            predecessors.append((11, 1))
            alignment.append(["Backward", "Forward"])

            # left road2，id+12
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((12, 4))
            predecessors.append((4, 12))
            predecessors.append((3, 12))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向三车道一转双向三车道一":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+7 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((2, 8))
            predecessors.append((8, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+9  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 0))
            predecessors.append((0, 9))
            predecessors.append((1, 9))
            alignment.append(["Backward", "Forward"])

            # right road1 id +10
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:16
            boundarylist.append(boundary5)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((0, 10))
            predecessors.append((10, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +11
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:18
            indexes.append((18, 16))
            directions.append("Forward")
            successors.append((5, 11))
            predecessors.append((11, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+12
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((12, 6))
            predecessors.append((6, 12))
            predecessors.append((2, 12))
            alignment.append(["Backward", "Forward"])

            # left road1 id+13
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:21
            indexes.append((21, 20))
            directions.append("Forward")
            successors.append((6, 13))
            predecessors.append((13, 6))
            successors.append((1, 13))
            predecessors.append((13, 1))
            alignment.append(["Backward", "Forward"])

            # left road2 id+14
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:22
            indexes.append((21, 22))
            directions.append("Forward")
            successors.append((14, 5))
            predecessors.append((5, 14))
            alignment.append(["Forward", "Forward"])

            # left road3 id+15
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((22, 23))
            directions.append("Forward")
            successors.append((15, 4))
            predecessors.append((4, 15))
            predecessors.append((3, 15))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向三车道一转双向三车道二":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,
                "BoundaryId2": self.StartBoundaryID + 10,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((8, 10))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[1])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+7 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((2, 8))
            predecessors.append((8, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+9  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 0))
            predecessors.append((0, 9))
            predecessors.append((1, 9))
            alignment.append(["Backward", "Forward"])

            # right road1 id +10
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:16
            boundarylist.append(boundary5)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((0, 10))
            predecessors.append((10, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +11
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary6)  # reuse id:18
            indexes.append((16, 18))
            directions.append("Forward")
            successors.append((11, 5))
            predecessors.append((5, 11))
            alignment.append(["Backward", "Forward"])

            # right road3 id+12
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((12, 6))
            predecessors.append((6, 12))
            predecessors.append((2, 12))
            alignment.append(["Forward", "Forward"])

            # left road1 id+13
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:21
            indexes.append((21, 20))
            directions.append("Forward")
            successors.append((6, 13))
            predecessors.append((13, 6))
            successors.append((1, 13))
            predecessors.append((13, 1))
            alignment.append(["Forward", "Forward"])

            # left road2 id+14
            lane7 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:22
            indexes.append((22, 21))
            directions.append("Forward")
            successors.append((5, 14))
            predecessors.append((14, 5))
            alignment.append(["Backward", "Forward"])

            # left road3 id+15
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((22, 23))
            directions.append("Forward")
            successors.append((15, 4))
            predecessors.append((4, 15))
            predecessors.append((3, 15))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向三车道一转双向四车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # straight4
            dict8 = {
                "ID": self.StartLaneID + 7,
                "Start": edgelist[3][1],
                "End": edgelist[3][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 11,  
                "BoundaryId2": self.StartBoundaryID + 12,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight4 = StraightLaneConnection(dict8)
            tmpBoundarys2 = []
            tmpBoundarys2.append(tmpStraight3.boundaryPoints[1])
            tmpBoundarys2.append(tmpStraight4.boundaryPoints[1])
            tmpStraight4.setBoundaryPoints(tmpBoundarys2)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append("Forward")
            indexes.append((11, 12))
            laneObjects.append(tmpStraight4)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+8 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:14
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((3, 8))
            predecessors.append((8, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+9  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((15, 14))
            directions.append("Forward")
            successors.append((2, 9))
            predecessors.append((9, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+10  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((10, 0))
            predecessors.append((0, 10))
            predecessors.append((1, 10))
            alignment.append(["Backward", "Forward"])

            # right road1 id +11 to right
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:17
            boundarylist.append(boundary5)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((4, 11))
            predecessors.append((11, 4))
            successors.append((0, 11))
            predecessors.append((11, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +12 to right
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:19
            indexes.append((19, 17))
            directions.append("Forward")
            successors.append((5, 12))
            predecessors.append((12, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+13 to left
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)  # reuse id:20
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((13, 6))
            predecessors.append((6, 13))
            predecessors.append((2, 13))
            alignment.append(["Backward", "Forward"])

            # right road4 id+14 to left
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    edgelist[3][1][1],
                ),
                (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                edgelist[3][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[3][1][0] + self.Width / 4,
                    edgelist[3][1][1] + self.Width / 2,
                ),
                (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)
            indexes.append((20, 21))
            directions.append("Forward")
            successors.append((14, 7))
            predecessors.append((7, 14))
            alignment.append(["Forward", "Forward"])

            # left road1 id+15 to left
            lane7 = [
                edgelist[3][0],
                (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    edgelist[3][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary9 = [
                (edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)),
                ),
            ]
            boundary10 = [
                (edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary9)
            boundarylist.append(boundary10)  # reuse,id:23
            indexes.append((23, 22))
            directions.append("Forward")
            successors.append((7, 15))
            predecessors.append((15, 7))
            alignment.append(["Forward", "Forward"])

            # left road2 id+16 to left
            lane8 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:24
            indexes.append((24, 23))
            directions.append("Forward")
            successors.append((6, 16))
            predecessors.append((16, 6))
            successors.append((1, 16))
            predecessors.append((16, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+17 to right
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)  # reuse id:25
            indexes.append((24, 25))
            directions.append("Forward")
            successors.append((17, 5))
            predecessors.append((5, 17))
            alignment.append(["Forward", "Forward"])

            # left road4 id+18 to right
            lane10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane10)
            boundary13 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary13)
            indexes.append((25, 26))
            directions.append("Forward")
            successors.append((18, 4))
            predecessors.append((3, 18))
            predecessors.append((4, 18))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向三车道二转双向双车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,  # reuse id:0
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            ，变成下右转
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[1][0],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",  # '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lane = list(reversed(tmpArc2.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc2.boundaryPoints[0]))
            right = list(reversed(tmpArc2.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[1][1],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            # lane=list(reversed(tmpArc3.lanePoints))
            lanelist.append(tmpArc3.lanePoints)
            # left=list(reversed(tmpArc3.boundaryPoints[0]))
            # right=list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2(统一左至右，设置道路方向)
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  # reuse
                "BoundaryId2": self.StartBoundaryID + 10,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((8, 10))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+6 to down
            lane1 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane1)
            boundary1 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary2 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary1)
            boundarylist.append(boundary2)  # reuse id:12
            indexes.append((12, 11))
            directions.append("Forward")
            successors.append((3, 6))
            predecessors.append((6, 3))
            successors.append((2, 6))
            predecessors.append((6, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+7  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((12, 13))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction3 id：+8  to up
            lane3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary4)
            indexes.append((13, 14))
            directions.append("Forward")
            successors.append((8, 0))
            predecessors.append((0, 8))
            predecessors.append((1, 8))
            alignment.append(["Forward", "Forward"])

            # right road1，id+9
            lane4 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary6 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary5)  # reuse id:15
            boundarylist.append(boundary6)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((4, 9))
            predecessors.append((9, 4))
            successors.append((0, 9))
            predecessors.append((9, 0))
            alignment.append(["Forward", "Forward"])

            # right road2，id+10
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane5)
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary7)  
            indexes.append((15, 17))
            directions.append("Forward")
            successors.append((10, 5))
            predecessors.append((5, 10))
            predecessors.append((2, 10))
            alignment.append(["Backward", "Forward"])

            # left road1，id+11
            lane6 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:19
            indexes.append((19, 18))
            directions.append("Forward")
            successors.append((5, 11))
            predecessors.append((11, 5))
            successors.append((1, 11))
            predecessors.append((11, 1))
            alignment.append(["Backward", "Forward"])

            # left road2，id+12
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((12, 4))
            predecessors.append((4, 12))
            predecessors.append((3, 12))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向三车道二转双向三车道一":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": self.Start,
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+7 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            successors.append((2, 7))
            predecessors.append((7, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to up
            lane1 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary2)
            indexes.append((13, 14))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction2 id：+9  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 0))
            predecessors.append((0, 9))
            predecessors.append((1, 9))
            alignment.append(["Forward", "Forward"])

            # right road1 id +10
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:16
            boundarylist.append(boundary5)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((0, 10))
            predecessors.append((10, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +11
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:18
            indexes.append((18, 16))
            directions.append("Forward")
            successors.append((5, 11))
            predecessors.append((11, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+12
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((12, 6))
            predecessors.append((6, 12))
            predecessors.append((2, 12))
            alignment.append(["Backward", "Forward"])

            # left road1 id+13
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1] + self.Width / 2,
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:21
            indexes.append((21, 20))
            directions.append("Forward")
            successors.append((6, 13))
            predecessors.append((13, 6))
            successors.append((1, 13))
            predecessors.append((13, 1))
            alignment.append(["Backward", "Forward"])

            # left road2 id+14
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:22
            indexes.append((21, 22))
            directions.append("Forward")
            successors.append((14, 5))
            predecessors.append((5, 14))
            alignment.append(["Forward", "Forward"])

            # left road3 id+15
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((22, 23))
            directions.append("Forward")
            successors.append((15, 4))
            predecessors.append((4, 15))
            predecessors.append((3, 15))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向三车道二转双向三车道二":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": self.Start,
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,
                "BoundaryId2": self.StartBoundaryID + 10,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((8, 10))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[1])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+7 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            successors.append((2, 7))
            predecessors.append((7, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to up
            lane1 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane1)
            boundary3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((13, 14))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction2 id：+9  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 0))
            predecessors.append((0, 9))
            predecessors.append((1, 9))
            alignment.append(["Forward", "Forward"])

            # right road1 id +10
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:16
            boundarylist.append(boundary5)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((0, 10))
            predecessors.append((10, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +11
            lane4 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane4)
            boundary6 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary6)  # reuse id:18
            indexes.append((16, 18))
            directions.append("Forward")
            successors.append((11, 5))
            predecessors.append((5, 11))
            alignment.append(["Backward", "Forward"])

            # right road3 id+12
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((12, 6))
            predecessors.append((6, 12))
            predecessors.append((2, 12))
            alignment.append(["Forward", "Forward"])

            # left road1 id+13
            lane6 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:21
            indexes.append((21, 20))
            directions.append("Forward")
            successors.append((6, 13))
            predecessors.append((13, 6))
            successors.append((1, 13))
            predecessors.append((13, 1))
            alignment.append(["Forward", "Forward"])

            # left road2 id+14
            lane7 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  # reuse id:22
            indexes.append((22, 21))
            directions.append("Forward")
            successors.append((5, 14))
            predecessors.append((14, 5))
            alignment.append(["Backward", "Forward"])

            # left road3 id+15
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)
            indexes.append((22, 23))
            directions.append("Forward")
            successors.append((15, 4))
            predecessors.append((4, 15))
            predecessors.append((3, 15))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向三车道二转双向四车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "-0",
                "Flag": "上左转",
            }
            tmpArc2 = ArcLane(dict2)
            lanelist.append(tmpArc2.lanePoints)
            boundarylist.append(tmpArc2.boundaryPoints[0])
            boundarylist.append(tmpArc2.boundaryPoints[1])
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1

            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": self.Start,
                "End": edgelist[2][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",  # 下左转
            }
            # print("start",self.Start)
            tmpArc3 = ArcLane(dict3)
            lane = list(reversed(tmpArc3.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc3.boundaryPoints[0]))
            right = list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # straight4
            dict8 = {
                "ID": self.StartLaneID + 7,
                "Start": edgelist[3][1],
                "End": edgelist[3][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 11,  
                "BoundaryId2": self.StartBoundaryID + 12,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight4 = StraightLaneConnection(dict8)
            tmpBoundarys2 = []
            tmpBoundarys2.append(tmpStraight3.boundaryPoints[1])
            tmpBoundarys2.append(tmpStraight4.boundaryPoints[1])
            tmpStraight4.setBoundaryPoints(tmpBoundarys2)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append("Forward")
            indexes.append((11, 12))
            laneObjects.append(tmpStraight4)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+8 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:14
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((3, 8))
            predecessors.append((8, 3))
            successors.append((2, 8))
            predecessors.append((8, 2))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+9  to up
            lane1 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width, self.Start[1]),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
            ]
            boundarylist.append(boundary2)
            indexes.append((14, 15))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction2 id：+10  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((10, 0))
            predecessors.append((0, 10))
            predecessors.append((1, 10))
            alignment.append(["Forward", "Forward"])

            # right road1 id +11 to right
            lane3 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary4)  # reuse id:17
            boundarylist.append(boundary5)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((4, 11))
            predecessors.append((11, 4))
            successors.append((0, 11))
            predecessors.append((11, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +12 to right
            lane4 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary6 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary6)  # reuse id:19
            indexes.append((19, 17))
            directions.append("Forward")
            successors.append((5, 12))
            predecessors.append((12, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+13 to left
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane5)
            boundarylist.append(boundary7)  # reuse id:20
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((13, 6))
            predecessors.append((6, 13))
            predecessors.append((2, 13))
            alignment.append(["Backward", "Forward"])

            # right road4 id+14 to left
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    edgelist[3][1][1],
                ),
                (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                edgelist[3][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[3][1][0] + self.Width / 4,
                    edgelist[3][1][1] + self.Width / 2,
                ),
                (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)
            indexes.append((20, 21))
            directions.append("Forward")
            successors.append((14, 7))
            predecessors.append((7, 14))
            alignment.append(["Forward", "Forward"])

            # left road1 id+15 to left
            lane7 = [
                edgelist[3][0],
                (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    edgelist[3][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary9 = [
                (edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)),
                ),
            ]
            boundary10 = [
                (edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary9)
            boundarylist.append(boundary10)  # reuse,id:23
            indexes.append((23, 22))
            directions.append("Forward")
            successors.append((7, 15))
            predecessors.append((15, 7))
            alignment.append(["Forward", "Forward"])

            # left road2 id+16 to left
            lane8 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:24
            indexes.append((24, 23))
            directions.append("Forward")
            successors.append((6, 16))
            predecessors.append((16, 6))
            successors.append((1, 16))
            predecessors.append((16, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+17 to right
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)  # reuse id:25
            indexes.append((24, 25))
            directions.append("Forward")
            successors.append((17, 5))
            predecessors.append((5, 17))
            alignment.append(["Forward", "Forward"])

            # left road4 id+18 to right
            lane10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane10)
            boundary13 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary13)
            indexes.append((25, 26))
            directions.append("Forward")
            successors.append((18, 4))
            predecessors.append((3, 18))
            predecessors.append((4, 18))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向四车道转双向双车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[1][0],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "下右转",  # '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lane = list(reversed(tmpArc2.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc2.boundaryPoints[0]))
            right = list(reversed(tmpArc2.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[1][1],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            # lane=list(reversed(tmpArc3.lanePoints))
            lanelist.append(tmpArc3.lanePoints)
            # left=list(reversed(tmpArc3.boundaryPoints[0]))
            # right=list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  # reuse
                "BoundaryId2": self.StartBoundaryID + 10,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((8, 10))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+6 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:12
            indexes.append((12, 11))
            directions.append("Forward")
            successors.append((3, 6))
            predecessors.append((6, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+7  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((2, 7))
            predecessors.append((7, 2))
            alignment.append(["Forward", "Forward"])

            # major direction3 id：+8  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((13, 14))
            successors.append((8, 1))
            predecessors.append((1, 8))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction4 id：+9  to up
            lane3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 3, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 3, self.Start[1]),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 3)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 3,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1]),
            ]
            boundarylist.append(boundary4)
            indexes.append((14, 15))
            directions.append("Forward")
            successors.append((9, 0))
            predecessors.append((0, 9))
            alignment.append(["Forward", "Forward"])

            # right road1，id+10
            lane4 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary6 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary5)  # reuse id:16
            boundarylist.append(boundary6)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((4, 10))
            predecessors.append((10, 4))
            successors.append((0, 10))
            predecessors.append((10, 0))
            alignment.append(["Forward", "Forward"])

            # right road2，id+11
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane5)
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary7)  
            indexes.append((16, 18))
            directions.append("Forward")
            successors.append((11, 5))
            predecessors.append((5, 11))
            predecessors.append((2, 11))
            alignment.append(["Backward", "Forward"])

            # left road1，id+12
            lane6 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane6)
            boundary8 = [
                (edgelist[1][0][0], edgelist[1][0][1] + self.Width / 2),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] + self.Width / 2)),
                ),
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary8)
            boundarylist.append(boundary9)  # reuse,id:20
            indexes.append((20, 19))
            directions.append("Forward")
            successors.append((5, 12))
            predecessors.append((12, 5))
            successors.append((1, 12))
            predecessors.append((12, 1))
            alignment.append(["Backward", "Forward"])

            # left road2，id+13
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane7)
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary10)  
            indexes.append((20, 21))
            directions.append("Forward")
            successors.append((13, 4))
            predecessors.append((4, 13))
            predecessors.append((3, 13))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

        if flag == "双向四车道转双向三车道一":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[2][0],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "下右转",  # '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lane = list(reversed(tmpArc2.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc2.boundaryPoints[0]))
            right = list(reversed(tmpArc2.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[2][1],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            # lane=list(reversed(tmpArc3.lanePoints))
            lanelist.append(tmpArc3.lanePoints)
            # left=list(reversed(tmpArc3.boundaryPoints[0]))
            # right=list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+7 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((2, 8))
            predecessors.append((8, 2))
            alignment.append(["Forward", "Forward"])

            # major direction3 id：+9  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            successors.append((9, 1))
            predecessors.append((1, 9))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction4 id：+10  to up
            lane3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 3, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 3, self.Start[1]),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 3)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 3,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1]),
            ]
            boundarylist.append(boundary4)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((10, 0))
            predecessors.append((0, 10))
            alignment.append(["Forward", "Forward"])

            # right road1 id +11
            lane4 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary6 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary5)  # reuse id:17
            boundarylist.append(boundary6)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((4, 11))
            predecessors.append((11, 4))
            successors.append((0, 11))
            predecessors.append((11, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +12
            lane5 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane5)
            boundary7 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary7)  # reuse id:19
            indexes.append((19, 17))
            directions.append("Forward")
            successors.append((5, 12))
            predecessors.append((12, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+13
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((13, 6))
            predecessors.append((6, 13))
            predecessors.append((2, 13))
            alignment.append(["Backward", "Forward"])

            # left road1 id+14
            lane7 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary9 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary10 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary9)
            boundarylist.append(boundary10)  # reuse,id:22
            indexes.append((22, 21))
            directions.append("Forward")
            successors.append((6, 14))
            predecessors.append((14, 6))
            successors.append((1, 14))
            predecessors.append((14, 1))
            alignment.append(["Backward", "Forward"])

            # left road2 id+15
            lane8 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:23
            indexes.append((22, 23))
            directions.append("Forward")
            successors.append((15, 5))
            predecessors.append((5, 15))
            alignment.append(["Forward", "Forward"])

            # left road3 id+16
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)
            indexes.append((23, 24))
            directions.append("Forward")
            successors.append((16, 4))
            predecessors.append((4, 16))
            predecessors.append((3, 16))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向四车道转双向三车道二":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[2][0],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "下右转",  # '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lane = list(reversed(tmpArc2.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc2.boundaryPoints[0]))
            right = list(reversed(tmpArc2.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[2][1],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            # lane=list(reversed(tmpArc3.lanePoints))
            lanelist.append(tmpArc3.lanePoints)
            # left=list(reversed(tmpArc3.boundaryPoints[0]))
            # right=list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][1],
                "End": edgelist[1][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,
                "BoundaryId2": self.StartBoundaryID + 10,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight2.boundaryPoints[1])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[1])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((8, 10))
            laneObjects.append(tmpStraight2)
            alignment.append(["Backward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[1])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+7 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:13
            indexes.append((13, 12))
            directions.append("Forward")
            successors.append((3, 7))
            predecessors.append((7, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+8  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((2, 8))
            predecessors.append((8, 2))
            alignment.append(["Forward", "Forward"])

            # major direction3 id：+9  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((14, 15))
            successors.append((9, 1))
            predecessors.append((1, 9))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction4 id：+10  to up
            lane3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 3, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 3, self.Start[1]),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 3)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 3,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1]),
            ]
            boundarylist.append(boundary4)
            indexes.append((15, 16))
            directions.append("Forward")
            successors.append((10, 0))
            predecessors.append((0, 10))
            alignment.append(["Forward", "Forward"])

            # right road1 id +11
            lane4 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary6 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary5)  # reuse id:17
            boundarylist.append(boundary6)
            indexes.append((17, 18))
            directions.append("Forward")
            successors.append((4, 11))
            predecessors.append((11, 4))
            successors.append((0, 11))
            predecessors.append((11, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +12
            lane5 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                edgelist[1][1],
            ]
            lanelist.append(lane5)
            boundary7 = [
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
            ]
            boundarylist.append(boundary7)  # reuse id:19
            indexes.append((17, 19))
            directions.append("Forward")
            successors.append((12, 5))
            predecessors.append((5, 12))
            alignment.append(["Backward", "Forward"])

            # right road3 id+13
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)
            indexes.append((19, 20))
            directions.append("Forward")
            successors.append((13, 6))
            predecessors.append((6, 13))
            predecessors.append((2, 13))
            alignment.append(["Forward", "Forward"])

            # left road1 id+14
            lane7 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane7)
            boundary9 = [
                (edgelist[2][0][0], edgelist[2][0][1] + self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] + self.Width / 2)),
                ),
            ]
            boundary10 = [
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary9)
            boundarylist.append(boundary10)  # reuse,id:22
            indexes.append((22, 21))
            directions.append("Forward")
            successors.append((6, 14))
            predecessors.append((14, 6))
            successors.append((1, 14))
            predecessors.append((14, 1))
            alignment.append(["Forward", "Forward"])

            # left road2 id+15
            lane8 = [
                edgelist[1][0],
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
            ]
            lanelist.append(lane8)
            boundary11 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary11)  # reuse id:23
            indexes.append((23, 22))
            directions.append("Forward")
            successors.append((5, 15))
            predecessors.append((15, 5))
            alignment.append(["Backward", "Forward"])

            # left road3 id+16
            lane9 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)
            indexes.append((23, 24))
            directions.append("Forward")
            successors.append((16, 4))
            predecessors.append((4, 16))
            predecessors.append((3, 16))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            # laneInfolist.append(laneObjects)
            return laneInfolist

        if flag == "双向四车道转双向四车道":
            # turn right
            dict1 = {
                "ID": self.StartLaneID,
                "Start": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    self.Start[1],
                ),
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID,
                "BoundaryId2": self.StartBoundaryID + 1,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+",
                "k1": "+0",
                "Flag": "上右转",
            }
            tmpArc1 = ArcLane(dict1)
            lanelist.append(tmpArc1.lanePoints)
            boundarylist.append(tmpArc1.boundaryPoints[0])
            boundarylist.append(tmpArc1.boundaryPoints[1])
            directions.append(tmpArc1.TravelDirection)
            indexes.append((0, 1))
            laneObjects.append(tmpArc1)
            
            alignment.append(["Forward", "Forward"])

            # turn left
            
            dict2 = {
                "ID": self.StartLaneID + 1,
                "Start": edgelist[2][0],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 2,
                "BoundaryId2": self.StartBoundaryID + 3,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "下右转",  # '上左转'
            }
            tmpArc2 = ArcLane(dict2)
            lane = list(reversed(tmpArc2.lanePoints))
            lanelist.append(lane)
            left = list(reversed(tmpArc2.boundaryPoints[0]))
            right = list(reversed(tmpArc2.boundaryPoints[1]))
            boundarylist.append(right)
            boundarylist.append(left)
            directions.append(tmpArc2.TravelDirection)
            indexes.append((2, 3))
            laneObjects.append(tmpArc2)
            alignment.append(["Forward", "Forward"])

            # turn left1
            dict3 = {
                "ID": self.StartLaneID + 2,
                "Start": edgelist[2][1],
                "End": (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    self.Start[1],
                ),
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 4,
                "BoundaryId2": self.StartBoundaryID + 5,
                "Direction": 1,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-",
                "Flag": "左下转",
            }
            tmpArc3 = ArcLane(dict3)
            # lane=list(reversed(tmpArc3.lanePoints))
            lanelist.append(tmpArc3.lanePoints)
            # left=list(reversed(tmpArc3.boundaryPoints[0]))
            # right=list(reversed(tmpArc3.boundaryPoints[1]))
            boundarylist.append(tmpArc3.boundaryPoints[0])
            boundarylist.append(tmpArc3.boundaryPoints[1])
            directions.append(tmpArc3.TravelDirection)
            indexes.append((4, 5))
            laneObjects.append(tmpArc3)
            alignment.append(("Forward", "Forward"))

            # turn right1
            dict4 = {
                "ID": self.StartLaneID + 3,
                "Start": edgelist[0][0],
                "End": self.Start,
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 6,
                "BoundaryId2": self.StartBoundaryID + 7,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "-",
                "Flag": "右下转",
            }
            tmpArc4 = ArcLane(dict4)
            lanelist.append(tmpArc4.lanePoints)
            boundarylist.append(tmpArc4.boundaryPoints[0])
            boundarylist.append(tmpArc4.boundaryPoints[1])
            directions.append(tmpArc4.TravelDirection)
            indexes.append((6, 7))
            laneObjects.append(tmpArc4)
            alignment.append(("Forward", "Forward"))

            # straight1
            dict5 = {
                "ID": self.StartLaneID + 4,
                "Start": edgelist[0][0],
                "End": edgelist[0][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 8,  
                "BoundaryId2": self.StartBoundaryID + 9,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight1 = StraightLaneConnection(dict5)
            lanelist.append(tmpStraight1.lanePoints)
            boundarylist.append(tmpStraight1.boundaryPoints[0])
            boundarylist.append(tmpStraight1.boundaryPoints[1])
            directions.append(tmpStraight1.TravelDirection)
            indexes.append((8, 9))
            laneObjects.append(tmpStraight1)
            alignment.append(["Forward", "Forward"])

            # straight2
            dict6 = {
                "ID": self.StartLaneID + 5,
                "Start": edgelist[1][0],
                "End": edgelist[1][1],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,
                "BoundaryId2": self.StartBoundaryID + 8,  
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "+0",
                "k1": "+0",
                "Flag": "左至右",
            }
            tmpStraight2 = StraightLaneConnection(dict6)
            tmpBoundarys = []
            tmpBoundarys.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys.append(tmpStraight1.boundaryPoints[0])
            tmpStraight2.setBoundaryPoints(tmpBoundarys)
            lanelist.append(tmpStraight2.lanePoints)
            
            boundarylist.append(tmpStraight2.boundaryPoints[0])
            directions.append(tmpStraight2.TravelDirection)
            indexes.append((10, 8))
            laneObjects.append(tmpStraight2)
            alignment.append(["Forward", "Forward"])

            # straight3
            dict7 = {
                "ID": self.StartLaneID + 6,
                "Start": edgelist[2][1],
                "End": edgelist[2][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 10,  
                "BoundaryId2": self.StartBoundaryID + 11,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight3 = StraightLaneConnection(dict7)
            tmpBoundarys1 = []
            tmpBoundarys1.append(tmpStraight2.boundaryPoints[0])
            tmpBoundarys1.append(tmpStraight3.boundaryPoints[1])
            tmpStraight3.setBoundaryPoints(tmpBoundarys1)
            lanelist.append(tmpStraight3.lanePoints)
            
            boundarylist.append(tmpStraight3.boundaryPoints[1])
            directions.append(tmpStraight3.TravelDirection)
            indexes.append((10, 11))
            laneObjects.append(tmpStraight3)
            alignment.append(["Backward", "Forward"])

            # straight4
            dict8 = {
                "ID": self.StartLaneID + 7,
                "Start": edgelist[3][1],
                "End": edgelist[3][0],
                "Width": self.Width,
                "BoundaryId1": self.StartBoundaryID + 11,  
                "BoundaryId2": self.StartBoundaryID + 12,
                "Direction": 0,
                "TravelDirection": "Forward",
                "LaneAssetType": {"Boundary1": "SW", "Boundary2": "SW"},
                "LaneType": "Driving",
                "k": "-0",
                "k1": "-0",
                "Flag": "右至左",
            }
            tmpStraight4 = StraightLaneConnection(dict8)
            tmpBoundarys2 = []
            tmpBoundarys2.append(tmpStraight3.boundaryPoints[1])
            tmpBoundarys2.append(tmpStraight4.boundaryPoints[1])
            tmpStraight4.setBoundaryPoints(tmpBoundarys2)
            lanelist.append(tmpStraight4.lanePoints)
            
            boundarylist.append(tmpStraight4.boundaryPoints[1])
            directions.append("Forward")
            indexes.append((11, 12))
            laneObjects.append(tmpStraight4)
            alignment.append(["Forward", "Forward"])

            # ourter road
            # major direction1 id：startLaneID+8 to down
            lane0 = [
                self.Start,
                (self.Start[0], self.Start[1] - self.Width / 4),
                (self.Start[0], float("{:.3f}".format(self.Start[1] - self.Width / 2))),
            ]
            lanelist.append(lane0)
            boundary0 = [
                (self.Start[0] - self.Width / 2, self.Start[1]),
                (self.Start[0] - self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] - self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundary1 = [
                (self.Start[0] + self.Width / 2, self.Start[1]),
                (self.Start[0] + self.Width / 2, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary0)
            boundarylist.append(boundary1)  # reuse id:14
            indexes.append((14, 13))
            directions.append("Forward")
            successors.append((3, 8))
            predecessors.append((8, 3))
            alignment.append(["Forward", "Forward"])

            # major direction2 id：+9  to down
            lane1 = [
                (self.Start[0] + self.Width, self.Start[1]),
                (self.Start[0] + self.Width, self.Start[1] - self.Width / 4),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            lanelist.append(lane1)
            boundary2 = [
                (self.Start[0] + self.Width / 2 + self.Width, self.Start[1]),
                (
                    self.Start[0] + self.Width / 2 + self.Width,
                    self.Start[1] - self.Width / 4,
                ),
                (
                    float("{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary2)
            indexes.append((15, 14))
            directions.append("Forward")
            successors.append((2, 9))
            predecessors.append((9, 2))
            alignment.append(["Forward", "Forward"])

            # major direction3 id：+10  to up
            lane2 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 2)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 2, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 2, self.Start[1]),
            ]
            lanelist.append(lane2)
            boundary3 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 2)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 2,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 2, self.Start[1]),
            ]
            boundarylist.append(boundary3)
            indexes.append((15, 16))
            successors.append((10, 1))
            predecessors.append((1, 10))
            directions.append("Forward")
            alignment.append(["Backward", "Forward"])

            # major direction4 id：+11  to up
            lane3 = [
                (
                    float("{:.3f}".format(self.Start[0] + self.Width * 3)),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (self.Start[0] + self.Width * 3, self.Start[1] - self.Width / 4),
                (self.Start[0] + self.Width * 3, self.Start[1]),
            ]
            lanelist.append(lane3)
            boundary4 = [
                (
                    float(
                        "{:.3f}".format(self.Start[0] + self.Width / 2 + self.Width * 3)
                    ),
                    float("{:.3f}".format(self.Start[1] - self.Width / 2)),
                ),
                (
                    self.Start[0] + self.Width / 2 + self.Width * 3,
                    self.Start[1] - self.Width / 4,
                ),
                (self.Start[0] + self.Width / 2 + self.Width * 3, self.Start[1]),
            ]
            boundarylist.append(boundary4)
            indexes.append((16, 17))
            directions.append("Forward")
            successors.append((11, 0))
            predecessors.append((0, 11))
            alignment.append(["Forward", "Forward"])

            # right road1 id +12 to right
            lane4 = [
                edgelist[0][1],
                (edgelist[0][1][0] + self.Width / 4, edgelist[0][1][1]),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    edgelist[0][1][1],
                ),
            ]
            lanelist.append(lane4)
            boundary5 = [
                (edgelist[0][1][0], edgelist[0][1][1] + self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] + self.Width / 2)),
                ),
            ]
            boundary6 = [
                (edgelist[0][1][0], edgelist[0][1][1] - self.Width / 2),
                (
                    edgelist[0][1][0] + self.Width / 4,
                    edgelist[0][1][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[0][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][1][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary5)  # reuse id:18
            boundarylist.append(boundary6)
            indexes.append((18, 19))
            directions.append("Forward")
            successors.append((4, 12))
            predecessors.append((12, 4))
            successors.append((0, 12))
            predecessors.append((12, 0))
            alignment.append(["Forward", "Forward"])

            # right road2 id +13 to right
            lane5 = [
                edgelist[1][1],
                (edgelist[1][1][0] + self.Width / 4, edgelist[1][1][1]),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    edgelist[1][1][1],
                ),
            ]
            lanelist.append(lane5)
            boundary7 = [
                (edgelist[1][1][0], edgelist[1][1][1] + self.Width / 2),
                (
                    edgelist[1][1][0] + self.Width / 4,
                    edgelist[1][1][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[1][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][1][1] + self.Width / 2)),
                ),
            ]
            # boundary4=[(edgelist[0][1][0],edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/4,edgelist[0][1][1]-self.Width/2),(edgelist[0][1][0]+self.Width/2,edgelist[0][1][1]-self.Width/2)]
            boundarylist.append(boundary7)  # reuse id:20
            indexes.append((20, 18))
            directions.append("Forward")
            successors.append((5, 13))
            predecessors.append((13, 5))
            alignment.append(["Forward", "Forward"])

            # right road3 id+14 to left
            lane6 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    edgelist[2][1][1],
                ),
                (edgelist[2][1][0] + self.Width / 4, edgelist[2][1][1]),
                edgelist[2][1],
            ]
            boundary8 = [
                (
                    float("{:.3f}".format(edgelist[2][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[2][1][0] + self.Width / 4,
                    edgelist[2][1][1] + self.Width / 2,
                ),
                (edgelist[2][1][0], edgelist[2][1][1] + self.Width / 2),
            ]
            lanelist.append(lane6)
            boundarylist.append(boundary8)  # reuse id:21
            indexes.append((20, 21))
            directions.append("Forward")
            successors.append((14, 6))
            predecessors.append((6, 14))
            predecessors.append((2, 14))
            alignment.append(["Backward", "Forward"])

            # right road4 id+15 to left
            lane7 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    edgelist[3][1][1],
                ),
                (edgelist[3][1][0] + self.Width / 4, edgelist[3][1][1]),
                edgelist[3][1],
            ]
            boundary9 = [
                (
                    float("{:.3f}".format(edgelist[3][1][0] + self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][1][1] + self.Width / 2)),
                ),
                (
                    edgelist[3][1][0] + self.Width / 4,
                    edgelist[3][1][1] + self.Width / 2,
                ),
                (edgelist[3][1][0], edgelist[3][1][1] + self.Width / 2),
            ]
            lanelist.append(lane7)
            boundarylist.append(boundary9)
            indexes.append((21, 22))
            directions.append("Forward")
            successors.append((15, 7))
            predecessors.append((7, 15))
            alignment.append(["Forward", "Forward"])

            # left road1 id+16 to left
            lane8 = [
                edgelist[3][0],
                (edgelist[3][0][0] - self.Width / 4, edgelist[3][0][1]),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    edgelist[3][0][1],
                ),
            ]
            lanelist.append(lane8)
            boundary10 = [
                (edgelist[3][0][0], edgelist[3][0][1] + self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] + self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] + self.Width / 2)),
                ),
            ]
            boundary11 = [
                (edgelist[3][0][0], edgelist[3][0][1] - self.Width / 2),
                (
                    edgelist[3][0][0] - self.Width / 4,
                    edgelist[3][0][1] - self.Width / 2,
                ),
                (
                    float("{:.3f}".format(edgelist[3][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[3][0][1] - self.Width / 2)),
                ),
            ]
            boundarylist.append(boundary10)
            boundarylist.append(boundary11)  # reuse,id:24
            indexes.append((24, 23))
            directions.append("Forward")
            successors.append((7, 16))
            predecessors.append((16, 7))
            alignment.append(["Forward", "Forward"])

            # left road2 id+17 to left
            lane9 = [
                edgelist[2][0],
                (edgelist[2][0][0] - self.Width / 4, edgelist[2][0][1]),
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    edgelist[2][0][1],
                ),
            ]
            lanelist.append(lane9)
            boundary12 = [
                (
                    float("{:.3f}".format(edgelist[2][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[2][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[2][0][0] - self.Width / 4,
                    edgelist[2][0][1] - self.Width / 2,
                ),
                (edgelist[2][0][0], edgelist[2][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary12)  # reuse id:25
            indexes.append((25, 24))
            directions.append("Forward")
            successors.append((6, 17))
            predecessors.append((17, 6))
            successors.append((1, 17))
            predecessors.append((17, 1))
            alignment.append(["Backward", "Forward"])

            # left road3 id+18 to right
            lane10 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    edgelist[1][0][1],
                ),
                (edgelist[1][0][0] - self.Width / 4, edgelist[1][0][1]),
                edgelist[1][0],
            ]
            lanelist.append(lane10)
            boundary13 = [
                (
                    float("{:.3f}".format(edgelist[1][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[1][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[1][0][0] - self.Width / 4,
                    edgelist[1][0][1] - self.Width / 2,
                ),
                (edgelist[1][0][0], edgelist[1][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary13)  # reuse id:26
            indexes.append((25, 26))
            directions.append("Forward")
            successors.append((18, 5))
            predecessors.append((5, 18))
            alignment.append(["Forward", "Forward"])

            # left road4 id+19 to right
            lane11 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    edgelist[0][0][1],
                ),
                (edgelist[0][0][0] - self.Width / 4, edgelist[0][0][1]),
                edgelist[0][0],
            ]
            lanelist.append(lane11)
            boundary14 = [
                (
                    float("{:.3f}".format(edgelist[0][0][0] - self.Width / 2)),
                    float("{:.3f}".format(edgelist[0][0][1] - self.Width / 2)),
                ),
                (
                    edgelist[0][0][0] - self.Width / 4,
                    edgelist[0][0][1] - self.Width / 2,
                ),
                (edgelist[0][0][0], edgelist[0][0][1] - self.Width / 2),
            ]
            boundarylist.append(boundary14)
            indexes.append((26, 27))
            directions.append("Forward")
            successors.append((19, 4))
            predecessors.append((3, 19))
            predecessors.append((4, 19))
            alignment.append(["Forward", "Forward"])

            laneInfolist.append(lanelist)
            laneInfolist.append(boundarylist)
            laneInfolist.append(indexes)
            laneInfolist.append(directions)
            laneInfolist.append(successors)
            laneInfolist.append(predecessors)
            laneInfolist.append(alignment)
            return laneInfolist

    def generate_road(self, f):

        Widget.LaneID += sum(self.OuterLaneNumber) + self.InnerLaneNumber
        Widget.BoundaryID += self.BoundaryNumber
        Widget.JunctionID += 1
        Widget.WidgetID += 1

        lanes = (
                str(self.StartLaneID)
                + ":"
                + str(
            self.StartLaneID + sum(self.OuterLaneNumber) + self.InnerLaneNumber + -1
        )
        ) 
        printAutoInd(f, "")
        printAutoInd(f, "% Here is a T-Junction widget.")
        for lane in range(
                self.StartLaneID,
                self.StartLaneID + sum(self.OuterLaneNumber) + self.InnerLaneNumber,
        ):
            printAutoInd(f, "rrMap.Lanes(" + str(lane) + ") = roadrunner.hdmap.Lane();")
        laneidlist = []
        for i in range(
                self.StartLaneID,
                self.StartLaneID + sum(self.OuterLaneNumber) + self.InnerLaneNumber,
        ):
            laneidlist.append("Lane" + str(i))
        laneid = ",".join(['"' + i + '"' for i in laneidlist])
        printAutoInd(f, "[rrMap.Lanes(" + lanes + ").ID] = deal(" + laneid + ");")

        laneInfoList = self.getLaneInfoList()
        # print("laneInfoList = ",laneInfoList)
        lanepointlist = self.rotation(laneInfoList[0])
        boundarypointlist = self.rotation(laneInfoList[1])
        indexes = laneInfoList[2]
        # laneObjects=laneInfoList[3]
        directions = laneInfoList[3]
        successors = laneInfoList[4]
        predecessors = laneInfoList[5]
        alignment = laneInfoList[6]

        lanepointstring = self.PointtoString(lanepointlist)
        boundarypointstring = self.PointtoString(boundarypointlist)

        printAutoInd(
            f, "[rrMap.Lanes(" + lanes + ").Geometry] = deal(" + lanepointstring + ");"
        )

       
        traveldirectionlist = []
        for direction in directions:
            traveldirectionlist.append(direction)
        traveldirection = ",".join(['"' + i + '"' for i in traveldirectionlist])
        printAutoInd(
            f,
            "[rrMap.Lanes("
            + lanes
            + ").TravelDirection] = deal("
            + traveldirection
            + ");",
        )
        printAutoInd(f, "[rrMap.Lanes(" + lanes + ').LaneType] = deal("Driving");')

        # boundary
        boundaries = (
                str(self.StartBoundaryID)
                + ":"
                + str(self.StartBoundaryID + self.BoundaryNumber - 1)
        )  
        printAutoInd(f, "% Set the lane boundaries.")
        for boundary in range(
                self.StartBoundaryID, self.StartBoundaryID + self.BoundaryNumber
        ):
            printAutoInd(
                f,
                "rrMap.LaneBoundaries("
                + str(boundary)
                + ") = roadrunner.hdmap.LaneBoundary();",
            )
        laneboundaryidlist = []
        for i in range(
                self.StartBoundaryID, self.StartBoundaryID + self.BoundaryNumber
        ):
            laneboundaryidlist.append("Boundary" + str(i))
        boundaryid = ",".join(['"' + i + '"' for i in laneboundaryidlist])
        printAutoInd(
            f,
            "[rrMap.LaneBoundaries(" + boundaries + ").ID] = deal(" + boundaryid + ");",
        )
        printAutoInd(
            f,
            "[rrMap.LaneBoundaries("
            + boundaries
            + ").Geometry] = deal("
            + boundarypointstring
            + ");",
        )
        
        printAutoInd(f, "% Associate lanes and lane boundaries.")
        for i in range(len(laneidlist)):
            printAutoInd(
                f,
                "leftBoundary(rrMap.Lanes("
                + str(self.StartLaneID + i)
                + '),"Boundary'
                + str(self.StartBoundaryID + indexes[i][0])
                + '",Alignment="'
                + alignment[i][0]
                + '");',
            )
            printAutoInd(
                f,
                "rightBoundary(rrMap.Lanes("
                + str(self.StartLaneID + i)
                + '),"Boundary'
                + str(self.StartBoundaryID + indexes[i][1])
                + '",Alignment="'
                + alignment[i][1]
                + '");',
            )
        for i in range(len(successors)):
            # rrMap.Lanes(3).Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="Lane4"));
            printAutoInd(
                f,
                "rrMap.Lanes("
                + str(self.StartLaneID + successors[i][0])
                + ').Successors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="'
                + laneidlist[successors[i][1]]
                + '"));',
            )

        for i in range(len(predecessors)):
            printAutoInd(
                f,
                "rrMap.Lanes("
                + str(self.StartLaneID + predecessors[i][0])
                + ').Predecessors = roadrunner.hdmap.AlignedReference(Reference=roadrunner.hdmap.Reference(ID="'
                + laneidlist[predecessors[i][1]]
                + '"));',
            )

        # junction definition
        printAutoInd(f, "% junction definition")
        printAutoInd(
            f, "rrMap.Junctions(" + str(self.ID) + ") = roadrunner.hdmap.Junction();"
        )

        geoPoints = self.getGeometryPoints()
        geoPoints1 = self.rotation(geoPoints)
        geoPointsStr = self.PointtoString([geoPoints1])
        printAutoInd(
            f,
            'polygon=roadrunner.hdmap.Polygon("ExteriorRing",deal('
            + geoPointsStr
            + "));",
        )
        printAutoInd(
            f, 'multipolygon=roadrunner.hdmap.MultiPolygon("Polygons",polygon);'
        )
        printAutoInd(
            f,
            "[rrMap.Junctions("
            + str(self.ID)
            + ":"
            + str(self.ID)
            + ").Geometry]=multipolygon;",
        )
        # rrMap.Junctions(1).Lanes=deal(roadrunner.hdmap.Reference("ID","Lane3"));
        tmpStr = 'roadrunner.hdmap.Reference("ID","' + laneidlist[0] + '")'
        for i in range(1, self.InnerLaneNumber):
            tmpStr += ',roadrunner.hdmap.Reference("ID","' + laneidlist[i] + '")'
        printAutoInd(
            f, "rrMap.Junctions(" + str(self.ID) + ").Lanes=deal([" + tmpStr + "]);"
        )
