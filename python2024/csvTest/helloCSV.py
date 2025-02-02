import csv
import numpy as np

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

pt = [Point(np.random.randint(0,1000)-500,np.random.randint(0,1000)-500) for _ in range(100)]

# 寫入 CSV 檔案
with open('points.csv', 'w', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])  # 寫入標題
    for point in pt:
        writer.writerow([point.x, point.y])

pt2 = []
with open('points.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        pt2.append(Point(int(row['x']), int(row['y'])))

# 顯示每個 Point 物件的內容
for p in pt2:
    print('x:{} y:{}'.format(p.x, p.y))