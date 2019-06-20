import timeit
print(timeit.timeit('''def fibonacci(n = 20):
    """
    Tagastab Fibonacci jada n-nda liikme
    """
    if n== 1 or n== 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)''',number=5000))

# antud valemiga fibonacci(n=5) = 0.0020744795470532883 sekundit
#antud valemiga fibonacci(n=5) = 0.0021298715769406504 sekundit
#antud valemiga fibonacci(n=5) = 0.002182381940533294 sekundit
#antud valemiga fibonacci(n=5) = 0.0012784992794233339 sekundit
#antud valemiga fibonacci(n=5) = 0.0008299198928788583 sekundit
#antud valemiga fibonacci(n=5) = 0.00210073472884961 sekundit
#antud valemiga fibonacci(n=5) = 0.002083124545937443 sekundit

#Minu fibonacci(n=5) = 0.001118086522350684 sekudnit 
#Minu fibonacci(n=10) = 0.002068396029319994 sekundit
#Minu fibonacci(n=15) = 0.002101375099137325 sekudnit 
#Minu fibonacci(n=20) =  0.0005183797479054289 sekudnit 
#Minu fibonacci(n=25) =  0.002113862319747771 sekundit 
#Minu fibonacci(n=30) =  0.0020856860270883036  sekundit
#Minu fibonacci(n=35) =  0.0021004145437057524 sekundit
""" Minu fibonacci ei olnud vaga kiirem,aga kiirem oli ikka"""
