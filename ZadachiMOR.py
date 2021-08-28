'''Найдите сумму всех чисел меньше 1000, кратных 3 или 5.'''
# sum=0
# for i in range(1,1000):
#     if (i%3==0 or i%5==0):
#         sum+=i
# print(sum)
'''Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.'''
# mas=[0,1]
# sum = 0
# for i in range(2,1000):
#     mas.append(mas[i-1]+mas[i-2])
#     if mas[i] >= 4000000:
#         break
#     if mas[i]%2==0:
#         sum+=mas[i]
# print(sum)
'''Каков самый большой делитель числа 600851475143, являющийся простым числом?'''
# def simpleDividers(n):
#    answer = []
#    d = 2
#    while d * d <= n:
#        if n % d == 0:
#            answer.append(d)
#            n //= d
#        else:
#            d += 1
#    if n > 1:
#        answer.append(n)
#    return answer
# print(max(simpleDividers(600851475143)))
'''Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.'''
# maximum = 0
# for i in range (900,1000):
#     for j in range (900,1000):
#         c = i*j
#         s = str(c)
#         s_reversed = s[::-1]
#         '''s_reversed = [::-1] v s_reserved poluchaet revers chisla s , [::-1]==list[<start>:<stop>:<step>]'''
#         if s == s_reversed and c > maximum:
#             maximum = int(s)
# print (maximum)
'''Какое самое маленькое число делится нацело на все числа от 1 до 20?'''
# for i in range(2520,1000000):
#     if i%2==0 and i%3==0 and i%5==0 and i%7==0 and i%11 and i%13==0 and i%17==0 and i%19==0:
#         print(i)
'''Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.'''
# c=0
# z=0
# for i in range(1,101):
#     c+=i
# c=c**2
# for i in range(1,101):
#     z+=i**2
# print("Raznost = ",c-z)
'''Какое число является 10001-м простым числом?'''
# import math
# count=0
# for num in range(2,1000000000):
#     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#         count+=1
#         if count==10001:
#             print(num)
#             break
'''Существует только одна тройка Пифагора, для которой a + b + c = 1000.Найдите произведение abc.'''
# for i in range(1,500):
#     for j in range(1,500):
#         for z in range(1,500):
#             if i**2+j**2==z**2 and i+j+z==1000:
#                 print(i,j,z)
#                 print(i*j*z)
