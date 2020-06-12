'''
Name: Avani Chandorkar

'''

from datetime import datetime           #package for calculating execution time of mergesort
import random                           #package for generating random numbers
import time
def quickSort(arr, low, high):          # Function to perform Quick sort
    if low < high:
        pi = partition(arr, low, high)  #pi is partitioning index
        quickSort(arr, low, pi - 1)     #Separately sort elements before partition and after partition
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = low  # pivot                #setting lowest element as pivot

    for i in range(low+1, high+1):
        if arr[i] <= arr[low]:
            # increment index of smaller element
            pivot = pivot + 1
            arr[i], arr[pivot] = arr[pivot], arr[i] #swapping i with pivot

    arr[pivot], arr[low] = arr[low], arr[pivot] #swapping low with pivot
    return pivot

arr = []
low=0
high= len(arr)-1
size = int(input("Enter size of the list: "))   #entering the size of array

for i in range(size):
    elements = int(input('Enter an element:'))
    arr.append(elements)

n = len(arr)                #calculating the length of array
print("Array to be sorted is:")
print(arr)
t1 = datetime.now()         #calculating current time
quickSort(arr, 0, n - 1)    #calling quicksort function
print("Sorted array is:")
print(arr)
t2 = datetime.now()         #calculating current time
print("Sorted list of size {} in {}".format(len(arr), t2 - t1)) #calculating total time elapsed for quicksort

'''
arr=[random.randrange(1000) for _ in range(1000)]   #Randomly generate 1000 numbers
#arr=list(range(100))
n = len(arr)                #calculating the length of array
print("Array to be sorted is:")
for i in range(n):
    print("%d" % arr[i]),
t1 = datetime.now()          #calculating current time
quickSort(arr, 0, n - 1)    #calling quicksort function
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
t2 = datetime.now()         #calculating current time
print("Sorted list of size {} in {}".format(len(arr), t2 - t1))     #calculating total time elapsed for quicksort

'''
