##################################################################################################
# Ammar Essajee
# Student ID: 102-43-821
# Date:2/7/2019
# Assignment #4
# This code allows the user to transform multiple objects on a canvas: rotate, scale, and
# translate (in-place). Also implements backface culling, fill, and z-buffer functionality.
# Faceted, Gourard, and Phong shading models have been implemented, alongside ambient diffuse,
# point diffuse, and point specular lighting functionality.
##################################################################################################



import math
from tkinter import *

CanvasWidth = 600
CanvasHeight = 600
d = 500
fil = 0
bfc = 0
buf = 0
faceted = 0
gourard = 0
phong = 0
light = 0
Ia = [0, 0, 255]
Kd = 0.5
Ip = 1
t = 0

class Pyramid(): # class for Pyramid
    # ***************************** Initialize Pyramid Object ***************************
    # Definition  of the five underlying points
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        
        self.apex = [0,50,100] # create pyramid origin
        self.base1 = [-50,-50,50]
        self.base2 = [50,-50,50]
        self.base3 = [50,-50,150]
        self.base4 = [-50,-50,150]
        
        self.apex[0] = self.apex[0] + x # initalize x compentent so new x can be passed in 
        self.base1[0] = self.base1[0] + x
        self.base2[0] = self.base2[0] + x
        self.base3[0] = self.base3[0] + x
        self.base4[0] = self.base4[0] + x
        
        self.apex[1] = self.apex[1] + y # initialize y so new y can be passed  in 
        self.base1[1] = self.base1[1] + y
        self.base2[1] = self.base2[1] + y
        self.base3[1] = self.base3[1] + y
        self.base4[1] = self.base4[1] + y
        
        self.apex[2] = self.apex[2] + z # initialize z so new z can be passed in
        self.base1[2] = self.base1[2] + z
        self.base2[2] = self.base2[2] + z
        self.base3[2] = self.base3[2] + z
        self.base4[2] = self.base4[2] + z

        # Definition of the five polygon faces using the meaningful point names
        # Polys are defined in counter clockwise order when viewed from the outside
        self.frontpoly = [self.apex,self.base1,self.base2]
        self.rightpoly = [self.apex,self.base2,self.base3]
        self.backpoly = [self.apex,self.base3,self.base4]
        self.leftpoly = [self.apex,self.base4,self.base1]
        self.bottompoly = [self.base4,self.base3,self.base2,self.base1]

        # Definition of the object
        self.Base = [self.bottompoly, self.frontpoly, self.rightpoly, self.backpoly, self.leftpoly]

        # Definition of the Pyramid's underlying point cloud.  No structure, just the points.
        self.PointCloud = [self.apex, self.base1, self.base2, self.base3, self.base4]        #************************************************************************************
        
            
  

class Cube: # establish cube class
    def __init__(self, x, y, z):
        # Definition  of the five underlying points
        
        self.x = x
        self.y = y
        self.z = z
        
        self.base1 = [-50,-50,-50] # creating cube in 'origin' position
        self.base2 = [50,-50,-50]
        self.base3 = [50,-50,50]
        self.base4 = [-50,-50,50]
        self.basetop1 = [-50,50,-50]
        self.basetop2 = [50,50,-50]
        self.basetop3 = [50,50,50]
        self.basetop4 = [-50,50,50]
        
        self.base1[0] = self.base1[0] + x # initializing x component for new x to be passed in 
        self.base2[0] = self.base2[0] + x
        self.base3[0] = self.base3[0] + x
        self.base4[0] = self.base4[0] + x
        self.basetop1[0] = self.basetop1[0] + x
        self.basetop2[0] = self.basetop2[0] + x
        self.basetop3[0] = self.basetop3[0] + x
        self.basetop4[0] = self.basetop4[0] + x
        
        self.base1[1] = self.base1[1] + y # initializes y component for new y
        self.base2[1] = self.base2[1] + y
        self.base3[1] = self.base3[1] + y
        self.base4[1] = self.base4[1] + y
        self.basetop1[1] = self.basetop1[1] + y
        self.basetop2[1] = self.basetop2[1] + y
        self.basetop3[1] = self.basetop3[1] + y
        self.basetop4[1] = self.basetop4[1] + y
        
        self.base1[2] = self.base1[2] + z # initialize z component for new z
        self.base2[2] = self.base2[2] + z
        self.base3[2] = self.base3[2] + z
        self.base4[2] = self.base4[2] + z
        self.basetop1[2] = self.basetop1[2] + z
        self.basetop2[2] = self.basetop2[2] + z
        self.basetop3[2] = self.basetop3[2] + z
        self.basetop4[2] = self.basetop4[2] + z

        # Definition of the five polygon faces using the meaningful point names
        # Polys are defined in counter clockwise order when viewed from the outside
        self.frontpoly = [self.base1, self.base2, self.basetop2, self.basetop1]
        self.rightpoly = [self.base2, self.base3, self.basetop3, self.basetop2]
        self.backpoly = [self.base3, self.base4, self.basetop4, self.basetop3]
        self.leftpoly = [self.base1, self.base4, self.basetop4, self.basetop1]
        self.bottompoly = [self.base4, self.base3, self.base2, self.base1]
        self.toppoly = [self.basetop2, self.basetop3, self.basetop4, self.basetop1]

        # Definition of the object
        self.Base = [self.bottompoly, self.frontpoly, self.rightpoly, self.backpoly, self.leftpoly, self.toppoly]

        # Definition of the Pyramid's underlying point cloud.  No structure, just the points.
        self.PointCloud = [self.base1, self.base2, self.base3, self.base4, self.basetop1, self.basetop2, self.basetop3, self.basetop4]
        #************************************************************************************

