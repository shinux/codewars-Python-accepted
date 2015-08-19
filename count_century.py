"""
Return the inputted numerical year in century format. For example 2014, would return 21st.

The input will always be a 4 digit string. So there is no need for year string validation

Examples:
Input: 1999 Output: 20th
Input: 2011 Output: 21st
Input: 2154 Output: 22nd
Input: 2259 Output: 23rd
Input: 1124 Output: 12th
Input: 2000 Output: 20th
"""

def whatCentury(year):
    suffix_dict = {'1': 'st',
                '2': 'nd',
                '3': 'rd',
                }
    current_year = str(year)
    head = current_year[:2] + '00'
    if current_year == head:
        result = head[:2]
    else:
        result = str(int(head[:2]) + 1)
    return result + suffix_dict[result[1]] if result[1] in suffix_dict and result[0] != '1' else result + 'th'


if __name__ == '__main__':
    print(whatCentury(2013))
    print(whatCentury(2000))
    print(whatCentury(1234))
