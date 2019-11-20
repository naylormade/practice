def plusOne(digits):
    nums = ""
    for dig in digits:
            nums += str(dig)
    ans = int(nums) + 1
    print(list(str(ans)))
    return list(str(ans))
plusOne([1,2,3])