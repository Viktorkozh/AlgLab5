import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

NumberOfDots = 100
NOD = (NumberOfDots + 10) * 10
a = {}
worstTime = {}
medianTime = {}
GraphStuff = np.linspace(0, 10, 101)#[i for i in range(10, NOD, 10)]
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

for i in range(10, NOD, 10):
    fillArr(i)
    worstTime[i] = timeit.timeit(lambda:sort(a, i+1), number = 1)

for i in range(10, NOD, 10):
    fillArr(i)
    medianTime[i] = timeit.timeit(lambda:sort(a, i+1), number = 1)

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(list(worstTime.values())), rcond = None)[0]
alpha = np.exp(log_alpha)
GraphStuff = np.array(GraphStuff)

plt.figure(1).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Худший случай)')
plt.scatter(GraphStuff, worstTime.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha*np.exp(beta*GraphStuff), 'r')

A = np.vstack([GraphStuff, np.ones(len(GraphStuff))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(list(medianTime.values())), rcond = None)[0]
alpha = np.exp(log_alpha)
GraphStuff = np.array(GraphStuff)

plt.figure(2).set_figwidth(8)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Среднее время выполнения (секунды)')
plt.title('Зависимость времени поиска элемента от размера массива\n(Средний случай)')
plt.scatter(GraphStuff, medianTime.values(), s=5)
plt.grid(False)
plt.plot(GraphStuff, alpha*np.exp(beta*GraphStuff), 'r')

plt.show()