"""
https://www.hackerrank.com/contests/w37/challenges/two-efficient-teams/problem

Score: 6.91/70
Submitted: 2018
Difficulty: Hard
"""


def maximum_efficiency(n, m):
    employees = {}
    total_efficiency = 0
    total_employees = {}

    for idx in range(m):
        n_members, efficiency = list(map(int, input().split()))
        members = list(map(int, input().split()))
        first_member = None
        for member in members:
            act_member = member - 1

            if first_member == None:
                first_member = act_member
                if first_member not in total_employees:
                    total_employees[first_member] = []
            else:
                total_employees[first_member].append(act_member)
            if act_member in employees:
                employees[member - 1] += efficiency
            else:
                employees[member - 1] = efficiency

        total_efficiency += efficiency

    to_study = [0]
    while to_study:
        act = to_study.pop()
        if act in total_employees:
            to_study.extend(total_employees[act])
            total_employees.pop(act)

    if total_employees:
        return total_efficiency

    vals = employees.items()
    min_eff = min(vals, key=lambda x: x[1])

    return total_efficiency - min_eff[1]


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    result = maximum_efficiency(n, m)
    print(result)
