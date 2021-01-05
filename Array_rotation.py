# https://www.geeksforgeeks.org/array-rotation/
arr = list(map(eval , input().split()))
times = int(input("Enter the rotation value : "))
rotated_arr = []

for i in range(len(arr)):
    rotated_arr.append(0)
    rotated_arr[i] = arr[(i + times) % len(arr)]

print(rotated_arr)
