# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

str = 'Captain Ruby'

first_word = str[:8]
print(first_word + 'Python')

str = str.replace('Ruby', 'Python')
print(str)