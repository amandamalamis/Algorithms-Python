#One way of doing the problem: 

# def Fibonacci(n): 
      
#     # Taking 1st two fibonacci nubers as 0 and 1 
#     FibArr = [0, 1] 
      
#     while len(FibArr) < n + 1:  
#         FibArr.append(0)  
      
#     if n <= 1: 
#        return n 
#     else: 
#        if FibArr[n - 1] ==  0: 
#            FibArr[n - 1] = Fibonacci(n - 1) 
      
#        if FibArr[n - 2] ==  0: 
#            FibArr[n - 2] = Fibonacci(n - 2) 
      
#        FibArr[n] = FibArr[n - 2] + FibArr[n - 1] 
#     return FibArr[n] 
      
# print(Fibonacci(10))

#Solution using recursion: 

def Fibonacci(n): 
    if n<0: 
        print("Must use a positive number.") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(6)) 
