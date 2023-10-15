import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
import math as m

NumberOfDots = 100
NOD = (NumberOfDots + 10) * 10
mid = 0
a = {}
worstTime = {}
medianTime = {}
GraphStuff = [i for i in range(10, NOD, 10)]
StuffForLsmWorst = {}
StuffForLsmMedian = {}

def sort(a, n):
    for j in range(1, n-1):
        f=0
        for i in range(n-1-j):
            if (a[i]>a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
        if f == 0:
            return 0

def fillArr(numOfEl):
    a.clear()
    for i in range(numOfEl):
        a[i] = random.randint(0, 100000)

plt.figure(1).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Худший случай)')

for i in range(10, NOD, 10):
    fillArr(i)
    mid = 0
    for j in range(30):
        worstTime[i] = timeit.timeit(lambda:sort(a, i+1), number = 1)
        mid += worstTime[i]
        e = 1 / 30 * worstTime[i]
        o = m.sqrt(1 / 29 * (worstTime[i] - e) ** 2)
        plt.scatter(i-1, worstTime[i], s=5, c='green')
    worstTime[i] = mid / 30
    plt.errorbar(i, e, yerr=o, fmt='none', capsize=2)

plt.scatter(GraphStuff, worstTime.values(), s=10, c='orange')
plt.tight_layout()
plt.grid(False)

plt.figure(2).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Средний случай)')

for i in range(10, NOD, 10):
    fillArr(i)
    mid = 0
    for j in range(30):
        medianTime[i] = timeit.timeit(lambda:sort(a, i+1), number = 1)
        mid += medianTime[i]
        plt.scatter(i-1, medianTime[i], s=5, c='green')
    medianTime[i] = mid / 30

plt.scatter(GraphStuff, medianTime.values(), s=5, c='orange')
plt.tight_layout()
plt.grid(False)


plt.show()