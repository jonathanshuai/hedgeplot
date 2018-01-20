from .hedgestyle import *
from .hedgeutil import *
#Simple functions to provide an interface from hedgeplot to use matplotlib functions
#so you don't have to explicitly use matplotlib in most situations.

#Create a single plot (can't do subplots yet...)
def create_plot():
  """
  This super simple function basically calls matplotlib.pyplot.subplots(). 
  It takes no arguments and does not handle more than one subplot. 

  Returns:
      matplotlib.figure.Figure: the matplotlib pyplot figure that was created
      matplotlib.axes._subplots.AxesSubplot: the matplotlib axes that was created

  Raises:
      TypeError: If labels or values is None
  """

  fig, ax = plt.subplots()
  return fig, ax

def title(text, fontsize=FONT_SIZE_L, color='dark ink', ax=None):
  """
  Function to set the title of a subplot. 

  Args:
      text (:obj: `str`): Title text.
      
      fontsize (int, optional): Default font size is FONT_SIZE_L.
      
      color (:obj:`str`, optional): Default is dark ink. See hedgeplot styles and colors 
          for more details.

  Returns:
      matplotlib.text.Text: matplotlib text object that was created
  """

  if ax is None:
    ax = plt.gca()
  color = decode_color(color)
  return ax.set_title(text, fontsize=fontsize, color=color)

def xlabel(text, fontsize=FONT_SIZE_M, color='medium ink', ax=None):
  """
  Function to set the xlabel of a subplot. 

  Args:
      text (:obj: `str`): Title text.
      
      fontsize (int, optional): Default font size is FONT_SIZE_L.
      
      color (:obj:`str`, optional): Default is medium ink. See hedgeplot styles and colors 
          for more details.

  Returns:
      matplotlib.text.Text: matplotlib text object that was created
  """

  if ax is None:
    ax = plt.gca()
  color = decode_color(color)
  return ax.set_xlabel(text, fontsize=fontsize, color=color)

def ylabel(text, fontsize=FONT_SIZE_M, color='medium ink', ax=None):
  """
  Function to set the ylabel of a subplot. 

  Args:
      text (:obj: `str`): Title text.
      
      fontsize (int, optional): Default font size is FONT_SIZE_L.
      
      color (:obj:`str`, optional): Default is medium ink. See hedgeplot styles and colors 
          for more details.

  Returns:
      matplotlib.text.Text: matplotlib text object that was created
  """

  if ax is None:
    ax = plt.gca()
  color = decode_color(color)
  return ax.set_ylabel(text, fontsize=fontsize, color=color)

#This will function will probably grow
def legend(colors, labels, shapes='box', loc='best', layout='vertical', reverse_vertical=True, ax=None):
  """
  Function to create a legend.  

  Args:
      text (:obj: `str`): Title text.
      
      fontsize (int, optional): Default font size is FONT_SIZE_L.
      
      color (:obj:`str`, optional): Default is medium ink. See hedgeplot styles and colors 
          for more details.

  Returns:
      matplotlib.text.Text: matplotlib text object that was created
  """
  if ax is None:
    ax = plt.gca()

  handles = get_handles(shapes, colors, labels)
  if not all(len(handles) == l for l in [len(colors), len(labels)]):
    warnings.warn('Lengths of one or more of colors, labels, and shapes did not match.', UserWarning)

  if layout == 'horizontal' or layout == 'h':
    ncol = len(labels)
  else:
    ncol = 1
    if reverse_vertical: #Reverse so that it goes from bottom to top
      handles = handles[-1::-1]

  return ax.legend(handles=handles, loc=loc, ncol=ncol, frameon=False)

#Show the plot
def show():
  plt.show()
  plt.clf()
