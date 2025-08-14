def ready4(n):
    if n == 0:
        return print(0)
    for _ in range(2): 
        print(n + 1)
        print(n + 1)
        print(n)
    ready4(n - 1)
ready4(1)   