#全局的组件父类，用来记录每个子类组件被调用时道路和边界初始的id
class Widget:
    LaneID = 1 #组件的起始车道id
    BoundaryID = 1 #组件的起始车道边界id
    JunctionID = 1
    WidgetID = 1

    # def get_self_TravelDirection(dict1):
    #     dict = {f'Lane{n}': v for n, v in enumerate(dict1.values(),start=Widget.LaneID)}
    #     return dict
    def get_self_LaneAssetType(dict2):
        dict = {f'Boundary{n}': v for n, v in enumerate(dict2.values(), start=Widget.BoundaryID)}
        return dict