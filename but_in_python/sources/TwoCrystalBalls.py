import math

def two_crystal_balls(breaks):
    curr = 0
    jump = math.floor(math.sqrt(len(breaks)))
    while curr < len(breaks):
        if not breaks[curr]:
            curr = curr + jump
        else:
            limit = curr
            curr = (curr - jump) + 1
            while curr < limit:
                if breaks[curr]:
                    return curr
                else:
                    curr += 1

    return -1
