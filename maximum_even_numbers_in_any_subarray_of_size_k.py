# https://www.geeksforgeeks.org/maximum-even-numbers-present-in-any-subarray-of-size-k/

arr = list(map(eval , input().split(', ')))
k   = int(input("Enter the value of k(size of subarray in which evens will be counted) : "))

# Counting initially how many evens are there in first window
evens_count = 0
for i in range(k):
    if arr[i] % 2 == 0 : # even number
        evens_count += 1

max_evens = evens_count


def check_even(num):
    if num % 2 == 0:
        return 1
    else:
        return 0


for i in range(1 , len(arr) - k + 1):
    evens_count += -check_even(arr[i - 1]) + check_even(arr[i + k - 1])
    if max_evens < evens_count:
        max_evens = evens_count

print(f"Max number of evens found in any subarray of length {k} is {max_evens}")