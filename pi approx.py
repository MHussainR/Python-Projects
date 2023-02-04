import cv2 as cv
import numpy as np
from random import randint, choice
from time import sleep
import matplotlib.pyplot as mt
from math import pi, inf

blank = np.zeros([600,600,3], np.uint8)

cv.circle(blank, (300, 300), 125, (255, 0, 0), 1)
cv.rectangle(blank, (50, 50), (550, 550), (255, 0, 0), 1)

green = [(0, 255, 0), (255, 255, 255)]
red = [(0, 0, 255), (0, 150, 255)]

total = 0
asal = 0
totalL = []
asall = []
valu = []
lst = []
min_mod = inf
count = 0

while total < 5000:
    blank2 = np.zeros([600,600,3], np.uint8)

    total += 1
    cv.imshow('points', blank)

    x = randint(50, 550)
    y = randint(50, 550)

    calc = ((x-300)**2) + ((y-300)**2)

    if calc <= (125**2):
        cv.circle(blank, (x, y), 3, choice(green), -1)
        asal += 1

    else:
        cv.circle(blank, (x, y), 3, choice(red), -1)

    val = (asal/total)*16
    totalL.append(total)
    asall.append(val)
    valu += [pi]
    lst.append((val, total))
    cv.rectangle(blank2, (55, 25), (480, 115), (255, 255, 255), 1)
    cv.putText(blank2, f"Total points: {total}", (60, 50), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)
    cv.putText(blank2, f"Points inside the circle: {asal}", (60, 80), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)
    cv.putText(blank2, f"Approx pi: {val}", (60, 110), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)
    cv.line(blank2, (0, int(pi*100)), (600, int(pi*100)), (255, 255, 255), 1)
    for i in range(len(lst)-1):
        if total > 280:
            cv.line(blank2, ((lst[i][1]-count)*2, -(int(lst[i][0]*100))+int(pi*100*2)), (((lst[i+1][1]-count)*2), -(int(lst[i+1][0]*100))+int(pi*100*2)), (254, 197, 61), 2)
        else:
            cv.line(blank2, (lst[i][1]*2, -(int(lst[i][0]*100))+int(pi*100*2)), ((lst[i+1][1]*2), -(int(lst[i+1][0]*100))+int(pi*100*2)), (254, 197, 61), 2)
    if total > 280:
        count += 1
        lst.pop(0)
    cv.rectangle(blank2, (0,0), (50, 600), (0, 0, 0), -1)
    cv.line(blank2, (50, 0), (50, 600), (255, 255, 255), 2)
    cv.putText(blank2, "pi", (20, int(pi*100)+5), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 255), 1)
    cv.imshow("graph", blank2)
    if total > 50:
        if (val % pi) < min_mod:
            mn = [val, total]
            min_mod = (val % pi)
    # sleep(0.01)
    cv.waitKey(1)

mt.plot(totalL, asall, totalL, valu)

print ('The obtained value of pi is', val)
print ('The closest value of pi obtained is', mn[0], "at the point number", mn[1])
print ("Original:", pi, "\nObtained:", mn[0])
mt.show()