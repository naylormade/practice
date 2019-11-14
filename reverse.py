def reverse( x: int) -> int:
    joined_list = ''.join(list(reversed(str(x)[:-1])))
    #print(joined_list)
    if str(x)[0] == "-":
        print("-" + ''.join(list(reversed(str(x)[1:]))))
        return "-" + ''.join(list(reversed(str(x)[1:])))
    else:
        if joined_list[0] != str(0):
            print(''.join(list(reversed(str(x)))))
            return ''.join(list(reversed(str(x))))
        else: 
            print(''.join(list(reversed(str(x)[1:]))))
            return ''.join(list(reversed(str(x)[1:])))
        
reverse(120)
#reverse(-123)


def reverse2( x: int) -> int:
    ans = ""
    if len(str(x)) == 1: return x
    testt = list(reversed(str(x)))
    #print(f'testt[0]:{testt[0]}')
    if testt[0] == str(0):
        #print(f'first: {"".join(testt[1:])}')
        ans = ''.join(testt[1:])
    if testt[-1] == "-":
        print("2nd")
        #print("-" + ''.join(testt))
        #print("-" + ans)
        ans = "-" + ans[:-1]
    #print(f'3rd: {"".join(testt)}')
    return ans
reverse2(-10)