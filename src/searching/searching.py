# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if target == arr[i]:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  mid = 0

  while high > low:
    mid = int((high + low) / 2)
    if arr[mid] > target:
      high = mid
    else:
      if arr[mid] == target:
        return mid

      low = mid + 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  
  if arr[middle] > target:
      return binary_search_recursive(arr, target, low, middle)
  else:
    if arr[middle] == target:
      return middle

    return binary_search_recursive(arr, target, middle + 1, high)
