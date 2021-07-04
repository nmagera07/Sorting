# TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




   # return arr



def selection_sort(arr):
    def findSmallest(arr):
        smallest = arr[0]
        smallest_index = 0

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i

        return smallest_index

    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr