import random
import json
from func.CountBasedChoose import CountBasedChoose
from func.GraphSimilarityV2 import GraphSimilarity, NodeSimilarityTest, EdgeExceptionCompare
from func.printConnection import printConnection
from func.printAuto import printAutoInd
from func.printAsserts import printAsserts
from func.widget import Widget
from func.CalculateSimilarity import calculatesimilarity
from settings.info import Info
from settings.connectionDict import Widget_Map

from laneswitch_widget.laneswitch import LaneSwitch
from fork_widget.fork import Fork
from straigntlane_widget.straightlane import StraightLane
from Ulane_widget.ulane import ULane
from curve_widget.curve import Curve
from roundabout_widget.roundabout import Roundabout
from Intersection_widget.intersection import Intersection
from TJunction_widget.tJunction import tJunction
from func.Quene import ConnectorQueue
from func.update import update, initialFirstwidget
from func.WidgetGraph import WidgetGraph
import pickle
from func.WidgetGraph import Node
from shapely.geometry import Polygon
from matplotlib import pyplot as plt
import time



def BuildRoad(widgetdict):
    type = widgetdict.get('Type')
    w = None
    if type == 'straightlane':
        w = StraightLane(widgetdict)
    elif type == 'ulane':
        w = ULane(widgetdict)
    elif type == 'curve':
        w = Curve(widgetdict)
    elif type == 'fork':
        w = Fork(widgetdict)
    elif type == 'laneswitch':
        w = LaneSwitch(widgetdict)
    elif type == 'intersection':
        w = Intersection(widgetdict)
    elif type == 'tJunction':
        w = tJunction(widgetdict)
    elif type == 'roundabout':
        w = Roundabout(widgetdict)
    return w


