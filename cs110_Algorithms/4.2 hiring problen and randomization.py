import random
import matplotlib.pyplot as plt


def hire_assistant (n):
	# set base values for the amount of assistants hired and the the best candidate
	count = 0 
	current_quality = -1  #0 is the least qulafied 
	
	# checks all candidates 
	for j in range(n):
		# set a probablities to be uniform
		potential_quality = random.random()

		# if the random var is greater than the current_quality one (current one) swap them , add 1 to count
		# if potential_quality > current_quality:
		if potential_quality > 1.1 * current_quality :

			current_quality = potential_quality
			count += 1
	
	return {'current_quality':current_quality,'hired':count}


def test_for_x_hired (amount_of_tests, n_asistants, x_hired):

	count_hired = 0.0
	for test in range (tests):

		asistants_hired = hire_assistant(n_asistants)['hired']
		if asistants_hired == x_hired:

			count_hired += 1.0

	return count_hired/amount_of_tests


def test_for_x (amount_of_tests, n_potential_assistants):
	
	count_hired_avg = []

	for n_assistant in range(1, n_potential_assistants):
		count_hired_sum = 0.0

		for test in range (amount_of_tests):
			assistants_hired = hire_assistant(n_assistant)['hired']
			count_hired_sum += assistants_hired

		count_hired_avg.append(count_hired_sum / amount_of_tests)

	return count_hired_avg


def party(n):
	hats = [ i for i in range(n) ]
	random.shuffle(hats)
	return len([hat for preson, hat in enumerate(hats) if hat == preson])


def test_hats_for_n (n):
	hats = []
	for i in range(n):
		hats.append(party(i))
	
	return hats

#####
tests = 10


## prob for 2 to hire
# test_for_x_hired test(tests, 10,2)

## n to hired	
n=1000
A = test_for_x(tests,n)
print A
x = range (1,n)
y = A


## hats 
# print test_hats_for_n(30)

plt.plot(x,y)
plt.show()


