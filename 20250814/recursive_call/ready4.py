def ready4(lev):
    if lev == 3:
        return
    
    for _ in range(2):
        ready4(lev + 1)
        
    print(lev)
    
    
ready4(0)   