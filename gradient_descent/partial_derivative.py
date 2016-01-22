"""When a function has many variables, it has multiple partial derivatives, 
each indicating how the function changes when we make small changes in just one 
of the input variables

We calculate a functions ith partial derivative by treating it as a function 
of just its ith variable, holding the other variables fixed."""

def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0) # add h to just the ith element of v
         for j, v_j in enumerate(v)]
    
    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]