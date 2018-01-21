##Hedgeplot
Hedgeplot is a simple wrapper for matplotlib for making clean, easy to read charts to use in presentations. The styles are inspired by the book Storytelling with Data, by Cole Nussbaumer Knaflic.
The name hedgeplot comes from the animal hedgehog.

###Requirements
Note: The default font for hedgeplot uses [Open Sans](https://fonts.google.com/specimen/Open+Sans) . If you don’t have it, you can follow [these instructions](https://gist.github.com/lightonphiri/5811226a1fba0b3df3be73ff2d5b351c) to install it.

You will probably have to rebuild matplotlib’s font cache before matplotlib notices it.
```
import matplotlib as mpl
mpl.font_manager._rebuild()
```

This is an ongoing project and is still very small and informal right now.

###Examples
```
fig, ax = plt.subplots()
ax.bar(labels, values)
plt.show()
```

```
#fig, ax = hplt.create_plot()
#hplt.bar(labels, values)
#hplt.show()
```


