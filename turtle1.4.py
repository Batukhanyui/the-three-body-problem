import math as m
from random import*
import turtle as t
import numpy as np
import matplotlib as plt

n=3  #количесвтво частиц
dt=0.1
time=1000
G=6.67*10**4
pool = [t.Turtle(shape='circle') for i in range(n)]
def force(r):
    return -G/r**2
def distance(el1, el2):
    return m.sqrt((particlesXcoordinate[el1] - particlesXcoordinate[el2])**2+(particlesYcoordinate[el1] - particlesYcoordinate[el2])**2)
def accelerationX(x):
    result = 0
    for el in range(n):
        if (el==x):
            result=result+0
        else:
            result = result + force(distance(el, x))*(particlesXcoordinate[x]-particlesXcoordinate[el])/distance(el, x) 
    return result/mass[x]
def accelerationY(x):
    result =0
    for el in range(n):
        if (el==x):
            result=result+0
        else:
            result = result + force(distance(el, x))*(particlesYcoordinate[x]-particlesYcoordinate[el])/distance(el, x)
    return result/mass[x]
particlesXcoordinate = [randint(-200., 200.) for i in range(n)]
particlesYcoordinate = [randint(-200., 200.) for i in range(n)]
particlesXvelocity = [randint(-50., 50.) for i in range(n)]
particlesYvelocity = [randint(-50., 50.) for i in range(n)]
mass = [0.5] * n

for unit in pool:
    unit.penup()
    unit.speed(150)
    unit.goto(particlesXcoordinate[pool.index(unit)], particlesYcoordinate[pool.index(unit)])
    unit.pendown()
for ul in range(time):
    for el in range(n):
        particlesXvelocity[el] = particlesXvelocity[el] + accelerationX(el)*dt
        particlesYvelocity[el] = particlesYvelocity[el] + accelerationY(el)*dt
    for el in range(n):
        particlesXcoordinate[el] = particlesXcoordinate[el] + particlesXvelocity[el]*dt
        particlesYcoordinate[el] = particlesYcoordinate[el] + particlesYvelocity[el]*dt
    for unit in pool:
        unit.speed(150)
        unit.goto(particlesXcoordinate[pool.index(unit)], particlesYcoordinate[pool.index(unit)])
for unit in pool:
    t.done()