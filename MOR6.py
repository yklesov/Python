'''Calculator'''
# d=int(input("Nermuceq araji arjeq@ "))
# b=int(input("Nermuceq erkrord arjeq@ "))
# c=input("Nermuceq ays gorcoxutyunneric mek@ : +,-,/,*  ")
# def Calculator(arg1,arg2,act):
#     if act=="/":
#        answ=arg1//arg2
#     elif act=="*":
#         answ=arg1*arg2
#     elif act=="-":
#         answ=arg1-arg2
#     elif act=="+":
#         answ=arg1+arg2
#     return answ
# answ=Calculator(d,b,c)
# print(d,c,b," havasare ",answ)
'''Max of two numbers'''
# a=int(input("Nermuceq araji tiv@ "))
# b=int(input("Nermuceq ekrord tiv@ "))
# def Max(arg1,arg2):
#     if arg1>arg2:
#         print("Araji tiv@ mece")
#     elif arg1<arg2:
#         print("Erkrord tiv@ mece")
#     else:
#         print("Tver@ irar havasaren")
# Max(a,b)
''' sum all numbers'''
# a=input("NErmuceq tox ")
# def Sum(arg):
#     answ = 0
#     for i in arg:
#         c=i.isdigit()
#         if c==True:
#             answ+=int(i)
#     return answ
# print(Sum(a))
'''count all letter and number in your string'''
# a=input("Nermuceq tox ")
# def Count(arg):
#     count1=0
#     count2=0
#     for i in arg:
#         c=i.isdigit()
#         if c==True:
#             count1+=1
#         else:
#             count2+=1
#     return count1,count2
# print(Count(a))
'''ages'''
# a=int(input("Nermuceq araji tariq@ "))
# b=int(input("Nermuceq erkrord tariq@ "))
# c=int(input("Nermuceq errord tariq@ "))
# def Tariq(arg1,arg2,arg3):
#     while(True):
#         if arg1<16:
#             print("Too young!")
#             break
#         else:
#             print("Get ready!")
#         if arg2<16:
#             print("Too young!")
#             break
#         else:
#             print("Get ready!")
#         if arg3<16:
#             print("Too young!")
#             break
#         else:
#             print("Get ready!")
#         break
# Tariq(a,b,c)