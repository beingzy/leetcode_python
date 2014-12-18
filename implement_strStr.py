# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.
#
# Update (2014-11-02):
# The signature of the function had been updated to return the index 
# instead of the pointer. If you still see your function signature returns a
# char * or String, please click the reload button  to reset your code definition.
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        occ_idx = -1
        
        for i in range(len_haystack - len_needle + 1):
            substr = haystack[i:(i + len_needle)]
            if substr == needle:
                occ_idx = i
                break
        
        return occ_idx