from decision_tree import partition_by
from decision_tree import partition_entropy_by
from classify import classify
from functools import partial

def build_tree_id3(inputs, split_candidates=None):
    # if this is our first pass,
    # all keys of the first input are split candidates
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()
        
    # count Trues and Falses in the inputs
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues
    
    if num_trues == 0: return False         # no Trues? return a "False" leaf
    if num_falses == 0: return True         # no Falses? return a "True" leaf
    
    if not split_candidates:                # if no split candidates left
        return num_trues >= num_falses      # return the majority leaf
    
    # otherwise, split on the best attribute
    best_attribute = min(split_candidates,
                         key=partial(partition_entropy_by, inputs))
    
    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates
                      if a != best_attribute]
    
    # recursively build the subtrees
    subtrees = { attribute_value : build_tree_id3(subset, new_candidates)
                 for attribute_value, subset in partitions.iteritems() }
    
    subtrees[None] = num_trues > num_falses         # default case
    
    return (best_attribute, subtrees)

if __name__ == '__main__':
    inputs = [
        ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'}, False),
        ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes'}, False),
        ({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
        ({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
        ({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
        ({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes'}, False),
        ({'level':'Mid',    'lang':'R', 'tweets':'yes', 'phd':'yes'}, True),
        ({'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, False),
        ({'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
        ({'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no'}, True),
        ({'level':'Senior', 'lang':'Python',  'tweets':'yes', 'phd':'yes'},True),
        ({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, True),
        ({'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no'}, True),
        ({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, False)
    ]
    tree = build_tree_id3(inputs)
    
    print classify(tree, {"level" : "Junior",
                          "lang" : "Java",
                          "tweets" : "yes",
                          "phd" : "no"})        # True
    
    print classify(tree, {"level" : "Junior",
                          "lang" : "Java",
                          "tweets": "yes",
                          "phd" : "yes"})       # False       
                