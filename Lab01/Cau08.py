def divisible_by_5(binary_number):
    decimal_number = int(binary_number, 2)
    if decimal_number%5 == 0:
        return True;
    else:
        return False;
binary_number = input("Input string of binary number (seperate by comma): ")
binary_number_list = binary_number.split(',')
number_divisible_by_5 = [number for number in binary_number_list if divisible_by_5(number)]
if len(number_divisible_by_5) > 0:
    answer = ','.join(number_divisible_by_5)
    print("The binary numbers divisible by 5 are: ",answer)
else:
    print("There is no binary numbers divisible by 5 in input string")