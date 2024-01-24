# Stephanie Fong and Alan Wang
# 1/23/24
import math
import numpy

#get the distance at the current moment
def getDistance(prior_point, current_point):
    distance = math.sqrt(math.pow(prior_point[0] - current_point[0], 2) + math.pow(prior_point[0] - current_point[0], 2))
    return distance

def get_vector (prior_point, current_point):
    vector = [(current_point[0] - prior_point[0]), (current_point[1] - prior_point[1])]
    return vector

#calculate angle from slope and math
def get_angle(prior_vector, current_vector):
    dot_product = numpy.dot(prior_vector, current_vector)
    prior_vector_mag = math.sqrt(pow(prior_vector[0], 2) + pow(prior_vector[1], 2))
    current_vector_mag = math.sqrt(pow(current_vector[0], 2) + pow(current_vector[1], 2))
    angle_rad = math.acos(dot_product / (prior_vector_mag * current_vector_mag))
    return angle_rad

#returns the distance the robot moves and sets the angle
def robot_move(distance, angle, clockwise):
    return


def main():
    #angle the robot is facing
    #preset to 0 (North)
    direction_angle = 0

    #sample point list
    point_list = [[1,0],[2,1],[3,4]]

    #start point/direction located
    prior_point = [0,0]
    prior_vector = [0, 1]
    
    for point in point_list:
        distance = getDistance(prior_point, point)
        vector = get_vector(prior_point, point)
        angle = get_angle(prior_vector, vector)
        if vector[0] > 0:
            clockwise = True
        else:
            clockwise = False
        robot_move(distance, angle, clockwise)

        prior_point = point
        prior_vector = vector
    
    print(prior_point)

main()

