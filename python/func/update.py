from func.judge import judge
from fork_widget.fork import Fork
from straigntlane_widget.straightlane import StraightLane
from Ulane_widget.ulane import ULane
from Intersection_widget.intersection import Intersection
from TJunction_widget.tJunction import tJunction
from laneswitch_widget.laneswitch import LaneSwitch
from roundabout_widget.roundabout import Roundabout
from curve_widget.curve import Curve
import random




def update(dict1, rules, totalCoveredArea, parametercount):
    dict = dict1
    type = dict.get("Type")
    print('尝试拼接' + type + '组件')
    # type=name.split("_")[0]
    if type == "straightlane":
        length = rules.get("lane_length")
        random.shuffle(length)
        lw = dict.get("LW")
        print('参数更新')
        for i in length:
            newlw = (i, lw[1])

            dict.update(LW=newlw)
            tmpStraightLane = StraightLane(dict)
            tmpCoveredArea = tmpStraightLane.get_coveredArea()
            isCovered = judge(totalCoveredArea, tmpCoveredArea)
            parametercount += 1
            if not isCovered:
                del tmpStraightLane  # 从内存的角度，是否要释放对象？
                return dict, parametercount
        newLength = [x for x in range(10 * int(min(length) / 20), min(length), 10)]
        random.shuffle(newLength)
        for i in newLength:
            # lw[0] = i
            newlw = (i, lw[1])
            dict.update(LW=newlw)
            tmpStraightLane = StraightLane(dict)
            tmpCoveredArea = tmpStraightLane.get_coveredArea()
            isCovered = judge(totalCoveredArea, tmpCoveredArea)
            parametercount += 1
            if not isCovered:
                del tmpStraightLane  # 从内存的角度，是否要释放对象？
                return dict, parametercount
            else:
                del tmpStraightLane
                continue
    elif type == "tJunction":
        tmpTJunction = tJunction(dict)
        tmpCoveredArea = tmpTJunction.get_coveredArea()
        isCovered = judge(totalCoveredArea, tmpCoveredArea)
        parametercount += 1
        if not isCovered:
            del tmpTJunction  # 从内存的角度，是否要释放对象？
            return dict, parametercount
        else:
            del tmpTJunction
    elif type == "intersection":
        tmpIntersection = Intersection(dict)
        tmpCoveredArea = tmpIntersection.get_coveredArea()
        isCovered = judge(totalCoveredArea, tmpCoveredArea)
        parametercount += 1
        if not isCovered:
            del tmpIntersection  # 从内存的角度，是否要释放对象？
            return dict, parametercount
        else:
            del tmpIntersection
    elif type == "laneswitch":
        tmpLaneSwitch = LaneSwitch(dict)
        tmpCoveredArea = tmpLaneSwitch.get_coveredArea()
        isCovered = judge(totalCoveredArea, tmpCoveredArea)
        parametercount += 1
        if not isCovered:
            del tmpLaneSwitch  # 从内存的角度，是否要释放对象？
            return dict, parametercount
        else:
            del tmpLaneSwitch
    elif type == "fork":
        R = rules.get("lane_R")
        random.shuffle(R)
        for i in R:
            dict.update(R=i)
            tmpFork = Fork(dict)
            tmpCoveredArea = tmpFork.get_coveredArea()
            isCovered = judge(totalCoveredArea, tmpCoveredArea)
            parametercount += 1
            if not isCovered:
                del tmpFork  # 从内存的角度，是否要释放对象？
                return dict, parametercount
            else:
                del tmpFork
                continue
    elif type == "roundabout":
        R = rules.get("lane_R")
        random.shuffle(R)
        print('参数更新')
        for i in R:
            dict.update(R=i)
            tmpRoundAbout = Roundabout(dict)
            tmpCoveredArea = tmpRoundAbout.get_coveredArea()
            isCovered = judge(totalCoveredArea, tmpCoveredArea)
            parametercount += 1
            if not isCovered:
                del tmpRoundAbout  # 从内存的角度，是否要释放对象？
                return dict, parametercount
            else:
                del tmpRoundAbout
                continue
    elif type == "ulane":
        length = rules.get("lane_length")
        ulane_D = rules.get("ulane_D")
        ulane_X = rules.get("ulane_X")
        print('参数更新')
        random.shuffle(length)
        random.shuffle(ulane_D)
        random.shuffle(ulane_X)
        lw = dict.get("LW")
        for d in ulane_D:
            for x in ulane_X:
                for i in length:
                    # lw[0] = i
                    newlw = (i, lw[1])
                    dict.update(LW=newlw)
                    dict.update(DX=(d, x))
                    tmpUlane = ULane(dict)
                    tmpCoveredArea = tmpUlane.get_coveredArea()
                    isCovered = judge(totalCoveredArea, tmpCoveredArea)
                    parametercount += 1
                    if not isCovered:
                        del tmpUlane  # 从内存的角度，是否要释放对象？
                        return dict, parametercount
                    else:
                        del tmpUlane
                        continue
                newLength = [x for x in range(10 * int(min(length) / 20), min(length), 10)]
                random.shuffle(newLength)
                for i in newLength:
                    newlw = (i, lw[1])
                    dict.update(LW=newlw)
                    dict.update(DX=(d, x))
                    tmpUlane = ULane(dict)
                    tmpCoveredArea = tmpUlane.get_coveredArea()
                    isCovered = judge(totalCoveredArea, tmpCoveredArea)
                    parametercount += 1
                    if not isCovered:
                        del tmpUlane  # 从内存的角度，是否要释放对象？
                        return dict, parametercount
                    else:
                        del tmpUlane
                        continue
    elif type == "curve":
        function = dict.get("Function")
        if function == "1/4Circle" or function == "S":
            R = rules.get("lane_R")
            random.shuffle(R)
            print('参数更新')
            for i in R:
                dict.update(R=i)
                tmpCurve = Curve(dict)
                tmpCoveredArea = tmpCurve.get_coveredArea()
                isCovered = judge(totalCoveredArea, tmpCoveredArea)
                parametercount += 1
                if not isCovered:
                    del tmpCurve  # 从内存的角度，是否要释放对象？
                    return dict, parametercount
                else:
                    del tmpCurve
                    continue
        elif function == "Bezier":
            R = rules.get("lane_R")
            direction = rules.get("direction")
            # controlPoint=rules.get("controlPoint")#应该根据curveset和start计算
            curveSetOffset = rules.get("curveSetOffset")
            curveSetLength = rules.get("curveSetLength")
            random.shuffle(R)
            random.shuffle(direction)
            # random.shuffle(controlPoint)
            random.shuffle(curveSetOffset)
            random.shuffle(curveSetLength)

            k = dict.get("K")
            ######how to select control point?
            start = dict.get("Start")
            print('参数更新')
            for r in R:
                for o in curveSetOffset:
                    for l in curveSetLength:
                        for d in direction:
                            dict.update(Direction=d)
                            dict.update(R=r)
                            dict.update(CurveSet=(o, l))
                            # if k == "+0":
                            controlPoint = [(start[0] + int(random.random() * l),start[1] + int(random.randrange(-40, 0))),(start[0] + int(random.random() * l),start[1] + int(random.randrange(0, 40)))]
                            # elif k == "-0":
                            #     controlPoint = [(start[0] - int(random.random() * l),start[1] + int(random.randrange(-40, 0))),(start[0] - int(random.random() * l),start[1] + int(random.randrange(0, 40)))]
                            # elif k == "+":
                            #     controlPoint = [(start[0] + int(random.randrange(-40, 0)),start[1] + int(random.random() * l)),(start[0] + int(random.randrange(0, 40)),start[1] + int(random.random() * l))]
                            # elif k == "-":
                            #     controlPoint = [(start[0] + int(random.randrange(-40, 0)),start[1] - int(random.random() * l)),(start[0] + int(random.randrange(0, 40)),start[1] - int(random.random() * l))]
                            dict.update(ControlPoint=controlPoint)
                            tmpCurve = Curve(dict)
                            tmpCoveredArea = tmpCurve.get_coveredArea()
                            isCovered = judge(totalCoveredArea, tmpCoveredArea)
                            parametercount += 1
                            if not isCovered:
                                del tmpCurve  # 从内存的角度，是否要释放对象？
                                return dict, parametercount
                            else:
                                del tmpCurve
                                continue
    print('该组件在该路口下无法拼接')
    return None, parametercount

def initialFirstwidget(dict1, rules, totalCoveredArea, parametercount):
    dict = dict1.copy()
    dict.update(Start=(0, 0))
    dict.update(K=random.choice(['+', '-', '+0', '-0']))
    return update(dict, rules, totalCoveredArea, parametercount)