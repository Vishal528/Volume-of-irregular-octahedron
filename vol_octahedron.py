import itertools
import numpy
import math
import copy
from scipy.spatial import ConvexHull


def volume_octahedron(input_list):


    """ The function takes a list of 6 co-ordinates in 3-d space as input and returns the volume
    of the octahedron formed by the six co-ordinates and returns None if no octahedron is formed"""

    #A copy of the list is defined to carry out operations not affecting the original data

    input_copy = copy.deepcopy(input_list)
 
    #A list M named to store the 4 co-ordinates of the octahedron which lie in the same plane

    M = []

    #Using  itertools package we find the 4 co-ordinates which lie in the same plane

    for comb in itertools.combinations(input_list,4):

        #Randomly 4 co-ordinates from the input_list are stored in M

        M=list(comb)

        #1 is added to every set of co-ordinates in order to find the volume of the polyhedron formed by the 4 co-ordinates
        for i in range(len(M)):
            M[i] = M[i]+[1]
        # The points lie in a plane if the determinant is zero . So, that condition is checked
        if numpy.linalg.det(M) == 0:
                input_copy.remove(list(comb)[i])
            break


    #The following matrices A and B are defined to apply the determinant formula of plane formed by 3 points

    A= [[input_copy[0][0]-M[0][0],input_copy[0][1]-M[0][1],input_copy[0][2]-M[0][2]],
       [M[1][0]-M[0][0],M[1][1]-M[0][1],M[1][2]-M[0][2]],
       [M[2][0]-M[0][0],M[2][1]-M[0][1],M[2][2]-M[0][2]]]

    B =[[input_copy[1][0]-M[0][0],input_copy[1][1]-M[0][1],input_copy[1][2]-M[0][2]],
       [M[1][0]-M[0][0],M[1][1]-M[0][1],M[1][2]-M[0][2]],
       [M[2][0]-M[0][0],M[2][1]-M[0][1],M[2][2]-M[0][2]]]

    #If the points lie on opposite sides of the plane the following condition is satisfied
    if numpy.linalg.det(A)*numpy.linalg.det(B) < 0:
        print("The 6 points form an octahedron in 3-d space")
        volume = ConvexHull(input_list).volume
        return volume
    else:
       print("The points don't form an octahedron")


sample_list = [[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],[0,0,2**0.5],[0,0,-2**0.5]]
print("\nThe volume of the octahedron is "+str(volume_octahedron(sample_list))+" cubic units")
