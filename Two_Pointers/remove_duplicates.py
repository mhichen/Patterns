#!/usr/bin/python3

# Given array of sorted numbers, remove all duplicates
# Should not use any extra space
# After removing duplicates in-place, return length of
# subarray that has no udplicate in it
# Time complexity: O(N)
# Space complexity: O(1)
def remove_duplicates(arr):

    i = 0
    j = 1
    curr_len = len(arr)

    while j < curr_len:

        if arr[i] == arr[j]:
            arr.pop(j)
            curr_len = len(arr)

        else:
            i += 1
            j += 1
            
    return curr_len

# Use 1 pointer to iterate and
# another to place the next non-duplicate
# number
def remove_duplicates_2(arr):

    # pointer to iterate
    i = 1

    # pointer to indicate where to place next
    # non-duplicate entry found by i
    j = 1

    while i < len(arr):

        # Place element at pointer i in spot
        # held by pointer j
        if arr[i] != arr[j - 1]:
            arr[j] = arr[i]
            j += 1

        i += 1

    return j
    

if __name__ == "__main__":

    A = [2, 3, 3, 3, 6, 9, 9]

    # Expected output: 4
    print(remove_duplicates(A))
    print(remove_duplicates_2(A))


    A = [2, 2, 2, 11]

    # Expected output: 2
    print(remove_duplicates(A))
    print(remove_duplicates_2(A))
