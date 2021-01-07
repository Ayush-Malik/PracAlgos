# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

arr = list(map(eval , input().split(', ')))

# Let's find the actual first index of rotated sorted array
min_ele = arr[0]
min_ele_index = 0

for i in range(1 , len(arr)):
    if arr[i] < min_ele:
        min_ele = arr[i]
        min_ele_index = i

# print(f"{min_ele} : {min_ele_index}")

def bin_search(ele , arr):
    first = 0
    last  = len(arr) - 1
    while first <= last:
        mid = ((first + last) // 2)
        up_mid = (mid + min_ele_index) % len(arr)
        if ele == arr[up_mid] :
            return up_mid
        elif ele < arr[up_mid]:
            last = mid - 1
        elif ele > arr[up_mid]:
            first = mid + 1
    return -1

print(bin_search(int(input("Enter the element to be searched : ")), arr))