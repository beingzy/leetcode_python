# Distinct Subsequences
# Given a string S and a string T, count the number of distinct subsequences of T in S.

# A subsequence of a string is a new string which is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Here is an example:
# S = "rabbbit", T = "rabbit"

# Return 3.
def findAppearanceMtx(S, T):
    """
    Get occurance matrix
    """
    S = "".join([letter for letter in S if letter in set(T)])
    
    pos = []
    for letter in T:
        pos.append([i for i, ref in enumerate(S) if ref == letter])
    
    return pos