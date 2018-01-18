import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

#Default style
#Font
_font_size_s = 12
_font_size_m = 15
_font_size_l = 20
_font_family = 'Open Sans'

#Palette
_ink_color = ['#ABB2B9', '#808B96', '#2C3E50'] #Ink color: 0 - axis lines, 1 - labels, 2 - text
_primary_color = '#F5B041' #Primary color (used by default for highlights/colors)
_secondary_color = '#85C1E9' #Secondary color
mpl.rcParams['font.family'] = _font_family #!! can you get around this?!

#Space
_bar_space_ratio = 0.10
_bar_width = 0.4

#def choose_palette(palette=None, ink=_ink_color, primary=_primary_color, secondary=_secondary_color):

  
#General styling that (nearly) all plots will use
def _stylize(ax):
  #Remove the box surrounding the plot
  for spine in ax.spines:
    ax.spines[spine].set_visible(False)
  #Color and set font for the ticks and labels
  ax.tick_params(axis='both', labelsize=_font_size_s, labelcolor=_ink_color[0], color=_ink_color[0])

#Highlight data (this should be called on the axis corresponding to independent variable)
def _color_data(ticklabels, items, labels, highlight, color=_primary_color):
  #If there is no highlight, fill with pri/sec color
  if highlight is None:
    highlight_warning = False
    fill_color = color
  #If there is highlight, fill with _ink_color[1] and highlight with pri/sec color
  else:
    highlight_warning = True
    fill_color = _ink_color[1]
    highlight_color = color

  #Color the data
  for i, tick in enumerate(ticklabels):
    #tick.set_color(_ink_color[0]) #Should have been set in _style_ticklabels
    items[i].set_color(fill_color)

    #Highlight the specified data
    if not highlight is None and i in highlight:
      highlight_warning = False
      tick.set_color(highlight_color)
      items[i].set_color(highlight_color)

  #Give a warning if there were no highlights
  if highlight_warning:
    warning.warn('Highlight was specified, but none were found in the labels.', UserWarning)

#Turn color argument into color code
def _decode_color(color):
  if color == 'primary':
    return _primary_color
  if color == 'secondary':
    return _secondary_color
  else:
    #If matplotlib can't recognize color, we'll get an error later
    return color

#Turn highlight argument into a list of array indices (to be used on labels)
def _decode_highlight(labels, highlight):
  if highlight is None:
    return None
  #Make sure highlight is a list
  if type(highlight) is str: 
    highlight = [highlight]
  else:
    highlight = list(highlight)
  indices = []
  for i, l in enumerate(labels):
    if l in highlight:
      indices.append(i)
  return indices

#Turn bar labels argument into percentages or a list of values. Didn't check for None.
def _decode_bar_labels(values, bar_labels):
  if type(bar_labels) is str and ('percent' in bar_labels or bar_labels == '%'):
    total = np.sum(values)
    return [str(np.round(x * 100 / total).astype('int')) + '%' for x in values] #find percentage values
  else:
    return list(bar_labels) 

#horizontal bar
def barh(labels, values, highlight=None, color='primary', show_data_axis=True, bar_labels=[], ax=None):
  #Type checking
  if labels is None or values is None:
    raise TypeError("Got None for labels or values")
  labels = list(labels)
  values = list(values)
  assert len(labels) == len(values), "Labels and values have unequal lengths!" 

  #Get current axis if necessary
  if ax is None:
    ax = plt.gca()

  #Decode arguments
  highlight = _decode_highlight(labels, highlight)
  color = _decode_color(color)
  bar_labels = _decode_bar_labels(values, bar_labels)

  #Create the plot  
  bars = ax.barh(labels, values, height=_bar_width)

  #Basic styling
  _stylize(ax)

  #Remove y ticks
  ax.tick_params(axis='y', left='off', labelsize=_font_size_m, labelcolor=_ink_color[2])

  #Format data axis (dependent variable)
  if show_data_axis:
    #Show the data axis (spine)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_color(_ink_color[0])
    ax.set_xticks(ax.get_xticks()) #Somehow this adds the last tick
  else:
    #Hide the labels and ticks
    ax.tick_params(axis='x', bottom='off', labelbottom='off')

  #Color the data
  _color_data(ax.get_yticklabels(), bars, labels, highlight, color)

  #Bar labels
  space = ax.get_xticks()[1] * _bar_space_ratio
  for i, bar_label in enumerate(bar_labels):
    if not highlight is None and i in highlight:
      text_color = color
    else:
      text_color = _ink_color[2]
    ax.text(values[i] + space, i, bar_label, color=text_color, fontsize=_font_size_m)


#Create a single plot (can't do subplots yet...)
def create_plot():
  fig, ax = plt.subplots()
  return ax

#Show the plot
def show():
  plt.show()
  plt.clf()
