# https://www.geeksforgeeks.org/find-subarray-least-average/

# [1] Test Case
# 3, 7, 90, 20, 10, 50, 40
# 3
# 20 10 50

arr = list(map(eval , input().split(', ')))
k = int(input("Enter the size of the subarray : "))

# Logic -> Subarray with least average has least sum

# Creating initial subarray

subarr_sum = 0
starting_index = 0
for i in range(k):
    subarr_sum += arr[i]

print(subarr_sum)

# Preparing other sub_arrays and storing the least sum sub_arr in (subarr_sum) VARIABLE and its starting index of least sum sub_array will be stored in (index) VARIABLE

for i in range(1 , len(arr) - k + 1):
    new_sub_arr_sum = subarr_sum - arr[i - 1] + arr[i + k - 1]
    if new_sub_arr_sum < subarr_sum:
        subarr_sum = new_sub_arr_sum
        starting_index = i

# Printing the least average sub_array
print("Subarray with least average is : " , end = " ")
for i in range(starting_index , starting_index + k):
    print(arr[i] , end = " ")
