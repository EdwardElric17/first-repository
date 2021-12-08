def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key] = []
        d[2*key].append(value)
    return(d)
d = {}
print(update_dictionary(d, 1, -1))
print(update_dictionary(d, 2, -2))
print(update_dictionary(d, 1, -3))