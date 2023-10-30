def max_number(list_number):
    sorted_strings = sorted(list_number, reverse=True)

    return int(''.join(sorted_strings))


list_number = []

for number in range(4):
    number = str(input())
    list_number.append(number)

print(max_number(list_number))
