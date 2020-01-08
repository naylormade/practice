def merge(nums1, m: int, nums2, n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()
    print(nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)