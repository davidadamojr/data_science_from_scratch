"""
Tree representation:

('level', 
    {'Junior': ('phd', {'no': True, 'yes': False}),
     'Mid': True,
     'Senior': ('tweets', {'no': False, 'yes': True})})
"""

def classify(tree, input):
    """classify the input using the given decision tree"""
    
    # if this is a leaf node, return its value
    if tree in [True, False]:
        return tree
    
    # otherwise this tree consists of an attribute to split on 
    # and a dictionary whose keys are values of that attribute
    # and whose values are subtrees to consider next
    attribute, subtree_dict = tree
    
    subtree_key = input.get(attribute)      # None if input is missing attribute
    
    if subtree_key not in subtree_dict:     # if no subtree for key,
        subtree_key = None                  # we will use the None subtree
    
    subtree = subtree_dict[subtree_key]     # choose the appropriate subtree
    return classify(subtree, input)         # and use it to classify the input