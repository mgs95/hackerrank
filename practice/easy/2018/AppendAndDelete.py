"""
https://www.hackerrank.com/challenges/append-and-delete/problem

Score: 10/10
Submitted: 2018
"""


def append_and_delete(s, t, k):
    # If is possible to remove all t and build s
    if k > (len(s) + len(t)):
        return 'Yes'

    while k:
        # If same strings, return 'Yes' if is possible to finish the
        # remain operations by adding and removing the same character
        if t == s:
            if not k % 2:
                return 'Yes'
            return 'No'

        if t.find(s) == 0:  # starts with s: add next char of t
            s = s + t[len(s)]
        else:  # else remove last character
            s = s[:-1]

        k -= 1

    return 'Yes' if s == t else 'No'


if __name__ == "__main__":
    s = input()
    t = input()
    k = int(input())
    result = append_and_delete(s, t, k)
    print(result)