class Octagon: # establish hexagon class
    def __init__(self, x, y, z):
        # Definition  of the five underlying points
        
        self.x = x
        self.y = y
        self.z = z
        
        self.base1 = [-10.355,-40,-25] # creating cube in 'origin' position
        self.base2 = [10.355,-40,-25]
        self.base3 = [25,-40,-10.355]
        self.base4 = [25,-40,10.355]
        self.base5 = [10.355,-40,25]
        self.base6 = [-10.355,-40,25]
        self.base7 = [-25,-40,10.355]
        self.base8 = [-25,-40,-10.355]
        self.basetop1 = [-10.355,40,-25]
        self.basetop2 = [10.355,40,-25]
        self.basetop3 = [25,40,-10.355]
        self.basetop4 = [25,40,10.355]
        self.basetop5 = [10.355,40,25]
        self.basetop6 = [-10.355,40,25]
        self.basetop7 = [-25,40,10.355]
        self.basetop8 = [-25,40,-10.355]
        
        self.base1[0] = self.base1[0] + x # initializing x component for new x to be passed in 
        self.base2[0] = self.base2[0] + x
        self.base3[0] = self.base3[0] + x
        self.base4[0] = self.base4[0] + x
        self.base5[0] = self.base5[0] + x
        self.base6[0] = self.base6[0] + x
        self.base7[0] = self.base7[0] + x
        self.base8[0] = self.base8[0] + x
        self.basetop1[0] = self.basetop1[0] + x
        self.basetop2[0] = self.basetop2[0] + x
        self.basetop3[0] = self.basetop3[0] + x
        self.basetop4[0] = self.basetop4[0] + x
        self.basetop5[0] = self.basetop5[0] + x
        self.basetop6[0] = self.basetop6[0] + x
        self.basetop7[0] = self.basetop7[0] + x
        self.basetop8[0] = self.basetop8[0] + x
        
        self.base1[1] = self.base1[1] + y # initializes y component for new y
        self.base2[1] = self.base2[1] + y
        self.base3[1] = self.base3[1] + y
        self.base4[1] = self.base4[1] + y
        self.base5[1] = self.base5[1] + y # initializes y component for new y
        self.base6[1] = self.base6[1] + y
        self.base7[1] = self.base7[1] + y
        self.base8[1] = self.base8[1] + y
        self.basetop1[1] = self.basetop1[1] + y
        self.basetop2[1] = self.basetop2[1] + y
        self.basetop3[1] = self.basetop3[1] + y
        self.basetop4[1] = self.basetop4[1] + y
        self.basetop5[1] = self.basetop5[1] + y
        self.basetop6[1] = self.basetop6[1] + y
        self.basetop7[1] = self.basetop7[1] + y
        self.basetop8[1] = self.basetop8[1] + y
        
        self.base1[2] = self.base1[2] + z # initialize z component for new z
        self.base2[2] = self.base2[2] + z
        self.base3[2] = self.base3[2] + z
        self.base4[2] = self.base4[2] + z
        self.base5[2] = self.base5[2] + z # initialize z component for new z
        self.base6[2] = self.base6[2] + z
        self.base7[2] = self.base7[2] + z
        self.base8[2] = self.base8[2] + z
        self.basetop1[2] = self.basetop1[2] + z
        self.basetop2[2] = self.basetop2[2] + z
        self.basetop3[2] = self.basetop3[2] + z
        self.basetop4[2] = self.basetop4[2] + z
        self.basetop5[2] = self.basetop5[2] + z
        self.basetop6[2] = self.basetop6[2] + z
        self.basetop7[2] = self.basetop7[2] + z
        self.basetop8[2] = self.basetop8[2] + z
        
        self.poly1 = [self.base1, self.base2, self.basetop2, self.basetop1]
        self.poly2 = [self.base2, self.base3, self.basetop3, self.basetop2]
        self.poly3 = [self.base3, self.base4, self.basetop4, self.basetop3]
        self.poly4 = [self.base4, self.base5, self.basetop5, self.basetop4]
        self.poly5 = [self.base5, self.base6, self.basetop6, self.basetop5]
        self.poly6 = [self.base6, self.base7, self.basetop7, self.basetop6]
        self.poly7 = [self.base7, self.base8, self.basetop8, self.basetop7]
        self.poly8 = [self.base8, self.base1, self.basetop1, self.basetop8]
        
        # Definition of the object
        self.Base = [self.poly1, self.poly2, self.poly3, self.poly4, self.poly5, self.poly6, self.poly7, self.poly8]

        # Definition of the Pyramid's underlying point cloud.  No structure, just the points.
        self.PointCloud = [self.base1, self.base2, self.base3, self.base4, self.base5, self.base6, self.base7, self.base8, self.basetop1, self.basetop2, self.basetop3, self.basetop4, self.basetop5, self.basetop6, self.basetop7, self.basetop8]

Pyramid1 = Pyramid(1500, 100, 0) # creating new pyramid
Pyramid2 = Pyramid(-500, 150, 50)
Cube1 = Cube(1000, -50, 0) # creating new cube
Cube2 = Cube(-1000, -75, -50)
Octagon1 = Octagon(0, 0, 0)

Objects = [Pyramid1, Pyramid2, Cube1, Cube2, Octagon1] # list used to cycle through objects
x = 4
curr_object = Objects[x]

center = 0
# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PointCloud

# this function transforms the pyramid to its original size, shape and location.
def resetPyramid1():
    # Accesses the PointCloud array.
    # The first [] is used to access the elements in 'PointCloud' (apex, base1...)
    # The second [] is used to access the elements within apex, base1, base2... which are integers (0, 50, 100)
    
    Pyramid1.PointCloud[0][0] = 200
    Pyramid1.PointCloud[0][1] = 150
    Pyramid1.PointCloud[0][2] = 100
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Pyramid1.PointCloud[1][0] = 150
    Pyramid1.PointCloud[1][1] = 50
    Pyramid1.PointCloud[1][2] = 50
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Pyramid1.PointCloud[2][0] = 250
    Pyramid1.PointCloud[2][1] = 50
    Pyramid1.PointCloud[2][2] = 50
    
    # [3] accesses the fourth element in 'PointCloud' (base3) followed by [] for each element in base3
    Pyramid1.PointCloud[3][0] = 250
    Pyramid1.PointCloud[3][1] = 50
    Pyramid1.PointCloud[3][2] = 150
    
    # [4] accesses the second element in 'PointCloud' (base4) followed by [] for each element in base4
    Pyramid1.PointCloud[4][0] = 150
    Pyramid1.PointCloud[4][1] = 50
    Pyramid1.PointCloud[4][2] = 150


def resetPyramid2(): 
    # Accesses the PointCloud array.
    # The first [] is used to access the elements in 'PointCloud' (apex, base1...)
    # The second [] is used to access the elements within apex, base1, base2... which are integers (0, 50, 100)
    
    Pyramid2.PointCloud[0][0] = 50
    Pyramid2.PointCloud[0][1] = 300
    Pyramid2.PointCloud[0][2] = 150
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Pyramid2.PointCloud[1][0] = 0
    Pyramid2.PointCloud[1][1] = 200
    Pyramid2.PointCloud[1][2] = 100
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Pyramid2.PointCloud[2][0] = 100
    Pyramid2.PointCloud[2][1] = 200
    Pyramid2.PointCloud[2][2] = 100
    
    # [3] accesses the fourth element in 'PointCloud' (base3) followed by [] for each element in base3
    Pyramid2.PointCloud[3][0] = 100
    Pyramid2.PointCloud[3][1] = 200
    Pyramid2.PointCloud[3][2] = 200
    
    # [4] accesses the second element in 'PointCloud' (base4) followed by [] for each element in base4
    Pyramid2.PointCloud[4][0] = 0
    Pyramid2.PointCloud[4][1] = 200
    Pyramid2.PointCloud[4][2] = 200

def resetCube1():
    # Accesses the PointCloud array.
    # The first [] is used to access the elements in 'PointCloud' (apex, base1...)
    # The second [] is used to access the elements within apex, base1, base2... which are integers (0, 50, 100)
    
    Cube1.PointCloud[0][0] = 50
    Cube1.PointCloud[0][1] = -100
    Cube1.PointCloud[0][2] = -50
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Cube1.PointCloud[1][0] = 150
    Cube1.PointCloud[1][1] = -100
    Cube1.PointCloud[1][2] = -50
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Cube1.PointCloud[2][0] = 150
    Cube1.PointCloud[2][1] = -100
    Cube1.PointCloud[2][2] = 50
    
    # [3] accesses the fourth element in 'PointCloud' (base3) followed by [] for each element in base3
    Cube1.PointCloud[3][0] = 50
    Cube1.PointCloud[3][1] = -100
    Cube1.PointCloud[3][2] = 50
    
    # [4] accesses the second element in 'PointCloud' (base4) followed by [] for each element in base4
    Cube1.PointCloud[4][0] = 50
    Cube1.PointCloud[4][1] = 0
    Cube1.PointCloud[4][2] = -50
    
    Cube1.PointCloud[5][0] = 150
    Cube1.PointCloud[5][1] = 0
    Cube1.PointCloud[5][2] = -50
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Cube1.PointCloud[6][0] = 150
    Cube1.PointCloud[6][1] = 0
    Cube1.PointCloud[6][2] = 50
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Cube1.PointCloud[7][0] = 50
    Cube1.PointCloud[7][1] = 0
    Cube1.PointCloud[7][2] = 50
    
