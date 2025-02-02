import matplotlib.pyplot as plt
import numpy as np

# 設定隨機種子以便重現結果
np.random.seed(100)
tmp = '0246813579'
tmp = [int(i) for i in tmp]
print(tmp)
# 假設 sel_img 是一個包含圖像數據的 NumPy 陣列
sel_img = np.array(tmp)  # 例子數據
print(f'sel_img 的形狀: {sel_img}')

# 定義 a, b, c, d, e 為張量的各個維度索引
a, b, c, d, e = 0, 1, 2, 3, 4

plt.figure(figsize=(5,5))
plt.imshow(sel_img.reshape((5,2,10,28,28)).transpose((a,b,c,d,e)).reshape((-1,280)), cmap='gray')
plt.axis(False)
plt.show()