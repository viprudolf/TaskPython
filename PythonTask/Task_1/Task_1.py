def good_number(input_number):
    char = '\\'
    index_symbol = input_number.index(char)

    new_txt_first = input_number[:index_symbol]

    distant_first = len(new_txt_first)

    if distant_first < 4:
        first_new_txt = str(new_txt_first).zfill(4)

        distant_last = input_number[index_symbol + 1:].zfill(6)

        new_char = f"{first_new_txt}\\{distant_last}"

    print(new_char)


input_number = str(input('Введите номер (пример - 000\\0000) :'))
good_number(input_number)
