
def unique_sum(lst):
    total = 0
    seen = []

    for num in lst:

        if num in seen:
            index = seen.index(num)
            seen = seen[index+1:]

        seen.append(num)
        print(seen)
        total = max(total, sum(seen))

    return total


print(unique_sum([100, 200, 100, 300, 400]))
print(unique_sum([1, 2, 3, 1, 2]))
print(unique_sum([5, 1, 3, 5, 2, 3, 4, 1]))
print(unique_sum([5, 1, 3, 5, 2]))
