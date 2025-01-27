def select_fruit(obj):
    fruits = {}
    for key, value in obj.items():
        if value == 'Fruit':
            fruits[key] = value
    return fruits


produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

# print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }


def double_numbers(numbers):
    for i in range(len(numbers)):
        print(numbers[i])
        numbers[i] *= 2
    return numbers


my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
# print(my_numbers)                 # [1, 4, 3, 7, 2, 6]

def double_odd_indexes(numbers):
    doubled = []
    for idx in range(len(numbers)):
        if idx % 2 != 0:
            doubled.append(numbers[idx] * 2)
        else:
            doubled.append(numbers[idx])

    return doubled

# print(double_odd_indexes(my_numbers)) # expect [1, 8, 3, 14, 2, 12]

def multiply(numbers, multiplier):
    product_list = []
    for num in numbers:
        product_list.append(num * multiplier)

    return product_list

print(multiply(my_numbers, 5)) # [5, 20, 15, 35, 10, 30]


def frequency_count(string):
    frequency = {}
    for c in string.replace(" ", ""):
       frequency[c] = 1 if c not in frequency else frequency[c] + 1

    return frequency

statement = "The Flintstones Rock"

print(frequency_count(statement))