def save_graph(graph, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(graph, file)


def load_graph(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)


def RandomAlgorithm(Mfile, rrhdfile, pklfile, graphlst, widgetcount):
    rules = Info.COMPILE_RULES
    widgetlist = Info.Widgetlist
    num = Info.WidgetNumber
    parametupdateercount = 0
    widgetupdatecount = 0

    finalMfilename = Mfile
    rrhdfilename = rrhdfile
    pklfilename = pklfile

    encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")

    with open(finalMfilename, "w", encoding=encodingFormat) as f:
        graph = WidgetGraph()
        printAsserts(f)！
        count = 0
        totalCoveredArea = []
        widgetdict = random.choice(widgetlist)
        widgetdict0, parametupdateercount = initialFirstwidget(widgetdict, rules, totalCoveredArea,
                                                               parametupdateercount)
        widgetupdatecount += 1
        w0 = BuildRoad(widgetdict0)
        w0.generate_road(f)
        count += 1
        CoveredArea = w0.get_coveredArea()
        totalCoveredArea += CoveredArea
        widgetcount[json.dumps(widgetdict)] += 1
        id1 = w0.WidgetID
        type1 = widgetdict0.get('Type')
        flag1 = widgetdict0.get('Flag')
        function1 = widgetdict0.setdefault('Function', None)
        direction1 = widgetdict0.setdefault('Direction', None)
        graph.add_node(id1, type1, flag1, function1, direction1)
        connectorqueue = ConnectorQueue()
        for i in w0.get_Nexts():
            connectorqueue.enqueue(i)
        del w0
        while count < num and connectorqueue.isempty() is False:
            connector = connectorqueue.dequeue()
            flag = random.randint(0, 1)
            if connectorqueue.isempty() or flag == 1:
                connectorType = connector['type']
                allwidget4connect = Widget_Map.get(connectorType)
                random.shuffle(allwidget4connect)
                availableNum = len(allwidget4connect)
                n = 0
                for wDict in allwidget4connect:
                    widgetupdatecount += 1
                    dict1 = wDict.copy()
                    dict1['Start'] = connector['endpoint']
                    dict1['K'] = connector['direction']
                    dict1, parametupdateercount = update(dict1, rules, totalCoveredArea, parametupdateercount)
                    if dict1 is not None:
                        break
                    else:
                        n += 1
                        continue
                if n == availableNum:
                    print('no component can be connected')
                    continue
                else:
                    w1 = BuildRoad(dict1)
                    w1.generate_road(f)
                    count += 1
                    CoveredArea = w1.get_coveredArea()
                    totalCoveredArea += CoveredArea
                    widgetcount[json.dumps(wDict)] += 1
                    id2 = w1.WidgetID
                    type2 = dict1.get('Type')
                    flag2 = dict1.get('Flag')
                    function2 = dict1.setdefault('Function', None)
                    direction2 = dict1.setdefault('Direction', None)
                    graph.add_node(id2, type2, flag2, function2, direction2)
                    graph.add_edge(connector['ID'], id2)
                    for i in w1.get_Nexts():
                        connectorqueue.enqueue(i)
                    if len(connector['lanes']) == len(w1.get_Currents()['CurrentLanes']):
                        printConnection(connector['lanes'], w1.get_Currents()['CurrentLanes'], connectorType, f)
                    del w1
        if count < num:
            print('number of component not satisfy setting')

        printAutoInd(f, '')
        printAutoInd(f, 'plot(rrMap)')
        printAutoInd(f, 'write(rrMap,"' + rrhdfilename + '");')

    print(finalMfilename + " " + "Compile successfully!")
    print(Info.widgetcount.values())

    graphlst.append(graph)
    save_graph(graph, pklfilename)
    return parametupdateercount, widgetupdatecount


def CountBasedAlgorithm(Mfile, rrhdfile, pklfile, graphlst, widgetcount):
    rules = Info.COMPILE_RULES
    widgetlist = Info.Widgetlist
    num = Info.WidgetNumber
    parametupdateercount = 0
    widgetupdatecount = 0

    finalMfilename = Mfile
    rrhdfilename = rrhdfile
    pklfilename = pklfile

    encodingFormat = Info.COMPILE_PREF.setdefault("M File Ecoding Format", "GBK")

    with open(finalMfilename, "w", encoding=encodingFormat) as f:
        graph = WidgetGraph()
        printAsserts(f)
        count = 0
        totalCoveredArea = []
        widgetdict = CountBasedChoose(widgetlist, widgetcount)
        widgetdict0, parametupdateercount = initialFirstwidget(widgetdict, rules, totalCoveredArea,
                                                               parametupdateercount)
        widgetupdatecount += 1
        print(widgetdict0)
        w0 = BuildRoad(widgetdict0)
        w0.generate_road(f)
        count += 1
        CoveredArea = w0.get_coveredArea()
        totalCoveredArea += CoveredArea
        widgetcount[json.dumps(widgetdict)] += 1
        id1 = w0.WidgetID
        type1 = widgetdict0.get('Type')
        flag1 = widgetdict0.get('Flag')
        function1 = widgetdict0.setdefault('Function', None)
        direction1 = widgetdict0.setdefault('Direction', None)
        graph.add_node(id1, type1, flag1, function1, direction1)
        ##############
        connectorqueue = ConnectorQueue()
        for i in w0.get_Nexts():
            connectorqueue.enqueue(i)
        del w0
        while count < num and connectorqueue.isempty() is False:
            connector = connectorqueue.dequeue()
            flag = random.randint(0, 1)
            if connectorqueue.isempty() or flag == 1:
                connectorType = connector['type']
                allwidget4connect1 = Widget_Map.get(connectorType)
                allwidget4connect = allwidget4connect1.copy()
                availableNum = len(allwidget4connect)

                while availableNum > 0:
                    wDict = CountBasedChoose(allwidget4connect, widgetcount)
                    widgetupdatecount += 1
                    dict1 = wDict.copy()
                    dict1['Start'] = connector['endpoint']
                    dict1['K'] = connector['direction']
                    dict1, parametupdateercount = update(dict1, rules, totalCoveredArea, parametupdateercount)
                    if dict1 is not None:
                        break
                    else:
                        allwidget4connect.remove(wDict)
                        availableNum -= 1
                if availableNum == 0:
                    print('no component can be connected')
                    continue
                else:
                    print('next component dict')
                    print(dict1)
                    w1 = BuildRoad(dict1)
                    w1.generate_road(f)
                    count += 1
                    CoveredArea = w1.get_coveredArea()
                    totalCoveredArea += CoveredArea
                    widgetcount[json.dumps(wDict)] += 1
                    id2 = w1.WidgetID
                    type2 = dict1.get('Type')
                    flag2 = dict1.get('Flag')
                    function2 = dict1.setdefault('Function', None)
                    direction2 = dict1.setdefault('Direction', None)
                    graph.add_node(id2, type2, flag2, function2, direction2)
                    graph.add_edge(connector['ID'], id2)
                    for i in w1.get_Nexts():
                        connectorqueue.enqueue(i)
                    if len(connector['lanes']) == len(w1.get_Currents()['CurrentLanes']):
                        printConnection(connector['lanes'], w1.get_Currents()['CurrentLanes'], connectorType, f)
                    del w1
        if count < num:
            print('number of component not satisfy setting')
        printAutoInd(f, '')
        printAutoInd(f, 'plot(rrMap)')
        printAutoInd(f, 'write(rrMap,"' + rrhdfilename + '");')

    print(finalMfilename + " " + "Compile successfully!")
    print('Current usage of components')
    print(Info.widgetcount.values())

    graphlst.append(graph)
    save_graph(graph, pklfilename)
    return parametupdateercount, widgetupdatecount


def compile():
    graphlst = []
    global count
    count = 1
    widgetcount = Info.widgetcount
    start_time = time.time()
    # 6hour
    duration = 24 * 60 * 60

    # while count <= 2:
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            print('Time out')
            break

        finalMfilename = Info.mFILE_DIRECTORY + Info.mFILE_NAME + str(count) + '.m'
        rrhdfilename = Info.rFILE_DIRECTORY + Info.rFILE_NAME + str(count) + '.rrhd'
        pklfilename = 'python/test_graph2/' + Info.mFILE_NAME + str(count) + '.pkl'
        parametupdateercount, widgetupdatecount = 0, 0
        try:
            # parametupdateercount, widgetupdatecount = RandomAlgorithm(finalMfilename, rrhdfilename, pklfilename,
                                                                    #   graphlst, widgetcount)
            parametupdateercount, widgetupdatecount = CountBasedAlgorithm(finalMfilename, rrhdfilename, pklfilename,graphlst, widgetcount)
            print('update times of components：')
            print(widgetupdatecount)
            print('update times of parameters：')
            print(parametupdateercount)
            count += 1
        except Exception as e:
            print(e)
            Widget.LaneID = 1  # start id of component road
            Widget.BoundaryID = 1  # start id of boundary
            Widget.JunctionID = 1
            Widget.WidgetID = 1

        Widget.LaneID = 1  # start id of component road
        Widget.BoundaryID = 1  # start id of boundary
        Widget.JunctionID = 1
        Widget.WidgetID = 1
        Info.parameterupdate += parametupdateercount
        Info.widgetupdate += widgetupdatecount
        time.sleep(0.1)

        if len([key for key, value in Info.widgetcount.items() if value == 0]) == 0:
            print('Time of 242 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 42:
            print('Time of 200 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 92:
            print('Time of 150 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 142:
            print('Time of 100 {:.5f} s'.format(time.time() - start_time))
        elif len([key for key, value in Info.widgetcount.items() if value == 0]) <= 192:
            print('Time of 50 {:.5f} s'.format(time.time() - start_time))
        
        print('used number of components')
        print(len([key for key, value in Info.widgetcount.items() if value != 0]))
        
        if 30 * 60 <= (time.time() - start_time) < 40 *60:
            print("30min:")
            output()
        elif 60 * 60 <= (time.time() - start_time) < 70 * 60 :
            print("1hour:")
            output()
        elif 120 * 60 <= (time.time() - start_time) < 130 * 60:
            print("2hour:")
            output()
        elif 180 * 60 <= (time.time() - start_time) < 190 * 60:
            print("3hour:")
            output()    
        elif 240 * 60 <= (time.time() - start_time) < 250 * 60:
            print("4hour:")
            output()
        elif 300 * 60 <= (time.time() - start_time) < 310 * 60:
            print("5hour:")
            output() 
        elif 360 * 60 <= (time.time() - start_time) < 370 * 60:
            print("6hour:")
            output()
        elif 420 * 60 <= (time.time() - start_time) < 430 * 60:
            print("7hour:")
            output()    
        elif 480 * 60 <= (time.time() - start_time) < 490 * 60:
            print("8hour:")
            output()
        elif 540 * 60 <= (time.time() - start_time) < 550 * 60:
            print("9hour:")
            output() 
        elif 600 * 60 <= (time.time() - start_time) < 610 * 60:
            print("10hour:")
            output()
        elif 660 * 60 <= (time.time() - start_time) < 670 * 60:
            print("11hour:")
            output() 
        elif 720 * 60 <= (time.time() - start_time) < 730 * 60:
            print("12hour:")
            output()
        elif 780 * 60 <= (time.time() - start_time) < 790* 60 :
            print("13hour:")
            output()
        elif 840 * 60 <= (time.time() - start_time) < 850* 60:
            print("14hour:")
            output()
        if 900 * 60 <= (time.time() - start_time) < 910 * 60:
            print("15hour:")
            output()    
        elif 960 * 60 <= (time.time() - start_time) < 970 * 60:
            print("16hour:")
            output()
        elif 1020 * 60 <= (time.time() - start_time) < 1030 * 60:
            print("17hour:")
            output() 
        elif 1080 * 60 <= (time.time() - start_time) < 1090 * 60:
            print("18hour:")
            output()
        elif 1140 * 60 <= (time.time() - start_time) < 1150 * 60:
            print("19hour:")
            output()    
        elif 1200 * 60 <= (time.time() - start_time) < 1210 * 60:
            print("20hour:")
            output()
        elif 1260 * 60 <= (time.time() - start_time) < 1270 * 60:
            print("21hour:")
            output() 
        elif 1320 * 60 <= (time.time() - start_time) < 1330 * 60:
            print("22hour:")
            output()
        elif 1380 * 60 <= (time.time() - start_time) < 1390 * 60:
            print("23hour:")
            output() 
        elif 1440 * 60 <= (time.time() - start_time) < 1450 * 60:
            print("24hour:")
            output()

        

def output():
        print('total number of updated components')
        print(Info.widgetupdate)
        print('total number of updated parameters')
        print(Info.parameterupdate)
        print('number of components used')
        print(len([key for key, value in Info.widgetcount.items() if value != 0]))

def TestException():
    graph_dir = "graph"
    file_dir1 = "graph/AGM3.pkl"
    file_dir2 = "graph/AGM4.pkl"
    GraphSimilarity(file_dir1, file_dir2).NodeSimilarity()
    # GetSimilarity(graph_dir)
    print("asda")
   


if __name__ == '__main__':
    # finalMfilename = Info.mFILE_DIRECTORY + Info.mFILE_NAME + ".m"
    # rrhdfilename = Info.rFILE_DIRECTORY + Info.rFILE_NAME + ".rrhd"
    # RandomAlgorithm(finalMfilename, rrhdfilename)

    # test()
    compile()
    # calculatesimilarity()
    # file_dir1 = "graph/AGM1.pkl"
    # file_dir2 = "graph/AGM2.pkl"
    # GraphSimilarity(file_dir1,file_dir2).EdgeSimilarity()
