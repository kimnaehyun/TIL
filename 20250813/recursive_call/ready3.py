def ready3(n):
    if n == 6:
        return
    print(n, end=' ')
    ready3(n + 1)
    print(n, end =' ')
    
ready3(0)
    