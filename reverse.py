def reverse( x: int) -> int:
    joined_list = ''.join(list(reversed(str(x)[:-1])))
    print(joined_list)
    if str(x)[0] == "-":
        print("-" + ''.join(list(reversed(str(x)[1:]))))
        return "-" + ''.join(list(reversed(str(x)[1:])))
    else:
        if joined_list[0] != 0:
            return ''.join(list(reversed(str(x))))
        else: 
            return ''.join(list(reversed(str(x)[:-1])))