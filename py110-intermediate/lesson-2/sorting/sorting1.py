from pprint import pprint
'''
Sort the following list of numbers first in ascending numeric order, then in
descending numeric order. Do not mutate the list.

[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
'''
lst = [10, 9, -6, 11, 7, -16, 50, 8]

descending = sorted(lst, reverse=True)
ascending = sorted(lst)
# print(descending, ascending, lst)

'''
Repeat the previous exercise but, this time, perform the sort by mutating the
original list.

'''

# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)

'''
passed to the sorting function and the returned list should contain numbers,
not strings.

'''

lst.sort(key=str)
# print(lst)
lst.sort(key=str, reverse=True)
# print(lst)

'''
How would you sort the following list of dictionaries based on the year of
publication of each book, from the earliest to the most recent?
'''
books = [ 
    { 
        'title': 'One Hundred Years of Solitude', 
        'author': 'Gabriel Garcia Marquez', 
        'published': '1967', 
    }, 
    { 
        'title': 'The Book of Kells',
        'author': 'Multiple Authors', 
        'published': '800', 
    }, 
    { 
        'title': 'War and Peace', 
        'author': 'Leo Tolstoy',
        'published': '1869', 
    }, 
]

def published_key(book):
    return int(book['published'])


pprint(books)
pprint(sorted(books, key=published_key))
