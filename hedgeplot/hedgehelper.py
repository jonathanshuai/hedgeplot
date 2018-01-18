from .hedgestyle import *

#Create a single plot (can't do subplots yet...)
def create_plot():
  fig, ax = plt.subplots()
  return ax

#Show the plot
def show():
  plt.show()
  plt.clf()