def resetCube2():
    # Accesses the PointCloud array.
    # The first [] is used to access the elements in 'PointCloud' (apex, base1...)
    # The second [] is used to access the elements within apex, base1, base2... which are integers (0, 50, 100)
    
    Cube2.PointCloud[0][0] = -200
    Cube2.PointCloud[0][1] = -125
    Cube2.PointCloud[0][2] = -100
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Cube2.PointCloud[1][0] = -100
    Cube2.PointCloud[1][1] = -125
    Cube2.PointCloud[1][2] = -100
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Cube2.PointCloud[2][0] = -100
    Cube2.PointCloud[2][1] = -125
    Cube2.PointCloud[2][2] = 0
    
    # [3] accesses the fourth element in 'PointCloud' (base3) followed by [] for each element in base3
    Cube2.PointCloud[3][0] = -200
    Cube2.PointCloud[3][1] = -125
    Cube2.PointCloud[3][2] = 0
    
    # [4] accesses the second element in 'PointCloud' (base4) followed by [] for each element in base4
    Cube2.PointCloud[4][0] = -200
    Cube2.PointCloud[4][1] = -25
    Cube2.PointCloud[4][2] = -100
    
    Cube2.PointCloud[5][0] = -100
    Cube2.PointCloud[5][1] = -25
    Cube2.PointCloud[5][2] = -100
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Cube2.PointCloud[6][0] = -100
    Cube2.PointCloud[6][1] = -25
    Cube2.PointCloud[6][2] = 0
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Cube2.PointCloud[7][0] = -200
    Cube2.PointCloud[7][1] = -25
    Cube2.PointCloud[7][2] = 0

def resetOctagon1():
    
    Octagon1.PointCloud[0][0] = -10.355
    Octagon1.PointCloud[0][1] = -40
    Octagon1.PointCloud[0][2] = -25
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base2
    Octagon1.PointCloud[1][0] = 10.355
    Octagon1.PointCloud[1][1] = -40
    Octagon1.PointCloud[1][2] = -25
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base3
    Octagon1.PointCloud[2][0] = 25
    Octagon1.PointCloud[2][1] = -40
    Octagon1.PointCloud[2][2] = -10.355
    
    # [3] accesses the fourth element in 'PointCloud' (base3) followed by [] for each element in base4
    Octagon1.PointCloud[3][0] = 25
    Octagon1.PointCloud[3][1] = -40
    Octagon1.PointCloud[3][2] = 10.355
    
    # [4] accesses the second element in 'PointCloud' (base4) followed by [] for each element in base4
    Octagon1.PointCloud[4][0] = 10.355
    Octagon1.PointCloud[4][1] = -40
    Octagon1.PointCloud[4][2] = 25
    
    Octagon1.PointCloud[5][0] = -10.355
    Octagon1.PointCloud[5][1] = -40
    Octagon1.PointCloud[5][2] = 25
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Octagon1.PointCloud[6][0] = -25
    Octagon1.PointCloud[6][1] = -40
    Octagon1.PointCloud[6][2] = 10.355
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Octagon1.PointCloud[7][0] = -25
    Octagon1.PointCloud[7][1] = -40
    Octagon1.PointCloud[7][2] = -10.355
    
    Octagon1.PointCloud[8][0] = -10.355
    Octagon1.PointCloud[8][1] = 40
    Octagon1.PointCloud[8][2] = -25
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Octagon1.PointCloud[9][0] = 10.355
    Octagon1.PointCloud[9][1] = 40
    Octagon1.PointCloud[9][2] = -25
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Octagon1.PointCloud[10][0] = 25
    Octagon1.PointCloud[10][1] = 40
    Octagon1.PointCloud[10][2] = -10.355
    
    # [3] accesses the fourth element in 'PointCloud' (base3) followed by [] for each element in base3
    Octagon1.PointCloud[11][0] = 25
    Octagon1.PointCloud[11][1] = 40
    Octagon1.PointCloud[11][2] = 10.355
    
    # [4] accesses the second element in 'PointCloud' (base4) followed by [] for each element in base4
    Octagon1.PointCloud[12][0] = 10.355
    Octagon1.PointCloud[12][1] = 40
    Octagon1.PointCloud[12][2] = 25
    
    Octagon1.PointCloud[13][0] = -10.355
    Octagon1.PointCloud[13][1] = 40
    Octagon1.PointCloud[13][2] = 25
    
    # [1] accesses the second element in 'PointCloud' (base1) followed by [] for each element in base1
    Octagon1.PointCloud[14][0] = -25
    Octagon1.PointCloud[14][1] = 40
    Octagon1.PointCloud[14][2] = 10.355
    
    # [2] accesses the third element in 'PointCloud' (base2) followed by [] for each element in base2
    Octagon1.PointCloud[15][0] = -25
    Octagon1.PointCloud[15][1] = 40
    Octagon1.PointCloud[15][2] = -10.355


# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.


# this function moves the object's location without changing the object's shape or size
def translate(object, displacement):
    
    s = 0 # set counter for primary element
    for a in object:  # iterates 'a' for the number of elements in the object
        i = 0 # set counter for secondary element
        for x in a: # iterates 'x' for each element in 'a' 
            object[s][i] = displacement[i] + a[i] # accesses the ith element in the current iteration of 's'. adds the displacement to the ith element
            i = i + 1 # increments counter to scroll through elements
        s = s + 1 # increments counter to scroll through elements

    
# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.

def key_in(event): # runs function when each key is input

    global curr_object
    global fil
    global bfc
    global buf
    global faceted
    global gourard
    global phong
    global light
    
    if event.keysym == '5': # '1' key is pressed
        curr_object = Objects[0]
    elif event.keysym == '2': # '2' key is pressed
        curr_object = Objects[1]
    elif event.keysym == '3': # '3' key is pressed
        curr_object = Objects[2]
    elif event.keysym == '4': # '4' key is pressed
        curr_object = Objects[3]
    elif event.keysym == '1': # '4' key is pressed
        curr_object = Objects[4]
    elif event.keysym == 'f': # 'f' key is pressed
        if fil == 0:
            fil = 1
        else:
            fil = 0
    elif event.keysym == 'b': # 'f' key is pressed
        if bfc == 0:
            bfc = 1
        else:
            bfc = 0
    elif event.keysym == 'z': # 'f' key is pressed
        if buf == 0:
            buf = 1
        else:
            buf = 0
    elif event.keysym =='q': # if 'q' is pressed
        if faceted == 0:
            faceted = 1
            gourard = 0
            phong = 0
            print("facet on")
        else:
            faceted = 0
            print("facet off")
    
    elif event.keysym =='w': # if 'w' is pressed
        if gourard == 0:
            faceted = 0
            gourard = 1
            phong = 0
            print("gourard on")
        else:
            gourard = 0
            print("gourard off")
            
    elif event.keysym =='e': # if 'e' is pressed
        if phong == 0:
            faceted = 0
            gourard = 0
            phong = 1
            print("phong on")
        else:
            phong = 0
            print("phong off")
            
    elif event.keysym =='l': # if 'q' is pressed
        if light == 0:
            light = 0
            light = light + 1
            print("ambient")
        elif light == 1:
            light = 1
            light = light + 1
            print("ambiet + point diffuse")
        elif light == 2:
            light = 2
            light = 0
            print("ambient + point diffuse + specular diffuse")    
            

    w.delete(ALL) # redraw so color changes when object is selected
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)
    
def surface_norm(poly): # calculates the surface normal of a poly
    vector1 = poly[2]
    vector2 = poly[1] # assings poly to vectors 
    vector3 = poly[0]
        
    A = vector2[0] - vector1[0]# find the points to perform backface culling
    B = vector2[1] - vector1[1]# find the points to perform backface culling
    C = vector2[2] - vector1[2]# find the points to perform backface culling
    
    a = vector3[0] - vector1[0]# find the points to perform backface culling
    b = vector3[1] - vector1[1]# find the points to perform backface culling
    c = vector3[2] - vector1[2]# find the points to perform backface culling
    
    point1 = [A, B, C] # one of two points for dot product
    point2 = [a, b, c] # second point set for dot product
    
    cx = (point1[1] * point2[2]) - (point1[2] * point2[1]) # dot product formula
    cy = (point1[2] * point2[0]) - (point1[0] * point2[2]) # dot porduct formula
    cz = (point1[0] * point2[1]) - (point1[1] * point2[0]) # dot product formula
    
    normal = (cx * vector1[0]) + (cy * vector1[1]) + (cz * vector1[2]) # implements the xyz dot product
    
    normalx = (cx * vector1[0]) # finds normal for x component
    normaly = (cy * vector1[1]) # finds normal for x component
    normalz = (cz * vector1[2]) # finds normal for x component
    
    return normalx, normaly, normalz # returns the values to the function
        
