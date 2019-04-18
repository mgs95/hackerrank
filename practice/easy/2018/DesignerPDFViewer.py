"""
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

Score: 20/20
Submitted: 2018
"""

from string import ascii_lowercase


def designer_pdf_viewer(h, word):
    height_dict = dict(zip(ascii_lowercase, h))

    rect_w = len(word)
    rect_h = height_dict[max(word, key=lambda l: height_dict[l])]

    return rect_w * rect_h


if __name__ == "__main__":
    h = list(map(int, input().split()))
    word = input()
    result = designer_pdf_viewer(h, word)
    print(result)
