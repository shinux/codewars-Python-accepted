"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Courtesy of ProjectEuler.net
"""
def solution(number):
    result = 0
    for i in range(1, number):
        if i % 5 == 0 or i % 3 == 0:
            result += i
            print(i)
    return result


if __name__ == '__main__':
    solution(14)
