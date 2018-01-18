from .hedgestyle import *
from .hedgeutil import *

#horizontal bar
def bar(labels, values, highlight=None, color='primary', show_data_axis=True, bar_labels=[], bar_labels_pos='out', ax=None, highlight_tick=True):
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
  highlight = decode_highlight(labels, highlight)
  color = decode_color(color)
  bar_labels = decode_bar_labels(values, bar_labels)

  #Create the plot  
  bars = ax.bar(labels, values, width=BAR_WIDTH)

  #Basic styling
  stylize(ax)

  #Remove x ticks
  ax.tick_params(axis='x', bottom='off', labelsize=FONT_SIZE_M, labelcolor=INK_COLOR[2])

  #Format data axis (dependent variable)
  if show_data_axis:
    #Show the data axis (spine)
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_color(INK_COLOR[0])
    ax.set_yticks(ax.get_yticks()) #Somehow this adds the last tick
  else:
    #Hide the labels and ticks
    ax.tick_params(axis='y', left='off', labelleft='off')

  #Color the data
  color_data(ax.get_xticklabels(), bars, labels, highlight, color, highlight_tick)

  #Bar labels
  space = ax.get_yticks()[1] * V_BAR_PAD_RATIO
  align = 'bottom'
  if bar_labels_pos == 'in':
    space = -space
    align = 'top'
  
  for i, bar_label in enumerate(bar_labels):
    if bar_labels_pos == 'in':
      text_color = 'white'
    else:
      if not highlight is None and i in highlight:
        text_color = color
      else:
        text_color = INK_COLOR[2]
    ax.text(i, values[i] + space, bar_label, color=text_color, fontsize=FONT_SIZE_M, ha='center', va=align)