def isValid(s: str) -> bool:
    if s == "": return "true"

    if len(s) % 2 != 0:
        print("False")
        return False
    aslist = list(s)
    print(f'{aslist}')

    for ch in aslist:
        print(f'{ch}')
    return False

if __name__ == "__main__":
    isValid("()[]{}")