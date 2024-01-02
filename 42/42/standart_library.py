from datetime import date

year_of_user = int(input("Enter your born year: "))
month_of_user = int(input("Enter your born month: "))
day_of_user = int(input("Enter your born day: "))

born_date_of_user = date(year_of_user, month_of_user, day_of_user)

print(date.today() - born_date_of_user)
