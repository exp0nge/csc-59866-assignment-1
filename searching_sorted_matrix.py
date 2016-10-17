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
	# first search m[0][0]
	row = None
	last_col = len(m) - 1
	for i in range(0, len(m)):
		val = m[i][last_col]
		if val == target:
			print 'val=target', i, len(m)
			if i == 0:
				return i + len(m) - 1
			else:
				return i + len(m)
		elif target < val:
			row = i
			break

	if row is None:
		return None
	else:
		position = binary_search(m[row], target)
		
		if position is not None:
			return (row * len(m)) + position
		else:
			return None	
	
	
if __name__ == '__main__':
	"""
	[ 1, 2, 3, 4 ]
	[ 5, 6, 7, 8 ]
	[ 9, 10, 11, 12 ]
	[ 13, 14, 15, 16 ]
	"""
	m = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
	N = len(m)
	for row in range(0, N):
		for col in range(0, N):
			position = matrix_binary_search(m, m[row][col])
			print m[row][col], position, row, col