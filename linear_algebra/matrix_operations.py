def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row
    return num_rows, num_cols

def get_row(A, i):
    return A[i] # A[i] is already the ith row

def get_column(A, j):
    return [A_i[j] # jth element of row A_i 
            for A_i in A] # for each row A_i

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols_matrix whose (i,j)th entry is 
    entry_fn(i,j)"""
    return [[entry_fn(i,j)               # given i, create a list
             for j in range(num_cols)]   # [entry_fn(i,0), ... ]
             for i in range(num_rows)]   # create one list for each i

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0