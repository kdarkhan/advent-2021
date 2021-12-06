input = 'day6.txt'


def do_stuff():

    with open(input) as f:
        s = [int(x) for x in f.readline().strip().split(',')]

        nums = [0] * 9

        for i in s:
            nums[i] += 1

        for _ in range(80):
            n = nums[1:] + [nums[0]]
            n[6] += nums[0]
            nums = n
        print(sum(nums))


do_stuff()
