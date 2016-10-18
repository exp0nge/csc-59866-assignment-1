# -*- coding: utf-8 -*-
"""
For a square N x N matrix A, assume the elements are sorted in ascending
order along the horizontal and vertical directions already, i.e., A[i][k] ≤
A[j][k] and A[k][i] ≤ A[k][j], where i<j. Develop an efficient algorithm to
search for the query value v from A, return the location if found, None
otherwise. Analyze the time complexity of your algorithm

[ 1, 2, 3, 4 ]
[ 5, 6, 7, 8 ]
[ 9, 10, 11, 12 ]

target = 6
binary search A[0][0] until value >= target (index T)
binary search A[T] => None if target found, else None
"""

def binary_search(a, target):
	size = len(a)
	start, end = 0, size - 1
	
	while start != end:
		mid = abs(start + end)/2
		
		if a[mid] == target:
			return mid
	
		if target < a[mid]:
			start, end = 0, mid - 1
		else:
			start, end = mid + 1, size - 1
		
	return start if a[start] == target else None
	
def matrix_binary_search(m, target):
	"""
	
	"""
	size = len(m)
	last_col = size - 1
	
	start, end = 0, last_col
	
	while start != end:
		# figure out what row to look at using modified version of 
		# binary search
		# mid is now the mid row
		mid = abs(start + end)/2
		if m[mid][0] <= target <= m[mid][last_col]:
			# we've found our row
			break
		elif m[mid][0] > target:
			# need to look at previous half
			start, end = 0, mid - 1
		elif m[mid][last_col] < target:
			# look at bottom half
			start, end = mid + 1, last_col
	if start == end:
		mid = start

	position = binary_search(m[mid], target)
	if position is None:
		return None
	else:
		return position + size * mid
	
	
if __name__ == '__main__':
	"""
	[ 1, 2, 3, 4 ]
	[ 5, 6, 7, 8 ]
	[ 9, 10, 11, 12 ]
	[ 13, 14, 15, 16 ]
	"""
	m = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
	N = len(m)
	# test case
	for row in range(0, N):
		for col in range(0, N):
			position = matrix_binary_search(m, m[row][col])

			if position != row * N + col:
				raise ValueError("Position should be %i, got %i" % (row * N + col, position))