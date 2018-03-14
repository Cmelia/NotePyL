def normalize(name):
    return name.lower().title()

print list(map(normalize,['adam','LISA','barT']))
