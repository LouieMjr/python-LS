'''
Write a function that counts the number of occurrences of each element in a
given list. Once counted, print each element alongside the number of
occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
'''
'''
Algo:
declare a set
iterate through list
    check if ele not in set, if true
        print ele, and current count of ele in the list

    add element to the set

'''

def count_occurrences(lst):
    seen = set()
    # uncomment below to make function case insensitive
    # lst = [string.lower() for string in lst]
    for ele in lst:
        if ele not in seen:
            count = lst.count(ele)
            print(ele, count, sep=' => ')

        seen.add(ele)



vehicles = ['car', 'car', 'suv', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']


count_occurrences(vehicles)
