#This file contains all of the styling constants. Every file
#in hedgeplot will refer to these. This shouldn't be directly accessed
#outside of the module
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings


#Default style
#Font
FONT_SIZE_S = 10
FONT_SIZE_M = 12
FONT_SIZE_L = 18
FONT_FAMILY = 'Open Sans'

#Palette
INK_COLOR = ['#ABB2B9', '#808B96', '#2C3E50'] #Ink color -- 0: axis lines, 1: labels, 2: text
PRIMARY_COLOR = '#F5B041' #Primary color (used by default for highlights/colors)
SECONDARY_COLOR = '#85C1E9' #Secondary color
mpl.rcParams['font.family'] = FONT_FAMILY #!! can you get around this?!

#Space
H_BAR_PAD_RATIO = 0.10
V_BAR_PAD_RATIO = 0.20
BAR_HEIGHT = 0.4
BAR_WIDTH = 0.4
MULTIBAR_SPACE_RATIO = 0.35 #This should be 0~1 (otherwise error)
#def choose_palette(palette=None, ink=_ink_color, primary=_primary_color, secondary=_secondary_color):
