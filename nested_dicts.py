def short_pattern():
    pattern = {"sequence":"101", "occurrences":5}
    return pattern

def medium_pattern():
    pattern = {"sequence":"111000", "occurrences":5}
    return pattern

def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    return pattern

def pattern():
    return {"sequence":s, "occurrences":o}

def run():
    print("Analysing Patterns...")
    d = {"print short pattern"}