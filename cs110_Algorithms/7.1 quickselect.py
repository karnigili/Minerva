import random
def swap (A, h, m):
	tmp = A[h]  
	A[h] = A[m]
	A[m]= tmp

def partition(A, start, end):
	#randomized 
	pivot_index = random.randint(start, end - 1)
	
	swap(A, pivot_index, start)


	pivot = A[start]

	#checks if all elemnts are the same
	if (all([A[i] == A[i + 1] for i in range(len(A) - 1)])) :
		return len(A)/2

	# the elemnt right after the pivot to the left
	index_after_pivot = start + 1

	for test_current_index in range(start + 1, end):
		if A[test_current_index] < pivot:
			# if the current element is smaller , we swap it to right after the pivot and move the mark to the right
			swap(A, index_after_pivot, test_current_index) 
			index_after_pivot += 1 

	#moving the pivot to its place and position 
	swap(A, start, index_after_pivot -1)

	return index_after_pivot-1


	


def quickselect (A, index, start=0, end=None):
	if end is None:
		end = len(A)
	if len(A) < 1:
		return 

	if index < 0 : 
		return A[0]
	if not index < len(A) -1:
		return A[-1]

	pivot_index = partition (A, start, end)

	if index == pivot_index:

		return A[pivot_index-1]

	elif index < pivot_index:

		return quickselect(A, index, start, pivot_index)

	else:

		return quickselect(A, index, pivot_index + 1, end)


e = [0,8,6,5,4,7,8,9]
index = 3

print quickselect(e,index)



# lst = range(10)
# random.shuffle(lst)

# for b in range(15):
# 	print e,b
# 	print(quickselect(e, b))









