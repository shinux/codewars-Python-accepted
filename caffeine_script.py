"""
Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".

If the integer is divisible by 3 and divisible by 4, return the string "Coffee"

If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"

caffeineBuzz(1)   => "mocha_missing!"
caffeineBuzz(3)   => "Java"
caffeineBuzz(6)   => "JavaScript"
caffeineBuzz(12)  => "CoffeeScript"
"""

def caffeineBuzz(n):
    current_string = ''
    if n % 3 == 0 and n % 4 == 0:
        current_string += 'Coffee'
    elif n % 3 == 0:
        current_string += 'Java'
    else:
        return "mocha_missing!"
    if n % 2 == 0:
        current_string += 'Script'

    return current_string


if __name__ == "__main__":
    print caffeineBuzz(1)
    print caffeineBuzz(3)
    print caffeineBuzz(6)
    print caffeineBuzz(12)

