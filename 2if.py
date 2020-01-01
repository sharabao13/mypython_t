#列表的方法求最大值
nums = []
out = None
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        if nums[1] > nums[2]:
            out = [2,1,0]
        else:
            out = [1,2,0]
    else:
        out = [1,0,2]
else:
    if nums[0] > nums[2]:
        out = [2,0,1]
    else:
        if nums[1] < nums[2]:
            out = [0,1,2]
        else:
            out = [0,2,1]
out.reverse()
for i in out:
    print(nums[i],end=', ')
