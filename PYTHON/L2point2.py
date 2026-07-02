a = int(input()) # lengths
nums = list(map(int, input().split())) #ribbons
cutnum = 0
cuts = []

for i in range(a):
    if i == 0:
        cuts.append([i])
    elif nums[i] == (nums[i - 1] + 1):
        cuts[cutnum].append(nums[i])
    else:
        cuts.append([i])
        cutnum += 1

print((len(cuts) - 1), len(max(cuts, key=len)))
