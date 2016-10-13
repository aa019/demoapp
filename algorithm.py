def find_diff(L, a, b):
    diff = abs(a - b)
    for x in L:
        if x == diff:
            return 1
    return 0