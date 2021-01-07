# https://www.geeksforgeeks.org/find-lost-element-from-a-duplicated-array/

arr_1 = list(map(eval , input().split(', ')))
arr_2 = list(map(eval , input().split(', ')))

# Any one array (arr_1 or arr_2) can be bigger and another one will be obviously smaller
#size -> (N)
#size -> (N - 1) -> This array is made using arr_1 but one elements is lost we have to find that


# LOGIC => Missing_element = abs( sum(arr_1) - sum(arr_2) )
# 2 Traversals required   => O(N)
# No extra space required => O(1)

print(f"Missing Element is :" , abs(sum(arr_1) - sum(arr_2)))
