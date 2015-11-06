"""
Here you will create the classic pascal's triangle. Your function will be passed the depth of the triangle and you code has to return the corresponding pascal triangle upto that depth

The triangle should be returned as a nested array.

for example:

pascal(5) # should return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together (except for the edges, which are all "1"). eg

          [1]
        [1   1]
       [1  2  1]
      [1  3  3  1]
here you get the 3 by adding the 2 and 1 above it.
"""

def pascal(p):
    if p == 1:
        return [[1]]
    else:
        _list = [[1], [1, 1]]
        tmp_list = None
        for i in range(2, p):
            new_list = []
            if i == 2:
                new_list = [1, 2, 1]
                tmp_list = new_list
            else:
                for i in range(len(tmp_list)):
                    if i == len(tmp_list)-1:
                        break
                    new_list.append(tmp_list[i] + tmp_list[i+1])
                tmp_list = [1] + new_list + [1]
            _list.append(tmp_list)
        return _list


if __name__ == '__main__':
    print(pascal(5))
