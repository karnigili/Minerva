import numpy as np
import math
from matplotlib import pyplot as plt



def get_random_position (size):
    #returns the x,y for the position of the middle of the needle
    # draws a position from a uniform distrbution; the location reflects the middle of the needle. position range vary between l/2 to length -l/2

    x_position = np.random.uniform(0, size)
    y_position = np.random.uniform(0, size)

    return (x_position, y_position)

def get_random_angle():
    #get_random_position
    #returns the x,y for the position of the middle of the needle

    # draws a position from a uniform distrbution; the location reflects the middle of the needle. position range vary between l/2 to length -l/2
	
	hyp = 1.1

	while hyp > 1:
		dx = np.random.uniform(-1,1)
		dy = np.random.uniform(0,1)
		hyp = math.sqrt (dx ** 2 + dy ** 2)
	
	if hyp <=1:
		# Return atan(y / x) in rad
		return math.atan2(dy,hyp)



def check_if_cross_line (mid_position, edge_position, length, line_gap):
    #examine if the needle touches the line
    #checks if a needle fell on a line

    for line in range(0, length+1, line_gap):

        if (line >= mid_position and line <= edge_position) or (line >= edge_position and line <= mid_position):
            
            return True


def drop_needles(size, needle_length, gap_between_lines): 
    #drop_needles
    needle_position = get_random_position(size)

    needle_x_position = needle_position[0]
    needle_y_position = needle_position[1]

    # have a random angle in radians  # deg2rad x * pi / 180
    angle = np.deg2rad(get_random_angle())
   
    # The needle edge is (needle_length/2)* sin(angle) 
    #(where x is the distance between the center of the needle to the closest line)
    # mid loaction + the trig function for the x,y edges.
    needle_edge_position_x_1 = (needle_x_position + ((needle_length/2.0) * np.cos(angle)))
    # needle_edge_position_y_1 = (needle_y_position + ((needle_length/2.0) * np.sin(angle)))

    needle_edge_position_x_2 = (needle_x_position - ((needle_length/2.0) * np.cos(angle)))
    # needle_edge_position_y_2 = (needle_y_position - ((needle_length/2.0) * np.sin(angle)))


    return check_if_cross_line(needle_x_position, needle_edge_position_x_1, size, gap_between_lines) or check_if_cross_line(needle_x_position, needle_edge_position_x_2, size, gap_between_lines)
    
    # if the needle crosses, returns True





