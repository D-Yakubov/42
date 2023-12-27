num = int(input("1 dan n gacha son kiriting: "))

for n in range(1, num+1):
    if n % 3 == 0 and n % 5 == 0:
        flag = "fizbuz"
    elif n % 5 == 0:
        flag = "buz"
    elif n % 3 == 0:
        flag = "fiz"
    else:
        flag = n

print(flag)
