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