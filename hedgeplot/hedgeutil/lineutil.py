#Utility functions used by line plots
from ..hedgestyle import *

#Turn highlight argument into a list of array indices (to be used on labels)
def split_line_highlight(xdata, ydata, highlight):
  if highlight is None:
    return [xdata], [ydata]

  highlight = np.array(highlight)
  #Make sure highlight is a 2d np array
  if highlight.ndim == 1:
    highlight = np.array([highlight])
  else:
    highlight = np.array(highlight)

  #Transform data to indices if we got strings
  xdata = list(xdata)
  v = np.vectorize(lambda x: xdata.index(x))
  highlight = v(highlight)

  #Make sure highlights are actually intervals:
  for h in highlight:
    if h[0] >= h[1]:
      raise ValueError('Highlight values must be proper intervals.')

  highlight = _merge_intervals(highlight)
  
  xdata_splits = []
  ydata_splits = []
  prev = 0

  for start, end in highlight:
    xdata_splits.append(xdata[prev:start+1]) #Uncolored
    ydata_splits.append(ydata[prev:start+1]) #Uncolored
    xdata_splits.append(xdata[start:end+1]) #Colored
    ydata_splits.append(ydata[start:end+1]) #Colored
    prev = end
  if end != len(xdata) - 1:
    xdata_splits.append(xdata[prev:]) #uncolored
    ydata_splits.append(ydata[prev:]) #uncolored

  xdata_splits = [[] if len(x) <= 1 else x for x in xdata_splits] #Remove single intervals
  ydata_splits = [[] if len(x) <= 1 else x for x in ydata_splits] #Remove single intervals
  return xdata_splits, ydata_splits

#Turns a list of intervals that overlap into ones
#large ones w/ no overlap
#e.g. (1,5) and (3,7) turns into (1, 7)
#intervals should be np array
def _merge_intervals(intervals):
  n = len(intervals)
  #array of length 1 has no overlaps
  if n == 1:
    return intervals

  intervals[intervals[:,0].argsort()] #Sorts the intervals by starting position (nlog(n))

  merged_intervals = []
  i = 0
  while i < n:
    current_interval = intervals[i]

    k = i + 1
    if k < n:
      next_interval = intervals[k]
    while current_interval[1] >= next_interval[0] and k < n:
      current_interval[1] = next_interval[1] #Expand the interval
      next_interval = intervals[k]
      k += 1

    if k == n:
      if current_interval[1] >= next_interval[0]:
        current_interval[1] = next_interval[1] #Expand the interval
        merged_intervals.append(current_interval)
      else: 
        merged_intervals.append(current_interval)
        merged_intervals.append(next_interval)
      break
    
    i = k
    merged_intervals.append(current_interval)

  return merged_intervals

