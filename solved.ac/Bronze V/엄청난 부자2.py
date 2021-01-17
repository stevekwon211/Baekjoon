n, m = map(int,input().split())
if 1 <= m <= n <= 10**1000:
    print(int(n//m))
    print(int(n%m))
