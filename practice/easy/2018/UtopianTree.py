"""
https://www.hackerrank.com/challenges/utopian-tree/problem

Score: 20/20
Submitted: 2018
"""

if __name__ == "__main__":
    stage_storage = {0: 1}
    t = int(input())

    for __ in range(t):
        stage = int(input())

        # If stage state has previously saved
        if stage in stage_storage:
            print(stage_storage[stage])
        else:
            # get maximum saved stated and compute and save next stages until target stage
            act_n, height = max(stage_storage.items(), key=lambda x: x[0])
            while act_n < stage:
                act_n += 1
                height = height * 2 if act_n % 2 else height + 1
                stage_storage[act_n] = height

            print(height)
