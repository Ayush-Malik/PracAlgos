# https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

# [1]
# 0, 2, 5, 8, 17
# 0

# [2]
# -10, -5, 3, 4, 7, 9
# -1

arr = list(map(eval , input().split(', ')))

def get_fixed_point(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1

print(get_fixed_point(arr))