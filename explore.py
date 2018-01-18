import time

import numpy as np
import pandas as pd

import hedgeplot as hplt


file_name = 'database.csv'

firearms = ['Rifle', 'Handgun', 'Shotgun', 'Gun', 'Firearm']
knife = ['Knife']
blunt = ['Blunt Object']
#others = ['Fall', 'Fire', 'Drowning', 'Drugs', 'Poison', 'Unknown', 'Strangulation', 'Suffocation']

df = pd.read_csv(file_name)
df = df.dropna()



df2 = df[df['Weapon'].isin(firearms)]

firearm_df = df[df['Weapon'].isin(firearms)]['Victim Count']
other_df = df[~df['Weapon'].isin(firearms)]['Victim Count']

values = [firearm_df.sum(), other_df.sum()]
labels = ('Guns', 'Other')


'''
font_size = 12
_ink_color = '#d5d8dc'
_primary_color = '#f5b041'

import matplotlib as mpl
import matplotlib.pyplot as plt

highlight = ['Guns']
#BARH DEFINITION; given: labels and data
fig, ax = plt.subplots()
bars = ax.barh(labels, values)


ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color(_ink_color)
ax.tick_params(axis='both', labelsize=font_size, color=_ink_color)
ax.set_xticks(ax.get_xticks()) #Somehow this adds the last tick

'''
highlight = ['Guns']
hplt.create_plot()
hplt.barh(labels, values, highlight=highlight, color='primary', show_data_axis=False, bar_labels=values)
hplt.show()

hplt.barh(labels, values, highlight=highlight, color='secondary', show_data_axis=True, bar_labels='%')
hplt.show()





