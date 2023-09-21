import json
from straigntlane_widget import StraightLaneLibrary as st

class TupleEncoder(json.JSONEncoder):
    def encode(self,obj):
        if isinstance(obj, tuple):
            return {"__tuple__": True, "data": list(obj)}

        return obj
def hint_tuple_hook(obj):
    if '__tuple__' in obj:
        return tuple(obj['data'])
    return obj

a = json.dumps(st.dict5, cls=TupleEncoder)
print(a)
b = json.loads(a,object_hook=hint_tuple_hook)
