def lengthOfLastWord(s: str) -> int:
    splitz = s.split(" ")
    if len(''.join(splitz).strip()) == 1:
        #print("1")
        return 1
    print(splitz)
    while(len(splitz[-1])) == 0:
        #print(f'ans: {len(splitz[-2])}')
        print(f'splitz:{splitz}')
        splitz.pop()
    print(f'ans: {len(splitz[-1])}')
    return len(splitz[-1])

lengthOfLastWord("b a ")