def hammingWhight(n: int) -> int:
    res = 0
    while n:
        if n & 1 == 1:
            res += 1
        n = n >> 1
    return res

n = 0b00000000000000000000000000001011
print(hammingWhight(n))