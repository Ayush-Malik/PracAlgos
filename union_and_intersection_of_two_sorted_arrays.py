# https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/


arr_1 = list(map(eval , input().split(', ')))
arr_2 = list(map(eval , input().split(', ')))

def remove_duplicates(arr):
    # o(n) time is required to remove duplicates from a sorted array
    ans = []
    ans.append(arr[0])

    for i in range(1 , len(arr)):
        if ans[-1] != arr[i]:
            ans.append(arr[i])
    return ans

# removing the duplicates from sorted arrays
arr_1 = remove_duplicates(arr_1)
arr_2 = remove_duplicates(arr_2)

def get_intersection_of(arr_1 , arr_2):
    # o(n) time
    intersection = []

    j = 0
    for i in range(len(arr_1)):
        ele = arr_1[i]
        while j < len(arr_2) and arr_2[j] <= ele :
            if ele == arr_2[j]:
                intersection.append(ele)
                break
            j += 1
    return intersection

def get_union_of_(arr_1 , arr_2):
    # o(n) time
    i = 0
    j = 0
    union = []

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            union.append(arr_1[i])
            i += 1
        elif arr_2[j] < arr_1[i]:
            union.append(arr_2[j])
            j += 1
        elif arr_1[i] == arr_2[j]:
            union.append(arr_1[i])
            i += 1
            j += 1

    if i == len(arr_1) and j < len(arr_2):
        union = union + arr_2[j ::]
    elif j == len(arr_2) and i < len(arr_1):
        union = union + arr_1[i ::]

    return union


print("union" , get_union_of_(arr_1 , arr_2))
print("intersection" , get_intersection_of(arr_1 , arr_2))

