import numpy as np

np.random.seed(100)
a = np.random.rand(100)
X = np.random.rand(1000, 10)

# exp1: 計算 r[i, j] = a[i] - a[j]
exp1 = 'np.subtract.outer(a, a)'
r = eval(exp1)

# 計算 X 中每個向量的平方和
X2 = np.sum(X**2, axis=1, keepdims=True)

# exp2: 計算歐幾里得距離矩陣 D
exp2 = "np.sqrt(np.maximum(X2 + X2.T - 2 * np.dot(X, X.T), 0))"
D = eval(exp2)

# 輸出 D 的形狀
print(D.shape)  # 應為 (1000, 1000)
exp3 = "np.sum(np.triu(D < 2, k=1))"


exp4 = "np.where(np.triu(D < 2, k=1))"

exp5 = "np.argmin(np.where(np.eye(D.shape[0], dtype=bool), np.inf, D), axis=1)"