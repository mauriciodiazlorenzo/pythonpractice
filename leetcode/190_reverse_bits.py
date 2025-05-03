class Solution:
    def reverseBits(self, n: int) -> int:
        out=0
        for i in range(32):
            out += n&1 # take the rightmost bit of n
            out <<= 1 # shift bits of output to the left
            n >>= 1 # shift bits of n to the right
        return out>>1 # undo the last extra shift