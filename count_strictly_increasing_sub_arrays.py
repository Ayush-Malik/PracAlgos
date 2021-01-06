# https://www.geeksforgeeks.org/count-strictly-increasing-subarrays/

# [1]
# 1, 2, 2, 4
# There are 2 number of strictly increasing sub_arrays in given array

# [2]
# 1, 2, 3, 4
# There are 6 number of strictly increasing sub_arrays in given array


arr = list(map(eval , input().split(', ')))

# Main funda -__- => suppose we found an strictly increasing sub_array in our array , then total number of sub_arrays that are strictly increasing contained in it is , take num = (size -1) ,,( num * (num + 1) ) // 2

len_of_sub_arr = 1
number_of_strictly_increasing_sub_arrs = 0
for i in range(len(arr) - 1): # Here we are traversing in pairs
    if arr[i] < arr[i + 1]: # Condition for strictly increasing sub_array
        len_of_sub_arr += 1
    else:
        num = len_of_sub_arr - 1
        number_of_strictly_increasing_sub_arrs += (num * (num + 1)) // 2
        len_of_sub_arr = 1
else:
    if len_of_sub_arr != 1:
        num = len_of_sub_arr - 1
        number_of_strictly_increasing_sub_arrs += (num * (num + 1)) // 2

print(f"There are {number_of_strictly_increasing_sub_arrs} number of strictly increasing sub_arrays in given array")
