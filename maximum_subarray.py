def maxSubArray(nums) -> int:
    maxy = 0
    sub_total = 0
    for i in range(len(nums)):
        sub_total += nums[i]

        if maxy < sub_total:
            maxy = sub_total
        if sub_total < 0:
            sub_total = 0
    print(f'maxy:{maxy}')
    return maxy

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])