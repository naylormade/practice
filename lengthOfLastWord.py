def lengthOfLastWord(s: str) -> int:
    if not s or s.strip() == 0: return 0
    splitz = s.split(" ")
    if len(''.join(splitz).strip()) == 1:
        #print("1")
        return 1
    print(splitz)
    while len(splitz[-1]) == 0 and len(splitz) > 1:
        #print(f'ans: {len(splitz[-2])}')
        print(f'splitz[-1]:{splitz[-1]}')
        splitz.pop()

    print(f'ans: {splitz[-1]}')
    if splitz:
        return len(splitz[-1])
    else:
        return 0

lengthOfLastWord("  ")