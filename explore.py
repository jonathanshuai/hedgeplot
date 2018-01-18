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

highlight = ['Guns']
hplt.create_plot()
hplt.barh(labels, values, highlight=highlight, color='primary', show_data_axis=False, bar_labels=values, bar_labels_pos='in')
hplt.show()

hplt.barh(labels, values, highlight=highlight, color='secondary', show_data_axis=True, bar_labels='%')
hplt.show()

hplt.bar(labels, values, highlight=highlight, color='primary', show_data_axis=False, bar_labels=values)
hplt.show()

hplt.bar(labels,values,  highlight=highlight, color='secondary', show_data_axis=True, bar_labels='%', bar_labels_pos='in', highlight_tick=False)
hplt.show()





