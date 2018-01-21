#Plot a horizontal bar chart
from .hedgestyle import *
from .hedgeutil import *

def barh(labels, values, highlight=None, color='primary', show_data_axis=True,
         show_label_axis=False, bar_labels=[], bar_labels_pos='out', height=BAR_HEIGHT,
        multibar_space_ratio=MULTIBAR_SPACE_RATIO, ax=None):
  """
  Plot a horizontal barchart. Note that the order goes from bottom to top for plotting

  Args:
      labels (:obj: `array-like`, shape (n_labels)): Labels for bar data.

      values (:obj: `array-like`, shape (n_labels, n_multibars)): Data for bar widths 
          (2d for multibars; see examples.)
      
      highlight (:obj:`array-like`, shape (n_labels * n_multibars), optional): Indices or labels 
          (as strings) to highlight. Highlighting will cause all other data items to filled with 
          'light ink'.

      color (:obj: `str`, optional): Specify the color to be used for filling in the data. Default is 
          'primary', which selects the primary color. Other options include 'secondary', 'light ink',
          'medium ink', 'dark ink', and others. See hedgeplot styles and colors for more details.
      
      show_data_axis (bool, optional): Default is True. If True, the data axis (corresponding to the
          dependent variable) is shown. If False, it is hidden (useful when axis is not important).

      show_label_axis (bool, optional): Default is False. If True, the label axis (corresponding to the
          independent variable) is shown (sometimes you want a separation). If False, it is hidden.

      bar_labels (:obj: `array-like`, shape (n_labels * n_multibars), optional): Specify labels to 
          show on right of the bars. Default is empty, which indicates no labels should be included.
      
      bar_labels_pos (:obj: `str`, optional): Default is 'out'. Other option is 'in', which puts the
          labels inside or outside of the bars. See examples for clarification.
      
      height (int, optional): Default is BAR_HEIGHT from hedgestyles. height of the bars (in multibars 
          it represents the total height of all the bars)
      
      multibar_space_ratio (int, range[0, 1) optional): Space between multibars. Default is MULTIBAR_SPACE_RATIO 
          from hedgestyles. 
      
      ax (:obj: `matplotlib.axes._subplots.AxesSubplot`, optional): Specify a matplotlib subplot axes
          to plot the bars on. By default, it uses plt.gca() (current axes).

  Returns:
      numpy.ndarray: A list of the matplotlib rectangle objects (corresponding to the bars). Same idea
          as what matplotlib's bar would return. 

  Raises:
      TypeError: If labels or values is None
  """

  #Type checking
  if labels is None or values is None:
    raise TypeError("Got None for labels or values")
  labels = np.array(labels)
  values = np.array(values)
  assert len(labels) == len(values), "Labels and values have unequal lengths!" 

  #Get current axis if necessary
  if ax is None:
    ax = plt.gca()

  #Decode arguments
  highlight = decode_bar_highlight(labels, values, highlight)
  #assert highlight is None or np.array(highlight).ndim == values.ndim, "Highlight and values have different dimensions!"
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

  #Format the label axis (independent variable)
  if show_label_axis:
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_color(INK_COLOR[0])

  #Color the data (note: we don't care about the 0th place)
  color_data(bars, highlight, color)

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
      #not sure about this 0.01 thing... maybe va='center' is off by a bit? 
      ax.text(values[i] + space, subticks[i] - 0.01, bar_label, color=text_color, fontsize=FONT_SIZE_M, va='center', ha=align)

  return bars