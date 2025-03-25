# Write a function that implements a miniature stack-and-register-based programming language that has the following commands (also called operations or tokens):

# n: Place an integer value, n, in the register. Do not modify the stack.

# PUSH : Push the current register value onto the stack. Leave the value in the
# register.

# ADD : Pop a value from the stack and add it to the register value, storing the result in the register.

# SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.

# MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.

# DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.

# REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.

# POP : Remove the topmost item from the stack and place it in the register.

# PRINT : Print the register value.

# All operations are integer operations (which is only important with DIV and REMAINDER).

# Programs will be supplied to your language function via a string argument.
# Your function may assume that all arguments are valid programs -- i.e., they will not do anything like trying to pop a non-existent value from the stack, and they won't contain any unknown tokens.

# Initialize the stack and register to the values [] and 0, respectively.

def minilang(program):
    commands = program.split()
    register = 0
    stack = []

    for command in commands:
        match command:
            case 'PRINT':
                print(register)
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                add = stack.pop()
                register += add
            case 'SUB':
                subtract = stack.pop()
                register -= subtract
            case 'MULT':
                multiplier = stack.pop()
                register *= multiplier
            case 'DIV':
                divisor = stack.pop()
                register //= divisor
            case 'REMAINDER':
                popped = stack.pop()
                register = register % popped
            case 'POP':
                most_recent_item = stack.pop()
                register = most_recent_item
            case _:
                register = int(command)

    return register


minilang('PRINT')
# 0
print('----------')
minilang('5 PUSH 3 MULT PRINT')
# 15
#
print('----------')
minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8
#
print('----------')
minilang('5 PUSH POP PRINT')
# 5
#
print('----------')
minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7
#
print('----------')
minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6
#
print('----------')
minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12
#
print('----------')
minilang('-3 PUSH 5 SUB PRINT')
# 8
#
print('----------')
minilang('6 PUSH')
# (nothing is printed)
