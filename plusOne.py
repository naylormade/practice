def plusOne(digits):
    return list(str(int(''.join([str(x) for x in digits])) + 1))
plusOne([1,2,3])

def plusOneAlternateMethod(digits):
    nums = ""
    for dig in digits:
            nums += str(dig)
    ans = int(nums) + 1
    #print(list(str(ans)))
    return list(str(ans))