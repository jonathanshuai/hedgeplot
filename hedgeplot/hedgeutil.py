from .hedgestyle import *
#Alphabet list to help get around matplotlib's stupid label sorting
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

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

#General styling that (nearly) all plots will use
def stylize(ax):
  #Remove the box surrounding the plot
  for spine in ax.spines:
    ax.spines[spine].set_visible(False)
  #Color and set font for the ticks and labels
  ax.tick_params(axis='both', labelsize=FONT_SIZE_S, labelcolor=INK_COLOR[0], color=INK_COLOR[0])

#Highlight data (this should be called on the axis corresponding to independent variable)
def color_data(items, labels, highlight, color=PRIMARY_COLOR):
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

#Turn highlight argument into a list of array indices (to be used on labels)
def decode_highlight(labels, values, highlight):
  if highlight is None:
    return None
  #Make sure highlight is a list
  if type(highlight) is str: 
    highlight = np.array([highlight])
  else:
    highlight = np.array(highlight)

  indices = []
  if highlight.ndim == 1:
    for i, l in enumerate(labels):
      if l in highlight:
        indices.append(i)

    if values.ndim == 2: #We have to highlight n_split for each index
      n_splits = values.shape[1]
      indices = np.array([np.arange(index * n_splits, (index + 1) * n_splits) for index in indices]).ravel() 

    return indices
  else:
    n_splits = values.shape[1]
    for i, index_set in enumerate(highlight):
      indices.extend([ index + (i * n_splits) for index in index_set])
    return indices


#Turn bar labels argument into percentages or a list of values. Didn't check for None.
def decode_bar_labels(values, bar_labels):
  if type(bar_labels) is str and ('percent' in bar_labels or bar_labels == '%'):
    total = np.sum(values)
    return [str(np.round(x * 100 / total).astype('int')) + '%' for x in values] #find percentage values
  else:
    return list(bar_labels) 