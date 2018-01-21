#General utility functions to be used throughout all types of charts
import matplotlib.patches as mpatches
import matplotlib.lines as mlines 

from ..hedgestyle import *
#Dictionary of colors to look up 
_color_dict = {'primary':   PRIMARY_COLOR, 
              'secondary':  SECONDARY_COLOR, 
              'ink1':       INK_COLOR[0],
              'light':      INK_COLOR[0],
              'light ink':  INK_COLOR[0],
              'ink2':       INK_COLOR[1],
              'medium':     INK_COLOR[1],
              'medium ink': INK_COLOR[1],
              'ink3':       INK_COLOR[2],
              'dark':       INK_COLOR[2],
              'dark ink':   INK_COLOR[2]
              }

_shape_dict = { 'box': (mpatches.Patch, {}),
                'line': (mlines.Line2D, {'xdata':[], 'ydata':[]})
              }

#General styling that (nearly) all plots will use
def stylize(ax):
  #Remove the box surrounding the plot
  for spine in ax.spines:
    ax.spines[spine].set_visible(False)
  #Color and set font for the ticks and labels
  ax.tick_params(axis='both', labelsize=FONT_SIZE_S, labelcolor=INK_COLOR[0], color=INK_COLOR[0])

#Highlight data (this should be called on the axis corresponding to independent variable)
def color_data(items, highlight, color=PRIMARY_COLOR):
  #If there is no highlight, fill with color
  if highlight is None:
    highlight_warning = False
    fill_color = color
  #If there is highlight, fill with ink_color[1] and highlight with color
  else:
    highlight_warning = True
    fill_color = INK_COLOR[1]
    highlight_color = color

  #Color the data
  for i, item in enumerate(items):
    #tick.set_color(_ink_color[0]) #Should have been set in style_ticklabels
    item.set_color(fill_color)

    #Highlight the specified data
    if not highlight is None and i in highlight:
      highlight_warning = False
      item.set_color(highlight_color)

  #Give a warning if there were no highlights
  if highlight_warning:
    warnings.warn('Highlight was specified, but none were found in the labels.', UserWarning)

#Turn color argument into color code
def decode_color(color):
  if color in _color_dict:
    return _color_dict[color]
  else:
    #If matplotlib can't recognize color, we'll get an error later
    return color

#For legend markers
def get_handles(shapes, colors, labels):
  if type(shapes) is str:
    shapes = [shapes] * len(colors)

  colors = [decode_color(color) for color in colors]
  shapes = [_shape_dict[shape] if shape in _shape_dict else shape for shape in shapes]
  handles = [shape(**args, color=color, label=label, ) for (shape, args), color, label in zip(shapes, colors, labels)]
  return handles