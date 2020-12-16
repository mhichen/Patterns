#!/usr/bin/python3

# Given a sorted array, create a new array
# containing square of all the numbers of
# the input array in the sorted order
def square_array(arr):

    res = [0] * len(arr)

    # i to iterate over arr
    # j to iterate over res to find where
    # to place new element
    # k to keep place of next empty spot
    j = 0
    k = 1

    res[0] = arr[0] * arr[0]
    
    for i in range(1, len(arr)):
        s = arr[i] * arr[i]

        if s < res[j]:
            res[k], res[j] = res[j], res[k]
        
            while s < res[j - 1]: 
                res[j - 1], res[j] = res[j], res[j - 1]
                j -= 1

            res[j] = s
            k += 1
            j = k - 1

        else:
            res[k] = s
            k += 1


    return res
    

if __name__ == "__main__":

    input_arr = [-2, -1, 0, 2, 3]
    
    # Expected output = [0, 1, 4, 4, 9]
    print(square_array(input_arr))


    input_arr = [-3, -1, 0, 1, 2]

    # Expected output = [0, 1, 1, 4, 9]
    print(square_array(input_arr))
