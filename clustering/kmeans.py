import sys
sys.path.insert(0, '../linear_algebra')

from linear_algebra.vector_operations import vector_mean

class KMeans:
    """performs k-means clustering"""
    
    def __init__(self, k):
        self.k = k          # number of clusters
        self.means = None   # means of clusters
    
    def classify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))
    
    def train(self, inputs):
        # choose k random points as the initial means
        self.means = random.sample(inputs, self.k)
        assignments = None
        
        while True:
            # Find new assignments
            new_assignments = map(self.classify, inputs)
            
            # if no assignments have changed, we're done
            if assignments == new_assignments:
                return
            
            # Otherwise keep the new assignments
            assignments = new_assignments
            
            # And compute new means based on the new assignments
            for i in range(self.k):
                # find all the points assigned to cluster i
                i_points = [p for p, a in zip(inputs, assignments) if a == i] 
                
            # make sure i_points is not empty so don't divide by 0
            if i_points:
                self.means[i] = vector_mean(i_points)