'''
input: list of numbers
output: number counting how many pairs exist in input

if a list is empty of contains 1 value return 0
if a certain number occurs more than once, count each complete pair once


check if list contains 1 or less elements, if true, return 0
declare a variable pairs set to 0
declare a variable seen, set to a set

iterate through the list
    check if element is not in the set
    if not, add element to the set
    store count of how many of the curr element exists in the list
    store whole number result of dividing count by 2
    add result to pairs variable


return pairs

'''

def pairs(numbers):
    if len(numbers) <= 1:
        return 0

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return sum(count // 2 for count in counts.values())

    # pair_count = 0
    # seen = set()
    #
    # for num in numbers:
    #     if num not in seen:
    #         seen.add(num)
    #         count = numbers.count(num)
    #         pair_count += count // 2
    #
    # return pair_count


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
