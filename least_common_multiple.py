"""
Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer.
"""
def lcm(*args):
    if len(args) == 1:
        return args[0]
    elif 0 in args:
        return 0
    else:
        args = sorted(args)
        start = args[-1]
        flag = True
        while flag:
            for i in args:
                if start % i == 0:
                    flag = False
                else:
                    start += 1
                    flag = True
                    break
        return start





if __name__ == '__main__':
    print(lcm(2))
    print(lcm(2, 3, 4))
    print(lcm(2, 5))
