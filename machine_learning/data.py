import random

def split_data(data, prob):
    """split data into fractions [prob, 1-prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

# we should not put a lot of credence in raw accuracy
def accuracy(tp, fp, fn, tn):
    correct = tp + tn           # true positive + true negative
    total = tp + fp + fn + tn   
    return correct / total

# precision measures how accurate our positive predictions are
def precision(tp, fp, fn, tn):
    return tp / (tp + fp)

# recall measures what fraction of the positives our model identified
def recall(tp, fp, fn, tn):
    return tp / (tp + fn)

# sometimes precision and recall are combined into an F1 score
def f1_score(tp, fp, fn, tn):
    """This is the harmonic mean of precision and recall and necessarily 
    lies between them"""
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    
    return 2 * p * r / (p + r)
