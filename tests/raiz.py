import array
import random
import numpy as np
import os
from scipy.optimize import minimize

os.system("clear")


def baskara(x):
    return x*x+3*x-10


def calcularFaval(population):
    fx = []
    i = 0

    while i < len(population):
        faval = (baskara(population[i][0]))
        fx.append(abs(faval))
        i = i+1

    return fx


x0 = np.array([2])
res = minimize(
    baskara,
    x0,
    method = 'nelder-mead',
    options = {
        'xatol' : 1e-3,
        'disp' : True}
)
print(res)
