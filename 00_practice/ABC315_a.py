# [https://atcoder.jp/contests/abc315/tasks/abc315_a]
S = input()
print(S.translate(str.maketrans('', '', 'aeiou')))