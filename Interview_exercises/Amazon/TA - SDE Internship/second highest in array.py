# Given an array of n numbers, return the second highest number.

#   ** Definitions/Requirements: **

# n = int()
# escalability n>>0
# unsorted
# O(n) --> Linear Time Complexity
# Has Duplicates
# O(C) --> Constant Space Complexity

# Array example:
#   arr1 = [2,11,34,21,22,2,5,64,29,1,-2,-111,101,-1302,100,3,44,0]

# Execution starts below
import math  # --> uses math.inf to use as a under infinite limit for possible lower negative values in the array


def highest_value(arr):
    maior = -math.inf
    for i in range(0, len(arr)):  # O(n)
        if arr[i] > maior:
            maior = arr[i]
        # print(maior)
    return (maior)
# could use a remove() to take the highest value out after knowing it. -->O(n)


def second_highest(arr):
    maior = (highest_value(arr))
    segun_maior = -math.inf
    for i in range(0, len(arr)):
        if arr[i] < maior and arr[i] > segun_maior:
            segun_maior = arr[i]
        # print(segun_maior)
    return (segun_maior)


# for testing possible cases:
# if use maior = 0 this use case leads the script to fail
arr2 = [-22, -1, -2, -4, -6, -22, -3, -5, -1]
arr1 = [2, 11, 34, 21, 22, 2, 5, 64, 29, 1, -2, -111, 101, -1302, 100, 3, 44, 0]

print(f"o maior número é: {highest_value(arr1)}")
print(f"o segundo maior número é: {second_highest(arr1)}")
