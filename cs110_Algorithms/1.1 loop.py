

#input : (f: a function (output: list), m:len of the list from f, n: number of lists)
#output : list of n lists
import numpy as np
from random import randint 

def rand_list(m):
	lis = []
	for _ in xrange(m):
		lis.append(randint(-1000,1000))
	return lis


def f1 (m1):
	return list(np.zeros(m1))


def g (f,m,n):

	return [f(m*(2**i)) for i in range(n)]

def ff(m,e, ml):
    return [e[0:randint(0,ml)] for i in range (m)]


def fff(m,e, ml):
	l = []

	for i in range (m):
		b = randint(0,len(e)-ml)
		r = randint(1,ml)
	
		l.append(e[b:b+r])
	return l


print fff(5,"helsgslowofasfa",6)
print

