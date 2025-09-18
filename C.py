print("歡迎使用單位轉換程式！")
print("請選擇想要轉換的類型：")
print("1. 長度 (公里 → 英里)")
print("2. 溫度 (攝氏 → 華氏)")
print("3. 重量 (公斤 → 磅)")

choice = input("輸入選項 (1/2/3)：")

if choice == "1":
    km = float(input("請輸入長度（公里）："))
    mile = km * 0.621371
    print(km, "公里 =", round(mile, 2), "英里")

elif choice == "2":
    celsius = float(input("請輸入溫度（攝氏）："))
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "°C =", round(fahrenheit, 2), "°F")

elif choice == "3":
    kg = float(input("請輸入重量（公斤）："))
    pound = kg * 2.20462
    print(kg, "公斤 =", round(pound, 2), "磅")

else:
    print("無效選項！請輸入 1、2 或 3。")