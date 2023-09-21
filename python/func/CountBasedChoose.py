import random
import json

from settings.info import Info
from straigntlane_widget import StraightLaneLibrary as st


def CountBasedChoose(widgetlist,widgetcount):
    subdict = extract_subset_by_keys(widgetcount, widgetlist)
    # print(len(subdict))
    dict1 = get_key_with_min_value_random(subdict)
    dict2 =json.loads(dict1)
    dict2['Start'] = tuple(dict2['Start'])
    if dict2.__contains__('LW'):
        dict2['LW'] = tuple(dict2['LW'])
    if dict2.__contains__('DX'):
        dict2['DX'] = tuple(dict2['DX'])
    if dict2.__contains__('CurveSet'):
        dict2['CurveSet'] = tuple(dict2['CurveSet'])
    if dict2.__contains__('ControlPoint'):
        dict2['ControlPoint'] = [tuple(i) for i in dict2['ControlPoint']]
    return dict2

def extract_subset_by_keys(original_dict,keys_list):
    # key 是字典，无法直接索引
    return {json.dumps(key,ensure_ascii=False): original_dict[json.dumps(key)] for key in keys_list if json.dumps(key) in original_dict}

def get_key_with_min_value_random(dictionary):
    min_value = min(dictionary.values())
    keys_with_min_value = [key for key, value in dictionary.items() if value == min_value]
    return random.choice(keys_with_min_value)


# a = [st.dict1, st.dict7, st.dict8, st.dict10, st.dict15, st.dict5]
# b = CountBasedChoose(a,widgetcount)
# print(b)
# print(type(b))
# c = json.dumps(b)
# print(type(c))
# widgetcount[c] += 1
# print(widgetcount.values())