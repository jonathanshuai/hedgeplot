#Utility functions used by bar plots
from ..hedgestyle import *

#Turn highlight argument into a list of array indices (to be used on labels)
def decode_bar_highlight(labels, values, highlight):
  if highlight is None:
    return None
  #Make sure highlight is a list
  if type(highlight) is str: 
    highlight = np.array([highlight])
  else:
    highlight = np.array(highlight)

  if type(highlight[0]) is np.int64:
    return highlight

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
#Also it does it across classes... update to select axis later?
def decode_bar_labels(values, bar_labels):
  if type(bar_labels) is str and ('percent' in bar_labels or bar_labels == '%'):
    if values.ndim == 1:
      total = np.sum(values)    
      return [str(np.round(x * 100 / total).astype('int')) + '%' for x in values] #find percentage values
    else:
      formatted = []
      for v in values:
        total = np.sum(v)    
        formatted.append([str(np.round(x * 100 / total).astype('int')) + '%' for x in v]) #find percentage values
    return formatted
  else:
    return list(bar_labels) 