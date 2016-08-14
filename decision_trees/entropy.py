import math

from collections import Counter

def entropy(class_probabilities):
    """given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2)
               for p in class_probabilities
               if p)                        # ignore zero probabilities
    
def class_probabilities(labels):
    total_count = len(labels)
    return [float(count) / total_count
            for count in Counter(labels).values()]
    
def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    """find the entropy from this partition of data into subsets
    subsets is a list of lists of labeled data"""
    
    total_count = sum(len(subset) for subset in subsets)
        
    return sum(data_entropy(subset) * len(subset) / total_count
               for subset in subsets)
    
    
    