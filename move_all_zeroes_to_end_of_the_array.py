# https://www.geeksforgeeks.org/move-zeroes-end-array/
arr = list(map(eval , input().split(', ')))

# We will use 2 pointer approach
def find_index_of_zero_in_(starting_index , arr):
    for i in range(starting_index , len(arr)):
        if arr[i] == 0:
            return i
    return -1


def swap(first_index , second_index , arr):
    arr[first_index] , arr[second_index] = arr[second_index] , arr[first_index]


# Let's find the index for first 0 in given array
index_of_zero = find_index_of_zero_in_(0 , arr)
# print("Initial value for zero index" , index_of_zero)

if index_of_zero != -1: # Means there exists atleast one 0 in arr

    x = index_of_zero + 1

    while x < len(arr):
        if arr[x] != 0:
            swap(index_of_zero , x , arr)
            index_of_zero = find_index_of_zero_in_(index_of_zero + 1 , arr)
            # print(index_of_zero , x , arr)
        x += 1

print("Array after moving all zeroes to end : ")
print(arr)