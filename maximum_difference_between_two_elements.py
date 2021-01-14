# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
# 7,6,4,3,1
# 0


arr = list(map(eval , input().split(',')))

max_ele = arr[-1]
max_diff = -1

for i in range(len(arr) - 2 , -1 , -1):
    max_ele = max(arr[i + 1] , max_ele)
    max_diff = max( max_diff ,  max_ele - arr[i])

if max_diff < 0:
    print(0)
else:
    print(max_diff)