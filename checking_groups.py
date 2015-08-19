"""
In English and programming, groups can be made using symbols such as "()" and "{}" that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]
The next are done incorrectly

{(})
([]
[])
A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols "()" "{}" or "[]" to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.
"""


# this is not my solution
# but very simple and clever
def group_check(s):
  l = 9223372036854775807
  while(l > len(s)):
    l = len(s)
    s = s.replace('()', '')
    s = s.replace('{}', '')
    s = s.replace('[]', '')
  return len(s) == 0


if __name__ == '__main__':
    print(group_check("({"))
    print(group_check("[[]()]"))
    #print(group_check("()"))
    #print(group_check(""))
