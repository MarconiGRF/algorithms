def bubble_sort(arr):
    i = 0
    while i < len(arr):
        j = 0
        while j < (len(arr) - i) - 1:
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            j += 1
        i += 1

    return arr
