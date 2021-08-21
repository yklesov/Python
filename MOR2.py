# 3-rd xndir
# min_year=3
# max_year=10
# employee=int(input("Nermiceq dzer ashxatanqayin porc@ "))
# if (min_year<=employee and max_year>=employee):
#     print("Duq karoxeq ashxatel mer mot")
# else:
#     print("Nereceq duq cheq karox mer mot ashxatel")
# 5-rd xndir
# a = int(input("Nermuceq a-i arjeq@ "))
# b = int(input("Nermuceq b-i arjeq@ "))
# z = (a + b) ** 3
# print("(a+b)^3 = ", z)
# 6-rd xndir
# import random
# ran=random.randint(1,10)
# z=ran
# ran=random.randint(1,10)
# x=ran
# ran=random.randint(1,10)
# c=ran
# ran=random.randint(1,10)
# v=ran
# ran=random.randint(1,10)
# v=ran
# ran=random.randint(1,10)
# b=ran
# a=[z,x,c,v,b]
# ran=random.randint(1,10)
# pc=ran
# if pc==a[0] or pc==a[1] or pc==a[2] or pc==a[3] or pc==a[4]:
#     print(True)
# else:
#     print(False)
# 7-rd xndir
# x = int(input("Nermuceq tiv@ "))
# factorial = 1
#
# for i in range(2, x + 1):
#     factorial *= i
# print(factorial)
# 8-rd xndir
# gramm=int(input("Nermuceq grammer@ "))
# x=int(gramm/20)
# print(x,"cigaretes")
# 1-i xndir
# x=10.5
# dog=int(input("Nermuceq shan tariq@ "))
# if dog==1:
#     print("shan tariq@ = 5.25")
# elif dog==2:
#     print("Shan tariq@ = ",x)
# else:
#     z=dog-2
#     x+=z*4
#     print("Shan tariq@ = ",x)
# 2-rd xndir
# vower="aeuio"
# z=0
# user = input("Nermuceq tar ")
# for i in vower:
#     if user==i:
#         z=1
#     else:
#         z=0
# if z==1:
#     print("Your letter is vower")
# else:
#     print("Your letter is consonant")
# names = ["Hi","Nigger","Valod"]
# for i in names:
#     print(i)
# import random
# while True:
#     x=random.randint(0,5)
#     print(x)
# import random
# for i in range(2):
#     x=random.randint(0,10)
#     y=random.randint(0,10)
#     z=random.randint(0,10)
#     print(z,y,x)
import random

list=["qar","mkrat","tuxt"]
user_point=0
pc_point = 0
x=""
user = input("Nermuceq ")
for i in range(5):
    if user_point!=3 or pc_point!=3:
        if x := random.choice(list) == user:
            user_point += 1
            print("useri hashiv@ = ",user_point)
        else:
            pc_point += 1
            print("pc-i hashiv@ = ",pc_point)
    else:
        break
        print(pc_point,user_point)
    user = input("Nermuceq ")
