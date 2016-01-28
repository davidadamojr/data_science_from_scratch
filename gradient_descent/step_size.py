"""To determine the right step size to use for minimizing a function, we 
can try a variety of step sizes and choose the one that results in the smallest 
value of the objective function"""

step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.0001, 0.00001]

"""To prevent a situation where certain sizes result in invalid inputs for 
our function, we'll create a "safe apply" function that returns infinity for 
invalid inputs"""

def safe(f):
    """return a new function that is the same as f, except that it outputs 
    infinity whenever f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')             # this means "inifinity" in Python
    
    return safe_f