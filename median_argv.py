from sys import argv

nums = argv[1:]

for index, value in enumerate(nums):
    nums[index] = float(value)

if len(nums) % 2 == 0:
    print (nums[(len(nums)/2)-1] + nums[len(nums)/2])/2.0
else:
    print nums[len(nums)/2]
