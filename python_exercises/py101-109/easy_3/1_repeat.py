# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.
 
def repeat(string_to_repeat, times):
    for _ in range(times):
        print(string_to_repeat)

repeat('Hello', 3)