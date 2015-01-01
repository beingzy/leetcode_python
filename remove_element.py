# Remove ELement
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
    	isDo = True
    	while isDo:
    		try:
    			pos = A.index(elem)
    			A.pop(pos)
    		except:
    			isDo = False
    	return len(A)