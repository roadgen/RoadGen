# 直线道路提供的范式的组件  不完整或者过饱和，后续需要重新定义。不影响直线道路组件的编译。本质为7种，但是道路线的原因会超过7种。
dict1 = {'Start': (-40, 80),
         'LW': (20, 3.5),
         'LaneNumber': 1,
         'BoundaryNumber':2,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW'},
         'K': '+',
         'Type': 'straightlane',
         'Flag': '单行道'}

dict2 = {'Start': (-20, 80),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber': 3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'SW'},
         'K': '+',
         'Type': 'straightlane',
         'Flag': '单向虚线双行道'}

dict3 = {'Start': (0, 80),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber': 3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'SW'},
         'K': '+',
         'Type': 'straightlane',
         'Flag':'单向实线双行道'}

dict4 = {'Start': (0, 80),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber':3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DSW','Boundary3':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag': '单向虚实线双行道'}

dict5 = {'Start': (20, 80),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber':3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SDW','Boundary3':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'单向双实线双行道'}

dict6 = {'Start': (-40, 40),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber':3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DY','Boundary3':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双向虚线双行道'}

dict7 = {'Start': (-20, 40),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber':3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SY','Boundary3':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双向实线双行道'}

dict8 = {'Start': (0, 40),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber':3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DSY','Boundary3':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双向虚实线双行道'}

dict9 = {'Start': (20, 40),
         'LW': (20, 3.5),
         'LaneNumber': 2,
         'BoundaryNumber':3,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SDY','Boundary3':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双向双实线双行道'}


dict10 = {'Start': (-40, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'DY','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'一前行虚白线虚黄线三行道'}

dict11 = {'Start': (-40, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'DY','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'一前行实白线虚黄线三行道'}

dict12 = {'Start': (-20, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'SY','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'一前行虚白线实黄线三行道'}

dict13 = {'Start': (-20, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'SY','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'一前行实白线实黄线三行道'}


dict14 = {'Start': (0, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DY','Boundary3':'DW','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'二前行虚黄线虚白线三行道'}

dict15 = {'Start': (0, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DY','Boundary3': 'SW','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'二前行虚黄线实白线三行道'}

dict16 = {'Start': (20, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SY','Boundary3':'DW','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'二前行实黄线虚白线三行道'}

dict17 = {'Start': (20, 0),
         'LW': (20, 3.5),
         'LaneNumber': 3,
         'BoundaryNumber':4,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SY','Boundary3':'SW','Boundary4':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'二前行实黄线实白线三行道'}

dict18 = {'Start': (-40, -40),
         'LW': (20, 3.5),
         'LaneNumber': 4,
         'BoundaryNumber':5,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'SDY','Boundary4':'DW','Boundary5':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双黄实线虚虚四车道'}


dict19 = {'Start': (-40, -40),
         'LW': (20, 3.5),
         'LaneNumber': 4,
         'BoundaryNumber':5,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'SDY','Boundary4':'SW','Boundary5':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双黄实线实实四车道'}

dict20 = {'Start': (-40, -40),
         'LW': (20, 3.5),
         'LaneNumber': 4,
         'BoundaryNumber':5,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'SDY','Boundary4':'SW','Boundary5':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双黄实线虚实四车道'}

dict21 = {'Start': (-40, -40),
         'LW': (20, 3.5),
         'LaneNumber': 4,
         'BoundaryNumber':5,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'SDY','Boundary4':'DW','Boundary5':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双黄实线实虚四车道'}


dict22 = {'Start': (0, -40),
         'LW': (20, 3.5),
         'LaneNumber': 6,
         'BoundaryNumber':7,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'DW','Boundary4':'SDY','Boundary5':'DW','Boundary6':'DW','Boundary7':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双实线虚虚虚虚六车道'}

dict23 = {'Start': (0, -40),
         'LW': (20, 3.5),
         'LaneNumber': 6,
         'BoundaryNumber':7,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'SW','Boundary3':'SW','Boundary4':'SDY','Boundary5':'SW','Boundary6':'SW','Boundary7':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双实线实实实实六车道'}

dict24 = {'Start': (0, -40),
         'LW': (20, 3.5),
         'LaneNumber': 6,
         'BoundaryNumber':7,
         'LaneAssetType': {'Boundary1': 'SW','Boundary2': 'DW','Boundary3':'DW','Boundary4':'SDY','Boundary5':'SW','Boundary6':'SW','Boundary7':'SW'},
         'K':'+',
         'Type': 'straightlane',
         'Flag':'双实线虚虚实实六车道'}
