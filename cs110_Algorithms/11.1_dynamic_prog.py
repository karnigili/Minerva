import numpy as np
import math
import time
import random
import matplotlib.pyplot as plt

def optionally_timed_function(func, *args, **kwargs):
	
	def wrapper_function(*args, **kwargs):
		if kwargs.pop("timed", None):
			start = time.time()
			res = func(*args, **kwargs)
			end = time.time()

			return res, end-start
		else:
			return func(*args, **kwargs)

	return wrapper_function

FibArray = []


def bu_fib(n):

	if n == 0 or n == 1 : 
		return 1

	fib_seq = [0 for i in range (n)]

	fib_seq[0] = 1 
	fib_seq[1] = 1

	for i in range (2, n):

		fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
	
	return fib_seq[-1]

def td_fib (n):
	
	if n == 1 or n == 2 : 
		return 1
		
	elif n <= len(FibArray) :
		return FibArray[n]

	else:
		temp_fib = td_fib(n-1) + td_fib(n-2)

		FibArray.append(temp_fib)

		return temp_fib
	
# print td_fib(3)
# print bu_fib(3)


@optionally_timed_function
def mem_td_cu (price, n, revenue):
	size = [0] * (n+1)

	if revenue[n] > 0 :
		return revenue[n]

	if n == 0:
		opt_rev = 0


	else:
		opt_rev = 0
		for i in range (1, n+1):

			size[n] = i
		
			opt_rev = max(opt_rev, price[i] + mem_td_cu(price,n-i-1,revenue))


	revenue[n] = opt_rev
	# td_r_Array[n] = opt_rev

	return opt_rev


def bu_cr (price, n):

	if n == 1:
		return price[0]


	revenue = [0] * (n+1)
	size = [0] * (n+1)

	revenue[0] = 0


	for j in range(1, n+1):
		opt_rev = float('-inf')

		for i in range (1, j+1):
			rev = price[i] + revenue[j-i]

			if rev > opt_rev :

				opt_rev = rev
				opt_size = i

			revenue[j] = opt_rev
			size[j] = opt_size

	return revenue[n], revenue, size


def print_solution (p,n):

	td_s_Array = [0] * (n+1)
	td_r_Array = [0] * (n+1)

	r = [0] * (n+1)


	best = mem_td_cu (p, n, r)
	
	return best, td_s_Array, td_r_Array

@optionally_timed_function
def naive_cr (price, n):
	if n <= 0 :
		return 0
	
	opt_rev = 0
	
	for i in range (1, n+1):
		opt_rev = max(opt_rev, price[i] + naive_cr(price, n - i - 1))

	return opt_rev


def timeit (function, *args):
	start = time.time()
	function(*args)
	end = time.time()

	return (end - start)



@optionally_timed_function
def test(x):
	print x





prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
rand_prices = [random.randint(0,1000) for r in xrange(1000)]
n = 7

array_of_times_naive = []
array_of_times_dyn = []

length = 20

for cuts in range (length):
	# res_naive = naive_cr(rand_prices, cuts, timed=True)
	res_dyn_prog = mem_td_cu(rand_prices, cuts, [0] * (cuts+1), timed=True)
	
	# array_of_times_naive.append(res_naive[1])
	array_of_times_dyn.append(res_dyn_prog[1])

# ploy =  np.poly1d(np.polyfit([i for i in range(length) ], array_of_times_naive, 10))
# exp_fit = np.poclyfit([i for i in range(length) ], np.log(array_of_times_naive), 1)


## log plot 
# plt.plot([i for i in range(length) ], np.log(array_of_times_naive))
# plt.plot ([i for i in range(length)], [exp_fit[0]*i+ exp_fit[1] for i in range(length)])

# print array_of_times_dyn
## exp plot 
# plt.plot([i for i  bin range(length)], array_of_times_naive)
# plt.plot([i for i in range(length)], [ exp_fit[0]*np.exp (-exp_fit[1]*i) for i in range(length)] )


# plt.plot([i for i in range(length) ], array_of_times_dyn) 

plt.show()




# print "bu"
print bu_cr (prices, n)
# print_solution (prices, n)
print "td"
print mem_td_cu(prices, n, [0] * (n+1))
print "naive"
print naive_cr(prices, n)

