# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/

arr = list(map(eval , input().split(', ')))

def swap(i , j , arr):
    arr[i] , arr[j] = arr[j] , arr[i]

# Condition : Array must contains distinct numbers
# If index is even then next number must be greater , if not then we will swap
# If index is odd then next number must be smaller , if not hen we will swap

# CORE LOGIC
for i in range(len(arr) - 1):
    if i % 2 == 0 : # even index
        if arr[i] > arr[i + 1]: # If next element is smaller
            swap(i , i + 1 , arr)
    else: # odd index
        if arr[i] < arr[i + 1]: # If next element is greater
            swap(i , i + 1 , arr)

print("Rearranged array :" , arr)