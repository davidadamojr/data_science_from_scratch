from kmeans import KMeans
from matplotlib import pyplot as plt

path_to_file = "casino1.jpg"
import matplotlib.image as mpimg
img = mpimg.imread(path_to_file)

pixels = [pixel for row in img for pixel in row]
clusterer = KMeans(5)
clusterer.train(pixels)     # this might take a while

def recolor(pixel):
    cluster = clusterer.classify(pixel)             # index of the closest cluster
    return clusterer.means[cluster]

new_img = [[recolor(pixel) for pixel in row]        # recolor this row of pixels
           for row in img]

plt.imshow(new_img)
plt.axis('off')
plt.show()