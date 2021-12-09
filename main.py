# -*- coding: UTF-8 -*-
import pandas as pd
from multiprocessing import Pool
from time import time
from matplotlib import pyplot as plt
import numpy as np

def chunk_using_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
    return lst

def calculate(*data):
    """сумма всех активных случаев"""
    a=list(data)
    return sum(a)


df = pd.read_csv("data.csv", sep=",", encoding='windows-1251')
print(df["Активные случаи"].tolist())
calculate()

if __name__=="__main__":
    """находим время работы при разном количестве процессов и выводим массив из времен"""
    #time_1 = time()
    lst=[]
    for i in range(1, 8):
        time_1 = time()
        print(chunk_using_generators(df["Активные случаи"].tolist(),i))
        with Pool(i) as p:
            print(p.apply(calculate, df["Активные случаи"].tolist()))
        a=time() - time_1
        lst.append(a)
        print(time() - time_1)
    print(lst)
    """Создаем точечную диаграмму используя время """
    fig=plt.figure(figsize=(10, 10))
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('y=sinc(x)')
    plt.scatter(list(range(1,8)),lst, color='teal', marker='o', linewidths=2, facecolors='none')
    plt.show()