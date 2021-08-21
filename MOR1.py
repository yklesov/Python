import random

pc = random.randint(0, 5)
x = 0
y = 0
user = input("Nermuceq tiv = ")
if user == pc:
    x = x + 1
    print(pc)
    user = input("Nermuceq tiv = ")
    pc = random.randint(0, 5)
    if user == pc:
        x = x + 1
        print(pc)
        print("User win")
    else:
        y = y + 1
        print(pc)
        user = input("Nermuceq tiv = ")
        pc = random.randint(0, 5)
        if user == pc:
            x = x + 1
            print(pc)
            print("User win")
        else:
            y = y + 1
            print(pc)
            print("Pc win")
else:
    y = y + 1
    print(pc)
    user = input("Nermuceq tiv = ")
    pc = random.randint(0, 5)
    if user == pc:
        x = x + 1
        print(pc)
        user = input("Nermuceq tiv = ")
        pc = random.randint(0, 5)
        if user == pc:
            x = x + 1
            print(pc)
            print("User win")
        else:
            y = y + 1
            print(pc)
            print("Pc win")

    else:
        y = y + 1
        print(pc)
        print("Pc win")