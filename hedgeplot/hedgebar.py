from .hedgestyle import *
from .hedgeutil import *

#horizontal bar
def bar(labels, values, highlight=None, color='primary', show_data_axis=True, 
        bar_labels=[], bar_labels_pos='out', ax=None, width=BAR_WIDTH,
        multibar_space_ratio=MULTIBAR_SPACE_RATIO):
  #Type checking
  if labels is None or values is None:
    raise TypeError("Got None for labels or values")
  labels = np.array(labels)
  values = np.array(values)
  assert len(labels) == len(values), "Labels and values have unequal lengths!" 
  assert highlight is None or np.array(highlight).ndim == values.ndim, "Highlight and values have different dimensions!"

  #Get current axis if necessary
  if ax is None:
    ax = plt.gca()

  #Decode arguments
  highlight = decode_highlight(labels, values, highlight)
  color = decode_color(color)
  bar_labels = decode_bar_labels(values, bar_labels)

  #Create the plot
  ticks = np.arange(len(labels))
  if values.ndim == 2:
    #Calculate the subticks for multiple bars
    bars = []
    subticks = []
    n_splits = values.shape[1]
    offset = width / n_splits
    start_offset = (width - offset) / 2
    for i in range(values.shape[0]):
      start = i - start_offset
      subticks.extend([start + t * offset for t in np.arange(n_splits)])

    thickness = offset * (1 - multibar_space_ratio)
    values = values.ravel() #flatten values
    subticks = np.array(subticks) #turn subticks into nparray 
    bars.append(ax.bar(subticks, values, width=thickness))
    bars = np.array(bars).T.ravel()

  else:
    bars = ax.bar(ticks, values, width=width)
    subticks = ticks

  ax.set_xticks(ticks)
  ax.set_xticklabels(labels)

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

  #Color the data (note: we don't care about the 0th place)
  color_data(bars, labels, highlight, color)

  #Bar labels
  if len(bar_labels):
    #Flatten out the bar labels and values to make this easy (in case of multiple bar plot)
    bar_labels = np.array(bar_labels).ravel()
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
      ax.text(subticks[i], values[i] + space, bar_label, color=text_color, fontsize=FONT_SIZE_M, ha='center', va=align)