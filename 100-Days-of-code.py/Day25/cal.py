import calendar

year = int(input("Enter your year: "))
month = int(input("Enter your month: "))
day = int(input("Enter your day: "))
cal = calendar.month(year, month, day)
print(cal)