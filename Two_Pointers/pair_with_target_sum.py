#!/usr/bin/python3


# Given an array of sorted numbers and a target sum
# find a pair in the array whose sum is equal to the
# given target.  The indices of the two numbers are returned

# Time complexity: O(N)
# Space complexity: O(1)
def pair_with_target_sum(arr, target):

    p1 = 0
    p2 = len(arr) - 1

    # idea is if p1 + p2 > target, decrement p2
    # if p1 + p2 < target, increment p1
    while p1 < p2:

        if arr[p1] + arr[p2] > target:
            p2 -= 1
            
        elif arr[p1] + arr[p2] < target:
            p1 += 1

        else:
            return p1, p2

    return [-1, -1]

# Use a hash table

# Time complexity: O(N)
# Space complexity: O(N)
def pair_with_target_sum_hash(arr, target):

    # Use hash table to store indices of
    # the elements in the array
    mdict = {}

    for ind, val in enumerate(arr):

        if target - val in mdict:
            return mdict[target - val], ind
        else:
            mdict[val] = ind
    
    return [-1, -1]

if __name__ == "__main__":

    A = [1, 2, 3, 4, 6]
    target = 6

    # Expected output: [1, 3]
    print(pair_with_target_sum(A, target))
    print(pair_with_target_sum_hash(A, target))

    A = [2, 5, 9, 11]
    target = 11

    # Expected output: [0, 2]
    print(pair_with_target_sum(A, target))
    print(pair_with_target_sum_hash(A, target))
    
    
