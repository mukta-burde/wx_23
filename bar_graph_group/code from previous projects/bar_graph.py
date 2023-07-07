import numpy as np
import matplotlib.pyplot as plt
from FigureAndAxes import makeAxes
from FigureAndAxes import makeFigure

#random test data generated
arr = np.random.rand(2200)
arr.shape
print(arr)
bins = 39
def bargraph(arr, bins):
#actual code
    bars = []
    data = np.array_split(arr,bins)
    x = np.linspace(-0.5,10.5,bins)
#to take avg of data for each bar so it can be plotted.
    for i in data:
        count = 0
        total = 0
        for j in i:
            count = count+1
            total = total+j
        bars.append(total/count)
#create figure and axes         
    axes = makeAxes(x,bars)
    a = [axes]
    figure = makeFigure(1,1,a)
#plot bars
    axes.bar(x,bars)
    return figure
    return arr
f = bargraph(arr, bins)
plt.show()
