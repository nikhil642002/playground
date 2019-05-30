# MERGE(A, p, q, r) # 25, 50, 75
# n1 = q - p + 1    # 26
# n2 = r - q        # 25
# let L[1 ... n1+1] and R[1 ... n2+1] be new arrays
# for i = 1 to n1   # 1...26
#     L[i] = A[p + i - 1]
# for j = 1 to n2   # 1...25
#     R[j] = A[q + j]
# L[n1 + 1] = ꚙ
# R[n2 + 1] = ꚙ
# i = 1
# j = 1
# for k = p to r
#     if L[i] <= R[j]
#         A[k] = L[i]
#         i = i + 1
#     else
#         A[k] = R[j]
#         j = j + 1

# Adjusted to account for Python 0 indexing

from numpy import inf


def merge(p, q, r):
    print("Merge called on ranges {}-{} and {}-{}".format(p, q - 1, q, r))
    global A
    L = A[p:q] + [inf]
    R = A[q:r + 1] + [inf]
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


# MERGE-SORT(A, p, r)
# if p < r
#     q = └ (p + r) / 2 ┘
#     MERGE-SORT(A, p, q)
#     MERGE-SORT(A, q+1, r)
#     MERGE(A, p, q, r)
#
def merge_sort(p, r):
    print("Merge_sort called from {} to {}".format(p, r))
    global A
    if p < r:
        q = int((p + r + 1) / 2)
        print("Splits are {}-{} and {}-{}".format(p, q - 1, q, r))
        print("Pre-merge {} and {}".format(A[p:q], A[q:r + 1]))
        merge_sort(p, q - 1)
        merge_sort(q, r)
        print("Post sub-sort {} and {}".format(A[p:q], A[q:r + 1]))
        merge(p, q, r)
        print("Post-merge {}".format(A))
        print("")


# A = [1,9,2,8,3,7,4,6,5]
# A = [1, 32, 41, 12, 23, 53, 12, 543, 76, 34, 234, 23, 65, 867, 98, 456, 34, 543, 2, 3, 1, 56, 253, 54]
A = [5, 2, 4, 7, 1, 3, 2, 6]
print("Input has length {}".format(len(A)))
merge_sort(0, len(A) - 1)
print(A)
