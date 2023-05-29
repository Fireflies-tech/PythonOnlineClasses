
def sort(arr):
    count_len = max(arr) + 1
    min_elm = min(arr)
    if min_elm < 0:
        count_len += abs(min_elm)

    count = [None] * count_len

    for i in range(len(arr)):
        idx = arr[i] - min_elm
        if count[idx] is None:
            count[idx] = 1
        else:
            count[idx] += 1

    i = 0
    for value, c in enumerate(count):
        if isinstance(c, int):
            arr[i:i + c] = [value - -min_elm] * c
            i += c

    return arr


# arr = [4, 2, 2, 8, 3, 3, 1]

arr = [-2, 45, 0, 11, -9, 0, 0]

print(sort(arr))
