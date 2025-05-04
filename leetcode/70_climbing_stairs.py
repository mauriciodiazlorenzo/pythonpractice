import math

def climbStairs(n: int) -> int:
    tot = 0
    # suppose we take num_double double steps
    for num_double in range(0,n//2+1):
        #we need to take num_single single steps
        num_single=n-2*num_double
        tot += math.comb(num_double+num_single,num_double)
    return tot

print(climbStairs(20))