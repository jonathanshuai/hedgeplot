import time

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import hedgeplot as hplt


file_name = 'database.csv'

firearms = ['Rifle', 'Handgun', 'Shotgun', 'Gun', 'Firearm']
knife = ['Knife']
blunt = ['Blunt Object']
#others = ['Fall', 'Fire', 'Drowning', 'Drugs', 'Poison', 'Unknown', 'Strangulation', 'Suffocation']

df = pd.read_csv(file_name)
df = df.dropna()


#Bar plots
firearm_df = df[df['Weapon'].isin(firearms)]
other_df = df[~df['Weapon'].isin(firearms)]
weapon_values = [firearm_df['Victim Count'].sum(), other_df['Victim Count'].sum()]
weapon_labels = ['Guns', 'Other']
weapon_highlight = ['Guns']

state_df = df[['State', 'Victim Count']].groupby('State').count().sort_values('Victim Count').tail()
state_values = state_df['Victim Count']
state_labels = state_df.index
state_highlight=['California']

state_weapon_values = [firearm_df[['State', 'Victim Count']].groupby('State').count().sort_values('Victim Count').tail()['Victim Count'],
                      other_df[['State', 'Victim Count']].groupby('State').count().sort_values('Victim Count').tail()['Victim Count']]
#cali tex ny flor mich populations
populations = [38.99, 27.43, 19.82, 20.24, 9.918]
prop_state_values = [np.round(a/b).astype('int') for (a,b) in zip(state_values, populations)] #kills per million people

#fig, ax = hplt.create_plot()

#hplt.bar(weapon_labels, weapon_values, highlight=weapon_highlight, color='secondary', show_data_axis=True, bar_labels='%', bar_labels_pos='in', highlight_tick=False)
#hplt.show()

#hplt.barh(weapon_labels, weapon_values, highlight=weapon_highlight, color='primary', show_data_axis=True, bar_labels=weapon_values, bar_labels_pos='out')
#hplt.show()

#hplt.barh(state_labels, state_values, highlight=state_highlight, color='secondary', show_data_axis=True, bar_labels=state_values, bar_labels_pos='out')
#hplt.show()

hplt.bar(weapon_labels, weapon_values, highlight=weapon_highlight, color='primary', show_data_axis=True, bar_labels=weapon_values, bar_labels_pos='out')
hplt.show()

#hplt.bar(state_labels, [a*1.2 for a in prop_state_values], color='light', show_data_axis=True, bar_labels=prop_state_values, bar_labels_pos='out')
#hplt.barh(state_labels, prop_state_values, highlight=state_highlight, color='secondary', show_data_axis=True, bar_labels_pos='out')
#hplt.barh(weapon_labels, weapon_values, highlight=weapon_highlight, bar_labels=weapon_values, color='secondary', show_data_axis=True, bar_labels_pos='out')
#hplt.show()
#hplt.barh(weapon_labels, state_weapon_values, highlight=[[1], [2]], bar_labels=state_weapon_values, color='primary', show_data_axis=True, bar_labels_pos='out')
#hplt.show()
hplt.barh(weapon_labels, state_weapon_values, highlight=[[4], [4]], color='primary', show_data_axis=True, bar_labels_pos='out')
hplt.title("Firearm related deaths by state")
hplt.ylabel("Number of Incidents")
hplt.xlabel("Weapon")
hplt.legend(['medium', 'medium', 'medium', 'medium', 'primary'], ['Michigan', 'Florida', 'New York', 'Texas', 'California'], shapes='box', loc='upper right')
hplt.show()

#For percentage bar stacks, use male/female + victim relationship



#Line plots
x = [1,2,3,4]
y = [1,4,9,16]
fig, ax = hplt.create_plot()
lines = ax.plot(x,y)
lines[0].set_color('red')
plt.show()
print(lines)
