import random
from matplotlib import pyplot as plt
from knn_classifier import knn_classify

# each entry is ([longitude, latitude], favorite language)
languages = ["Python", "Java", "R"]
cities = []
for i in range(0, 10000):
    longitude = '{:5.2f}'.format(random.uniform(-180.0, 180.0))
    latitude = '{:5.2f}'.format(random.uniform(-180.0, 180.0))
    entry = ([float(longitude), float(latitude)], random.choice(languages))
    cities.append(entry)

# try several different values for k
for k in [1, 3, 5, 7]:
    num_correct = 0
    
    for city in cities:
        location, actual_language = city
        other_cities = [other_city
                        for other_city in cities
                        if other_city != city]
        
        predicted_language = knn_classify(k, other_cities, location)
        if predicted_language == actual_language:
            num_correct = num_correct + 1
    
    print k, "neighbors[s]:", num_correct, "correct out of", len(cities)