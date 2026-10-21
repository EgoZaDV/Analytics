#Зайцев Егор ЭФБО-01-26 Рабочая тетрадь №2
#Задание 1
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
d = int(input("Введите четвертое число:"))

def nod(x, y): #Функция вычисления НОД двух чисел
  while x != y:
    if y > x:
      x, y = y, x
    x -= y
  return x

print(nod(nod(nod(a, b), c), d))

#Задание 2
def factorize(n):
  x = 2
  divs = []
  while x*x <= n:
    while n % x == 0:
      divs.append(x)
      n //= x
    x += 1
  if n > 1:
    divs.append(n)
  return divs

def prime(n):
  m = [i for i in range(n+1)]
  m[1] = 0
  p = 2
  while p <= n:
    if m[p] != 0:
      j = p + p
      while j <= n:
        m[j] = 0
        j = j + p
    p += 1
  m = [i for i in m if i != 0]
  return m

a = int(input("Введите число:"))

print(factorize(a))
print(prime(a))

#Задание 3
n = int(input("Введите число: "))

def ferma(n):
  m = int(n ** 0.5)
  x = 1
  while not int(((m + x)**2 - n) ** 0.5) ** 2 == (m + x)**2 - n:
    x += 1
  A = m + x
  B = int((A**2 - n) ** 0.5)
  p = A + B
  q = A - B
  return q, p

def prime(n):
  m = [i for i in range(n+1)]
  m[1] = 0
  p = 2
  while p <= n:
    if m[p] != 0:
      j = p + p
      while j <= n:
        m[j] = 0
        j = j + p
    p += 1
  m = [i for i in m if i != 0]
  return m

print(ferma(n))
print(prime(n))

#Задание 4
p = int(input("Введите число: "))
S = 4
k = 1
M = 2**p - 1
while k != p - 1:
  S = ((S * S) - 2) % M
  k += 1

if S == 0:
  print("Число простое")
else:
  print("Число составное")

#Задание 5
n = int(input("Введите пятизначное число: "))

if len(str(abs(n))) == 5:
  for i in range(10):
    s = str(n**2)

    start = (len(s) - 5) // 2
    next = s[start:start+5]

    print(next)
    n = int(next)
else:
  print("Введено некорректное число")

#Задание 6
n = int(input())

k = (n - 1) // 2
check = [True] * (k+1)

answer = []

for i in range(1, k+1):
  if 2 * i + 2 * i**2 > k: #Если минимальное значение для текущего i (при j = i) больше k — выходим
    break
  for j in range(i, k+1):
    val = i+j+2*i*j

    if val > k:
      break
    check[val] = False

if n >= 2:
  answer.append(2)

for i in range(1, len(check)):
  if check[i]:
    answer.append(2*i+1)

print(answer)

