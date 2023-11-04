def max_number(list_number):
    sorted_numbers = sorted(list_number, key=lambda x: (x[0], -int(x)), reverse=True)

    nasw = ""

    for number in sorted_numbers:
        nasw += number

    print(nasw)


list_number = []

for _ in range(4):
    number = input()
    list_number.append(number)

max_number(list_number)
