# https://www.geeksforgeeks.org/find-the-missing-number/
arr = list(map(eval , input().split(', ')))

# we will find the missing number using => [sum of numbers upto size numberi + 1] -  sum(arr)

# Solution will be in O(N) time and O(1) constant space

sum_of_arr = 0
for val in arr:
    sum_of_arr += val

num = len(arr) + 1
sum_upto_size = ( num * (num + 1) ) // 2

print("Missing number is :" , sum_upto_size - sum_of_arr)