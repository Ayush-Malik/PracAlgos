# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/
arr = list(map(eval , input().split(', ')))

pos_ptr = -1
neg_ptr = -1

def find_next_negative_number(start_index , arr):
    for i in range(start_index , len(arr)):
        if arr[i] < 0: # if current element is negative
            return i
    return None

for i in range(len(arr)):
    if arr[i] > 0: # if currrent element is positive
        pos_ptr = i
        neg_ptr = find_next_negative_number(pos_ptr + 1 , arr)

        if neg_ptr is None: # No negative exist now , all negatives are already placed at front
            break

        # Swapping the positive_num with negative_num
        arr[pos_ptr] , arr[neg_ptr] = arr[neg_ptr] , arr[pos_ptr]

    print(arr)

