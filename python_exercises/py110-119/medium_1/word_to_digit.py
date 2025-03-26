# Write a function that takes a string as an argument and returns that string
# with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three',
# 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its
# corresponding digit character.

# You may assume that the string does not contain any punctuation.

def word_to_digit(message):

    num_strings = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    message_list = message.split()

    processed_words = [num_strings.get(word, word) for word in message_list]
    return ' '.join(processed_words)

    # for i, word in enumerate(message_list):
    #     if num_strings.get(word) != None:
    #         message_list[i] = num_strings[word]
    #
    # return ' '.join(message_list)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
