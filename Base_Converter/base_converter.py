LETTER_TABLE = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35
}

def to_base_10(start_num: list, start_base: int):
    end_num = 0
    for i in range(len(start_num)):
        # (len(start_num) - i - 1) = count down from len() - 1 up to 0
        end_num += int(start_num[i]) * start_base ** (len(start_num) - i - 1)

    return end_num

def change_base(start_num: list, start_base: int, end_base: int):
    end_num = ""
    
    # turn all into base 10
    start_num = to_base_10(start_num, start_base)

    base_num = start_num

    if end_base == 10:
        return start_num
    elif 10 < end_base < 37:
        OPPO_TABLE = {value:key for (key, value) in LETTER_TABLE.items()}
        while base_num:
            remainder = base_num % end_base
            if remainder in OPPO_TABLE:
                end_num = str(OPPO_TABLE[remainder]) + end_num
            else:
                end_num = str(remainder) + end_num
            base_num = base_num // end_base
        return end_num
    else:
        first = True
        while base_num:
            if first:
                end_num = str(base_num % end_base) + end_num
                first = False
            else:
                end_num = str(base_num % end_base) + ";" + end_num
            base_num = base_num // end_base
        return end_num

def proper_base(number: list, base: int):
    for digit in number:
        if int(digit) >= base:
            return False
    return True

def separate(input_answer):
    number_list = []
    last_place = 0
    # get everything between ;
    for letter_place in range(len(input_answer)):
        if input_answer[letter_place] == ";":
            if len(input_answer[last_place:letter_place]):
                number_list.append(input_answer[last_place:letter_place])
            last_place = letter_place + 1
        else:
            try:
                int(input_answer[letter_place])
            except ValueError:
                raise Exception("I will not bother to check, so... Invalid Input!")
    if len(input_answer[last_place:len(input_answer)]):
        number_list.append(input_answer[last_place:len(input_answer)])

    return number_list

# ---- customizable
def check_viable(input_answer, question_num):
    error = Exception("Invalid Input!")
    imp_error = Exception("The number given above and its base do not match!")
    
    if question_num == 0:
        if ";" in input_answer:
            return separate(input_answer)
        else:
            input_answer = input_answer.upper()
            new_input = ""
            for integer in input_answer:
                try:
                    new_input += str(int(integer)) + ";"
                except ValueError:
                    new_input += str(LETTER_TABLE[integer]) + ";"
            return separate(new_input)
    else:
        input_answer = int(input_answer)
        if question_num == 1:
            if input_answer < 2 and input_answer.is_integer():
                raise error
            elif not proper_base(prev_answer, input_answer):
                raise imp_error
        return input_answer

def ask_info(questions):
    output = []
    num_input = 0
    while num_input < 3:
        try:
            # ask each question on the questions and ask for input, while checking if it is viable
            for question_num in range(len(questions)):
                if num_input <= question_num:
                    if question_num == 0:
                        print (PROMPT)
                    output.append(check_viable(input(questions[question_num]), question_num))

                    # know prev_answer
                    global prev_answer
                    prev_answer = output[question_num - 1]

                    num_input += 1
        except Exception as e:
            print (str(e))
            print ()

    return output

# ---
print ("Welcome to the Base Converter")
PROMPT = '''
For number bases 11 - 36, you can use letters.
However, for bases 37 and above, you have to separate them on the number it is supposed to carry.
Example: A = 10, so A1 becomes 10;1
Reason is that, when the number is for example in base 37, how are you able to write number 36?
I didn't allow letters in ; form because the code will become longer
'''

using = True
action = True
while using:
    if action:
        start_num, start_base, end_base = tuple(
            ask_info([
                "Number: ",
                "From base: ", 
                "To base: "
            ]))

        # print (start_num, start_base, end_base)
        print (change_base(start_num, start_base, end_base))

    # try again?
    answer = input("\nWould you like to try another one (y/n)? ")
    if answer == "y":
        action = True
        continue
    elif answer == "n":
        using = False
    else:
        print ("Invalid Input!")
        action = False


