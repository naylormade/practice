def removeElement(nums, val: int) -> int:
    while val in nums:
        nums.remove(val)
    print(nums)
    return nums

removeElement([3,2,2,3], 3)