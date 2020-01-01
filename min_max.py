# min max 方法求最大值
nums = []
out = None
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
while True:
    cur = min(nums)
    print(cur)
    nums.remove(cur)
    if len(nums) == 1:
        print(nums[0])
        break