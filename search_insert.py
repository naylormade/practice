def searchInsert(nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            count = 0
            try:
                while target > nums[count]:
                    count += 1
            except IndexError:
                return len(nums)
            print(count)
            return count

searchInsert([1,3,5,6], 7)