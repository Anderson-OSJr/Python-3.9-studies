list1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [2, 3, 4, 4, 5, 2, 6, 7, 9, 2],
    [3, 2, 1, 3, 4, 5, 6, 4, 10, 2],
    [5, 6, 2, 1, 2, 5, 4, 8, 10, 8]]

list2 = [[3, 4, 5, 1, 2, 3, 7, 7, 10, 7],
    [5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
    [12, 13, 14, 12, 12, 5, 6, 7, 8, 9],
    [1, 1, 1, 1, 2, 2, 3, 4, 5, 6],
    [1,2,3,4,5,6,8,12,15,56,78,90]]


"""
Given a set of lists composed by numbers, the function below returns the first repeated number in each list,
if exists at least one repeated number.
"""

def check_reapeted(listn):
    for index in listn:
        checked_numbers = set() # create a empty set to be filled with non-repeated numbers.
        check = True
        number = 0    # this variable is initialized here to be recognized outside the loop below.
        for number in index:
            if number not in checked_numbers:
                checked_numbers.add(number) # the ".add()"  is the way to add items in a set. Dealing with sets,
                                            # the ".append()" can not be used.
            else:
                check = False
                break
        if check:
            print('\n', index, '\n****The list above does not have repeated numbers.****')
        else:
            print('\n', index, f'\nThe first repeated number in the list above is {number}.')

                                                   ### END OF FUNCTION ###
print('\n\n')
check_reapeted(list1)
print('\n\n')
check_reapeted(list2)
print('\n\n\n\n')




