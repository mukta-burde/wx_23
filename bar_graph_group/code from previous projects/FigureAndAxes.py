import matplotlib.pyplot as plt
import numpy as np
import math

x = [1,2,3,4,5]
y = [1,2,3,4,5]
x2 = [2,4,6,8]
y2 = [1,5,8,0]

def makeFigure(rows,columns,axes):
    """
    rows and columns should be sel explanatory
    axes is an array of axes that should be added, this must be done manually for
    now outside of the function
    """
    rows = rows*100
    columns = columns*10
    f = plt.figure()
    for x in range(len(axes)):
        y=x+1
        position = rows+columns+y
        print(position)
        axes[x].figure = f
        f.axes.append(axes[x])
        f.add_axes(axes[x])
        dummy = f.add_subplot(position)
        axes[x].set_position(dummy.get_position())
        dummy.remove()
    
    return f

def makeAxes(x,y,xLabel="",yLabel="",showGrid=True,name="line1"):
    """
    makes a normal set of axes but does not plot the data on it
    
    """
    f,ax = plt.subplots()
    #ax.plot(x,y,label = name)
    ax.set_xlim(min(x),max(x))
    ax.set_ylim(min(y),max(y))
    ax.set_ylabel(yLabel)
    ax.set_xlabel(xLabel)
    ax.legend()
    ax.grid(showGrid)
    ax.remove()
    plt.close(f)
    return ax
