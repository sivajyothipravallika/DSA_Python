def foo(n):
    if (n==0):
        return 1
    else:
        return n*foo(n-1)
    
print(foo(5))