# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.pyplot as plt
from FigureAndAxes import makeAxes
from FigureAndAxes import makeFigure
import time
#DataFiltering
from DataFilter import DataFilter
#DATA HANDLING
import numpy as np
import pandas as pd
import glob
import statistics
from copy import deepcopy

blms=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]

def tolerance(blms, data, tolerances):
    toleranceGraph = plt.bar(blms,tolerances, color = "red")
    graph = plt.bar(blms,data, color = "green")
    true = True
    while true == True:
        for i in blms:
            i = i-1
            if tolerances[i] <= data[i]:
                graph[i].set_color("r")
            else:
                graph[i].set_color("g")
        plt.show()


files = glob.glob("C:/Users/jde35739/Documents/BLM_R5IM_Data/cycle" + '/*.csv')
plt.ion()

tolerances=[5,5,10,4,5,35,5,8,10,10,10,5,5,5,5,5,5,5,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,4,4,4,4,1]
#blms = np.linspace(1,40,39)
def ReadBLMFile(w):
	global files
	selected_file = files[w]
	input_data = pd.read_csv(selected_file)
	#input_data = input_data.drop(index = 39)
	dataframe = input_data.drop(columns = input_data.columns[0]).to_numpy()

	return dataframe



def CreateBar(data):
		#plt.figure()
		totals = []
		for i in data:
				temptotal = np.sum(i)
				totals.append(temptotal)
		x = np.linspace(1, 40, 39)
		#print("HELLO", x, totals[:-1])
		return (x, totals[:-1])

def findnearest(x_data, time: list = [10.1, 10.5]):
		try:
				#print("trying")
				firstidx = np.where(x_data == time[0])[0][0]
				lastidx = np.where(x_data == time[1])[0][0]
		except:
				#print("execpting")
				x_data = np.asarray(x_data)
				firstidx = (np.abs(x_data - time[0])).argmin()
				lastidx = (np.abs(x_data - time[1])).argmin()
		#print("first, last =", firstidx, lastidx)
		return [firstidx, lastidx]

def filterit(dataframe, minvalue = 0):
		filterer = DataFilter()
		filterer.set("auto_offset", findnearest(np.linspace(-0.5, 10.5, 2200)))
		dataframe = filterer.apply(dataframe)
		#print(type(dataframe))
		for each in dataframe:
				each[each < 0] = 0
		return dataframe



# main window which inherits QDialog
class Window(QDialog):
	
	# constructor
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		# a figure instance to plot on
		self.figure = plt.figure()

		# this is the Canvas Widget that displays the 'figure'it takes the 'figure' instance as a parameter to __init__
		self.canvas = FigureCanvas(self.figure)

		# this is the Navigation widget it takes the Canvas widget and a parent
		self.toolbar = NavigationToolbar(self.canvas, self)
		# Just some button connected to 'plot' method
		self.button = QPushButton('Begin Updating')
		
		# adding action to the button
		self.button.clicked.connect(self.plot)

		# creating a Vertical Box layout
		layout = QVBoxLayout()
		# adding tool bar to the layout
		layout.addWidget(self.toolbar)
		# adding canvas to the layout
		layout.addWidget(self.canvas)
		# adding push button to the layout
		layout.addWidget(self.button)
		# setting layout to the main window
		self.setLayout(layout)

	# action called by the push button
	def plot(self):
		while True:
			for w in range(0,18):
				global tolerances
				global blms

				dataarray = ReadBLMFile(w)
				filterit(dataarray)
				data = CreateBar(dataarray)
				plt.cla()
				newgraph = plt.bar(blms,data[1], color = "red")
				print(data[0])
				newgraph = plt.bar(blms,tolerances,color = "#6CBB3C")
				#tolerance(blms, data[1], tolerances)
				#newgraph = plt.bar(data[0],data[1], color = "red")
				plt.show
				#newgraph = plt.bar(x,dataarray, color = "green")
				#plt.show

				# This will run the GUI event loop until all UI events currently waiting have been processed
				self.canvas.flush_events()
				time.sleep(0.6)

# driver code
if __name__ == '__main__':
	# creating apyqt5 application
	app = QApplication(sys.argv)
	# creating a window object
	main = Window()	
	# showing the window
	main.show()
	# loop
	sys.exit(app.exec_())
