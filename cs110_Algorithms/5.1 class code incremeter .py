import numpy as np
import random


class Counter(object):
    one = np.uint8(1)  # <= Google what "uint8" is

    def __init__(self):
        self.exp = np.uint8(0)

    def increment(self):
        if random.random() < 2.0 ** (-int(self.exp)):
            self.exp += self.one

    def to_int(self):
        return int(2.0 ** self.exp)

    def to_str(self):
        return "%d" % self.to_int()

c = Counter()
for a in range(10000):
    c.increment()

print(c.to_str())


