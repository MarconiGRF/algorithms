def bs_list(haystack, needle):
    low = 0
    high = len(haystack)

    while low < high:
        mid = (low + (high - low)) // 2
        if haystack[mid] == needle:
            return True
        elif needle < haystack[mid]:
            high = mid
        else:
            low = mid + 1

    return False;