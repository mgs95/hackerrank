"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem

Score: 35/35
Submitted: 2018
"""

"""
Steps:
  1. Finds the first unsorted element traversing the word backwards.
  2. Replace with the next higher letter in the actual traversed
     section of the word.
  3. Sort the remain elements of the traversed section.
"""


def bigger_is_greater(w):
    w = list(w)
    last = w[-1]
    result = ''
    for i in range(len(w) - 2, -1, -1):
        act = w[i]
        # 1. Is element sorted compared with last element?
        if act >= last:
            last = act
            continue

        # 2. Finds next higher letter
        to_replace_list = sorted(list(set(w[i:])))
        try:
            to_replace = to_replace_list[to_replace_list.index(act) + 1]
        except IndexError:
            # Element to replace does not exist
            return 'no answer'

        replaced = w[i:].index(to_replace)

        # 3. Sort the remain elements and join all sections
        w[replaced + i] = act
        following = sorted(w[i + 1:])
        result = w[:i] + [to_replace] + following

        return ''.join(result)

    return 'no answer'


if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = bigger_is_greater(w)
        print(result)
