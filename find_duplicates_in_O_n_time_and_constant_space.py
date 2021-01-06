# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

# [1]
# 1, 2, 3, 6, 3, 6, 1
# 3
# 6
# 1

# Number in array must be in range (0 to n - 1)
arr = list(map(eval , input().split(', ')))

# In this we use marking on the basis of indexing --> A very very intresting approach

def get_duplicates(arr):
    for i in range(len(arr)):
        if arr[ abs(arr[i]) ] > 0 : # if positive means this is the first occurence of that element
           arr[ abs(arr[i]) ] = - arr[ abs(arr[i]) ] # Marking the value using negative sign such that its index is the value which is marked
        else: # if negative means this is the second occurene of that element so we will append the element to our ans list
           print(abs(arr[i]))

get_duplicates(arr)