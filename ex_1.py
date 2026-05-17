# 1.7 Exerciții
# 1.1 Aplicați algoritmii insert și select pentru cazurile T = [1, 2, 3, 4, 5, 6] și
# U = [6, 5, 4, 3, 2, 1]. Asigurați-vă că ați înțeles cum funcționează. 

T = [1, 2, 3, 4, 5, 6]
U = [6, 5, 4, 3, 2, 1]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = key
    
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(insertion_sort(T))
print(selection_sort(U))
