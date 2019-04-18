"""
https://www.hackerrank.com/contests/w37/challenges/dynamic-line-intersection

Score: 7.69/50
Submitted: 2018
Difficulty: Hard
"""


def dynamic_line_intersection(n):
    lines = {}
    instructions = []
    mem = {}
    for __ in range(n):
        event, *data = input().split()
        instructions.append([event, list(map(int, data))])

        if event == '?':
            lines[int(data[0])] = 0

    for event, *data in instructions:
        if event == '?':
            print(lines[data[0][0]])
        else:
            a, b = data[0]
            if b >= a:
                b = b % a
            val = 1 if event == '+' else -1
            mem_val = (a, b)
            if mem_val in mem:
                for idx in mem[mem_val]:
                    lines[idx] += val
            else:
                res = []
                for nl in lines.keys():
                    if ((nl - b) / a).is_integer():
                        res.append(nl)
                        lines[nl] += val
                mem[mem_val] = res


if __name__ == '__main__':
    n = int(input())

    dynamic_line_intersection(n)
