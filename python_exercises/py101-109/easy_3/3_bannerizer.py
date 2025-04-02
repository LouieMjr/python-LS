# Write a function that takes a short line of text and prints it within a box.

def print_in_box(message, length = None):
    if length is None:
        length = len(message)

    message = message[:length]
    print(f'+-{'-' * len(message)}-+')
    print(f'| {' ' * len(message)} |')
    print(f'| {message} |')
    print(f'| {' ' * len(message)} |')
    print(f'+-{'-' * len(message)}-+')

print_in_box('To boldly go where no one has gone before.', 10)
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
