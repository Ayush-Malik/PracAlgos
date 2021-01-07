# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

# [1]
# 1   2   3   4  5   6
# 7   8   9  10  11  12
# 13  14  15 16  17  18
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11


rows = int(input("Enter the number of rows for the matrix : "))

lis = []
for i in range(rows):
    lis.append(list(map(eval , input().split())))

for val in lis:
    print(val)

cols = len(lis[0]) - 1
rows -= 1

print(rows , cols)

pattern =[ (0 , 1) , (1 , 0) , (0 , -1) , (-1 , 0) ]
x , y = 0 , -1
pattern_index = 0
val = 0

counter = 0
while counter < (rows + 1) * (cols + 1):
    if pattern_index % 2 == 0: #Even means change is in y[column wise]
        if pattern[pattern_index][1] > 0 and y == cols - val:
            pattern_index += 1
        elif pattern[pattern_index][1] < 0 and y == val:
            pattern_index += 1
    else: # Odd means change is in x[rows wise]
        if pattern[pattern_index][0] > 0 and x == rows - val:
            pattern_index += 1
        elif pattern[pattern_index][0] < 0 and x == val + 1:
            pattern_index = 0
            val += 1

    x += pattern[pattern_index][0]
    y += pattern[pattern_index][1]
    print(lis[x][y] , end = " ")
    counter += 1

