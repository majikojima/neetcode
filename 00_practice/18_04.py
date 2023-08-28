def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res += bit << (31 - i)
    print(bin(res))
    return res

n = 0b00000010100101000001111010011100
print(reverseBits(n))