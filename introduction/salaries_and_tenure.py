from collections import defaultdict

# SALARIES AND EXPERIENCE
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# bucket the tenures then group together the salaries corresponding to each bucket
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
# compute the average salary for each group
# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
                            tenure_bucket : sum(salaries) / len(salaries)
                            for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
                            }

print average_salary_by_bucket
