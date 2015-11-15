from collections import defaultdict
from collections import Counter

interests = [
             (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
             (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
             (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
             (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
             (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
             (3, "statistics"), (3, "regression"), (3, "probability"), 
             (4, "machine learning"), (4, "regression"), (3, "probability"),
             (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
             (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
             (6, "probability"), (6, "mathematics"), (6, "theory"), 
             (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
             (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
             (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
             (9, "Java"), (9, "MapReduce"), (9, "Big Data")
             ]

# find users with a certain interest
def data_scientists_who_like(target_interest):
    # not very efficient since the entire list of user, interest pairs has to be 
    # examined for every search
    return [user_id for user_id, user_interest in interests 
            if user_interest == target_interest]

# instead build an index from interests to users
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# build another index from users to interests
# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interest_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])
