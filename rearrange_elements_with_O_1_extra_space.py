# https://practice.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Amazon&problemType=functional&page=1&sortBy=submissions&query=category[]Arrayscompany[]AmazonproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncategory[]Arrays#

arr = list(map(eval , input().split(', ')))
# In this we will try to store 2 values in a single term becuase all numbers are less than n(size)
# convert a to (a + b * n)
# Now to a is old value and b is newer value
# To get new val a => (a + b * n) % n  = [ Here (b*n) % n = 0 ]
# To get old val b => (a + b * n) // n = [ Here a / n = 0 , because a < n]


n = len(arr)
for i in range(n):
    x = arr[i]
    y = arr[arr[i]] % n  # Getting previous value using (%n)
    arr[i] = x + (y * n)

for i in range(n):
    print(arr[i] // n)