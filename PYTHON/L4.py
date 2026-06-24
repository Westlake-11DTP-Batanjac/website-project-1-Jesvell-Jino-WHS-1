
nums = map(int, input().split())

cons = []
cuts = []

def consecutive(cons, index):
    if nums[index] == (cons[-1] + 1):
        cons.append(nums)
for i in range(len(nums) - 1):
    nums[i]