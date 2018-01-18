from .hedgestyle import *
from .hedgeutil import *

#horizontal bar
def barh(labels, values, highlight=None, color='primary', show_data_axis=True, bar_labels=[], bar_labels_pos='out', ax=None, highlight_tick=True):
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
  bars = ax.barh(labels, values, height=BAR_HEIGHT)

  #Basic styling
  stylize(ax)

  #Remove y ticks
  ax.tick_params(axis='y', left='off', labelsize=FONT_SIZE_M, labelcolor=INK_COLOR[2])

  #Format data axis (dependent variable)
  if show_data_axis:
    #Show the data axis (spine)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_color(INK_COLOR[0])
    ax.set_xticks(ax.get_xticks()) #Somehow this adds the last tick
  else:
    #Hide the labels and ticks
    ax.tick_params(axis='x', bottom='off', labelbottom='off')

  #Color the data
  color_data(ax.get_yticklabels(), bars, labels, highlight, color, highlight_tick)

  #Bar labels
  space = ax.get_xticks()[1] * H_BAR_PAD_RATIO 
  align = 'left'
  if bar_labels_pos == 'in':
    space = -space
    align = 'right'

  for i, bar_label in enumerate(bar_labels):
    if bar_labels_pos == 'in':
      text_color = 'white'
    else:
      if not highlight is None and i in highlight:
        text_color = color
      else:
        text_color = INK_COLOR[2]
    ax.text(values[i] + space, i, bar_label, color=text_color, fontsize=FONT_SIZE_M, va='center', ha=align)