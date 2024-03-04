def no_duplicates(arr):
    return list(set(arr))

#example test_list
list1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 2, 2, 2, 3, 3, 3, 10]

print(no_duplicates(list1))