def backface_removal(poly): # implements the back face culling
    if len(poly) == 3: # does the formula for any poly with 3 points
        vector1 = poly[2] # assigning vector to each poly
        vector2 = poly[1]
        vector3 = poly[0]
    else: # does back face formula for poly with more than 3 points
        vector1 = poly[3]
        vector2 = poly[1] # assings poly to vectors 
        vector3 = poly[0]
    
    A = vector2[0] - vector1[0] # find the points to perform backface culling
    B = vector2[1] - vector1[1]# find the points to perform backface culling
    C = vector2[2] - vector1[2]# find the points to perform backface culling
    
    a = vector3[0] - vector1[0]# find the points to perform backface culling
    b = vector3[1] - vector1[1]# find the points to perform backface culling
    c = vector3[2] - vector1[2]# find the points to perform backface culling
    
    point1 = [A, B, C] # one of two points for dot product
    point2 = [a, b, c] # second point set for dot product
    
    cx = (point1[1] * point2[2]) - (point1[2] * point2[1]) # dot product formula
    cy = (point1[2] * point2[0]) - (point1[0] * point2[2]) # dot porduct formula
    cz = (point1[0] * point2[1]) - (point1[1] * point2[0]) # dot product formula
    
    D1 = (cx * vector1[0]) + (cy * vector1[1]) + (cz * vector1[2]) # implements the xyz dot product
    v3 = (cz * (-d)) # points are (0, 0, -d)
    visible = ((v3) - D1) # visible point

    
    if (visible > 0): # if condition to draw poly
        return 1
        
    else:
        return 0

