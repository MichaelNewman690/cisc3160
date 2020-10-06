

#python implementation of merge sort
def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr)//2 #uses and needs floor divion operator since regular / returns a float
        left = arr[:middle]
        right = arr[middle:]

        #call itself on the left and right side. will work recursively
        mergeSort(left)
        mergeSort(right)

        i = 0
        j =0
        k = 0
        #copy and merge data back from 2 temp arrays.
        #Starts with leftmost element thanks to recursion
        #
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        #check if any elements are left (there will be 2 if
        # there was a odd number of elements or 1 if there was a even number
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k+=1

        while j < len(right):
            arr[k]= right[j]
            j += 1
            k+=1

def printArray(arr):
    for x in range(len(arr)):
        print(arr[x])

#testing out mergeSort
arr = [35, 16, 22, 18, 91, 108, 5, 4, 3, 2, 1]
mergeSort(arr)
printArray(arr)



