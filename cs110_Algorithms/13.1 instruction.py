# Instructions:
# -------------
#  1. This is a valid python file. Update the code at the bottom to include
#     your student email address.
#  2. Run the code to find out which one of the problems you need to do.
#  3. Solve your assigned problem.  Since the assignment is deterministic, you
#     can also find out who else is working on the same problem.  Feel free to
#     approach other students if you get stuck conceptually, but write your
#     code by yourself.
#  4. Now answer the following questions on your solution
#     a) Define variables which will be useful in determining the computational
#        complexity of your solution.
#     b) How does it scale in terms of time (using your variables from a)?
#     c) How does it scale in terms of space (using your variables from a)?
#     d) Each problem has an example so that you can see how to structure your
#        solution.  However the answers to the examples are wrong.  What is the
#        actual answer for your example documentation?
#
# Directions:
# -----------
#
# You and your friends rented a bus and have gotten lost.  This is because the
# person with the map was sitting at the back of the bus and gave directions to
# the person in front of them.  This person then told the person in front of them.
# Eventually the directions reached the driver in the front.  Occasionally someone
# would make a mistake, and they would either:
#  - leave out a step,
#  - add a step,
#  - give the wrong instruction.
#
# Each direction was either "Straight", "Left", or "Right".
#
# You and you friends would like to figure out who made the most mistakes.
# Fortunately everyone wrote down the instructions they gave. Write a function
# ('blame') to figure out who is to blame.
#
# directions = [('map', 'SSSRSSLRLS'), ('jane', 'SSRSLSLSSRLS'), ('jayna',
#                'SRSLSLSRLS'), ('jomo', 'SRSLRRSLSRSLSR')]
#
# >>> print(blame(directions))
# 'jayna'
#
# Aquarium:
# -----------
#
# The Cape Town aquarium is designing a new feature and asks you to help. There
# will be fish tanks of different sizes all arranged in a large circle. Each fish
# tank will only contain fish from a single species. If the same fish species are
# stocked in adjacent tanks then they will continually attempt to fight and
# eventually will die of stress.
#
# You will be given a list of fish species, and how much it costs to stock those
# fish per liter of water. You will also be given a list of the tanks and how many
# liters each tank is. Your job is to find which fish should be stocked in which
# tank to achieve minimum cost without incurring any stress on the fish.
#
# Don't forget that the tanks are in a circle, so the beginning and ending tanks
# also mustn't contain the same species either.
#
# >>> tanks = [10, 15, 200, 35, 18, 99, 99, 10]
# >>> fish = [('shark', 12.1), ('marlin', 8.1), ('sole', 9.1)]
# >>> print(aquarium(tanks, fish))
# ['marlin', 'sole', 'marlin', 'sole', 'marlin', 'sole', 'marlin', 'shark']
#
#
# Baggage:
# -----------
#
# Next semester you need to move to a new country.  You have lots of useful things
# that you'd like to take with you, but your baggage allowance for the flight is
# very small.  The airline does allow you to pay extra for each bag that you want
# to take.  Anything that you don't pack you will need to buy in the new country.
#
# You need to decide how many extra bags to take, and what you should pack in
# those bags.
#
# >>> weights = {'glasses': 1.0,'plates': 0.7, 'coffee': 1.1,'keyboard': 1.1,
#                'pens': 2.1, 'socks': 0.5, 'undies': 0.3, 'laptop': 2.1,
#                'jersey': 0.5, 'shoes': 0.7, 'jeans': 1.1}
# >>> values = {'glasses': 0.1,'plates': 0.1, 'coffee': 0.1,'keyboard': 0.1,
#               'pens': 1.1, 'socks': 3.1, 'undies': 3.1, 'laptop': 10.1,
#               'jersey': 2.1, 'shoes': 2.1, 'jeans': 2.1}
# >>> baggage_limit = 3
# >>> extra_cost = 10
# >>> print(baggage(weights, values, baggage_limit, extra_cost))
# [['socks', 'undies', 'laptop'], ['jersey', 'shoes', 'jeans']]
#
#

import hashlib


def which_problem(email, seminar, problems):
    email = email.strip().lower()
    assert "@minerva.kgi.edu" in email
    seminar = seminar.strip().lower()
    md5 = hashlib.md5(email + seminar).hexdigest()
    ind = int(md5, 16) % len(problems)
    return problems[ind]


email = 'gili.karni@minerva.kgi.edu'
print(which_problem(email, '12.1', ['directions', 'aquarium', 'baggage']))


