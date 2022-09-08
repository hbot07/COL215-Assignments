n = int(input())
for i in range(n):
    print(' ' * (n - i) + "#" * i, "#" * i + ' ' * (n - i))