def fill(poly): # function that defines the fill algorithm
    global buf
    if len(poly) == 3: # perform fill for any poly with 3 points
        p1 = project(poly[0]) # project point
        p2 = project(poly[1])# project point
        p3 = project(poly[2])# project point
        
        P1 = convertToDisplayCoordinates(p1) # convert point
        P2 = convertToDisplayCoordinates(p2) # convert point
        P3 = convertToDisplayCoordinates(p3) # convert point
        q = p1[2]
        if buf == 1:
            za1 = p1[2] + ((p2[2]-p1[2])/(p2[1]-p1[1])) # calculates z points
            
            xa1 = p1[0] + ((p2[0]-p1[0])/(p2[1]-p1[1])) # calculates z points
                
            zb1 = p1[2] + ((p3[2]-p1[2])/(p3[1]-p1[1])) # calculates z points
            
            xb1 = p1[0] + ((p3[0]-p1[0])/(p3[1]-p1[1])) # calculates z points
            
            za1b1 = za1 + ((zb1 - za1)/(xb1 - xa1)) # calculates z points
            
        
        else:
            za1b1 = 0
            q = 1
        
        
        if P1[1] < P2[1] and P1[1] < P3[1]: # find smallest Y in vertex
            Ymin = P1[1]
            Xmin = P1[0]
            if P2[1] < P3[1]: # if statement for finding the max/middle
                Ymid = P2[1] # calculating min/max
                Ymax = P3[1]# calculating min/max
                Xmid = P2[0]# calculating min/max
                Xmax = P3[0]# calculating min/max
                
                edge1 = (P1, P2) # assigns points to edges
                edge2 = (P1, P3) # assigns points to edges
                edge3 = (P2, P3) # assigns points to edges
            else: # if statement for finding the max/middle
                Ymid = P3[1]# calculating min/max
                Ymax = P2[1]# calculating min/max
                Xmid = P3[0]# calculating min/max
                Xmax = P2[0]# calculating min/max
                
                edge1 = (P1, P3) # assigns points to edges
                edge2 = (P1, P2) # assigns points to edges
                edge3 = (P3, P2) # assigns points to edges
            
        elif P2[1] < P3[1] and P2[1] < P1[1]: # if statement for finding the max/middle/min
            Ymin = P2[1]
            Xmin = P2[0]
            if P1[1] < P3[1]:
                Ymid = P1[1]# calculating min/max
                Ymax = P3[1]
                Xmid = P1[0]# calculating min/max
                Xmax = P3[0]
                
                edge1 = (P2, P1) # assigns points to edges
                edge2 = (P2, P3) # assigns points to edges
                edge3 = (P1, P3) # assigns points to edges
                
            else:
                Ymid = P3[1]# calculating min/max
                Ymax = P1[1]
                Xmid = P3[0]# calculating min/max
                Xmax = P1[0]
                
                edge1 = (P2, P3) # assigns points to edges
                edge2 = (P2, P1) # assigns points to edges
                edge3 = (P3, P1) # assigns points to edges
                
        elif P3[1] < P2[1] and P3[1] < P1[1]:
            Ymin = P3[1]
            Xmin = P3[0]
            if P2[1] < P1[1]:
                Ymid = P2[1]
                Ymax = P1[1]# calculating min/max
                Xmid = P2[0]
                Xmax = P1[0]# calculating min/max
                
                edge1 = (P3, P2) # assigns points to edges
                edge2 = (P3, P1) # assigns points to edges
                edge3 = (P2, P1) # assigns points to edges
                
            else:
                Ymid = P1[1]
                Ymax = P2[1]# calculating min/max
                Xmid = P1[0]
                Xmax = P2[0]# calculating min/max
                
                edge1 = (P3, P1) # assigns points to edges
                edge2 = (P3, P2) # assigns points to edges
                edge3 = (P1, P2) # assigns points to edges
                
        InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # finds the inverse slope
        InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1]) # finds the inverse slope
        
        edge1x = edge1[0][0] # initializing edges
        edge2x = edge2[0][0]
        
        for i in range(int(Ymin), int(Ymax)): # for loop to draw each line
            for a in range(int(edge1x), int(edge2x)):
                w.create_line(a, i, a+1, i+1, fill = "green") # create line between points
            edge1x = edge1x + InvSlope1 # update edge value
            edge2x = edge2x + InvSlope2
            if i > edge1[1][1]:
                edge1x = edge2[0][0] # select next point
            if i > edge2[1][1]:
                edge2x = edge3[0][0] # select next point
                
            
    else:
        p1 = project(poly[0]) # convert
        p2 = project(poly[1]) # convert
        p3 = project(poly[2]) # convert
        p4 = project(poly[3]) # convert
        
        P1 = convertToDisplayCoordinates(p1) # project
        P2 = convertToDisplayCoordinates(p2) # project
        P3 = convertToDisplayCoordinates(p3) # project
        P4 = convertToDisplayCoordinates(p4) # project
        
        sumx = 0
        sumy = 0
        sumz = 0
        
        pixel = "blue"
        if faceted == 1 and gourard == 0 and phong == 0: # faceted shading setup
           
            if light == 0: # ambient lighting setup
                Ir = Kd * Ia[0] # finds the intensity of red
                Ig = Kd * Ia[1] # finds the intensity of green
                Ib = Kd * Ia[2] # finds the intensity of blue
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
                
            elif light == 1:
                Ir = Ia[0] * Kd + Ip * Kd * (math.cos(t)) / d # ambient + emitted diffuse intensity for red
                Ig = Ia[1] * Kd + Ip * Kd * (math.cos(t)) / d # ambient + emitted diffuse intensity for green
                Ib = Ia[2] * Kd + Ip * Kd * (math.cos(t)) / d # ambient + emitted diffuse intensity for blue
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
            elif light == 2:
                pass
        
        elif faceted == 0 and gourard == 1 and phong == 0: # gourard shading setup
            normalx, normaly, normalz = surface_norm(poly) # calls the surface_norm() funtion to calculate normals
            for x in poly: # cycles through each poly
                sumx = sumx + normalx # calculates vertex sums
                sumy = sumy + normaly # calculates vertex sums
                sumz = sumz + normalz # calculates vertex sums
            
            mag = (((sumx**(.5)) + (sumy**(.5)) + (sumz**(.5)))**(0.5) + 1) # formula for magnitude
            vertex_normx = sumx/mag # formulates the vertex normals
            vertex_normy = sumy/mag # formulates the vertex normals
            vertex_normz = sumz/mag # formulates the vertex normals
            
            if light == 0: # ambient lighting setup
                Ir = Kd * Ia[0] # finds the intensity of red
                Ig = Kd * Ia[1] # finds the intensity of green
                Ib = Kd * Ia[2] # finds the intensity of blue
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
            
            elif light == 1: # ambient + point diffuse lighting
                n = 1
                Ir = Ia[0] * Kd + Ip * Kd * (math.cos(t)**n) / d # ambient + emitted diffuse intensity for red
                Ig = Ia[1] * Kd + Ip * Kd * (math.cos(t)**n) / d # ambient + emitted diffuse intensity for green
                Ib = Ia[2] * Kd + Ip * Kd * (math.cos(t)**n) / d # ambient + emitted diffuse intensity for blue
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
             
            elif light == 2: # ambient + point diffuse + point specular
                pass
        
        elif faceted == 0 and gourard == 0 and phong == 1: # phong shading setup
            normalx, normaly, normalz = surface_norm(poly) # calls the surface_norm() funtion to calculate normals
            for x in poly: # cycles through each poly
                sumx = sumx + normalx # calculates vertex sums
                sumy = sumy + normaly # calculates vertex sums
                sumz = sumz + normalz # calculates vertex sums
            
            mag = (((sumx**(.5)) + (sumy**(.5)) + (sumz**(.5)))**(0.5) + 1) # formula for magnitude
            vertex_normx = sumx/mag # formulates the vertex normals
            vertex_normy = sumy/mag # formulates the vertex normals
            vertex_normz = sumz/mag # formulates the vertex normals
            
            if light == 0: # ambient lighting setup
                Ir = Kd * Ia[0] # finds the intensity of red
                Ig = Kd * Ia[1] # finds the intensity of green
                Ib = Kd * Ia[2] # finds the intensity of blue
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
            
            elif light == 1: # ambient + point diffuse lighting
                Ir = Ia[0] * Kd + Ip * Kd * (math.cos(t)) / d # ambient + emitted diffuse intensity for red
                Ig = Ia[1] * Kd + Ip * Kd * (math.cos(t)) / d # ambient + emitted diffuse intensity for green
                Ib = Ia[2] * Kd + Ip * Kd * (math.cos(t)) / d # ambient + emitted diffuse intensity for blue
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
            
            elif light == 2: # ambient + point diffuse + point specular
                Ir = (Kd * Ia[0]) + (Ia[0] * Kd + Ip * Kd * (math.cos(t)) / d) + (Ip * Kd * (math.cos(t))) # Calculate RGB values for R
                Ig = (Kd * Ia[1]) + (Ia[1] * Kd + Ip * Kd * (math.cos(t)) / d) + (Ip * Kd * (math.cos(t))) # Calculate RGB values for R
                Ib = (Kd * Ia[2]) + (Ia[2] * Kd + Ip * Kd * (math.cos(t)) / d) + (Ip * Kd * (math.cos(t))) # Calculate RGB values for R
                
                pixel = '#%02x%02x%02x' % (int(Ir), int(Ig), int(Ib)) # creates the pixel with the specified hex code
            
        if P1[1] < P2[1] and P1[1] < P3[1] and P1[1] < P4[1]: # find smallest Y in vertex
            Ymin = P1[1]
            Xmin = P1[0]
            if P2[1] < P3[1] and P2[1] < P4[1]: # if to find the min/mid/max
                
                Ymid1 = P2[1]
                Xmid1 = P2[0]
                
                if P3[1] < P4[1]: # if to find the min/mid/max
                    Ymid2 = P3[1]
                    Xmid2 = P3[0]# calculating min/max
                    Ymax = P4[1]
                    Xmax = P4[0]# calculating min/max
                    
                    edge1 = (P1, P2)# assigngs point to edge
                    edge2 = (P1, P3)# assigngs point to edge
                    edge3 = (P3, P4)# assigngs point to edge
                    edge4 = (P2, P4)# assigngs point to edge
            
                    
                else:
                    Ymid2 = P4[1]
                    Xmid2 = P4[0]# calculating min/max
                    Ymax = P3[1]# calculating min/max
                    Xmax = P3[0]# calculating min/max
                
                    edge1 = (P1, P2)# assigngs point to edge
                    edge2 = (P1, P4)# assigngs point to edge
                    edge3 = (P4, P3)# assigngs point to edge
                    edge4 = (P2, P3)# assigngs point to edge
                    
                
            elif P3[1] < P2[1] and P3[1] < P4[1]: # if to find the min/mid/max
                Ymid1 = P3[1]
                Xmid1 = P3[0]
                if P2[1] < P4[1]: # if to find the min/mid/max
                    Ymid2 = P2[1]# calculating min/max
                    Xmid2 = P2[0]
                    Ymax = P4[1]# calculating min/max
                    Xmax = P4[0]
                            
                    edge1 = (P1, P3)# assigngs point to edge
                    edge2 = (P1, P2)# assigngs point to edge
                    edge3 = (P2, P4)# assigngs point to edge
                    edge4 = (P3, P4)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P4[1]# calculating min/max
                    Xmid2 = P4[0]
                    Ymax = P2[1]
                    Xmax = P2[0]# calculating min/max
                            
                    edge1 = (P1, P3)# assigngs point to edge
                    edge2 = (P1, P4)# assigngs point to edge
                    edge3 = (P4, P2)# assigngs point to edge
                    edge4 = (P3, P2)# assigngs point to edge
                    
                   
            elif P4[1] < P2[1] and P4[1] < P3[1]: # if to find the min/mid/max
                Ymid1 = P4[1]
                Xmid1 = P4[0]
                if P2[1] < P3[1]: # if to find the min/mid/max
                    Ymid2 = P2[1]# calculating min/max
                    Xmid2 = P2[0]
                    Ymax = P3[1]# calculating min/max
                    Xmax = P3[0]
                            
                    edge1 = (P1, P4)# assigngs point to edge
                    edge2 = (P1, P2)# assigngs point to edge
                    edge3 = (P2, P3)# assigngs point to edge
                    edge4 = (P4, P3)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P3[1]
                    Xmid2 = P3[0]# calculating min/max
                    Ymax = P2[1]# calculating min/max
                    Xmax = P2[0]
                            
                    edge1 = (P1, P4)# assigngs point to edge
                    edge2 = (P1, P3)# assigngs point to edge
                    edge3 = (P3, P2)# assigngs point to edge
                    edge4 = (P4, P2)# assigngs point to edge
            
            InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
            InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1]) # calculates inv slope
            InvSlope3 = (edge3[1][0] - edge3[0][0])/(edge3[1][1] - edge3[0][1]) # calculates inv slope
            InvSlope4 = (edge4[1][0] - edge4[0][0])/(edge4[1][1] - edge4[0][1]) # calculates inv slope
                
            edge1x = edge1[0][0]# assign edges
            edge2x = edge2[0][0]
            edge3x = edge3[0][0]# assign edges
            edge4x = edge4[0][0]
                    
                
            
            for i in range(int(Ymin), int(Ymax)):
                for x in range(int(edge1x), int(edge2x)):
                    w.create_oval(x, i, x, i, outline = pixel, fill = pixel, width = 1)
                
                edge1x = edge1x + InvSlope1
                edge2x = edge2x + InvSlope2# updates edges
              
                if i > edge1[1][1]:
                    edge1 = edge3 #increments edges
                    edge1x = edge1[0][0]# assign edges
                    InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
                if i > edge2[1][1]:
                    edge2 = edge4
                    edge2x = edge2[0][0]# assign edges
                    InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1]) # calculates inv slope

                    
           
        elif P2[1] < P3[1] and P2[1] < P1[1] and P2[1] < P4[1]: # if to find the min/mid/max
            Ymin = P2[1]
            Xmin = P2[0]

            if P1[1] < P3[1] and P1[1] < P4[1]:# if to find the min/mid/max
                Ymid1 = P1[1]
                Xmid1 = P1[0]
                if P3[1] < P4[1]: # if statement to calculate min/max
                    Ymid2 = P3[1]
                    Xmid2 = P3[0]# calculating min/max
                    Ymax = P4[1]# calculating min/max
                    Xmax = P4[0]# calculating min/max
                    
                    edge1 = (P2, P1)# assigngs point to edge
                    edge2 = (P2, P3)# assigngs point to edge
                    edge3 = (P3, P4)# assigngs point to edge
                    edge4 = (P1, P4)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P4[1]
                    Xmid2 = P4[0]# calculating min/max
                    Ymax = P3[1]# calculating min/max
                    Xmax = P3[0]# calculating min/max
                
                    edge1 = (P2, P1)# assigngs point to edge
                    edge2 = (P2, P4)# assigngs point to edge
                    edge3 = (P4, P3)# assigngs point to edge
                    edge4 = (P1, P3)# assigngs point to edge
                    
                    
            elif P3[1] < P1[1] and P3[1] < P4[1]: # if to find the min/mid/max
                Ymid1 = P3[1]
                Xmid1 = P3[0]
                if P1[1] < P4[1]:# if to find the min/mid/max
                    Ymid2 = P1[1]
                    Xmid2 = P1[0]# calculating min/max
                    Ymax = P4[1]# calculating min/max
                    Xmax = P4[0]# calculating min/max
                            
                    edge1 = (P2, P3)# assigngs point to edge
                    edge2 = (P2, P1)# assigngs point to edge
                    edge3 = (P1, P4)# assigngs point to edge
                    edge4 = (P3, P4)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P4[1]
                    Xmid2 = P4[0]# calculating min/max
                    Ymax = P1[1]# calculating min/max
                    Xmax = P1[0]
                            
                    edge1 = (P2, P3)# assigngs point to edge
                    edge2 = (P2, P4)# assigngs point to edge
                    edge3 = (P4, P1)# assigngs point to edge
                    edge4 = (P3, P1)# assigngs point to edge
                    
                    
            elif P4[1] < P1[1] and P4[1] < P3[1]: # if to find the min/mid/max
                Ymid1 = P4[1]
                Xmid1 = P4[0]
                if P1[1] < P3[1]: # if to find the min/mid/max
                    Ymid2 = P1[1]
                    Xmid2 = P1[0]# calculating min/max
                    Ymax = P3[1]# calculating min/max
                    Xmax = P3[0]
                            
                    edge1 = (P2, P4)# assigngs point to edge
                    edge2 = (P2, P1)# assigngs point to edge
                    edge3 = (P1, P3)# assigngs point to edge
                    edge4 = (P4, P3)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P3[1]
                    Xmid2 = P3[0]# calculating min/max
                    Ymax = P1[1]
                    Xmax = P1[0]# calculating min/max
                            
                    edge1 = (P2, P4)# assigngs point to edge
                    edge2 = (P2, P3)# assigngs point to edge
                    edge3 = (P3, P1)# assigngs point to edge
                    edge4 = (P4, P1)# assigngs point to edge
            
            InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
            InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1])     # calculates inv slope
            InvSlope3 = (edge3[1][0] - edge3[0][0])/(edge3[1][1] - edge3[0][1]) # calculates inv slope
            InvSlope4 = (edge4[1][0] - edge4[0][0])/(edge4[1][1] - edge4[0][1]) # calculates inv slope
                
            edge1x = edge1[0][0]# assign edges
            edge2x = edge2[0][0]
            edge3x = edge3[0][0]# assign edges
            edge4x = edge4[0][0]
                    
                
            
            for i in range(int(Ymin), int(Ymax)):
                for x in range(int(edge1x), int(edge2x)):
                    w.create_oval(x, i, x, i, outline = pixel, fill = pixel, width = 1)
                
                edge1x = edge1x + InvSlope1
                edge2x = edge2x + InvSlope2# updates edges
              
                if i > edge1[1][1]:
                    edge1 = edge3 #increments edges
                    edge1x = edge1[0][0]# assign edges
                    InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
                if i > edge2[1][1]:
                    edge2 = edge4
                    edge2x = edge2[0][0]# assign edges
                    InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1])     # calculates inv slope
        
              
        elif P3[1] < P1[1] and P3[1] < P2[1] and P3[1] < P4[1]: # if to find the min/mid/max
            Ymin = P3[1]
            Xmin = P3[0]
            if P1[1] < P2[1] and P1[1] < P4[1]: # if to find the min/mid/max
                Ymid1 = P1[1]
                Xmid1 = P1[0]
                if P2[1] < P4[1]: # if to find the min/mid/max
                    Ymid2 = P2[1]
                    Xmid2 = P2[0]# calculating min/max
                    Ymax = P4[1]# calculating min/max
                    Xmax = P4[0]
                    
                    edge1 = (P3, P1)# assigngs point to edge
                    edge2 = (P3, P2)# assigngs point to edge
                    edge3 = (P2, P4)# assigngs point to edge
                    edge4 = (P1, P4)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P4[1]
                    Xmid2 = P4[0]# calculating min/max
                    Ymax = P2[1]
                    Xmax = P2[0]# calculating min/max
                
                    edge1 = (P3, P1)# assigngs point to edge
                    edge2 = (P3, P4)# assigngs point to edge
                    edge3 = (P4, P2)# assigngs point to edge
                    edge4 = (P1, P2)# assigngs point to edge
                    
                   
            elif P2[1] < P1[1] and P2[1] < P4[1]: # if to find the min/mid/max
                Ymid1 = P2[1]
                Xmid1 = P2[0]
                if P1[1] < P4[1]: # if to find the min/mid/max
                    Ymid2 = P1[1]# calculating min/max
                    Xmid2 = P1[0]
                    Ymax = P4[1]# calculating min/max
                    Xmax = P4[0]
                            
                    edge1 = (P3, P2)# assigngs point to edge
                    edge2 = (P3, P1)# assigngs point to edge
                    edge3 = (P1, P4)# assigngs point to edge
                    edge4 = (P2, P4)# assigngs point to edge
                    
                    
                    
                else:
                    Ymid2 = P4[1]
                    Xmid2 = P4[0]# calculating min/max
                    Ymax = P1[1]
                    Xmax = P1[0]# calculating min/max
                            
                    edge1 = (P3, P2)# assigngs point to edge
                    edge2 = (P3, P4)# assigngs point to edge
                    edge3 = (P4, P1)# assigngs point to edge
                    edge4 = (P2, P1)# assigngs point to edge
                    
                   
            elif P4[1] < P1[1] and P4[1] < P2[1]: # if to find the min/mid/max
                Ymid1 = P4[1]
                Xmid1 = P4[0]
                if P1[1] < P2[1]: # if to find the min/mid/max
                    Ymid2 = P1[1]
                    Xmid2 = P1[0]# calculating min/max
                    Ymax = P2[1]
                    Xmax = P2[0]# calculating min/max
                            
                    edge1 = (P3, P4)# assigngs point to edge
                    edge2 = (P3, P1)# assigngs point to edge
                    edge3 = (P1, P2)# assigngs point to edge
                    edge4 = (P4, P2)# assigngs point to edge
                    
                  
                    
                else:
                    Ymid2 = P2[1]
                    Xmid2 = P2[0]# calculating min/max
                    Ymax = P1[1]
                    Xmax = P1[0]# calculating min/max
                            
                    edge1 = (P3, P4)# assigngs point to edge
                    edge2 = (P3, P2)# assigngs point to edge
                    edge3 = (P2, P1)# assigngs point to edge
                    edge4 = (P4, P1)# assigngs point to edge
            
            InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
            InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1])     # calculates inv slope
            InvSlope3 = (edge3[1][0] - edge3[0][0])/(edge3[1][1] - edge3[0][1]) # calculates inv slope
            InvSlope4 = (edge4[1][0] - edge4[0][0])/(edge4[1][1] - edge4[0][1]) # calculates inv slope
                
            edge1x = edge1[0][0]# assign edges
            edge2x = edge2[0][0]
            edge3x = edge3[0][0]# assign edges
            edge4x = edge4[0][0]
                    
                
            
            for i in range(int(Ymin), int(Ymax)):
                for x in range(int(edge1x), int(edge2x)):
                    w.create_oval(x, i, x, i, outline = pixel, fill = pixel, width = 1)
                
                edge1x = edge1x + InvSlope1
                edge2x = edge2x + InvSlope2# updates edges
              
                if i > edge1[1][1]:
                    edge1 = edge3 #increments edges
                    edge1x = edge1[0][0]# assign edges
                    InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
                if i > edge2[1][1]:
                    edge2 = edge4
                    edge2x = edge2[0][0]# assign edges
                    InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1])     # calculates inv slope

            
                    
        elif P4[1] < P3[1] and P4[1] < P1[1] and P4[1] < P2[1]: # if to find the min/mid/max
            Ymin = P4[1]
            Xmin = P4[0]
            if P1[1] < P3[1] and P1[1] < P2[1]: # if to find the min/mid/max
                Ymid1 = P1[1]
                Xmid1 = P1[0]
                if P3[1] < P2[1]: # if to find the min/mid/max
                    Ymid2 = P3[1]
                    Xmid2 = P3[0]# calculating min/max
                    Ymax = P2[1]# calculating min/max
                    Xmax = P2[0]
                    
                    edge1 = (P4, P1)# assigngs point to edge
                    edge2 = (P4, P3)# assigngs point to edge
                    edge3 = (P3, P2)# assigngs point to edge
                    edge4 = (P1, P2)# assigngs point to edge
                    
                    
                else:
                    Ymid2 = P2[1]
                    Xmid2 = P2[0]# calculating min/max
                    Ymax = P3[1]# calculating min/max
                    Xmax = P3[0]
                
                    edge1 = (P4, P1)# assigns point to edge
                    edge2 = (P4, P2)# assigns point to edge
                    edge3 = (P2, P3)# assigns point to edge
                    edge4 = (P1, P3)# assigns point to edge
                    
                    
            elif P3[1] < P1[1] and P3[1] < P2[1]: # if to find the min/mid/max
                Ymid1 = P3[1]
                Xmid1 = P3[0]
                if P1[1] < P2[1]: # if to find the min/mid/max
                    Ymid2 = P1[1]
                    Xmid2 = P1[0]
                    Ymax = P2[1]# calculating min/max
                    Xmax = P2[0]# calculating min/max
                            
                    edge1 = (P4, P3)# assigngs point to edge
                    edge2 = (P4, P1)# assigngs point to edge
                    edge3 = (P1, P2)# assigngs point to edge
                    edge4 = (P3, P2)# assigngs point to edge
                    
                            
                else:
                    Ymid2 = P2[1]
                    Xmid2 = P2[0]# calculating min/max
                    Ymax = P1[1]
                    Xmax = P1[0]# calculating min/max
                            
                    edge1 = (P4, P3)# assigngs point to edge
                    edge2 = (P4, P2)# assigngs point to edge
                    edge3 = (P2, P1)# assigngs point to edge
                    edge4 = (P3, P1)# assigngs point to edge
                    
                    
            elif P2[1] < P1[1] and P2[1] < P3[1]: # if to find the min/mid/max
                Ymid1 = P2[1]
                Xmid1 = P2[0]
                if P1[1] < P3[1]: # if to find the min/mid/max
                    Ymid2 = P1[1]
                    Xmid2 = P1[0]# calculating min/max
                    Ymax = P3[1]
                    Xmax = P3[0]# calculating min/max
                            
                    edge1 = (P4, P2)# assigngs point to edge
                    edge2 = (P4, P1)# assigngs point to edge
                    edge3 = (P1, P3)# assigngs point to edge
                    edge4 = (P2, P3)# assigngs point to edge
                    
                    
                    
                else:
                    Ymid2 = P3[1]
                    Xmid2 = P3[0]# calculating min/max
                    Ymax = P1[1]
                    Xmax = P1[0]# calculating min/max
                            
                    edge1 = (P4, P2)# assigngs point to edge
                    edge2 = (P4, P3)# assigngs point to edge
                    edge3 = (P3, P1)# assigngs point to edge
                    edge4 = (P2, P1) # assigngs point to edge
                    
           
        
            InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
            InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1])     # calculates inv slope
            InvSlope3 = (edge3[1][0] - edge3[0][0])/(edge3[1][1] - edge3[0][1]) # calculates inv slope
            InvSlope4 = (edge4[1][0] - edge4[0][0])/(edge4[1][1] - edge4[0][1]) # calculates inv slope
                
            edge1x = edge1[0][0]# assign edges
            edge2x = edge2[0][0]
            edge3x = edge3[0][0]# assign edges
            edge4x = edge4[0][0]
                    
                
            
            for i in range(int(Ymin), int(Ymax)):
                for x in range(int(edge1x), int(edge2x)):
                    w.create_oval(x, i, x, i, outline = pixel, fill = pixel, width = 1)
                
                edge1x = edge1x + InvSlope1
                edge2x = edge2x + InvSlope2# updates edges
              
                if i > edge1[1][1]:
                    edge1 = edge3 #increments edges
                    edge1x = edge1[0][0]# assign edges
                    InvSlope1 = (edge1[1][0] - edge1[0][0])/(edge1[1][1] - edge1[0][1]) # calculates inv slope
                if i > edge2[1][1]:
                    edge2 = edge4
                    edge2x = edge2[0][0]# assign edges
                    InvSlope2 = (edge2[1][0] - edge2[0][0])/(edge2[1][1] - edge2[0][1])     # calculates inv slope

