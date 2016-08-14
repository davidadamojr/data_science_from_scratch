from functools import partial
from logistic_functions import logistic_log_gradient
from logistic_functions import logistic_log_likelihood

random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(rescaled_x, y, 0.33)

# want to maximize log likelihood on the training data
fn = partial(logistic_log_likelihood, x_train, y_train)
gradient_fn = partial(logistic_log_gradient, x_train, y_train)

# pick a random starting point
beta_0 = [random.random() for _ in range(3)]

# and maximize using gradient descent
beta_hat = maximize_batch(fn, gradient_fn, beta_0)

# # beta_hat = maximize_stochastic(logistic_log_likelihood_i,
#                                 logistic_log_gradient_i,
#                                 x_train, y_train, beta_0)

