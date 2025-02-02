import numpy as np
import json
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

pt = [Point(np.random.randint(0,1000)-500,np.random.randint(0,1000)-500) for _ in range(100)]
def point_to_dict(obj):
    if isinstance(obj, Point):
        return {'x': obj.x, 'y': obj.y}
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

with open('point.txt', 'w') as file:
    json.dump(pt, file, default=point_to_dict)

def dict_to_point(d):
    return Point(d['x'], d['y'])

with open('points.txt', 'r') as file:
    pt2 = json.load(file, object_hook=dict_to_point)


for p in pt2:
    print('x:{} y:{}'.format(p.x,p.y))