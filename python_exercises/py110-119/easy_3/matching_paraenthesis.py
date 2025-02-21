'''
Write a function that takes a string as an argument and returns True if all
parentheses in the string are properly balanced, False otherwise. To be
properly balanced, parentheses must occur in matching '(' and ')' pairs.
'''

'''
input: string
output: boolean

rules:
return true if all paraentheses are balanced - balanced means parentheses must
occur in matching '(' and ')' pairs

if there are odd number of () seems like that wouldnt be balanced

data structure:
potentially a dict
list

'''
'''
Further Exploration There are a few other characters that should be matching as
well. Square brackets and curly brackets normally come in pairs. Quotation
marks(single and double) also typically come in pairs and should be balanced.
Can you expand this function to take into account those characters?
'''

def is_balanced(string):

    stack = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for c in string:
        if pairs.get(c) is not None:
            stack.append(pairs[c])

        if c in [')', ']', '}']:
            if len(stack) == 0 or c != stack[-1]:
                return False
            stack.remove(c)

    return len(stack) == 0


print(is_balanced('[{()}]') == True)
print(is_balanced('[()()]{}') == True)
print(is_balanced('([]') == False)
print(is_balanced('([{]})') == False)
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

'''
Further Exploration There are a few other characters that should be matching as
well. Square brackets and curly brackets normally come in pairs. Quotation
marks(single and double) also typically come in pairs and should be balanced.
Can you expand this function to take into account those characters?
'''
