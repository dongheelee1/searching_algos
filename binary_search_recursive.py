#binary search

#in binary search, we assume that the list is already sorted in ascending order 
a = [1, 2, 3, 4, 5, 6, 7, 8]

# x is the number that we are searching for in the array 
# arr is the given list 
#start is the start index of the list 
#end is the end index of the list 

def binary_search(arr, x, start, end):
    
    if start > end:
        return -1 #return -1 when start index is greater than end index 
    
    mid = (start + end) // 2 #get the middle idx 
    
    if arr[mid] == x: 
        return mid  #return mid idx if the middle element equals the element we are searching for 
    elif x < arr[mid]:
        return binary_search(arr, x, 0, mid) #if middle element is greater than element we are searching for 
    elif x > arr[mid]:
        return binary_search(arr, x, mid + 1, len(arr) - 1) #if middle element is smaller than element we are searching for 


print(binary_search(a, 100, 0, len(a) - 1))
  
