#Leap Year https://www.mathsisfun.com/leap-years.html

#we need take a number from users and then check that number is leap or not

num = int(input("Enter a number: "))
#we declared a flag which is named: isLeapYear
isLeapYear = False
if (num % 4 == 0 and num % 100 != 0) or (num % 400  == 0):
    isLeapYear = True
else:
    isLeapYear = False
print(f"{num} is Leap Year? {isLeapYear}")
