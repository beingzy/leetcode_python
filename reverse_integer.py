class Solution:
    # @return an integer
    def reverse(self, x):
        x = [i for i in str(x)]
        limit_lower, limit_upper = -2147483648, 2147483647 # range of 32 bit integer

    	if x[0] == '-':
        	x.pop(0)
        	x.reverse()
        	res = int(''.join(['-', ''.join(x)]))
        	res = 0 if res < limit_lower else res
        else:
        	x.reverse()
        	res = int(''.join(x))
        	res = 0 if res > limit_upper else res

    	return res
