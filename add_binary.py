def addBinary(a: str, b: str) -> str:
    print(bin(int(a, 2) + int(b, 2))[2:])
    return bin(int(a, 2) + int(b, 2))[2:]
addBinary("11","1")