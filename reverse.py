def reverse( x: int) -> int:

    if len(str(x)) == 1: return x

    ans = ''.join(list(reversed(str(x))))
    while ans[0] == str(0):
        ans = ''.join(ans[1:])
    if ans[-1] == "-":
        ans = "-" + ans[:-1]
    print(f'ans:{ans}')
    if abs(int(ans)) > (2 ** 31 - 1):
        return 0
    return ans

# reverse(100)
# reverse(-10)
# reverse(123)