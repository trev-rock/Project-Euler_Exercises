from sympy import Eq, symbols, solve

def hex(x): # given formula for generating a hexagonal number
    return x*(2*x-1)

def pent_check(x):
    rhs = x # this is the hexagonal number we want to see is pentagonal
    n = symbols('n') # n is the variable we will use in the eqation
    lhs = Eq((n*(3*n-1))/2, rhs) # solving for n will get us the number that would be used to generate the same pent number 
    sol = solve(lhs,n)[1] # the negative solution is in the 0 index, and sol is the exact value
    int_sol = int(sol) # convert it to an integer in a new variable
    if sol == int_sol: # if they are both integers then that means the number was pentagonal because int_sol would be unchanged from sol then
        return True
    else:
        return False

num = 20000 # 143 is the first number and given in the example, so the next is our starting point
while True: 
    temp = hex(num) # the number to check
    if pent_check(temp): # we only need to check if it is a pent number because all hexagonal numbers are triangular 
        break
    num += 1
print(temp) # our final result



