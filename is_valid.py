def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    maps = {
        ")": "(", 
        "]": "[",
        "}": "{"
    }
    stackx = []
    for ch in s:
        if ch in maps:
            last_element = stackx.pop() if stackx else ""
            
            if maps[ch] != last_element:
                return False
        else:  #if we encounter an opening bracket
            stackx.append(ch)
    return not stackx

if __name__ == "__main__":
    isValid("(((((((()")