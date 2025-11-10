def fibonacci(n):
    step_count=0

    print("Fibonacci Sequence:")
    print(0,end=" ")
    print(1,end=" ")

    if n==0:
        step_count+=1
        return 0,step_count
    elif n==1:
        step_count+=1
        return 1,step_count
    
    a,b=0,1
    step_count+=2

    for i in range(2,n+1):
        step_count+=1
        a,b= b,a+b
        print(b,end=" ")
    print()
    return b,step_count

n=int(input("Enter n:"))
fib_num,steps=fibonacci(n)

print(f"Fibonacci({n})={fib_num}")
print(f"Step Count={steps}")


#def fibonacci(n):
#    global step_count
#    step_count+=1
#    if n<=1:
#        return n
#    else:
#        return fibonacci(n-1)+fibonacci(n-2)
#if __name__=="__main__":
#    m=int(input("Enter the number"))
#    print("fibonnaci series")
#    for i in range(m):
#        step_count=0
#        fib=fibonacci(i)
#        print(f"fibonacii({i})=={fib} || step_count={step_count}")




