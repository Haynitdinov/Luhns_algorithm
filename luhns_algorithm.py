input_num = str(input("Enter number of your card: "))
rev_input = input_num[::-1]


def multiply_digit(rev_input):
    # Multiply every other digit by 2,
    # starting with the number’s second-to-last digit,
    # and then add those products’ digits together.

    sum_result = 0
    i = 1
    k = 0
    result = 0

    for i in rev_input[1::2]:
        k = int(i) * 2
        if k > 9:
            h = str(k)
            g = int(h[0]) + int(h[1])
            result += g
        else:
            result += k

    return result


def add_not_multiplied(rev_input):
    # Add the sum to the sum of the digits
    # that weren’t multiplied by 2.

    sum_result = 0

    for i in rev_input[0::2]:
        sum_result += int(i)

    return sum_result + multiply_digit(rev_input)


def is_valid(input_num):
    # If the total’s last digit is 0 the number is valid!
    # Also check wich card it is

    test_num = add_not_multiplied(rev_input)

    if test_num % 10 == 0:
        if (int(input_num[0:2]) == 34 and len(input_num) == 15) or \
           (int(input_num[0:2]) == 37 and len(input_num) == 15):

            print("American Express")

        elif (int(input_num[0:2]) == 51 and len(input_num) == 16) or \
             (int(input_num[0:2]) == 52 and len(input_num) == 16) or \
             (int(input_num[0:2]) == 53 and len(input_num) == 16) or \
             (int(input_num[0:2]) == 54 and len(input_num) == 16) or \
             (int(input_num[0:2]) == 55 and len(input_num) == 16) or \
             (int(input_num[0:2]) == 22 and len(input_num) == 16):

            print("MasterCard")

        elif int(input_num[0:1]) == 4 and \
             (len(input_num) == 13 or len(input_num) == 16):

            print("Visa")

        else:
            print("Other card")

    else:
        print("IS NOT VALID!")



is_valid(input_num)
