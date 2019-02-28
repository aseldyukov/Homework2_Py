# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
def enough(cap, on, wait):
    if cap <= on+wait:
        return on+wait-cap
    else:
        return 0