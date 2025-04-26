number = int(input("Enter a number: ")) #Set as int to avoid errors
def sum_of_digits(number):
    # Convert number into string to make it easier to add each digit
    digit_string = str(abs(number)) #To take care of negative numbers
    total = 0

    for digit in digit_string:
        total += int(digit)
    return total
print(sum_of_digits(number))
