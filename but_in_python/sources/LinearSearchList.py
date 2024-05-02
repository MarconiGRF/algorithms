def linear_search_list(array, value) -> bool:
    for curr in array:
        if curr == value:
            return True
    return False