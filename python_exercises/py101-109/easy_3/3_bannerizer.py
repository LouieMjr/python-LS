# Write a function that takes a short line of text and prints it within a box.

def print_in_box(string):
    dashes = '+'.rjust(len(string) + 3, '-')
    print('+' + dashes)
    print('|' + '|'.rjust(len(string) + 3))
    print(f'| {string} |')
    print('|' + '|'.rjust(len(string) + 3))
    print('+' + dashes)

print_in_box('To boldly go where no one has gone before.')
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

print_in_box('')
# +--+
# |  |
# |  |
# |  |
# +--+
