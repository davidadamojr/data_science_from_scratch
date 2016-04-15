"""
Points in high-dimensional spaces tend not to be close to one another at all. 
One way to see this is by randomly generating pairs of points in the d-dimensional 
"unit cube" in a variety of dimensions, and calculating the distances between 
them.
"""
import sys
sys.path.insert(0, "../statistics")
from central_tendencies import mean

def random_point(dim):
    return [random.random() for _ in range(dim)]

def random_distances(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]

dimensions = range(1, 101)

avg_distances = []
min_distances = []

random.seed(0)
for dim in dimensions:
    distances = random_distances(dim, 10000)        # 10,000 random pairs
    avg_distances.append(mean(distances))           # track the average
    min_distances.append(min(distances))            # track the minimum
    
# ratio between the closest distance and the average distance
min_avg_ratio = [min_dist / avg_dist
                 for min_dist, avg_dist in zip(min_distances, avg_distances)]

