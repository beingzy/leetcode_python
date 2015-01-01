#Remove Duplicates from Sorted Array 
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        isDo = True
        
        while isDo:
        	for i in range(1, len(A)):
        		isDup = x[i] == x[i-1]
        		if isDup:
        			A.pop(i)
        			break
        		elif i == len(A) - 1:
        			isDo = False
        		else:
        			pass

        return len(A), A