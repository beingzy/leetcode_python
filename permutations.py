## Permutations:
##
## Given a collection of numbers, return all possible permutations.
##
## For example,
## [1,2,3] have the following permutations:
## [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

def permuTwoItems(x, return_idx = True):
	''' Return all permuations of 2 elements 

		Parameters:
		-----------
		x: vector-like, consited of two elements
		return_idx: boolean, if return index for permutations
		Returns:
		--------
		res: (idx, permutations) or permutations
	'''
	pmt = [ [x[0], x[1]], 
	        [x[1], x[0]]
	      ]
	idx = range(len(pmt))
	if return_idx:
		res = idx, pmt 
	else:
		res = pmt 
	return res


def comb(one_item, two_items):
	''' Return all permutations of 3 elements
	'''
	pmts = []
	index_all2Pmts, all2Pmts = permuTwoItems(two_items, return_idx=True)
	for pos in range(len(x)):
		for idx in index_all2Pmts:
			if pos == 0:
				pmt = [one_item, all2Pmts[idx][0], all2Pmts[idx][1]]
			elif pos == 1:
				pmt = [all2Pmts[idx][0], one_item, all2Pmts[idx][1]]
			else:
				pmt = [all2Pmts[idx][0], all2Pmts[idx][1], one_item]
		pmts.append(pmt)
	return pmts

def permutation(x):
	

x = [3, 2, 1]
print permuThreeItems(x)



