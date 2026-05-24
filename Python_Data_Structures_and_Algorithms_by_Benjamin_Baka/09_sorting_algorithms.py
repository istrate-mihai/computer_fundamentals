# • Bubble Sort
# Time complexity:
# O(n ^ 2): worst / average case
# O(n):     best case

def bubble_sort(arr):
    iterations = len(arr) - 1

    for i in range(iterations):
        for j in range(iterations):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# • Selection Sort
# Time Complexity:
# Worst / Best O(n ^ 2)
def selection_sort(arr):
	n = len(arr)

	for i in range(n - 1):
		min_idx = i

		for j in range(i + 1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j

		arr[i], arr[min_idx] = arr[min_idx], arr[i]

# • Insertion Sort
# Time complexity:
# O(n ^ 2): worst / average case
# O(n):     best case
# Stable:   Doesn't change the relative order of elements that have equal keys, it doesn't require more
# memory than it is consumed by the list because it does the sorting in place

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j = j - 1

		arr[j + 1] = key

# • Quick Sort
# Time Complexity:
# Worst case: O(n ^ 2)
# Best case:  O(n log n)

def partition(unsorted_array, first_index, last_index):
    pivot                 = unsorted_array[first_index]
    pivot_index           = first_index
    index_of_last_element = last_index
	
    less_than_pivot    = index_of_last_element
    greater_than_pivot = first_index + 1
	
    while True:
        while unsorted_array[greater_than_pivot] < pivot and greater_than_pivot < last_index:
            greater_than_pivot += 1

        while unsorted_array[less_than_pivot] > pivot and less_than_pivot > first_index:
            less_than_pivot -= 1

        if unsorted_array[greater_than_pivot] < unsorted_array[less_than_pivot]:
            unsorted_array[greater_than_pivot], unsorted_array[less_than_pivot] = unsorted_array[less_than_pivot], unsorted_array[greater_than_pivot]
        else:
            break
    
    unsorted_array[less_than_pivot], unsorted_array[pivot_index] = unsorted_array[pivot_index], unsorted_array[less_than_pivot]
    return less_than_pivot

def quick_sort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        partition(unsorted_array, first, partition_point - 1)
        partition(unsorted_array, partition_point + 1, last)
