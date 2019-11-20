def lengthOfLastWord(s: str) -> int:
    if not s or s.strip() == 0: return 0
    splitz = s.split(" ")

    if len(''.join(splitz).strip()) == 1:
        return 1

    while len(splitz[-1]) == 0 and len(splitz) > 1:
        splitz.pop()

    if splitz:
        return len(splitz[-1])
    else:
        return 0

lengthOfLastWord("  ")