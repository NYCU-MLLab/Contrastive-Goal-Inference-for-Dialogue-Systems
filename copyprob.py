from matplotlib.hatch import HorizontalHatch
import numpy as np
import matplotlib
import matplotlib.pylab as plt
import seaborn as sns
copyprob = np.load("./copyprob/copydata.npy")

# # attraction
# index = [208,655]
# x_axis_labels = [
# ["the", "phone", "number", "is", "01223464646", ".", "is", "there", "anything", "else", "i", "can", "help", "you", "with", "?",],
# ["absolutely", ".", "holy_trinity_church", "is", "on", "market_street", "in", "the", "centre", "of", "town", ".", "their", "postcode", "is", "cb23nz", "and", "is", "free", "to", "enter", ".", "would", "you", "need", "their", "phone", "number", "?",],
# ]

# # restaurant
# index = [258,333]
# x_axis_labels = [
# ["the", "postcode", "is", "cb21db",],
# ["it", "is", "located", "at", "100_mill_road\n_city_centre", "and", "the", "phone", "number", "is", "01223367660", ".", "is", "there", "anything", "else", "i", "can", "help", "you", "with", "?",],
# ]

# hotel
index = [386, 315]
x_axis_labels = [
["the", "number", "for", "the", "ashley_hotel", "is", "01223350059", ".", "can", "i", "book", "that", "for", "you", "?",],
["okay", ",", "that", "booking", "was", "successful", "for", "tuesday", ".", "the", "reference", "number", "is", "sid7a0h4", ".", "is", "there", "anything", "else", "you", "need", "?",],
]


# maxlen = 35
# for i in range(len(x_axis_labels)):
#     x_axis_labels[i] += [" " for j in range(maxlen-len(x_axis_labels[i]))]

y_axis_labels = [
"dictionary", 
"memory", 
"knowledge", 
]

f,axx = plt.subplots(len(index),sharey=True)
cbar_ax = f.add_axes([.93, 0.1, .01, 0.75])
for i in range(len(index)):
    ax = sns.heatmap(copyprob[index[i], :len(x_axis_labels[i]), :].T, cmap="YlGnBu", square=True, xticklabels=1, cbar_ax=cbar_ax, ax=axx[i])
    ax.set_yticklabels(y_axis_labels, rotation=315, verticalalignment='bottom')
    ax.set_xticklabels(x_axis_labels[i], rotation=45, horizontalalignment='right')

figure = ax.get_figure()
plt.savefig("./copyprob/goal_hotel.png", dpi=400)


