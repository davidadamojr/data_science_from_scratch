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

def get_merge_order(cluster):
    if is_leaf(cluster):
        return float('inf')
    else:
        return cluster[0]           # merge_order is first element of 2-tuple

def bottom_up_cluster(inputs, distance_agg=min):
    # start with every input a leaf cluster / 1-tuple
    clusters = [(input,) for input in inputs]

    # as long as we have more than one cluster left...
    while len(clusters) > 1:
        # find the two closest clusters
        c1, c2 =  min([(cluster1, cluster2)
                       for i, cluster1 in enumerate(clusters)
                       for cluster2 in clusters[:i]],
                      key=lambda(x, y): cluster_distance(x, y, distance_agg))

        # remove them from the list of clusters
        clusters = [c for c in clusters if c != c1 and c != c2]

        # merge them, using merge_order = # of clusters left
        merged_cluster = (len(clusters), [c1, c2])

        # and add their merge
        clusters.append(merged_cluster)

    # when there is only one cluster left, return it
    return clusters[0]


if __name__ == '__main__':
    def generate_clusters(base_cluster, num_clusters):
        # start with a list with just the base cluster
        clusters = [base_cluster]

        # as long as we don't have enough clusters yet...
        while len(clusters) < num_clusters:
            # choose the last-merged of our clusters
            next_cluster = min(clusters, key=get_merge_order)
            # remove it from the list
            clusters = [c for c in clusters if c != next_cluster]
            # and add its children to the list (i.e., unmerge it)
            clusters.extend(get_children(next_cluster))

        # once we have enough clusters..
        return clusters