#Задание 1
from math import *

#Функция
def f(n):
  return (1 - n)**0.5 - tan(n)

#Переменные
esp = 0.0001
L, R = 0, 1
B = 0
step = 0

#Цикл
while abs(R - L) > esp:
  step += 1
  B = (L + R) / 2
  if f(L) * f(B) < 0:
    R = B
  else:
    L = B
  print(step, B)
print(B)


#Задание 2
from math import *

def f(n):
  return (1 - n)**0.5 - tan(n)

esp = 0.0001
a, b = 0, 1
step = 0

#Формула хорды и сравнение с предыдущим шагом
xk = a - ((f(a) * (b - a)) / (f(b) - f(a)))
xk1 = a

while abs(xk - xk1) > esp:
  if f(xk1) * f(xk) < 0:
    b = xk
  else:
    a = xk
  
  xk1 = xk
  xk = a - ((f(a) * (b - a)) / (f(b) - f(a)))
  step += 1
  print(step, xk)
print(xk)
