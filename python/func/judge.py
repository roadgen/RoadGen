from shapely.geometry import Polygon


# def judge(totalCoveredAreas, judgeArea):  # 相交返回False 不相交返回True
#     # totalCoveredAreas:[[]]
#     # judgeArea:[]
#     # return:ture(covered)/false(not covered)
#
#     # 只看顶点版本，结果会有覆盖
#     # for coveredArea in totalCoveredAreas:
#     #     for area in judgeArea:
#     #         for point in area:
#     #             if (point[0] < coveredArea[0][0] and point[0] > coveredArea[2][0]) or (
#     #                     point[0] > coveredArea[0][0] and point[0] < coveredArea[2][0]):
#     #                 if (point[1] < coveredArea[0][1] and point[1] > coveredArea[2][1]) or (
#     #                         point[1] > coveredArea[0][1] and point[1] < coveredArea[2][1]):
#     #                     return True
#
#     # 修订版本
#     for coveredArea in totalCoveredAreas:
#         for area in judgeArea:
#             point1 = area[0]
#             point3 = area[2]
#             for i in range(0, int(point3[0] - point1[1])):
#                 for j in range(0, int(point3[1])):
#                     point = (i, j)
#                     if (point[0] < coveredArea[0][0] and point[0] > coveredArea[2][0]) or (
#                             point[0] > coveredArea[0][0] and point[0] < coveredArea[2][0]):
#                         if (point[1] < coveredArea[0][1] and point[1] > coveredArea[2][1]) or (
#                                 point[1] > coveredArea[0][1] and point[1] < coveredArea[2][1]):
#                             return True
#
#     return False



def judge(totalCoveredAreas, judgeArea):  # 相交返回False 不相交返回True
    if totalCoveredAreas == []:
        return False
    for coverArea in totalCoveredAreas:  # 相交返回False 不相交返回True
        for current_Area in judgeArea:
            coverPoly = Polygon(coverArea)
            currentPoly = Polygon(current_Area)
            intersection1 = currentPoly.intersection(coverPoly)
            intersection2 = coverPoly.intersection(currentPoly)
            if intersection1.area > 0 or intersection2.area > 0:
                return True
            else:
                continue
    print("找到不重叠的组件...")
    return False
