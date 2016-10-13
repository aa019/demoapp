def find_avg(L, a, b):
    avg = (a + b)/2
    for x in L:
        if x == avg:
            return True
    return False