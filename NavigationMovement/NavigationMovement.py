# Stephanie Fong and Alan Wang
# 1/23/24
import math
import numpy

# get the x movement and y movement between 2 points
def get_vector (from_point, to_point):
    vector = [(from_point[0] - to_point[0]), (from_point[1] - to_point[1])]
    return vector

# get the distance between 2 points
def get_distance(vector):
    distance = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
    return distance

# get the angle between 2 vectors to know how much to turn the robot
def get_angle(prior_vector, current_vector):
    dot_product = numpy.dot(prior_vector, current_vector)
    prior_vector_mag = math.sqrt(pow(prior_vector[0], 2) + pow(prior_vector[1], 2))
    current_vector_mag = math.sqrt(pow(current_vector[0], 2) + pow(current_vector[1], 2))
    angle_rad = math.acos(dot_product / (prior_vector_mag * current_vector_mag))
    return angle_rad


def move(start, vector):
    return [(start[0] + vector[0]), (start[1] + vector[1])]

def simulation(path):
    points = path
    movements = []
    from_point = [0, 0]
    for point in points:
        movements.append(get_vector(from_point, point)) # which way the robot moves
        from_point = point

    curr_pos = [0, 0]
    for movement in movements:
        curr_pos = move(curr_pos, movement) # actually moves the robot
    return curr_pos

def main():
    #sample point list
    point_list = [[0,0],[1,0],[2,1],[3,4]]
    from_point = point_list[0]
    prior_vector = get_vector(from_point, point_list[1])
    
    for point in point_list[1:]:
        vector = get_vector(from_point, point)
        distance = get_distance(vector)
        angle = get_angle(prior_vector, vector)
        if vector[0] > 0:
            clockwise = True
        else:
            clockwise = False
        move(distance, angle, clockwise, point)

        from_point = point
        prior_vector = vector
    
main()

