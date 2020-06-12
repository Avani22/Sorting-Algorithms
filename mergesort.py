'''
Name: Avani Chandorkar
Student ID: 1001668554
Assignment1: Merge Sort
'''

from datetime import datetime           #package for calculating execution time of mergesort
import random                           #package for generating random numbers

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2             # Finding the mid of the array
        left = arr[:mid]                # Dividing the array elements into 2 halves (left subarray)
        right = arr[mid:]               # (right subarray)

        mergeSort(left)                 # MergeSort on the first half
        mergeSort(right)                # MergeSort on the second half

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:      #condition to check smaller number
                arr[k] = left[i]        #copying the number to final sorted array
                i += 1                  #incrementing value of i by 1
            else:
                arr[k] = right[j]       #copying the number to final sorted array
                j += 1                  #incrementing value of j by 1
            k += 1                      #incrementing value of k by 1

        while i < len(left):            # condition to check if any element was left
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def printList(arr):                     #function to print the list of numbers
    for i in range(len(arr)):
        print(arr[i])
    print()

if __name__ == '__main__':

    arr = []
    size = int(input("Enter size of the list: ")) #entering the size of array

    for i in range(size):           #loop for entering the numbers in the given range
        elements = int(input("Enter an element:"))
        arr.append(elements)

    n = len(arr)                    #calculating the length of array
    print("Array to be sorted is:")
    print(arr)
    t1 = datetime.now()             #calculating current time
    mergeSort(arr)                  #calling mergesort function
    print("Sorted array is:")
    print(arr)
    t2 = datetime.now()             #calculating current time
    print("Sorted list of size {} in {}".format(len(arr), t2 - t1)) #calculating total time elapsed for mergesort

'''
    arr = [random.randrange(1000) for _ in range(1000)]  # Randomly generate 1000 numbers
    #arr=list(range(100))
    n = len(arr)  # calculating the length of array
    print("Array to be sorted:")
    printList(arr)
    t1 = datetime.now()  # calculating current time
    mergeSort(arr)  # calling mergesort function
    print("Sorted array is:")
    printList(arr)
    t2 = datetime.now()  # calculating current time
    print("Sorted list of size {} in {}".format(len(arr), t2 - t1))  # calculating total time elapsed for mergesort
'''