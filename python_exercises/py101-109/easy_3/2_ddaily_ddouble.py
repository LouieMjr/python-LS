def crunch(string):
    if not len(string):
        return ''

    crunched = string[0]

    for i in range(1, len(string)):
        if crunched[-1] != string[i]:
            crunched += string[i]

    return crunched

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
