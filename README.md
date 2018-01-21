## Hedgeplot
Hedgeplot is a simple wrapper for matplotlib for making clean, easy to read charts to use in presentations. The styles are inspired by the book Storytelling with Data, by Cole Nussbaumer Knaflic.
The name hedgeplot comes from the animal hedgehog.

### Requirements
Note: The default font for hedgeplot uses [Open Sans](https://fonts.google.com/specimen/Open+Sans) . If you don’t have it, you can follow [these instructions](https://gist.github.com/lightonphiri/5811226a1fba0b3df3be73ff2d5b351c) to install it.

You will probably have to rebuild matplotlib’s font cache before matplotlib notices it.
```python
import matplotlib as mpl
mpl.font_manager._rebuild()
```

This is an ongoing project and is still very small and informal right now.

### Examples
These examples use data from FBI's Supplementary Homicide Report. This dataset was downloaded from [Kaggle](https://www.kaggle.com/murderaccountability/homicide-reports).

Basic bar graph with matplotlib (number of homicide incidents with guns vs. all other types of weapons):

```python
labels = ['Guns', 'Others']
values = [53821, 24922]

fig, ax = plt.subplots()
ax.bar(labels, values)
plt.show()
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/mpl_basic_weapon.png?raw=true)

Hedgeplot removes the clutter (like the box around the chart and the independent variable axis) and lightens up the tick labels:
```python
fig, ax = hplt.create_plot()
hplt.bar(labels, values)
hplt.show()
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplt_basic_weapon.png?raw=true)


You can choose to highlight a label, which will turn the other bars grey:

```python
hplt.bar(labels, values, color='secondary', highlight='Guns')
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplt_seconday_highlight.png?raw=true)


The highlight parameter can also take in either a list of labels or a list of indices. These two barplots produce the same result:

```python
labels = state_labels # ['Michigan', 'Florida', 'New York', 'Texas', 'California']
values = state_values # number of homicides in each state from 1980-2014 

hplt.bar(labels, values, highlight=['California', 'New York'])
hplt.bar(labels, values, highlight=[4, 2])
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplt_highlight_2_state.png?raw=true)

We can add labels to the bars quite easily (this works with vertical barplots too):
```python
hplt.barh(labels, values, highlight='California', bar_labels=values)
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplt_hbar_label.png?raw=true)

The labels can be a list of strings too. 

Passing in a % sign will calculate percentages of the total for each bar. The bar label position argument puts the labels inside the bar:
```python
hplt.barh(labels, values, highlight='California', bar_labels='%', bar_label_pos='in')
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplt_percent_label.png?raw=true)

Note that the horizontal bar chart plots bars from bottom to top.

Passing in a 2d array for the values will create two groups of bars; with the rows as groups:
```python
hplt.barh(['Group 1', 'Group 2'], [[1,2,3], [5,4,3]], highlight='Group 1')
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplt_2d_basic_example.png)

For a more complete example:
```python
#labels = ['Guns', 'Others']
#values = 2d array: [guns deaths per state, other deaths per state]
hplt.barh(labels, values, highlight=[[4],[4]], bar_labels=values)
hplt.title("States With The Most Homicides (1980-2014)")
hplt.ylabel("Weapon Type")
hplt.xlabel("Number of Incidents")
hplt.legend(['medium','medium','medium','medium','primary'], 
						['Michigan', 'Florida', 'New York', 'Texas', 'California'], 
						loc='upper right', layout='v') #medium and primary will be explained more in the colors section
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/complicated1.png?raw=true)

Example with line plot highlighting intervals:
```python
#xdata is the years 1980, 1985,... 2010
#ydata is the number of homicides for each year in xdata 
hplt.plot(xdata, ydata, highlight=[[1995, 2000]], line_label='Murder Trend')
hplt.title("Homicide Trends In The US (1980-2010)")
hplt.ylabel("Number of Homicides")
hplt.xlabel("Year")
hplt.show()
```

![alt text](https://github.com/jonathanshuai/hedgeplot/blob/master/examples/hplot_line_example.png?raw=true)