## Pascal's Triangle II
## Input num_rows
## return ith row of Pascal's Triangle 
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
    	# get the Pascal‘s Triagnle:
    	triangle = getPascalTriangle(rowIndex)
    	print "%dth rows of Pascal‘s traigle: %d" % (rowIndex, len(triangle))
    	res = triangle[rowIndex - 1]
    	return res

def getPascalTriangle(numRows):
	"""
	Return the next row given the current row

	Parameters:
	-----------
	current_row: {vector-like, list}

	Returns:
	--------
	res: {vector-like, list}

	e.g. [1, 2, 1] --> [1, 3, 3, 1]
	"""

	res = []

	for i in range(numRows):
		if i == 0:
			res.append([1])
		else:
			nr = gen_next_row(res[i - 1])
			res.append(nr)

	return res
        
def gen_next_row(current_row):
	"""
	Return the next row given the current row

	Parameters:
	-----------
	current_row: {vector-like, list}

	Returns:
	--------
	res: {vector-like, list}

	e.g. [1, 2, 1] --> [1, 3, 3, 1]
	"""
	nr = [0 for i in range(len(current_row) + 1)]
	nr[0], nr[len(nr) - 1] = 1, 1
	if len(nr) > 2:
		for i in range(len(nr))[1:len(nr)-1]:
			nr[i] = sum(current_row[ i-1 : i+1 ])
	return nr


