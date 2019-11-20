def removeElement(nums, val: int) -> int:
    count = 0
    while val in nums:
        nums.remove(val)
    print(nums)
    return nums

removeElement([3,2,2,3], 3)