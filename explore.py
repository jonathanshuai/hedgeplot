import time

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



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
#populations = [38.99, 27.43, 19.82, 20.24, 9.918]
#prop_state_values = [np.round(a/b).astype('int') for (a,b) in zip(state_values, populations)] #kills per million people

#firearm_df = df[df['Weapon'].isin(firearms)]
#other_df = df[~df['Weapon'].isin(firearms)]
#weapon_values = [firearm_df['Victim Count'].sum(), other_df['Victim Count'].sum()]


labels = ['Guns', 'Others']
values = [53821, 24922]

#mpl basic weapon
#fig, ax = plt.subplots()
#ax.bar(labels, values)
#plt.show()

import hedgeplot as hplt


#hplt basic weapon
#fig, ax = hplt.create_plot()
#hplt.bar(labels, values)
#hplt.show()

#hplt seconday weapon
#fig, ax = hplt.create_plot()
#hplt.bar(labels, values, color='secondary')
#hplt.show()

#hplt highlight weapon
#fig, ax = hplt.create_plot()
#hplt.bar(labels, values, color='secondary', highlight='Guns')
#hplt.show()

labels = state_labels #['Michigan', 'Florida', 'New York', 'Texas', 'California']
values = state_values

#hplt highlight list state
#fig, ax = hplt.create_plot()
#hplt.bar(labels, values, highlight=['California', 'New York'])
#hplt.show()

#fig, ax = hplt.create_plot()
#hplt.bar(labels, values, highlight=[4, 2])
#hplt.show()


#Labels
fig, ax = hplt.create_plot()
#hplt.barh(labels, values, highlight='California', bar_labels=values)
#hplt.show()

hplt.barh(labels, values, color='secondary', highlight='California', bar_labels='%', bar_labels_pos='in')
hplt.show()

#2d example
#fig, ax = hplt.create_plot()
#hplt.barh(['Group 1', 'Group 2'], [[1,2,3], [5,4,3]], highlight='Group 1')
#hplt.show()

labels = weapon_labels
values = state_weapon_values #2d array [[1, 2, 3], [3, 2, 1]]
hplt.barh(labels, values, highlight=[[4],[4]], bar_labels=values)
hplt.title("States With The Most Homicides (1980-2014)")
hplt.ylabel("Weapon Type")
hplt.xlabel("Number of Incidents")
hplt.legend(['medium','medium','medium','medium','primary'], ['Michigan', 'Florida', 'New York', 'Texas', 'California'], loc='upper right', layout='v')
hplt.show()

#hplt.bar(weapon_labels, weapon_values, highlight=weapon_highlight, color='secondary', show_data_axis=True, bar_labels='%', bar_labels_pos='in', highlight_tick=False)
#hplt.show()

#hplt.barh(weapon_labels, weapon_values, highlight=weapon_highlight, color='primary', show_data_axis=True, bar_labels=weapon_values, bar_labels_pos='out')
#hplt.show()

#hplt.barh(state_labels, state_values, highlight=state_highlight, color='secondary', show_data_axis=True, bar_labels=state_values, bar_labels_pos='out')
#hplt.show()

#hplt.bar(weapon_labels, weapon_values, highlight=weapon_highlight, color='primary', show_data_axis=True, bar_labels=weapon_values, bar_labels_pos='out')
#hplt.show()

#hplt.bar(state_labels, [a*1.2 for a in prop_state_values], color='light', show_data_axis=True, bar_labels=prop_state_values, bar_labels_pos='out')
#hplt.barh(state_labels, prop_state_values, highlight=state_highlight, color='secondary', show_data_axis=True, bar_labels_pos='out')
#hplt.barh(weapon_labels, weapon_values, highlight=weapon_highlight, bar_labels=weapon_values, color='secondary', show_data_axis=True, bar_labels_pos='out')
#hplt.show()
#hplt.barh(weapon_labels, state_weapon_values, highlight=[[1], [2]], bar_labels=state_weapon_values, color='primary', show_data_axis=True, bar_labels_pos='out')
#hplt.show()
#hplt.barh(weapon_labels, state_weapon_values, highlight=[[4], [4]], color='primary', show_data_axis=True, bar_labels_pos='out')
#hplt.title("Firearm related deaths by state")
#hplt.ylabel("Number of Incidents")
#hplt.xlabel("Weapon")
#hplt.legend(['medium', 'medium', 'medium', 'medium', 'primary'], ['Michigan', 'Florida', 'New York', 'Texas', 'California'], shapes='box', loc='upper right')
#hplt.show()

#For percentage bar stacks, use male/female + victim relationship
year_df = df.groupby('Year').count()['Victim Count']
xdata = [1980, 1985, 1990, 1995, 2000, 2005, 2010]
ydata = [year_df[year_df.index == 1980], year_df[year_df.index == 1985], 
          year_df[year_df.index == 1990], year_df[year_df.index == 1995], 
          year_df[year_df.index == 2000], year_df[year_df.index == 2005], 
          year_df[year_df.index == 2010]]
ydata = [y.values[0] for y in ydata]

#xdata is the years 1980, 1985,... 2010
#ydata is the number of homicides for each year in xdata 
hplt.plot(xdata, ydata, highlight=[[1995, 2000]], line_label='Murder Trend')
hplt.title("Homicide Trends In The US (1980-2010)")
hplt.ylabel("Number of Homicides")
hplt.xlabel("Year")
hplt.show()

#Line plots
#x = [1,2,3,4]
#y = [1,4,9,16]
#fig, ax = hplt.create_plot()
#lines = ax.plot(x[:2],y[:2])
#lines = ax.plot(x[2:],y[2:])
#lines[0].set_color('red')
#plt.show()
#print(lines)
