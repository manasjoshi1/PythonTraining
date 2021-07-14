def rec(n):
    if n<=1:
        return n
    else:
        return(rec(n-1)+rec(n-2))    
def fact(n):
    if n<=1:
        return n
    else:
        return (n*fact(n-1))            
print(fact(5))        