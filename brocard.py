import math
from decimal import *
import numpy as np


def get_maxes():
    n_max = input("n_max: ")
    while n_max.isnumeric() == 0:
        n_max = input("Enter integer n_max: ")
    n_max = int(n_max)

    i_max = input("i_max: ")
    while i_max.isnumeric() == 0:
        i_max = input("Enter integer i_max: ")
    i_max = int(i_max)

    getcontext().prec = len(str(math.factorial(n_max)+i_max))

    return n_max, i_max


def get_factorials(n_max):
    factorials = [Decimal(math.factorial(i)) for i in range(0, n_max)]
    array = np.array(factorials)

    return array


def clear_solutions():
    f = open("solutions.txt", "w")
    f.write("")
    f.close()


def get_solutions(n_max, i_max, array):
    s_list, n_list, i_list, m_list = [], [], [], []
    f = open("solutions.txt", "a")

    for i in range(0, i_max):
        s, n = 0, 0
        ms = np.sqrt(array+i)

        while n != n_max-1:
            n += 1
            m = ms[n]

            if m == int(m):
                s += 1

                print(f"{n}, {i}, {m}")
                f.write(f"{n}, {i}, {m}\n")
                n_list.append(n)
                i_list.append(i)
                m_list.append(int(m))
        s_list.append(s)

    f.close()
    return s_list, n_list, i_list, m_list


def get_brocard():
    n_max, i_max = get_maxes()
    array = get_factorials(n_max)
    clear_solutions()
    s_list, n_list, i_list, m_list = get_solutions(n_max, i_max, array)
    return i_max, s_list, n_list, i_list, m_list
