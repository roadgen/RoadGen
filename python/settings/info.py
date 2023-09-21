import json
import re
from straigntlane_widget import StraightLaneLibrary as st
from Ulane_widget import ULaneLibrary as ul
from curve_widget import curvelibrary as cur
from laneswitch_widget import LaneSwitchLibrary as ls
from Intersection_widget import intersectionlibrary as ins
from roundabout_widget import roundaboutlibrary as rdb
from fork_widget import forklibrary as fk
from TJunction_widget import tJunctionLibrary as tj


class Info(object):
    """
    info，setting information
    """
    # 文件存储
    mFILE_NAME = "AGM"
    mmFILE_NAME_M = "test.m"
    # mFILE_DIRECTORY="C:/Users/22340/Desktop/map/map_generation/matlab/m1_map/"
    # mFILE_DIRECTORY = "E:\map_generation\matlab\m_map/"
    # mFILE_DIRECTORY = "D:\Desktop\Code\LAB\V2\map_generation\matlab\m2_map"
    # mFILE_DIRECTORY = "/Users/leason/Documents/map_generation/matlab/m_map/"
    mFILE_DIRECTORY = "./matlab/test_map2/"
    rFILE_NAME = "AGM"
    rrFILE_NAME = "test1.m"
    rFILE_DIRECTORY = "../test_r_map2/"

    # information of component
    WID_NAME = {}
    WID_NODE = {}
    Names = WID_NAME
    Nodes = WID_NODE
    ######################################################################################
    Widgetlist = [
        st.dict1, st.dict2, st.dict3, st.dict4, st.dict5, st.dict6, st.dict7, st.dict8, st.dict9, st.dict10, st.dict11,
        st.dict12, st.dict13, st.dict14, st.dict15, st.dict16, st.dict17, st.dict18, st.dict19, st.dict20, st.dict21,
        st.dict22, st.dict23, st.dict24,
        ul.dict1_0, ul.dict2_0, ul.dict3_0, ul.dict4_0, ul.dict5_0, ul.dict6_0, ul.dict7_0, ul.dict8_0, ul.dict9_0,
        ul.dict10_0, ul.dict11_0, ul.dict12_0, ul.dict13_0, ul.dict14_0, ul.dict15_0, ul.dict16_0, ul.dict17_0,
        ul.dict18_0, ul.dict19_0, ul.dict20_0, ul.dict21_0, ul.dict22_0, ul.dict23_0, ul.dict24_0, ul.dict1_1,
        ul.dict2_1, ul.dict3_1, ul.dict4_1, ul.dict5_1, ul.dict6_1, ul.dict7_1, ul.dict8_1, ul.dict9_1, ul.dict10_1,
        ul.dict11_1, ul.dict12_1, ul.dict13_1, ul.dict14_1, ul.dict15_1, ul.dict16_1, ul.dict17_1, ul.dict18_1,
        ul.dict19_1, ul.dict20_1, ul.dict21_1, ul.dict22_1, ul.dict23_1, ul.dict24_1,
        cur.dict1_0, cur.dict2_0, cur.dict3_0, cur.dict4_0, cur.dict5_0, cur.dict6_0, cur.dict7_0, cur.dict8_0,
        cur.dict9_0, cur.dict10_0, cur.dict11_0, cur.dict12_0, cur.dict13_0, cur.dict14_0, cur.dict15_0, cur.dict16_0,
        cur.dict17_0, cur.dict18_0, cur.dict19_0, cur.dict20_0, cur.dict21_0, cur.dict1_1, cur.dict2_1, cur.dict3_1,
        cur.dict4_1, cur.dict5_1, cur.dict6_1, cur.dict7_1, cur.dict8_1, cur.dict9_1, cur.dict10_1, cur.dict11_1,
        cur.dict12_1, cur.dict13_1, cur.dict14_1, cur.dict15_1, cur.dict16_1, cur.dict17_1, cur.dict18_1, cur.dict19_1,
        cur.dict20_1, cur.dict21_1, cur.Sdict1_0, cur.Sdict2_0, cur.Sdict3_0, cur.Sdict4_0, cur.Sdict5_0, cur.Sdict6_0,
        cur.Sdict7_0, cur.Sdict8_0, cur.Sdict9_0, cur.Sdict10_0, cur.Sdict11_0, cur.Sdict12_0, cur.Sdict13_0,
        cur.Sdict14_0, cur.Sdict15_0, cur.Sdict16_0, cur.Sdict17_0, cur.Sdict18_0, cur.Sdict19_0, cur.Sdict20_0,
        cur.Sdict21_0, cur.Sdict1_1, cur.Sdict2_1, cur.Sdict3_1, cur.Sdict4_1, cur.Sdict5_1, cur.Sdict6_1, cur.Sdict7_1,
        cur.Sdict8_1, cur.Sdict9_1, cur.Sdict10_1, cur.Sdict11_1, cur.Sdict12_1, cur.Sdict13_1, cur.Sdict14_1,
        cur.Sdict15_1, cur.Sdict16_1, cur.Sdict17_1, cur.Sdict18_1, cur.Sdict19_1, cur.Sdict20_1, cur.Sdict21_1,
        cur.Bdict1_0, cur.Bdict2_0, cur.Bdict3_0, cur.Bdict4_0, cur.Bdict5_0, cur.Bdict6_0, cur.Bdict7_0, cur.Bdict8_0,
        cur.Bdict9_0, cur.Bdict10_0, cur.Bdict11_0, cur.Bdict12_0, cur.Bdict13_0, cur.Bdict14_0, cur.Bdict15_0,
        cur.Bdict16_0, cur.Bdict17_0, cur.Bdict18_0, cur.Bdict19_0, cur.Bdict20_0, cur.Bdict21_0,
        ls.dict1, ls.dict2, ls.dict3, ls.dict4, ls.dict5, ls.dict6, ls.dict7, ls.dict8, ls.dict9,
        ls.dict10, ls.dict11, ls.dict12, ls.dict13, ls.dict14,
        fk.dict1, fk.dict2, fk.dict3, fk.dict4, fk.dict5, fk.dict6, fk.dict7, fk.dict8, fk.dict9, fk.dict10, fk.dict11,
        fk.dict12, fk.dict13, fk.dict14, fk.dict15, fk.dict16, fk.dict17, fk.dict18, fk.dict19, fk.dict20, fk.dict21,
        fk.dict22,
    ]
    widgetcount = {
        json.dumps(st.dict1): 0, json.dumps(st.dict2): 0, json.dumps(st.dict3): 0, json.dumps(st.dict4): 0, json.dumps(st.dict5): 0, json.dumps(st.dict6): 0, json.dumps(st.dict7): 0,
json.dumps(st.dict8): 0, json.dumps(st.dict9): 0, json.dumps(st.dict10): 0, json.dumps(st.dict11): 0,
json.dumps(st.dict12): 0, json.dumps(st.dict13): 0, json.dumps(st.dict14): 0, json.dumps(st.dict15): 0, json.dumps(st.dict16): 0, json.dumps(st.dict17): 0, json.dumps(st.dict18): 0,
json.dumps(st.dict19): 0, json.dumps(st.dict20): 0, json.dumps(st.dict21): 0,
json.dumps(st.dict22): 0, json.dumps(st.dict23): 0, json.dumps(st.dict24): 0,

json.dumps(ul.dict1_0): 0, json.dumps(ul.dict2_0): 0, json.dumps(ul.dict3_0): 0, json.dumps(ul.dict4_0): 0, json.dumps(ul.dict5_0): 0, json.dumps(ul.dict6_0): 0,
json.dumps(ul.dict7_0): 0, json.dumps(ul.dict8_0): 0, json.dumps(ul.dict9_0): 0,
json.dumps(ul.dict10_0): 0, json.dumps(ul.dict11_0): 0, json.dumps(ul.dict12_0): 0, json.dumps(ul.dict13_0): 0, json.dumps(ul.dict14_0): 0, json.dumps(ul.dict15_0): 0,
json.dumps(ul.dict16_0): 0, json.dumps(ul.dict17_0): 0,
json.dumps(ul.dict18_0): 0, json.dumps(ul.dict19_0): 0, json.dumps(ul.dict20_0): 0, json.dumps(ul.dict21_0): 0, json.dumps(ul.dict22_0): 0, json.dumps(ul.dict23_0): 0,
json.dumps(ul.dict24_0): 0,
 
json.dumps(ul.dict1_1): 0,
json.dumps(ul.dict2_1): 0, json.dumps(ul.dict3_1): 0, json.dumps(ul.dict4_1): 0, json.dumps(ul.dict5_1): 0, json.dumps(ul.dict6_1): 0, json.dumps(ul.dict7_1): 0,
json.dumps(ul.dict8_1): 0, json.dumps(ul.dict9_1): 0, json.dumps(ul.dict10_1): 0,
json.dumps(ul.dict11_1): 0, json.dumps(ul.dict12_1): 0, json.dumps(ul.dict13_1): 0, json.dumps(ul.dict14_1): 0, json.dumps(ul.dict15_1): 0, json.dumps(ul.dict16_1): 0,
json.dumps(ul.dict17_1): 0, json.dumps(ul.dict18_1): 0,
json.dumps(ul.dict19_1): 0, json.dumps(ul.dict20_1): 0, json.dumps(ul.dict21_1): 0, json.dumps(ul.dict22_1): 0, json.dumps(ul.dict23_1): 0, json.dumps(ul.dict24_1): 0,

json.dumps(cur.dict1_0): 0, json.dumps(cur.dict2_0): 0, json.dumps(cur.dict3_0): 0, json.dumps(cur.dict4_0): 0, json.dumps(cur.dict5_0): 0, json.dumps(cur.dict6_0): 0,
json.dumps(cur.dict7_0): 0, json.dumps(cur.dict8_0): 0,
json.dumps(cur.dict9_0): 0, json.dumps(cur.dict10_0): 0, json.dumps(cur.dict11_0): 0, json.dumps(cur.dict12_0): 0, json.dumps(cur.dict13_0): 0,
json.dumps(cur.dict14_0): 0, json.dumps(cur.dict15_0): 0, json.dumps(cur.dict16_0): 0,
json.dumps(cur.dict17_0): 0, json.dumps(cur.dict18_0): 0, json.dumps(cur.dict19_0): 0, json.dumps(cur.dict20_0): 0, json.dumps(cur.dict21_0): 0,
json.dumps(cur.dict1_1): 0, json.dumps(cur.dict2_1): 0, json.dumps(cur.dict3_1): 0,
json.dumps(cur.dict4_1): 0, json.dumps(cur.dict5_1): 0, json.dumps(cur.dict6_1): 0, json.dumps(cur.dict7_1): 0, json.dumps(cur.dict8_1): 0, json.dumps(cur.dict9_1): 0,
json.dumps(cur.dict10_1): 0, json.dumps(cur.dict11_1): 0,
json.dumps(cur.dict12_1): 0, json.dumps(cur.dict13_1): 0, json.dumps(cur.dict14_1): 0, json.dumps(cur.dict15_1): 0, json.dumps(cur.dict16_1): 0,
json.dumps(cur.dict17_1): 0, json.dumps(cur.dict18_1): 0, json.dumps(cur.dict19_1): 0,
json.dumps(cur.dict20_1): 0, json.dumps(cur.dict21_1): 0, json.dumps(cur.Sdict1_0): 0, json.dumps(cur.Sdict2_0): 0, json.dumps(cur.Sdict3_0): 0,
json.dumps(cur.Sdict4_0): 0, json.dumps(cur.Sdict5_0): 0, json.dumps(cur.Sdict6_0): 0,
json.dumps(cur.Sdict7_0): 0, json.dumps(cur.Sdict8_0): 0, json.dumps(cur.Sdict9_0): 0, json.dumps(cur.Sdict10_0): 0, json.dumps(cur.Sdict11_0): 0,
json.dumps(cur.Sdict12_0): 0, json.dumps(cur.Sdict13_0): 0,
json.dumps(cur.Sdict14_0): 0, json.dumps(cur.Sdict15_0): 0, json.dumps(cur.Sdict16_0): 0, json.dumps(cur.Sdict17_0): 0, json.dumps(cur.Sdict18_0): 0,
json.dumps(cur.Sdict19_0): 0, json.dumps(cur.Sdict20_0): 0,
json.dumps(cur.Sdict21_0): 0, json.dumps(cur.Sdict1_1): 0, json.dumps(cur.Sdict2_1): 0, json.dumps(cur.Sdict3_1): 0, json.dumps(cur.Sdict4_1): 0,
json.dumps(cur.Sdict5_1): 0, json.dumps(cur.Sdict6_1): 0, json.dumps(cur.Sdict7_1): 0,
json.dumps(cur.Sdict8_1): 0, json.dumps(cur.Sdict9_1): 0, json.dumps(cur.Sdict10_1): 0, json.dumps(cur.Sdict11_1): 0, json.dumps(cur.Sdict12_1): 0,
json.dumps(cur.Sdict13_1): 0, json.dumps(cur.Sdict14_1): 0,
json.dumps(cur.Sdict15_1): 0, json.dumps(cur.Sdict16_1): 0, json.dumps(cur.Sdict17_1): 0, json.dumps(cur.Sdict18_1): 0, json.dumps(cur.Sdict19_1): 0,
json.dumps(cur.Sdict20_1): 0, json.dumps(cur.Sdict21_1): 0,
json.dumps(cur.Bdict1_0): 0, json.dumps(cur.Bdict2_0): 0, json.dumps(cur.Bdict3_0): 0, json.dumps(cur.Bdict4_0): 0, json.dumps(cur.Bdict5_0): 0,
json.dumps(cur.Bdict6_0): 0, json.dumps(cur.Bdict7_0): 0, json.dumps(cur.Bdict8_0): 0,
json.dumps(cur.Bdict9_0): 0, json.dumps(cur.Bdict10_0): 0, json.dumps(cur.Bdict11_0): 0, json.dumps(cur.Bdict12_0): 0, json.dumps(cur.Bdict13_0): 0,
json.dumps(cur.Bdict14_0): 0, json.dumps(cur.Bdict15_0): 0,
json.dumps(cur.Bdict16_0): 0, json.dumps(cur.Bdict17_0): 0, json.dumps(cur.Bdict18_0): 0, json.dumps(cur.Bdict19_0): 0, json.dumps(cur.Bdict20_0): 0,
json.dumps(cur.Bdict21_0): 0,
json.dumps(ls.dict1): 0, json.dumps(ls.dict13): 0, json.dumps(ls.dict2): 0, json.dumps(ls.dict14): 0, json.dumps(ls.dict3): 0, json.dumps(ls.dict4): 0, json.dumps(ls.dict5): 0,
json.dumps(ls.dict6): 0, json.dumps(ls.dict7): 0, json.dumps(ls.dict8): 0, json.dumps(ls.dict9): 0,
json.dumps(ls.dict10): 0, json.dumps(ls.dict11): 0, json.dumps(ls.dict12): 0,
json.dumps(fk.dict1): 0, json.dumps(fk.dict2): 0, json.dumps(fk.dict3): 0, json.dumps(fk.dict4): 0, json.dumps(fk.dict5): 0, json.dumps(fk.dict6): 0, json.dumps(fk.dict7): 0,
json.dumps(fk.dict8): 0, json.dumps(fk.dict9): 0, json.dumps(fk.dict10): 0, json.dumps(fk.dict11): 0,
json.dumps(fk.dict12): 0, json.dumps(fk.dict13): 0, json.dumps(fk.dict14): 0, json.dumps(fk.dict15): 0, json.dumps(fk.dict16): 0, json.dumps(fk.dict17): 0, json.dumps(fk.dict18): 0,
json.dumps(fk.dict19): 0, json.dumps(fk.dict20): 0, json.dumps(fk.dict21): 0,
json.dumps(fk.dict22): 0,
json.dumps(ins.Intersectiondict1): 0, json.dumps(ins.Intersectiondict2): 0, json.dumps(ins.Intersectiondict3): 0,
json.dumps(tj.Jdict1): 0, json.dumps(tj.Jdict2): 0, json.dumps(tj.Jdict3): 0, json.dumps(tj.Jdict4): 0, json.dumps(tj.Jdict5): 0, json.dumps(tj.Jdict6): 0, json.dumps(tj.Jdict7): 0,
json.dumps(tj.Jdict8): 0, json.dumps(tj.Jdict9): 0, json.dumps(tj.Jdict10): 0, json.dumps(tj.Jdict11): 0, json.dumps(tj.Jdict12): 0, json.dumps(tj.Jdict13): 0,
json.dumps(tj.Jdict14): 0, json.dumps(tj.Jdict15): 0, json.dumps(tj.Jdict16): 0, json.dumps(tj.Jdict17): 0, json.dumps(tj.Jdict18): 0, json.dumps(tj.Jdict19): 0,
json.dumps(tj.Jdict20): 0, json.dumps(tj.Jdict21): 0, json.dumps(tj.Jdict22): 0, json.dumps(tj.Jdict23): 0, json.dumps(tj.Jdict24): 0, json.dumps(tj.Jdict25): 0,
json.dumps((rdb.dict1)): 0,
                   }
    ######################################################################################

    COMPILE_RULES = {
        'lane_width': [2.5, 3, 3.5, 4],
        'lane_length': [100,120, 140, 160, 180, 200,220,240,260,280,300,320,350],  # [min,max]
        'lane_R': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],  # [min,max]
        'ulane_D': [16,18,20,22,24,26,28,30],  # [min,max]
        'ulane_X': [5, 6, 7, 8, 9, 10, 11, 12,13,14,15],  # [min,max]
        'direction': [0, 1, 2],
        'controlPoint': [],
        'curveSetOffset': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'curveSetLength': [100,120, 140, 160, 180, 200,220,240,260,280,300,320,350]
    }

    COMPILE_PREF = {}

    WidgetNumber = 8
    parameterupdate = 0
    widgetupdate = 0
