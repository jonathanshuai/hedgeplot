from .hedgestyle import *
from .hedgeutil import *

#horizontal bar
def barh(labels, values, highlight=None, color='primary', show_data_axis=True,
         bar_labels=[], bar_labels_pos='out', ax=None, height=BAR_HEIGHT,
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
    offset = height / n_splits
    start_offset = (height - offset) / 2
    for i in range(values.shape[0]):
      start = i - start_offset
      subticks.extend([start + t * offset for t in np.arange(n_splits)])

    thickness = offset * (1 - multibar_space_ratio)
    values = values.ravel() #flatten values
    subticks = np.array(subticks) #turn subticks into nparray 
    bars.append(ax.barh(subticks, values, height=thickness))
    bars = np.array(bars).T.ravel()
    print(subticks)
  else:
    bars = ax.barh(ticks, values, height=height)
    subticks = ticks

  ax.set_yticks(ticks)
  ax.set_yticklabels(labels)

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

  #Color the data (note: we don't care about the 0th place)
  color_data(bars, labels, highlight, color)

  #Bar labels
  if len(bar_labels):
    #Flatten out the bar labels and values to make this easy (in case of multiple bar plot)
    bar_labels = np.array(bar_labels).ravel()
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
      ax.text(values[i] + space, subticks[i], bar_label, color=text_color, fontsize=FONT_SIZE_M, va='center', ha=align)