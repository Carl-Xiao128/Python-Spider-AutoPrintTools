'''
Created on 2016年10月21日

@author: kitxiao
'''
#demo1
# import math
#  
# def quadratic(a,b,c):
#     if a == 0:
#         return('a为0，非一元二次方程。')
#     elif a != 0:
#         delta = b*b - 4*a*c
#         if delta < 0:
#             return(None)
#         elif delta == 0:
#             return(-b/(2*a))
#         else:
#             return((-b - math.sqrt(delta))/(2*a),(-b + math.sqrt(delta))/(2*a))
#  
# print('ax^2 + bx + c = 0公式解法\n请输入各项系数：')
# a = float(input('a='))
# b = float(input('b='))
# c = float(input('c='))
# print(quadratic(a,b,c))

#demo2
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# 
# num=[1,2,3]
# print(calc(*num))

#demo3
# def person(name, age, **kw):
#     print('name:', name, ';age:', age, ';other:', kw)
#     
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person("xiao", 19,**extra)
    
#demo4
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#         print('name:', name, 'age:', age, 'other:', kw) 
#      
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)    
    
    
#demo5
# def person(name, age, *, city, job):
#     print(name, age, city, job)   
#      
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456,job='ccc')       
    
    
#demo6
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)    
# 
# person('Jack', 24, 'Beijing', 'Engineer',city='ss',job='cc')    
    
#demo7
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw,'\n')
#      
# def f3(a, b, c=0, *args,aa, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, aa,'kw =', kw,'\n')
#  
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw,'\n')  
#      
# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, 'a', 'b')   
# f3(1, 2, 3, 'a', 'b',aa='aa')   
# f1(1, 2, 3, 'a', 'b', x=99)    
# f2(1, 2, d=99, ext=None)    
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f1(*args, **kw)
    
#demo8
print('汉诺塔移动')
def move(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print('11111','a','-->',c)
        move(n-1,b,a,c)
n=int(input('请输入n的值:'))
move(n,'a','b','c')





















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    