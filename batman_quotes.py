"""
Batman & Robin have gotten into quite a pickle this time. The Joker has mixed up their iconic quotes and also replaced one of the characters in their names, with a number. They need help getting things back in order.

Implement the getQuote method which takes in an array of quotes, and a string comprised of letters and a single number (e.g. "Rob1n") where the number corresponds to their quote indexed in the passed in array.

Return the quote along with the character who said it:

Hint: You are guaranteed that the number in the passed in string is placed somewhere after the first 3 characters of the string. The quotes either belong to Batman, Robin, or Joker.
"""


class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        hero_dict = {'JOK': 'Joker', 'BAT': 'Batman', 'ROB': 'Robin'}
        _name = hero_dict.get(hero[:3].upper())
        _index = int(filter(lambda x: x.isdigit(), hero))
        return _name + ": " + quotes[_index]


if __name__ == '__main__':
    quotes = ["WHERE IS SHE?!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"]
    print BatmanQuotes.get_quote(quotes, "Rob1n")
