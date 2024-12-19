car = {
    'type':    'sedan',
    'color':   'blue',
    'year':    2003,
  }
print([[key, car[key]] for key in car])

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

# print([numbers[number] / 2 for number in numbers])
# print([numbers[number] // 2 for number in numbers])

# print([num // 2 for num in dict.values(numbers)])

for key, value in numbers.items():
  print(f'A {key} number is {value}')

for key in numbers:
  print(f'A {key} number is {numbers[key]}')