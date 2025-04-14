'''
input: string
output: string with every 2nd char in every 3rd word for input string uppercased

word has to have a length of at least 2 to convert char to uppercase


declare an empty string
declare a char count, set to 0
declare a multiple, set to 1
split word by spaces

iterate through lst of words skipping every 3 words

    check if lst of words has a length of 2 or more
    if true, access current elements char at index of 2 and replace with
    uppercase version


join back to a string
return string

'''

def to_weird_case(string):
    words = string.split()

    for i in range(2, len(words), 3):
            word = words[i]
            words[i] = ''.join(
                char.upper() if idx % 2 == 1 else char
                for idx, char in enumerate(word)
            )

    return ' '.join(words)


    #    if len(words[i]) >= 2:
    #         weird_str = ''
    #
    #         for j, char in enumerate(words[i]):
    #             if j % 2 == 1:
    #                 weird_str += char.upper()
    #             else:
    #                 weird_str += char
    #
    #         words[i] = weird_str
    #
    # return ' '.join(words)


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
