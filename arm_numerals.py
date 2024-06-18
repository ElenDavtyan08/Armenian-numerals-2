import json


def json_reader(file):  
    with open(file, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    return data

def arm_letter_to_num(letters):
    letter_to_num = json_reader('arm_nums_letters.json')["letter_to_int"]
    total = 0
    prev_value = 0
    for letter in letters:
        value = letter_to_num[letter]

        if prev_value < value:
            total += value - 2* prev_value
        else:
            total += value
        prev_value = value

    return total
    

def num_to_arm_letters(number):
    if number > 9999:
        print('Cannot convert that number')
        return False
    else:
        num_to_letter = json_reader("arm_nums_letters.json")["number_to_letter"]
        sorted_mapping = sorted(
            {int(num): letter for num, letter in num_to_letter.items()}.items(),
            key=lambda x: x[0], reverse=True
        )
        result = ""
        for num, letter in sorted_mapping:
            while number >= num:
                result += letter
                number -= num
        return result

