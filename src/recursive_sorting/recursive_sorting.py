# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    size = max(len(arrA), len(arrB))
    while (len(arrA) > 0 or len(arrB) > 0):
        if len(arrA) > 0 and len(arrB) > 0:
            if (arrA[0] < arrB[0]):
                merged_arr.append(arrA[0])
                del arrA[0]
            else:
                merged_arr.append(arrB[0])
                del arrB[0]
        elif len(arrA) > 0:
            merged_arr.append(arrA[0])
            del arrA[0]
        elif len(arrB) > 0:
            merged_arr.append(arrB[0])
            del arrB[0]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr

    length = len(arr)
    midPoint = int((length - 1)/ 2)

    merged_arr = merge(merge_sort(arr[0: midPoint + 1]), merge_sort(arr[midPoint + 1: length]))
    return merged_arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
