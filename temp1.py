print("THE DAILY TEMPERATURE")

temperatures = [int(input(f"Enter temperature of Day {day}: ")) for  day in range(1, 8)]
for day, temp in enumerate(temperatures, start=1):
    print(f"DAY {day} TEMP: ", temp)