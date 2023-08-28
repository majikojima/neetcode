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
    res = 0
    while n:
        res += (n % 10) ** 2
        n //= 10
    return res


n = 19
print(isHappy(n))