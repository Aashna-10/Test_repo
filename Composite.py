def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted part
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [29, 10, 14, 37, 13]
selection_sort(arr)
print("Sorted array:", arr)
