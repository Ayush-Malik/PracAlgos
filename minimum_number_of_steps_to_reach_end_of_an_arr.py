# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#
arr = list(map(eval , input().split()))

i = 0

def find_max_val_index_in(arr):
    max_val = arr[0]
    max_ind = 0

    for i in range(1 , len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_ind = i

    return max_ind


def get_minimum_jumps_reach_end_of_(arr):
    i = 0
    jumps = 0

    if arr[0] == 0 : # Edge Case
        return -1

    while i < len(arr) - 1:

        if arr[i] == 0 and i != len(arr) - 1: #Edge case
            return -1

        jumps += 1

        if i + arr[i] == len(arr) - 1:
            return jumps

        i = i + 1 + find_max_val_index_in(arr[i + 1 : min(i + arr[i] + 1 , len(arr))])

    return jumps

print(get_minimum_jumps_reach_end_of_(arr))
