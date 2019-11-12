def isValid(s: str) -> bool:
    if s == "": return "true"

    if len(s) % 2 != 0:
        print("False")
        return False
    #aslist = list(s)
    maps = {
        ")": "(", 
        "]": "[",
        "}": "{"
    }
    stackx = []
    for ch in list(s):
        #print(f'{ch}')
        if ch == "(" or ch == "[" or ch == "{":
            stackx.append(ch)
        else:  #if we encounter a closing bracket
            if (stackx[-1]) == maps[ch]:
                stackx.pop()
    return True

if __name__ == "__main__":
    isValid("()")