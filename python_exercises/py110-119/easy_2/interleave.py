'''
Write a function that combines two lists passed as arguments and returns a new
list that contains all elements from both list arguments, with each element
taken in alternation.

You may assume that both input lists are non-empty, and that they have the same
number of elements.
'''
'''
input: two lists with the same length
output: one list with elements from both lists interweaved

they will be non empty lists
both lists contain the same amount of elements
store all elements into one list with each element taken in alternation
lists can contain any kind of elements, numbers, strings etc.

Data structure:
list

Algo:
declare an empty list
iterate through the length of one list
if list 1 at the current index is inbounds
    append current element to the empty list

if list 2 at the current index is inbounds
    append current element to the empty list

return empty list



'''
def interleave(list1 , list2):

    combined = []
    for item in zip(list1, list2):
        combined.extend([*item])

    return combined

    # joined_list = []
    # larger_list = len(list1) if len(list1) >= len(list2) else len(list2)
    #
    # for i in range(larger_list):
    #     if i < len(list1):
    #         joined_list.append(list1[i])
    #
    #     if i < len(list2):
    #         joined_list.append(list2[i])
    #
    # print(joined_list)
    # return joined_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected) 
