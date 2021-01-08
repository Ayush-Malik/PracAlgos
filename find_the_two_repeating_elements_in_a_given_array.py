# https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

# [1]
# 2, 3, 1, 3, 9, 4, 5, 9, 6, 7, 8
# Duplicate elements are : 3 9

# O(N) Time => 2 Traversals
# O(1) Constant space




arr = list(map(eval , input().split(', ')))

def get_two_duplicates_from_(arr):
    for i in range(len(arr)):
        arr[ abs(arr[i]) - 1 ] = -arr[ abs(arr[i]) - 1]

    print("Duplicate elements are :" , end = " ")
    for i in range(len(arr) - 2):
        if arr[i] > 0:
            print(i + 1 , end = " ")

get_two_duplicates_from_(arr)