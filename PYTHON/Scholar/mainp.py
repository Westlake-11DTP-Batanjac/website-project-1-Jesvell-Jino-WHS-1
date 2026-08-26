# Do now Q1
# 3
# 2
# 1
# "Liftoff!"

# def sum_to(n):
#    if n == 1:
#        return 1
 #   return n + sum_to(n - 1)

# print(sum_to(3))

def fib(n):
   if n <= 1:
       return n
   return fib(n - 1) + fib(n - 2)