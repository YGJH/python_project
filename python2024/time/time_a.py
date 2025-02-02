from datetime import datetime

# 輸入兩個時間
time1_str = input()
time2_str = input()

# 將字串轉換為datetime物件
time1 = datetime.strptime(time1_str, "%Y-%m-%d %H:%M:%S")
time2 = datetime.strptime(time2_str, "%Y-%m-%d %H:%M:%S")

# 計算時間差
time_diff = time1 - time2 if time1 > time2 else time2 - time1

# 計算天數和秒數
days = time_diff.days
seconds = time_diff.seconds

# 計算總秒數
total_seconds = time_diff.total_seconds()

# 輸出結果
print(f"{days} {seconds}")
print(int(total_seconds))