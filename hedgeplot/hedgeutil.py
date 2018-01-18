from .hedgestyle import *

#General styling that (nearly) all plots will use
def stylize(ax):
  #Remove the box surrounding the plot
  for spine in ax.spines:
    ax.spines[spine].set_visible(False)
  #Color and set font for the ticks and labels
  ax.tick_params(axis='both', labelsize=FONT_SIZE_S, labelcolor=INK_COLOR[0], color=INK_COLOR[0])

#Highlight data (this should be called on the axis corresponding to independent variable)
def color_data(ticklabels, items, labels, highlight, color=PRIMARY_COLOR, highlight_tick=True):
  #If there is no highlight, fill with pri/sec color
  if highlight is None:
    highlight_warning = False
    fill_color = color
  #If there is highlight, fill with ink_color[1] and highlight with pri/sec color
  else:
    highlight_warning = True
    fill_color = INK_COLOR[1]
    highlight_color = color

  #Color the data
  for i, tick in enumerate(ticklabels):
    #tick.set_color(_ink_color[0]) #Should have been set in style_ticklabels
    items[i].set_color(fill_color)

    #Highlight the specified data
    if not highlight is None and i in highlight:
      highlight_warning = False
      items[i].set_color(highlight_color)
      if highlight_tick:
        tick.set_color(highlight_color)

  #Give a warning if there were no highlights
  if highlight_warning:
    warnings.warn('Highlight was specified, but none were found in the labels.', UserWarning)

#Turn color argument into color code
def decode_color(color):
  if color == 'primary':
    return PRIMARY_COLOR
  if color == 'secondary':
    return SECONDARY_COLOR
  else:
    #If matplotlib can't recognize color, we'll get an error later
    return color

#Turn highlight argument into a list of array indices (to be used on labels)
def decode_highlight(labels, highlight):
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
def decode_bar_labels(values, bar_labels):
  if type(bar_labels) is str and ('percent' in bar_labels or bar_labels == '%'):
    total = np.sum(values)
    return [str(np.round(x * 100 / total).astype('int')) + '%' for x in values] #find percentage values
  else:
    return list(bar_labels) 