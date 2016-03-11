import sys
sys.path.insert(0, '../linear_algebra')
sys.path.insert(0, '../gradient_descent')
from matrix_operations import shape
from vector_operations import magnitude
from gradient_descent import gradient_descent
from vector_operations import scalar_multiply
from vector_operations import dot
from vector_operations import vector_subtract

def de_mean_matrix(A):
    """returns the result of subtracting from every value in A the mean 
    value of its column. The resulting matrix has mean 0 in every column"""
    nr, nc = shape(A)
    column_means, _ = scale(A)
    return make_matrix(nr, nc, lambda i, j: A[i][j] - column_means[j])

def direction(w):
    mag = magnitude(w)
    return [w_i / mag for w_i in w]

def directional_variance_i(x_i, w):
    """the variance of the row x_i in the direction determined by w"""
    return dot(x_i, direction(w)) ** 2

def directional_variance(X, w):
    """the variance of the data in the direction determined by w"""
    return sum(directional_variance_i(x_i, w)
               for x_i in X)
    
def directional_variance_gradient_i(x_i, w):
    """the contribution of row x_i to the gradient of the direction-w variance"""
    projection_length = dot(x_i, direction(w))
    return [2 * projection_length * x_ij for x_ij in x_i]

def directional_variance_gradient(X, w):
    return vector_sum(directional_variance_gradient_i(x_i, w)
                      for x_i in X)

def first_principal_component(X):
    """the first principal component is the direction that maximizes the 
    directional_variance function"""
    guess = [1 for _ in X[0]]
    unscaled_maximizer = maximize_batch(
                                        partial(directional_variance, X),
                                        partial(directional_variance_gradient, X),
                                        guess)
    return direction(unscaled_maximizer)

def project(v, w):
    """return the projection of v onto the direction w"""
    projection_length = dot(v, w)
    return scalar_multiply(projection_length, w)

def remove_projection_from_vector(v, w):
    """If we want to find further components beyond the first, we first remove the 
    projections from the data using this function"""
    """projects v onto w and subtracts the result from v"""
    return vector_subtract(v, project(v, w))

def remove_projection(X, w):
    """for each row of X
    projects the row onto w, and subtracts the result from the row"""
    return [remove_projection_from_vector(x_i, w) for x_i in X]

def principal_component_analysis(X, num_components):
    """on a high dimensional data set, we can iteratively find as many components 
    as we want"""
    components = []
    for _ in range(num_components):
        component = first_principal_component(X)
        components.append(component)
        X = remove_projection(X, component)
    
    return components

def transform_vector(v, components):
    return [dot(v, w) for w in components]

def transform(X, components):
    return [transform_vector(x_i, components) for x_i in X]