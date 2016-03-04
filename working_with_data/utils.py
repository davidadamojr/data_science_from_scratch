"""
Function to pluck a field out of a collection of dicts.

Assume we have data of the form (list of dicts):
data = [{ 'closing_price': 102.06,
          'date': datetime.datetime(2014, 8, 29, 0, 0),
          'symbol': 'AAPL'}, 
        ]
"""

from collections import defaultdict

def picker(field_name):
    """returns a function that picks a field out of a dict"""
    return lambda row: row[field_name]

def pluck(field_name, rows):
    """turn a list of dicts into the list of field_name values"""
    return map(picker(field_name), rows)

def group_by(grouper, rows, value_transform=None):
    """function to group rows and apply a transform"""
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    
    if value_transform is None:
        return grouped
    else:
        return { key : value_transform(rows)
                 for key, rows in grouped.iteritems() }