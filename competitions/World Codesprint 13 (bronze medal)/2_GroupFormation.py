"""
https://www.hackerrank.com/challenges/solve-me-first/problem

Score: 30/30
Submitted: 2018
Difficulty: Medium
"""

GRADE = 0
GROUP = 1


def members_in_the_largest_groups(n_students, n_requests, _min, _max, first, second, third):
    students = {}
    groups = {}
    group_n = 1

    for __ in range(n_students):
        name, grade = input().split()

        students[name] = [int(grade), group_n]
        groups[group_n] = [grade == 1, grade == 2, grade == 3, 1, [name]]

        group_n += 1

    for __ in range(n_requests):
        A, B = input().split()

        if students[A][GROUP] == students[B][GROUP]:
            continue

        group_c = [0, 0, 0, 0, []]

        members = groups[students[A][GROUP]][4] + groups[students[B][GROUP]][4]
        for s in members:
            if s in group_c[4]:
                continue
            group_c[students[s][GRADE] - 1] += 1
            group_c[3] += 1
            group_c[4].append(s)

        if group_c[3] > _max or group_c[0] > first or group_c[1] > second or group_c[2] > third:
            continue

        groups[students[A][GROUP]] = [0, 0, 0, 0, []]
        groups[students[B][GROUP]] = [0, 0, 0, 0, []]
        groups[group_n] = group_c

        for s in group_c[4]:
            students[s][GROUP] = group_n

        group_n += 1

    groups = list(filter(lambda x: x[3] >= _min and x[3] <= _max, groups.values()))

    if not groups:
        return ['no groups']

    result = sorted(groups, key=lambda x: x[3], reverse=True)
    groups = list(filter(lambda x: x[3] == result[0][3], groups))

    result = set()

    for g in groups:
        for s in g[4]:
            result.add(s)

    return sorted(list(result))


if __name__ == '__main__':
    n, m, a, b, f, s, t = list(map(int, input().split()))

    r = members_in_the_largest_groups(n, m, a, b, f, s, t)

    print('\n'.join(r))
