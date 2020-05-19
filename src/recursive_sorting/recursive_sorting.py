# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i=0
    j=0
    k=0
    #traverse both array
    while i < len(arrA)and j < len(arrB):
        #check if current element of the first array is smaller than currrent element second array
        if arrA[i] <= arrB[j]:
            merged_arr[k]=arrA[i]
            k = k+1
            i= i+1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1
        # store remaining elements of first array
    while i <len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1
    #store remaining element of second array
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k  = k +1
        j = j + 1



    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        arrA= merge_sort(left)
        arrB=merge_sort(right)
        arr=merge(arrA,arrB)


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid +1
    # if the direct merge is already sorted
    if (arr[mid]<= arr[start2]):
        return
    # Two pointers to maintain start
    # of both arrays to merge    
    while (start <= mid and start2 <= end):
        # if element 1 is in right place
        if (arr[start]<= arr [start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            #shift all the elements between element 1
            #element 2 , right by 1
            while (index != start):
                arr[index]=arr[index -1]
                index -=1
            arr[start] = value

            start += 1
            mid += 1
            start2 +=1


    return arr


def merge_sort_in_place(arr, l, r):
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2 
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m) 
        merge_sort_in_place(arr, m + 1, r)
  
        merge_in_place(arr, l, m, r)


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
