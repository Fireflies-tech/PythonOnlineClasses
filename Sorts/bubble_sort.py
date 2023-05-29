
def sort(arr):
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


arr = [-2, 45, 0, 11, -9]

print(sort(arr))

# assert sorted([-2, 45, 0, 11, -9]) == sort(arr)
