# Сортировать список от меньшего к большему с помощью heapq
from random import random
import heapq
k = int(input('введите длину списка'))
a = []
for i in range(k):
    a.append(int(random()*10))
print(a)
heapq.heapify(a)
a=heapq.nsmallest(len(a), a)
print(a)