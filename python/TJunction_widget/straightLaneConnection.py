from func.printAuto import printAutoInd
from func.widget import Widget
import sympy as sy
import numpy as np
import math

class StraightLaneConnection(Widget):
    ID=1 
    Start=(0,0)
    End=(0,0) 
    Width=3.5
    BoundaryId1='b1' 
    BoundaryId2='b2' 
    Diretction = 0 
    TravelDirection = 'Forward' 
    LaneAssetType = {} 
    LaneType = 'Driving'
    k = '+0' 
    k1= '+0'
    Flag = ''
    lanePoints=[]
    boundaryPoints=[]

    def __init__(self,dict1):
        self.ID=dict1.get('ID')
        self.Start=dict1.get('Start')
        self.End=dict1.get('End')
        self.Width=dict1.get('Width')
        self.BoundaryId1=dict1.get('BoundaryId1')
        self.BoundaryId2=dict1.get('BoundaryId2')
        self.Direction=dict1.get('Direction')
        self.TravelDirection=dict1.get('TravelDirection')
        self.LaneAssetType=dict1.get('LaneAssetType')
        self.LaneType=dict1.get('LaneType')
        self.k=dict1.get('k')
        self.k1=dict1.get('k1')
        self.Flag=dict1.get('Flag')
        self.lanePoints=self.getLanePoint()
        self.boundaryPoints=self.getboundarypoint()


    def setBoundaryPoints(self,boundaryPoints):    
        self.boundaryPoints=boundaryPoints
    def getLanePoint(self):
        pointlist=[]
        # if self.k == "+0":
        point1 = self.Start
        point2 = ((self.Start[0]+self.End[0])/2, (self.Start[1]+self.End[1])/2)
        point3 =self.End
        lane1 = [point1, point2, point3]
        return(lane1)



    def getboundarypoint(self):
        twoBoundary=[]
        result=self.getBoundarySEPoint()
        # print(result)
        leftStart=result[0]
        leftEnd=result[1]
        rightStart=result[2]
        rightEnd=result[3]
        leftBoundary=[]
        rightBoundary=[]

        leftBoundary.append(leftStart)
        leftMiddle=((leftStart[0]+leftEnd[0])/2,(leftStart[1]+leftEnd[1])/2)
        leftBoundary.append(leftMiddle)
        leftBoundary.append(leftEnd)

        rightBoundary.append(rightStart)
        rightMiddle=((rightStart[0]+rightEnd[0])/2,(rightStart[1]+rightEnd[1])/2)
        rightBoundary.append(rightMiddle)
        rightBoundary.append(rightEnd)

        twoBoundary.append(leftBoundary)
        twoBoundary.append(rightBoundary)
        return(twoBoundary)
    
    def getBoundarySEPoint(self):
        result=[]#leftStart,leftEnd,rightStart,rightEnd
        leftStart=(0,0)
        leftEnd=(0,0)
        rightStart=(0,0)
        rightEnd=(0,0)
        if self.k=='+0':
            leftStart=(self.Start[0],self.Start[1]+self.Width/2)
            rightStart=(self.Start[0],self.Start[1]-self.Width/2)
            leftEnd=(self.End[0],self.End[1]+self.Width/2)
            rightEnd=(self.End[0],self.End[1]-self.Width/2)
        if self.k=='-0':
            leftStart=(self.Start[0],self.Start[1]-self.Width/2)
            rightStart=(self.Start[0],self.Start[1]+self.Width/2)
            leftEnd=(self.End[0],self.End[1]-self.Width/2)
            rightEnd=(self.End[0],self.End[1]+self.Width/2)
        if self.k=='+':
            leftStart=(self.Start[0]-self.Width/2,self.Start[1])
            rightStart=(self.Start[0]+self.Width/2,self.Start[1])
            leftEnd=(self.End[0]-self.Width/2,self.End[1])
            rightEnd=(self.End[0]+self.Width/2,self.End[1])
        if self.k=='-':
            leftStart=(self.Start[0]+self.Width/2,self.Start[1])
            rightStart=(self.Start[0]-self.Width/2,self.Start[1])
            leftEnd=(self.End[0]+self.Width/2,self.End[1])
            rightEnd=(self.End[0]-self.Width/2,self.End[1])
        result.append(leftStart)
        result.append(leftEnd)
        result.append(rightStart)
        result.append(rightEnd)
        return(result)

    def PointtoString(self,lst):
        # [[(-1.5, 0), (-1.5, 5.0), (-1.5, 10)], [(1.5, 0), (1.5, 5.0), (1.5, 10)]] 变成 [-1.5 0;-1.5 5.0;-1.5 10],[1.5 0;1.5 5.0;1.5 10]的字符串
        lst=[str(i).replace(',', '').replace(') (', ';').replace('(', '').replace(')', '') for i in lst]
        string = ','.join(lst)
        return string

    def generate_road(self,f):
        printAutoInd(f, '')
        printAutoInd(f, '% Here is a StraightRoad widget.')
        printAutoInd(f, '% Set the lanes.')
        printAutoInd(f, 'rrMap.Lanes(' + str(self.ID) + ') = roadrunner.hdmap.Lane();')

        printAutoInd(f, '[rrMap.Lanes(' + str(self.ID) + ').ID] = deal(\'Lane' + str(self.ID) + '\');')
        lanePointList=self.getlanepoint()
        lanePointStr=self.PointtoString(lanePointList)
        printAutoInd(f,'[rrMap.Lanes(' + str(self.ID) + ').Geometry] = deal(' + lanePointStr + ');')
        printAutoInd(f, '[rrMap.Lanes(' + str(self.ID) + ').TravelDirection] = deal(\'' + self.TravelDirection + '\');')
        printAutoInd(f, '[rrMap.Lanes(' + str(self.ID) + ').LaneType] = deal(\''+self.LaneType+'\');')
        #Boundary
        printAutoInd(f, '% Set the lane boundaries.')
        printAutoInd(f, 'rrMap.LaneBoundaries(' + str(self.BoundaryId1) + ') = roadrunner.hdmap.LaneBoundary();')
        printAutoInd(f, 'rrMap.LaneBoundaries(' + str(self.BoundaryId2) + ') = roadrunner.hdmap.LaneBoundary();')

        boundaryPointList=self.getboundarypoint()
        leftBoundaryPointList=boundaryPointList[0]
        rightBoundaryPointList=boundaryPointList[1]
        leftBoundaryPointStr=self.PointtoString(leftBoundaryPointList)
        rightBoundaryPointstr=self.PointtoString(rightBoundaryPointList)

        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId1) + ').ID] = deal(\'Boundary' + str(self.BoundaryId1) + '\');')
        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId2) + ').ID] = deal(\'Boundary' + str(self.BoundaryId2) + '\');')

        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId1) + ').Geometry] = deal(' + leftBoundaryPointStr + ');')
        printAutoInd(f, '[rrMap.LaneBoundaries(' + str(self.BoundaryId2) + ').Geometry] = deal(' + rightBoundaryPointstr + ');')
   
        printAutoInd(f, '% Associate lanes and lane boundaries.')
        printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.ID) + '),"Boundary' + str(self.BoundaryId1) + '",Alignment="Forward");')
        printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.ID) + '),"Boundary'+ str(self.BoundaryId2) +'",Alignment="Forward");')
        printAutoInd(f, '% End of this widget')