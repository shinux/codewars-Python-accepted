"""
Feynman's squares

Richard Phillips Feynman was a well-known American physicist and a recipient of the Nobel Prize in Physics. He worked in theoretical physics and pioneered the field of quantum computing.

Recently, an old farmer found some papers and notes that are believed to have belonged to Feynman. Among notes about mesons and electromagnetism, there was a napkin where he wrote a simple puzzle: "how many different squares are there in a grid of NxN squares?".

For example, when N=2, the answer is 5: the 2x2 square itself, plus the four 1x1 squares in its corners:



Task

You have to write a function

def count_squares(n):
that solves Feynman's question in general. The input to your function will always be a positive integer.

Examples

count_squares(1) =  1
count_squares(2) =  5
count_squares(3) = 14
"""

def count_squares(n):
    return sum([pow(i, 2) for i in range(1, n+1)])


if __name__ == '__main__':
    print(count_squares(15))
