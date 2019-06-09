'''
QUICKSORT Algorithm
Directly following the pseudocode from CLRS
'''


# QUICKSORT(A, p, r)
# 1 if p < r
# 2     q = PARTITION(A, p, r)
# 3     QUICKSORT(A, p, q-1)
# 4     QUICKSORT(A, q+1, r)

def quickSort(p, r):
    if p < r:
        q = partition(p, r)
        quickSort(p, q - 1)
        quickSort(q + 1, r)


# PARTITION(A, p, r)
# 1  v = A[r]
# 2  i = p − 1
# 3  for j = p to r − 1
# 4        if A[j ] ≤ v
# 5             i =i + 1
# 6             exchange A[i ] withA[j]
# 7  exchange A[i + 1] with A[r]
# 8  return i + 1

def partition(p, r):
    v = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= v:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


global arr  # Array defined as global so that it is available to all methods without being passed back and forth
arr = [54, 23, 13, 546, 234, 412, 12, 32, 543, 41, 1342, 421, 1232, 2, 1]
print(f"Array before sorting: {arr}")
p = 0
r = len(arr) - 1
quickSort(p, r)
print(f"Array after sorting: {arr}")
