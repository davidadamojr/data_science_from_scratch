from __future__ import division # help avoid integer division
from collections import Counter
from collections import defaultdict

users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"}]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"]) # length of friend_ids list

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in  users]

# sort by num_friends from largest to smallest
sorted(num_friends_by_id, key=lambda(user_id, num_friends): num_friends, reverse=True)

# DATA SCIENTISTS YOU MAY KNOW
def friends_of_friends_ids_bad(user):
    """
    This returns certain friends of friends multiple times and also returns friends of friends
    that are already friends of _user_
    """
    # "foaf" is short for "friend of a friend"
    # for each of user's friends, get each of _their_ friends
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]] 

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, ifhe's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user) for friend in user["friends"])

# mutual friends
def friends_of_friend_ids(user):
    return Counter(foaf["id"] for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf) and not_friends(user, foaf))
    
# friend of friends for user[3]
print friends_of_friend_ids(users[3])
