import random

def x_maxsubarray_dc(A, start, end, mid):

   	l, h = 0, 0
	i = mid
	s = 0

	left_sum = A[i] - 1

	while i >= start:
		s = s + A[i]
		if s > left_sum:
			left_sum = s
			l = i
		i = i - 1
	j = mid + 1
	s = 0

	right_sum = A[j] - 1

	while j <= end:
		s = s + A[j]
		if s > right_sum:
			right_sum = s
			h = j
		j = j + 1

	return (l, h, left_sum + right_sum)

def maxsubarray_dc(A, start, end):
	if start == end:
		return (start, end, A[start])

	mid = (start + end) / 2
	left_start, left_end, left_sum = maxsubarray_dc(A, start, mid)
	right_start, right_end, right_sum = maxsubarray_dc(A, mid + 1, end)
	x_start,x_end, x_sum = x_maxsubarray_dc(A, start, end, mid)
	
	if left_sum > right_sum:
		if left_sum > x_sum:
			return (left_start, left_end, left_sum)
		else:
			return (x_start, x_end, x_sum)
	else:
		if right_sum > x_sum:
			return (right_start, right_end, right_sum)
		else:
			return (x_start, x_end, x_sum)



def incremental_max_subarray(x, mx):
	# x array + adittion (assuming th enew int is added in the end of the old array)
	#mx is the maxsubarray of x[0:-1]
	# the new max subarray potentially between some index on the array all the way to the end(inclusive of the new int)

	max_value = sum(mx) # cuurent max value
	running_sum = 0 #looking for a new max sub array
	new_max_value = x[-1] #storing the new max sub array
	
	start = len(x) # the index that indicates the start point of the new max subarray 
	# end is the end of the array

	for index in range(len(x)-1,0,-1): #looping from the new int to the start and looking for the max sub array
		running_sum += x[index] #accumulative sum of the array from end to the beginning 

		if running_sum > new_max_value : #if the new running sum is bigger than the known max sum of x
			new_max_value = running_sum
			start = index #save the starting index

	#comparing the max subarray of x to mx
	if new_max_value > max_value:
		return new_max_value, x[start:] 


	return max_value, mx

def cursive_max_subarray(A):
   if len(A) == 0:
      return (0, 0)
    (mx_subarray, mx_endarray) = recursive_mx_subarray(A[:-1])
    mx_endarray = max(mx_endarray + A[-1], 0)
    mx_subarray = max(mx_subarray, mx_endarray)
    return mx_subarray, mx_



#creates a random subarray 
random_array = [random.randint(-10,10) for r in xrange(6)]
print "original array"
print random_array

pervious = maxsubarray_dc(random_array,0, len(random_array)-1)
arr = random_array[pervious[0]:pervious[1]+1]
print pervious
print arr

new_A = random_array
new_A.append(random.randint(-10,10))
print 'original array with an added integer'
print new_A

print incremental_max_subarray(new_A,arr)







