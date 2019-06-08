def quickSort(p, r):
    if p < r:
        q = partition(p, r)
        quickSort(p, q - 1)
        quickSort(q + 1, r)


def partition(p, r):
    v = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= v:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


global arr  # Array defined as global so that it is available to all methods without being passed
arr = [54, 23, 13, 546, 234, 412, 12, 32, 543, 41, 1342, 421, 1232, 2, 1]
print(f"Array before sorting: {arr}")
p = 0
r = len(arr) - 1
quickSort(p, r)
print(f"Array after sorting: {arr}")
