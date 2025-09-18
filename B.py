# 單位轉換程式

# 長度轉換：公里 ↔ 英里
km = float(input("請輸入長度（公里）："))
mile = km * 0.621371
print(f"{km} 公里 = {mile:.2f} 英里")

# 溫度轉換：攝氏 ↔ 華氏
celsius = float(input("請輸入溫度（攝氏）："))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")

# 重量轉換：公斤 ↔ 磅
kg = float(input("請輸入重量（公斤）："))
pound = kg * 2.20462
print(f"{kg} 公斤 = {pound:.2f} 磅")