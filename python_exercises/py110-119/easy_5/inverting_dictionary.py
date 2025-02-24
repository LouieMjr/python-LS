'''
Given a dictionary where both keys and values are unique, invert this
dictionary so that its keys become values and its values become keys.
'''

def invert_dict(groceries):
    return {value: key for key, value in groceries.items()}

    # for key, value in groceries.items():
    #     tmp_key = key
    #     tmp_value = value
    #
    #     del groceries[key]
    #     groceries[tmp_value] = tmp_key
    #
    # return groceries


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

