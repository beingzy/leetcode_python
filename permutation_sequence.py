# @Challenge
# Title: Permutation Sequence
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.
class Solution:
    # @return a string        
    def getPermutation(self, n, k):
        """
        Report kth sorted permutation in a form of string
        """
        if n > 1:
            all_permutations = getAllPermutations(n)
            perm_integers = vec2int(all_permutations)
            perm_integers = sorted(perm_integers)
            perm_str = [str(i) for i in perm_integers]
            res = perm_str[k-1]
        else:
            res = '1'
        return res
        
def getAllPermutations(n):
    """
    Return all permutations of n
    """
    permutations = []
    if n >= 2:
        for i in range(n):
            i = i + 1
            if i == 2:
                permutations = muteValue([i - 1], i)
            else:
                permutations = permuteArray(permutations, i)
    if n == 1:
        permutations = [n]
    return permutations
        
       
def permuteArray(array, val):
    """
    Permute an array-like with value
    """
    all_muted = []
    
    for i in range(len(array)):
        temp_res = muteValue(array[i], val)
        for j in range(len(temp_res)):
            if len(all_muted) == 0:
                all_muted = [temp_res[j]]
            else:
                all_muted.append(temp_res[j])
    return all_muted
    
    
def muteValue(vec, val):
    """
    Permute a vector with a value
    """
    vec_copy = [i for i in vec]
    vec_backup = [i for i in vec]
    all_muted = []
        
    for i in range(len(vec) + 1):
        vec_copy.insert(i, val)

        if len(all_muted) == 0:
            all_muted = [vec_copy]
        else:
            all_muted.append(vec_copy)
        vec_copy = [i for i in vec_backup]

    return all_muted
        
def vec2int(array):
    """
    Convert each row of array into an integer resepectively 
    """
    res = []
    for i in range(len(array)):
        ndigits = len(array[i])
        integers = [item * pow(10, ndigits - (j + 1)) for j, item in enumerate(array[i])]
        res.append(sum(integers))
    return res