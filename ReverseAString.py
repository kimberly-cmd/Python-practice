def reverse_string(s):
    reversed_word = "" #Initializing an empty string that will hold the results
    for char in s:
        reversed_word = char + reversed_word
    return reversed_word #loops through each character in the string

word = "hello"
reversed_string = reverse_string(word)
print(reversed_string)