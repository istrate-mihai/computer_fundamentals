# Iterative
def binary_search_iter(arr, item):

    size = len(arr) - 1
    low  = 0
    high = size

    while low <= high:

        mid = (low + high) // 2

        if item == arr[mid]:
            return mid
        elif item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Recursive
def binary_search_recur(arr, low, high, item):

    if low <= high:

        mid = (low + high) // 2

        if item == arr[mid]:
            return mid
        elif item > arr[mid]:
            return binary_search_recur(arr, mid + 1, high, item) 
        else:
            return binary_search_recur(arr, low, mid - 1, item)

    return -1

store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binary_search_recur(store, 0, 7, 2))

def nearest_mid(arr, low, high, search_term):
	return low + (high - low) / (arr[high] - arr[low]) * (search_term - arr[low])
