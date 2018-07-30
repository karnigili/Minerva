import heapq
import random 

def add_to_median_heap (minh, maxh, elem):
	

	# heaps are not empty
	if len(maxh) != 0 and len(minh) != 0 :
		
		# if smaller than max[0] - push to max 
		if elem <= -1 * maxh[0]:
			heapq.heappush(maxh, -1 * elem)

		else:

			heapq.heappush(minh, elem)
	else:
		heapq.heappush(minh, elem)


	# compare size and balance
	if abs(len(maxh) - len(minh)) > 1 :

		if len(maxh) > len(minh):
			to_min = -1 * heapq.heappop(maxh) 
			heapq.heappush(minh, to_min)

		elif len(maxh) < len(minh):
			to_max = heapq.heappop(minh)
			heapq.heappush(maxh, -1 * to_max)
	


def median (minh, maxh):
	#return the median element
	maxh_size = len(maxh)
	minh_size = len (minh)


	if maxh_size == minh_size:	
		return -1 * maxh[0], minh[0]
	else:
			if maxh_size > minh_size:
				return -1* maxh[0]
			else:
				return minh[0]




# maxx = [-2,-3,-4,0,-1]
# minn = [5,10,9,11]

# heapq.heapify(maxx)
# heapq.heapify(minn)

# add_to_median_heap(minn,maxx,6)
# print median(minn,maxx)


min1 = []
max1 = [] 

for a in range(1,10):
	b = random.randint (1,100)

	add_to_median_heap(min1, max1, b)
	print(median(min1, max1))
