from arm_numerals import arm_letter_to_num, num_to_arm_letters

if __name__ == "__main__":

    choice = input('Enter 1: to convert letter to number and 2: to convert number to letter. ')
    if choice == "1": # letters to number
        letters = input('Enter ARMENIAN letters: ').upper()
        num = arm_letter_to_num(letters)
        print(f"{letters} --> {num}")
    elif choice == "2": # number to letters
        number = int(input('Enter number(1-9999): '))
        let = num_to_arm_letters(number)
        if let:
            print(f"{number} --> {let}")

# If you want to know about armnenian numerals --- https://en.wikipedia.org/wiki/Armenian_numerals ---
    
