import calendar
while True: 
  print("========= SEE THE DAY YOU WERE BORN =========")
  print('\n')
  year = int(input("Enter a year, you were born : "))
  month = int(input("Enter a month, you were born : "))
  print("\r")
  print("== The result is : ==")
  print("\r")
  print(calendar.month(year, month))
# Good Luck
