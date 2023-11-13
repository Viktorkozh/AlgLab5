#!/usr/bin/env python3 
#coding: utf-8 -*-

import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import curve_fit

number_of_dots = 100
e, o, mid = 0, 0, 0
nod = (number_of_dots + 10) * 10
a = {}
worst_time = {}
graph_stuff = [i for i in range(10, nod, 10)]
oarr = []
earr = []
something = {}


def sort(a, n):
    for j in range(1, n - 1):
        f = 0
        for i in range(n - 1 - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        if f == 0:
            return 0


def fill_arr(num_of_el):
    a.clear()
    for i in range(num_of_el):
        a[i] = random.randint(0, 100000)


def fill_arr_worst(num_of_el):
    a.clear()
    for i in range(num_of_el):
        a[i] = 100 - i


def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c


def lsm(name):
    x_data = np.array(graph_stuff)
    y_data = np.array(list(worst_time.values()))

    params, trash = curve_fit(quadratic_model, x_data, y_data)

    a_fit, b_fit, c_fit = params
    print(f"Коэффициенты уравнения ({name}): a = {a_fit}, b = {b_fit}, c = {c_fit}")

    x_fit = np.linspace(min(x_data), max(x_data), 100)
    y_fit = quadratic_model(x_fit, *params)

    plt.plot(x_fit, y_fit, "r-", label="Quadratic Fit")

if __name__ == '__main__':
    plt.figure(1).set_figwidth(8)
    plt.xlabel("Количество элементов в массиве")
    plt.ylabel("Среднее время выполнения (секунды)")
    plt.title("Зависимость времени сортировки от размера массива\n(Средний случай)")

    for i in range(10, nod, 10):
        fill_arr(i)
        mid, e, o = 0, 0, 0
        for j in range(30):
            worst_time[i] = timeit.timeit(lambda: sort(a, i + 1), number=1)
            mid += worst_time[i]
            e += 1 / 30 * worst_time[i]
            plt.scatter(i - 1, worst_time[i], s=2, c="green")
            something[j] = worst_time[i]
        worst_time[i] = mid / 30
        for s in something:
            o += 1 / 29 * (something[s] - e) ** 2
        o = m.sqrt(o)
        oarr.append(o)
        earr.append(e)

    plt.tight_layout()
    plt.grid(False)

    plt.figure(2).set_figwidth(8)
    plt.xlabel("Количество элементов в массиве")
    plt.ylabel("Среднее время выполнения (секунды)")
    plt.title("Зависимость времени сортировки от размера массива\n(Средний случай)")

    for i in range(10, nod, 10):
        plt.errorbar(i, earr[i // 10 - 1], yerr=oarr[i // 10 - 1], fmt="none", capsize=5)

    plt.scatter(graph_stuff, worst_time.values(), s=5, c="orange")
    plt.tight_layout()
    plt.grid(False)

    lsm("Средний случай")

    # Case 3
    plt.figure(3).set_figwidth(8)
    plt.xlabel("Количество элементов в массиве")
    plt.ylabel("Среднее время выполнения (секунды)")
    plt.title("Зависимость времени сортировки от размера массива\n(Худший случай)")

    for i in range(10, nod, 10):
       fill_arr_worst(i)
       worst_time[i] = timeit.timeit(lambda: sort(a, i + 1), number=1)

    plt.scatter(graph_stuff, worst_time.values(), s=5, c="orange")

    lsm("Худший случай")

    plt.tight_layout()
    plt.grid(False)

    plt.show()