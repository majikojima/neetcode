def same():
  N = int(input())
  A = list(map(int, input().split()))
  
  for i in range(N-1):
    if A[i] != A[i+1]:
      return False
  return True

if same():
  print("Yes")
else:
  print("No")