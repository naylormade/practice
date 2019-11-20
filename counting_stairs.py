def climbStairs(n: int) -> int:
    if n == 2: return 2
    if n == 3: return 3
    increment = 2
    total = 3
    while increment < n - 1:
        total += increment
        increment += 1
    return total