# changes the size of the object without changi,ng the location/shape
def scale(object, scalefactor):
    origin, neg_origin = Origin()
    translate(curr_object.PointCloud, neg_origin)
    s = 0 # initializes counter
    for a in object:  # iterates 'a' for the number of elements in the object
        i = 0 # initializes second counter
        for x in a: # iterates 'x' for each element in 'a'
            object[s][i] = scalefactor * a[i] # equation for scaling, multiplies ith element by scalefactor
            i = i + 1 # increments counter to scroll through elements
        s = s + 1 # increments counter to scroll through elements
    translate(curr_object.PointCloud, origin)

# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]

# rotates the object around the Z axis without changing size/shape
def rotateZ(object,degrees):
    origin, neg_origin = Origin() # calls the function
    translate(curr_object.PointCloud, neg_origin) # translates to origin
    
    degrees = (math.radians(degrees)) # converts degrees to radians
    s = 0 # initializes counter
    for a in object:
        
        x = ((math.cos(degrees) * a[0]) - (math.sin(degrees) * a[1])) # changes values for X using formula
        y = ((math.sin(degrees) * a[0]) + (math.cos(degrees) * a[1])) # changes values for Y using formula
        object[s][0] = x
        object[s][1] = y
        s = s + 1 # increments counter to scroll through elements
        
    translate(curr_object.PointCloud, origin)# translates back from origin
    
# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.

# rotates the object around the Y axis without changing size/shape
def rotateY(object,degrees):
    origin, neg_origin = Origin()
    translate(curr_object.PointCloud, neg_origin)# translates to origin
    
    degrees = (math.radians(degrees)) * -1 # radians to degrees. multiplied by -1 to rotate clockwise
    s = 0
    for a in object:
        x = ((math.cos(degrees) * a[0]) - (math.sin(degrees) * a[2])) # changes values for X using formula
        y = ((math.sin(degrees) * a[0]) + (math.cos(degrees) * a[2])) # changes values for Z using formula
        object[s][0] = x
        object[s][2] = y
        s = s + 1 # increments counter
    translate(curr_object.PointCloud, origin) # translates back from origin
# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.

# rotates the object around the Y axis without changing size/shape
def rotateX(object,degrees):
    origin, neg_origin = Origin() # calls the origin function to reference the center point
    translate(curr_object.PointCloud, neg_origin) # translates to origin
    degrees = (math.radians(degrees)) # degrees to radians
    s = 0
    for a in object:
        
        x = (math.cos(degrees) * a[1]) - (math.sin(degrees) * a[2]) # changes values for Y using formula
        y = (math.sin(degrees) * a[1]) + (math.cos(degrees) * a[2]) # changes values for Z using formula
         
        object[s][1] = x
        object[s][2] = y
        # increments counter
        s = s + 1
    translate(curr_object.PointCloud, origin) # translates back from origin

