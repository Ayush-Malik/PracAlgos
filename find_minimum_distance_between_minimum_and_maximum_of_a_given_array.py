# https://www.geeksforgeeks.org/minimum-distance-between-the-maximum-and-minimum-element-of-a-given-array/?ref=rp

# [1] Test Case
# 3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 8, 2
# 3

arr = list(map(eval , input().split(', ')))
min_element = arr[0]
max_element = arr[1]


# Finding minimum and maximum element in the array , Now we will find minimum distance between min and max element
for i in range(1 , len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
    if arr[i] < min_element:
        min_element = arr[i]



f_index = -1
x = min_element
y = max_element
min_dis = -1

first_element_found = False
for i in range(len(arr)):
    if not first_element_found:
        if arr[i] == x:
            next = y
            first_element_found = True
            f_index = i
        elif arr[i] == y:
            next = x
            first_element_found = True
            f_index = i

    else:
        if arr[i] == next:
            if min_dis == -1 or min_dis > i - f_index:
                min_dis = i - f_index
            f_index = i
            next = x + y - next
        if arr[i] == x + y - next:
            f_index = i

print(min_dis)