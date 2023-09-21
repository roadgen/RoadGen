from func.printAuto import printAutoInd
from func.widget import Widget
import sympy as sy
import numpy as np
import math
class ArcLane(Widget):
    ID=1 #road id
    Start=(0,0) #start position
    End=(0,0) #end position
    Width=3.5
    BoundaryId1='b1' #id of left boundary
    BoundaryId2='b2' #id of right boundary
    Diretction = 0 #0:turn right，1:turn left
    TravelDirection = 'Forward' #forward, backward, bidirectional
    LaneAssetType = {} #{BoundaryID:'SSW',...} 
    LaneType = 'Driving' #default:driving
    k = '+0'  # direction of start point.+0:right，-0:left，+:up，-:down。
    k1= '+0'  # direction of end point.+0:right，-0:left，+:up，-:down。
    Flag = '' #flag of component
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
        self.lanePoints=self.getlanepoint()
        self.boundaryPoints=self.getboundarypoint()
        
        # Widget.LaneID +=1
        # Widget.BoundaryID +=2

 #judge circle point's relative position to start point
    def relativePositon(self):
        relative=0 #1：left-up 2：left-down 3：right-up 4：right-down
        if self.End[0]<self.Start[0]:#left+1
            relative=1
        else:#right+3
            relative=3 
        if self.End[1]<self.Start[1]:#down+1
            relative+=1
        return relative

    #get Center coordinates
    def getCirclePoint(self,tag,start,end):
        point=(0,0)
        if tag==0:
            x=float("{:.3f}".format((start[0]**2-end[0]**2-(start[1]-end[1])**2)/(2*start[0]-2*end[0])))
            point=(x,start[1])
        else:
            y=float("{:.3f}".format((start[1]**2-end[1]**2-(start[0]-end[0])**2)/(2*start[1]-2*end[1])))
            point=(start[0],y)
        return point

    #get circle function
    def getCircleFunction(self,start,end):
        relative=self.relativePositon()
        tag=0 #0:horizontal 1：vertical
        if relative==1 and self.Direction==0:
            tag=1
        elif relative==1 and self.Direction==1:
            tag=0
        elif relative==2 and self.Direction==0:
            tag=0
        elif relative==2 and self.Direction==1:
            tag=1
        elif relative==3 and self.Direction==0:
            tag=0
        elif relative==3 and self.Direction==1:
            tag=1
        elif relative==4 and self.Direction==0:
            tag=1
        elif relative==4 and self.Direction==1:
            tag=0
        point=self.getCirclePoint(tag,start,end)
        radius=0
        if tag==0:
            radius=abs(point[0]-start[0])
        elif tag==1:
            radius=abs(point[1]-start[1])
        result=[point,radius]
        return result
    
    #generate point of lane
    def getlanepoint(self):
        pointlist=[]
        result=self.getCircleFunction(self.Start,self.End)
        circlePoint=result[0]
        circleRadius=result[1]
        pointlistx=np.linspace(self.Start[0],self.End[0],100)
        
        pointlisty=[]
        pointlistx=np.delete(pointlistx,0)
        pointlistx=np.delete(pointlistx,len(pointlistx)-1)
        for i in pointlistx:
            y=sy.symbols('y')
            a=sy.solve((i-circlePoint[0])**2+(y-circlePoint[1])**2-circleRadius**2,y)
            for j in a:
                
                if j>=min(self.Start[1],self.End[1]) and j<=max(self.Start[1],self.End[1]):
                    pointlisty.append(j)
        pointlist.append(self.Start)
        for i in range(len(pointlistx)):
            point=(pointlistx[i],pointlisty[i])
            pointlist.append(point)
        pointlist.append(self.End)
        return(pointlist)
        

    #generate point of boundary
    def getboundarypoint(self):
        twoBoundary=[]
        result=self.getBoundarySEPoint()
        leftStart=result[0]
        leftEnd=result[1]
        rightStart=result[2]
        rightEnd=result[3]
        leftCircleResult=self.getCircleFunction(leftStart,leftEnd)
        rightCircleResult=self.getCircleFunction(rightStart,rightEnd)
        leftCirclePoint=leftCircleResult[0]
        leftCircleRadius=leftCircleResult[1]
        rightCirclePoint=rightCircleResult[0]
        rightCircleRadius=rightCircleResult[1]

        leftBoundary=[]
        rightBoundary=[]
        leftBoundaryX=np.linspace(leftStart[0],leftEnd[0],100)
        leftBoundaryY=[]
        leftBoundaryX=np.delete(leftBoundaryX,0)
        leftBoundaryX=np.delete(leftBoundaryX,len(leftBoundaryX)-1)
        for i in leftBoundaryX:
            y=sy.symbols('y')
            a=sy.solve((i-leftCirclePoint[0])**2+(y-leftCirclePoint[1])**2-leftCircleRadius**2,y)
            for j in a:
                if j>=min(leftStart[1],leftEnd[1]) and j<=max(leftStart[1],leftEnd[1]):
                    leftBoundaryY.append(j)
        leftBoundary.append(leftStart)

        for i in range(len(leftBoundaryX)):
            leftBoundary.append((leftBoundaryX[i],leftBoundaryY[i]))
        leftBoundary.append(leftEnd)
        
        rightBoundaryX=np.linspace(rightStart[0],rightEnd[0],100)
        rightBoundaryY=[]
        rightBoundaryX=np.delete(rightBoundaryX,0)
        rightBoundaryX=np.delete(rightBoundaryX,len(rightBoundaryX)-1)
        for i in rightBoundaryX:
            y=sy.symbols('y')
            a=sy.solve((i-rightCirclePoint[0])**2+(y-rightCirclePoint[1])**2-rightCircleRadius**2,y)
            for j in a:
                if j>=min(rightStart[1],rightEnd[1]) and j<=max(rightStart[1],rightEnd[1]):
                    rightBoundaryY.append(j)
        rightBoundary.append(rightStart)
        for i in range(len(rightBoundaryX)):
            rightBoundary.append((rightBoundaryX[i],rightBoundaryY[i]))
        rightBoundary.append(rightEnd)
        twoBoundary.append(leftBoundary)
        twoBoundary.append(rightBoundary)
        return(twoBoundary)
        
    #get start and end point of boundary
    def getBoundarySEPoint(self):
        result=[]#leftStart,leftEnd,rightStart,rightEnd
        leftStart=(0,0)
        leftEnd=(0,0)
        rightStart=(0,0)
        rightEnd=(0,0)
        if self.k=='+0':
            leftStart=(self.Start[0],self.Start[1]+self.Width/2)
            rightStart=(self.Start[0],self.Start[1]-self.Width/2)
        if self.k=='-0':
            leftStart=(self.Start[0],self.Start[1]-self.Width/2)
            rightStart=(self.Start[0],self.Start[1]+self.Width/2)
        if self.k=='+':
            leftStart=(self.Start[0]-self.Width/2,self.Start[1])
            rightStart=(self.Start[0]+self.Width/2,self.Start[1])
        if self.k=='-':
            leftStart=(self.Start[0]+self.Width/2,self.Start[1])
            rightStart=(self.Start[0]-self.Width/2,self.Start[1])
        if self.k1=='+0':
            leftEnd=(self.End[0],self.End[1]+self.Width/2)
            rightEnd=(self.End[0],self.End[1]-self.Width/2)
        if self.k1=='-0':
            leftEnd=(self.End[0],self.End[1]-self.Width/2)
            rightEnd=(self.End[0],self.End[1]+self.Width/2)
        if self.k1=='+':
            leftEnd=(self.End[0]-self.Width/2,self.End[1])
            rightEnd=(self.End[0]+self.Width/2,self.End[1])
        if self.k1=='-':
            leftEnd=(self.End[0]+self.Width/2,self.End[1])
            rightEnd=(self.End[0]-self.Width/2,self.End[1])
        result.append(leftStart)
        result.append(leftEnd)
        result.append(rightStart)
        result.append(rightEnd)
        return(result)

    def PointtoString(self,lst):
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
         # connect lane and lane boundaries
        printAutoInd(f, '% Associate lanes and lane boundaries.')
        printAutoInd(f, 'leftBoundary(rrMap.Lanes(' + str(self.ID) + '),"Boundary' + str(self.BoundaryId1) + '",Alignment="Forward");')
        printAutoInd(f, 'rightBoundary(rrMap.Lanes(' + str(self.ID) + '),"Boundary'+ str(self.BoundaryId2) +'",Alignment="Forward");')
        printAutoInd(f, '% End of this widget')