# finds the center point to translate to for in-place rotations
def Origin():
    if curr_object == Objects[0] or curr_object == Objects[1]: # applys to Pyramid 1 & 2
        i = 1
        origin_x = 0
        for a in curr_object.PointCloud: #items in the points cloud excluding apex
            if i <= 4:
                center_x = curr_object.PointCloud[i][0] 
                origin_x = center_x + origin_x # adds the x components
                i = i + 1 # increments counter
        origin_x = origin_x / (len(curr_object.PointCloud) - 1) # find the average
        origin_x = (origin_x + curr_object.PointCloud[0][0]) / 2 # Addes apex x and averages again
        
        b = 1
        origin_y = 0 # repeats the same process for y components
        for a in curr_object.PointCloud: # applys to the Cubes
            if b <= 4:
                center_y = curr_object.PointCloud[b][1]
                origin_y = center_y + origin_y
                b = b + 1
        origin_y = origin_y / (len(curr_object.PointCloud) - 1)
        origin_y = (origin_y + curr_object.PointCloud[0][1]) / 2
        
        r = 1 # repeats same process for z compontents
        origin_z = 0
        for a in curr_object.PointCloud:
            if r <= 4:
                center_z = curr_object.PointCloud[r][2]
                origin_z = center_z + origin_z
                r = r + 1
        origin_z = origin_z / (len(curr_object.PointCloud) - 1)
        origin_z = (origin_z + curr_object.PointCloud[0][2]) / 2
        origin = [origin_x, origin_y, origin_z]
        neg_origin = [-x for x in origin]
        return origin, neg_origin
   
    else: # finds average of all the x,y,z points of the cube
        i = 0 
        origin_x = 0
        for a in curr_object.PointCloud:
            center_x = curr_object.PointCloud[i][0]
            origin_x = center_x + origin_x
            i = i + 1
        origin_x = origin_x / len(curr_object.PointCloud)


        s = 0
        origin_y = 0
        for a in curr_object.PointCloud:
            center_y = curr_object.PointCloud[s][1]
            origin_y = center_y + origin_y
            s = s + 1
        origin_y = origin_y / len(curr_object.PointCloud)

        t = 0
        origin_z = 0
        for a in curr_object.PointCloud:
            center_z = curr_object.PointCloud[t][2]
            origin_z = center_z + origin_z
            t = t + 1
        origin_z = origin_z / len(curr_object.PointCloud)
        origin = [origin_x, origin_y, origin_z]
        neg_origin = [-x for x in origin]
        return origin, neg_origin


# The function will draw an object by repeatedly callying drawPoly on each polygon in the object
def drawObject(object):
    if curr_object.Base == object:
        i = 0
        for i in object:
            drawPoly(i, 'red') # draws frontpoly by calling drawPoly
    else:
        i = 0
        for i in object:
            drawPoly(i, 'black') # draws frontpoly by calling drawPoly


# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly, color):
    surface_norm(poly)
    if fil == 1:
        fill(poly)
    
    if bfc == 1:
        if backface_removal(poly) == 1:
            for a in range(len(poly) - 1):
                #backface_removal(poly)# iterates 'a' for the number of elements except the last in the object
                drawLine(poly[a], poly[a+1],color) # draws a line for each point (ie; 0 to 1, 1 to 2...)
            i = len(poly) - 1 # variable to find the one before the last element
            drawLine(poly[i], poly[0], color) # connects the final point to the initial point
    else:
        for a in range(len(poly) - 1):
            #backface_removal(poly)# iterates 'a' for the number of elements except the last in the object
            drawLine(poly[a], poly[a+1],color) # draws a line for each point (ie; 0 to 1, 1 to 2...)
        i = len(poly) - 1 # variable to find the one before the last element
        drawLine(poly[i], poly[0], color) # connects the final point to the initial point

        

# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start, end, color):

    startdisplay = convertToDisplayCoordinates(project(start)) # projects the first point and then converts to display coordinate
    #print(startdisplay)
    enddisplay = convertToDisplayCoordinates(project(end)) # projects the second point and then converts to display coordinate
    #print(enddisplay)
    
    w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1], fill = color) # creates the line
    
   
# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    ps = [] # creates array
    ps.append((d * point[0]) / (d + point[2])) # adds new X coordinates to empty array ps
    ps.append((d * point[1]) / (d + point[2])) # adds new Y coordinates to array ps
    ps.append(point[2] / (d + point[2])) # adds new Z coordinates to array ps
    return ps


# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    displayXY = []
    displayXY.append(point[0] + (CanvasWidth/2)) # changes the X axis to the center of tkinter canvas
    displayXY.append(((-1) * (point[1])) + (CanvasHeight/2)) # inverts the Y axis and centers it onto the canvas
    return displayXY
    


# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    #resetPyramid1()
    #resetPyramid2()
    #resetCube1()
    #resetCube2()
    resetOctagon1()
    drawObject(Pyramid1.Base)# redraw each object indiviually
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def larger():
    w.delete(ALL)
    scale(curr_object.PointCloud,1.1)
    drawObject(Pyramid1.Base) # redraw objects that werent changed as well
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def smaller():
    w.delete(ALL)
    scale(curr_object.PointCloud,.9) #scales to whichever object is selected
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def forward():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,0,5])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def backward():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,0,-5])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def left():
    w.delete(ALL)
    translate(curr_object.PointCloud,[-5,0,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def right():
    w.delete(ALL)
    translate(curr_object.PointCloud,[5,0,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def up():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,5,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def down():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,-5,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def xPlus():
    w.delete(ALL)
    rotateX(curr_object.PointCloud,5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def xMinus():
    w.delete(ALL)
    rotateX(curr_object.PointCloud,-5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def yPlus():
    w.delete(ALL)
    rotateY(curr_object.PointCloud,5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def yMinus():
    w.delete(ALL)
    rotateY(curr_object.PointCloud,-5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def zPlus():
    w.delete(ALL)
    rotateZ(curr_object.PointCloud,5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)

def zMinus():
    w.delete(ALL)
    rotateZ(curr_object.PointCloud,-5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject(Octagon1.Base)


root = Tk()
outerframe = Frame(root)
outerframe.pack()


w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight, bg = 'white')
drawObject(Pyramid1.Base)
drawObject(Pyramid2.Base)
drawObject(Cube1.Base)
drawObject(Cube2.Base)
drawObject(Octagon1.Base)
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="DN", command=down)
upButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

root.bind_all('<Key>', key_in)
root.mainloop()


