
def binary_add_positive(a: int, b: int):
    # where bits of a and b are both one they should move one column to the left
    # print(bin((a & b) << 1))
    # exclusive or where one of a or b has a 1 and the other has a zero
    # print(bin(a ^ b))
    x = a
    y = b
    while (x & y) != 0:  # keep carrying the overlapping bits to the left until there is no overlap
        xprev = x
        yprev = y
        x = (xprev & yprev) << 1
        y = xprev ^ yprev
    return(x ^ y)  # then simply return the xor since there is no overlap

def binary_subtract_positive(a: int, b: int):
    # do a-b, assuming x>=y and x>y>=0
    x=a
    y=b
    z = 0
    # what do we need to add to y to obtain x? add that to 0 to get the diff
    check=1
    while (x ^ y) > 0:  # there are some bits that dont match
        # print(bin(x))
        # print(bin(y))
        # print(bin(x^y))
        # print(bin((x^y)&y))
        diff = (x ^ y) # bits that don't match
        # find the lowest bit that doesn't match
        while check&diff==0:
            check=check<<1 # move the bit over by one until there is overlap
        y = binary_add_positive(y,check)
        z = binary_add_positive(z,check)
    # eventually all the bits match, as we keep adding the non matching bits back to y to increment y
    return z


print(binary_add_positive(213,543))
print(binary_subtract_positive(234662,75))
print(binary_subtract_positive(100,1))
print(binary_subtract_positive(100,0))
print(binary_subtract_positive(999,999))

# bitwise complement ~x = -x-1
# for cases like 50 - 100, do 100 - 50 and then multiply by minus one -> ~(100-50)+1