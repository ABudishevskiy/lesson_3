# Есть список. Нужно реализовать операцию левый и правый сдвиг на указанный шаг.
# Нужно решение с deque и без него. Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4].
from collections import deque
from random import random
a = []
for i in range(10):
    a.append(int(random()*10))
d=deque(a)
print(d)
n=int(input('введите сдвиг, отрицательный влево'))
d.rotate(n)
print(d)
print(list(d))
b = []
for i in range(10):
    b.append(a[(i-n)%10])
print(b)