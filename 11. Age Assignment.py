def age_assignment(*args, **kwargs):
    details = {}
    for arg in args:
        details[arg] = kwargs[arg[0]]
    return details


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))