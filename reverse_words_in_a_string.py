## Reverse words in a string
##
## Author: Yi Zhang
## Date: Dec/24/2014, 9:44 AM
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s_item = s.split(" ")
        s_item = [i for i in s_item if i != '']
        if len(s_item) > 0:
        	s_item_rev = [ s_item[len(s_item)- i - 1] for i in range(len(s_item)) ]
        	s_rev = " ".join(s_item_rev)
        else:
        	s_rev = ""
        return s_rev