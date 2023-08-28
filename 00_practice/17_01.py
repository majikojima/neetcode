def isHappy(n: int) -> bool:
    slow = n
    fast = sumSquard(n)
    while slow != fast:
        slow = sumSquard(slow)
        fast = sumSquard(fast)
        fast = sumSquard(fast)
    if fast == 1:
        return True
    else:
        return False

def sumSquard(n):
    sumS = 0
    while n:
        sumS += (n % 10) ** 2
        n //= 10
    return sumS


n = 19
print(isHappy(n))