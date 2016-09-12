import sys
sys.path.insert(0, "../linear_algebra")
from linear_algebra.vector_operations import distance


def is_leaf(cluster):
    """a cluster is a leaf if it has a length 1"""
    return len(cluster) == 1

def get_children(cluster):
    """returns the two children of this cluster if it is a merged cluster;
    raises an exception if this is a leaf cluster"""
    if is_leaf(cluster):
        raise TypeError("a leaf cluster has no children")
    else:
        return cluster[1]

def get_values(cluster):
    """returns the value in this cluster (if it is a leaf cluster) or all the values in the leaf clusters below it
    (if it is not)"""
    if is_leaf(cluster):
        return cluster                  # is already a 1-tuple containing value
    else:
        return [value
                for child in get_children(cluster)
                for value in get_values(child)]

def cluster_distance(cluster1, cluster2, distance_agg=min):
    """compute all the pairwise distances between cluster1 and cluster2 and apply _distance_agg_ to the resulting
    list"""
    return distance_agg([distance(input1, input2)
                         for input1 in get_values(cluster1)
                         for input2 in get_values(cluster2)])

def get_merge_rder(cluster):
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]           # merge_order is first element of 2-tuple