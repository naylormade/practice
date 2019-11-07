def isValid(s: str) -> bool:
    if s == "": return "true"

    if len(s) % 2 != 0:
        return "False"
    aslist = list(s)
    print(f'{aslist}')
    return False