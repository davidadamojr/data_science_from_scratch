import random

def bootstrap_sample(data):
    """ randomly samples len(data) elements with replacement """
    return [random.choice(data) for _ in data]

def bootstrap_statistic(data, stats_fn, num_samples):
    """ evaluates stats_fn on num_samples bootstrap samples from data """
    return [stats_fn(bootstrap_sample(data))
            for _ in range(num_samples)]