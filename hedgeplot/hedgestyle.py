import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings

#Default style
#Font
font_size_s = 12
font_size_m = 15
font_size_l = 20
font_family = 'Open Sans'

#Palette
ink_color = ['#ABB2B9', '#808B96', '#2C3E50'] #Ink color -- 0: axis lines, 1: labels, 2: text
primary_color = '#F5B041' #Primary color (used by default for highlights/colors)
secondary_color = '#85C1E9' #Secondary color
mpl.rcParams['font.family'] = font_family #!! can you get around this?!

#Space
bar_space_ratio = 0.10
bar_width = 0.4

#def choose_palette(palette=None, ink=_ink_color, primary=_primary_color, secondary=_secondary_color):
