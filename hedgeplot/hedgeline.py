#Plot a line chart
from .hedgestyle import *
from .hedgeutil import *

def plot(xdata, ydata, highlight=None, color='primary', line_label='', linewidth=LINE_WIDTH, linestyle='-', ax=None):
  """
  Plot a horizontal barchart. Note that the order goes from bottom to top for plotting

  Args:
      xdata (:obj: `array-like`, shape (n_labels)): Labels for bar data.

      ydata (:obj: `array-like`, shape (n_labels, n_multibars)): Data for bar widths 
          (2d for multibars; see examples.)
      
      highlight (:obj:`array-like`, optional): Indices or labels (as strings)
          to highlight. Highlighting will cause all other data items to filled with 'light ink'.
      
      color (:obj: `str`, optional): Specify the color to be used for filling in the data. Default is 
          'primary', which selects the primary color. Other options include 'secondary', 'light ink',
          'medium ink', 'dark ink', and others. See hedgeplot styles and colors for more details.
      
      line_label (:obj: `str`, optional): Specify label to show next to the plotted line. Default is empty, 
          which indicates no labels should be included.
      
      ax (:obj: `matplotlib.axes._subplots.AxesSubplot`, optional): Specify a matplotlib subplot axes
          to plot the bars on. By default, it uses plt.gca() (current axes).

  Returns:
      numpy.ndarray: A list of the matplotlib rectangle objects (corresponding to the bars). Same idea
          as what matplotlib's bar would return. 

  Raises:
      TypeError: If labels or values is None
  """

  #Type checking
  if xdata is None or ydata is None:
    raise TypeError("Got None for xdata or ydata")
  xdata = np.array(xdata)
  ydata = np.array(ydata)
  assert len(xdata) == len(ydata), "xdata and ydata have unequal lengths!" 

  #Get current axis if necessary
  if ax is None:
    ax = plt.gca()

  #Decode arguments
  xdata_splits, ydata_splits = split_line_highlight(xdata, ydata, highlight)
  color = decode_color(color)

  #Create the plot
  lines = []
  index = 0
  highlight_segment = False
  highlight_indices = []
  for (xsegment, ysegment) in zip(xdata_splits, ydata_splits):
    if xsegment != []:
      line = ax.plot(xsegment, ysegment, linewidth=linewidth, linestyle=linestyle)
      lines.extend(line)
      if highlight_segment:
        highlight_indices.append(index)
      index += 1
    highlight_segment = not highlight_segment

  #Basic styling
  stylize(ax)

  #Remove y ticks
  #ax.tick_params(axis='y', left='off', labelsize=FONT_SIZE_M, labelcolor=INK_COLOR[2])

  #Format data axis (dependent variable)
  #Show the data axis (spine)
  ax.spines['left'].set_visible(True)
  ax.spines['left'].set_color(INK_COLOR[0])
  ax.set_yticks(ax.get_yticks()) #Somehow this adds the last tick

  #Format the label axis (independent variable)
  ax.spines['bottom'].set_visible(True)
  ax.spines['bottom'].set_color(INK_COLOR[0])

  #Color the data (note: we don't care about the 0th place)
  if not highlight is None:
    highlight = highlight_indices
  color_data(lines, highlight, color)

  #Line label
  ticks = ax.get_xticks()
  space = (ticks[1] - ticks[0]) * LINE_LABEL_PAD_RATIO
  ypos = ax.get_yticks()[-1]
  xpos = ax.get_xticks()[-1]
  if highlight is None:
    text_color = color
  else:
    text_color = INK_COLOR[2]

  ax.text(xpos + space, ypos, line_label, color=text_color, fontsize=FONT_SIZE_M, ha='left', va='center')