import random
from matplotlib import pyplot as plt

# each entry is ([longitude, latitude], favorite language)
languages = ["Python", "Java", "R"]
cities = []
for i in range(0, 10000):
    longitude = '{:5.2f}'.format(random.uniform(-180.0, 180.0))
    latitude = '{:5.2f}'.format(random.uniform(-180.0, 180.0))
    entry = ([longitude, latitude], random.choice(languages))
    cities.append(entry)

# We want to know if we can use the "survey" results in cities to predict the 
# favorite programming languages for places that were not part of our survey
# A good first step is plotting the data

# key is language, value is pair (longitudes, latitudes)
plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

# we want each language to have a different marker and color
markers = { "Java" : "o", "Python" : "s", "R" : "^" }
colors = { "Java" : "r", "Python" : "b", "R" : "g"}

for (longitude, latitude), language in cities:
    plots[language][0].append(longitude)
    plots[language][1].append(latitude)
    
# create a scatter series for each language
for language, (x, y) in plots.iteritems():
    plt.scatter(x, y, color=colors[language], marker=markers[language], label=language, zorder=10)
    
plt.legend(loc=0)               # let matplotlib choose the location
plt.axis([-130, -60, 20, 55])   # set the axis
plt.title("Favorite Programming Languages")
plt.show()


    