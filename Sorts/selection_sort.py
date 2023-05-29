
def sort(arr):
    for step in range(len(arr)):
        min_idx = step

        for i in range(step + 1, len(arr)):

            if arr[i] < arr[min_idx]:
                min_idx = i

        # min_idx = 4

        arr[step], arr[min_idx] = arr[min_idx], arr[step]

    return arr

arr = [-2, 45, 0, 11, -9]
print(sort(arr))

