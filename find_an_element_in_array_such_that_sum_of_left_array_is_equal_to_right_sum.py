# https://www.geeksforgeeks.org/find-element-array-sum-left-array-equal-sum-right-array/?ref=rp

arr = list(map(eval , input().split()))

# Logic
# We maintain left_sum and right_sum for each element and finds that whether left_sum == right_sum to find partition element

# 2 traversals => O(N) time
# constant space => O(1)

right_sum = 0
for val in arr:
    right_sum += val

left_sum = 0
prev_val = 0
for i in range(len(arr)):
    left_sum  += prev_val
    right_sum -= arr[i]
    prev_val   = arr[i]

    if left_sum == right_sum:
        print(arr[i] , "is the required partition element!!!")
        break