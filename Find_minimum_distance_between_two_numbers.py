# https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/


# [1] Test Case for multiple ranges
# 2, 5, 3, 5, 4, 4, 2, 1, 3, 2
# 3 2
# 1

# [2] Test case with duplicates in contiguous way --> important case
# 2, 5, 3, 5, 4, 4, 2, 1, 3, 3, 2
# 3 2
# 1




arr = list(map(eval , input().split(', ')))
x , y = list(map(eval , input().split()))

first_element_found = False
f_index = -1
min_dis = -1
for i in range(len(arr)):
    if not first_element_found:
        if arr[i] == x:
            first_element_found = True
            f_index = i
            next = y
        elif arr[i] == y:
            first_element_found = True
            f_index = i
            next = x
    else:
        if arr[i] == next:
            if min_dis == -1 or min_dis > i - f_index:
                min_dis = i - f_index
            f_index = i
            next = x + y - next

        elif arr[i] == x + y - next: # Important if element found itself for test case 2
            f_index = i

print(min_dis)
