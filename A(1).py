# calculator.py

# 輸入兩個數字
a = float(input("請輸入第一個數字: "))
b = float(input("請輸入第二個數字: "))

# 計算並輸出結果
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

# 避免除以 0
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("無法除以 0")