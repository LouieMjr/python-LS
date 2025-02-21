'''
Write a function that takes a string argument consisting of a first name, a
space, and a last name. The function should return a new string consisting of
the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes
("Jr.", "Sr.").
'''

def swap_name(name):
    name_lst = name.split()
    last_name = name_lst.pop(-1)

    name_lst.insert(0, last_name + ',')

    return ' '.join(name_lst)


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

'''
Suppose the named person has one or more middle names? Refactor the current
solution so it can accommodate this. The middle names should be listed after
the first name:
'''

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
