#  correct the broken function to make sure that the second argument (tail), 
# is the same as the last letter of the first argument (body) - 
# otherwise the tail wouldn't fit!
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False