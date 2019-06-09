'''
QUICKSORT Algorithm
Modified from CLRS Algorithm to:
- Leave the pivot in place in the first position in the sub-array
- During partition, the original order of digits is retained in the two partitioned arrays
  (slightly less efficient than the original algorithm but required for a Hackerrank question)
'''


def quickSort(p, r):
    if p < r:
        q = partition(p, r)
        quickSort(p, q - 1)
        quickSort(q + 1, r)


def partition(p, r):
    v = arr[p]
    i = p
    for j in range(p + 1, r + 1):
        if arr[j] <= v:
            i += 1
            arr[i], arr[i + 1:j + 1] = arr[j], arr[i:j]
    arr[i], arr[p:i] = arr[p], arr[p + 1:i + 1]
    return i


global arr  # Array defined as global so that it is available to all methods without being passed back and forth
arr = [54, 23, 13, 546, 234, 412, 12, 32, 543, 41, 1342, 421, 1232, 2, 1]
print(f"Array before sorting: {arr}")
p = 0
r = len(arr) - 1
quickSort(p, r)
print(f"Array after sorting: {arr}")
