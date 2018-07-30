import random
import math
import matplotlib.pyplot as plt
import numpy as np



class Node:
    def __init__(self, val, left=None, right=None):
        self.l_child = left
        self.r_child = right
        self.parent = None
        self.data = val
        self.l_count = 0
        self.red = False 

class RB_tree(object):
    def __init__(self, create_node=Node):
        self.nil = create_node(val = None)
        self.root = self.nil
        self.create_node = create_node


    def _left_rotate (self, x):
        y = x.r_child
        x.r_child = y.l_child
        if y.l_child != self.nil:
            y.l_child.parent = x

        y.parent = x.parent

        if x.parent == self.nil:
            self.root = y

        elif x == x.parent.l_child:
            x.parent.r_child = y

        y.l_child = x
        x.parent = y


    def _right_rotate (self, x):
        y = x.l_child 
        x.l_child = y.r_child 
        if y.r_child != self.nil: 
            self.r_child.parent = x 

        if y.parent == x.parent:
            
            if x.parent == self.nil :

                self.root = y 

            elif x == x.parent.l_child:
                x.parent.l_child = y 
            else :
                x.parent.r_child = y 
            
            if y.r_child == x :
                x.parent = y

    def insert (self, z):
        y = self.nil
        x = self.root

        while x is not self.nil:
            y = x
            if z.data < x.data :
                x = x.l_child
            else:
                x = x.r_child
        
        z.parent = y

        if y == self.nil:
            self.root = z

        elif z.data < y.data:
            y.l_child = z

        else:
            y.r_child = z

        z.l_child = self.nil
        z.r_child = self.nil
        z.red = True

        self._rb_fix (z)


    def _rb_fix (self, z):
        
        while z.parent.red :
            if z.parent == z.parent.parent.l_child:
                y = z.parent.parent.r_child

                if y.red:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent

                else:
                    if z == z.parent.r_child :
                        z = z.parent
                        self._left_rotate (z)

                    z.parent.red = False
                    z.parent.parent.red = True
                    self._right_rotate (z.parent.parent)

            else :

                y = z.parent.parent.l_child
                if y.red :
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.l_child:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self._left_rotate(z.parent.parent)
        
        self.root.red = False



RB = RB_tree ()

numbers = range(10)
random.shuffle(numbers)

for i in numbers:
    RB.insert(Node(i)) 
    print "elem {} inserted ".format(i)

