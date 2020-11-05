##################################################################################################
# Ammar Essajee
# Student ID: 102-43-821
# Date:1/8/2019
# Assignment #2
# This code allows the user to transform multiple objects on a canvas: rotate, scale, and translate (in-place).
##################################################################################################



import math
from tkinter import *

CanvasWidth = 600
CanvasHeight = 600
d = 500


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


Pyramid1 = Pyramid(200, 100, 0) # creating new pyramid
Pyramid2 = Pyramid(50, 250, 50)
Cube1 = Cube(100, -50, 0) # creating new cube
Cube2 = Cube(-150, -75, -50)

Objects = [Pyramid1, Pyramid2, Cube1, Cube2] # list used to cycle through objects
x = 0
curr_object = Objects[x]


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
    if event.keysym == '1': # '1' key is pressed
        curr_object = Objects[0]
    elif event.keysym == '2': # '2' key is pressed
        curr_object = Objects[1]
    elif event.keysym == '3': # '3' key is pressed
        curr_object = Objects[2]
    elif event.keysym == '4': # '4' key is pressed
        curr_object = Objects[3]
    
    w.delete(ALL) # redraw so color changes when object is selected
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)
    drawObject()

# changes the size of the object without changing the location/shape
def scale(object,scalefactor):
    
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

        drawPoly(object[1], 'yellow') # draws frontpoly by calling drawPoly
        drawPoly(object[2], 'yellow') # draws rightpoly by calling drawPoly
        drawPoly(object[3], 'yellow') # draws backpoly by calling drawPoly
        drawPoly(object[4], 'yellow') # draws leftpoly by calling drawPoly
        drawPoly(object[0], 'yellow') # draws bottompoly by calling drawPoly
    else:
        drawPoly(object[1], 'white') # draws frontpoly by calling drawPoly
        drawPoly(object[2], 'white') # draws rightpoly by calling drawPoly
        drawPoly(object[3], 'white') # draws backpoly by calling drawPoly
        drawPoly(object[4], 'white') # draws leftpoly by calling drawPoly
        drawPoly(object[0], 'white') # draws bottompoly by calling drawPoly


# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly, color):
    for a in range(len(poly) - 1): # iterates 'a' for the number of elements except the last in the object
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
    resetPyramid1()
    resetPyramid2()
    resetCube1()
    resetCube2()
    drawObject(Pyramid1.Base)# redraw each object indiviually
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def larger():
    w.delete(ALL)
    scale(curr_object.PointCloud,1.1)
    drawObject(Pyramid1.Base) # redraw objects that werent changed as well
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def smaller():
    w.delete(ALL)
    scale(curr_object.PointCloud,.9) #scales to whichever object is selected
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def forward():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,0,5])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def backward():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,0,-5])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def left():
    w.delete(ALL)
    translate(curr_object.PointCloud,[-5,0,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def right():
    w.delete(ALL)
    translate(curr_object.PointCloud,[5,0,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def up():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,5,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def down():
    w.delete(ALL)
    translate(curr_object.PointCloud,[0,-5,0])
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def xPlus():
    w.delete(ALL)
    rotateX(curr_object.PointCloud,5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def xMinus():
    w.delete(ALL)
    rotateX(curr_object.PointCloud,-5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def yPlus():
    w.delete(ALL)
    rotateY(curr_object.PointCloud,5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def yMinus():
    w.delete(ALL)
    rotateY(curr_object.PointCloud,-5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def zPlus():
    w.delete(ALL)
    rotateZ(curr_object.PointCloud,5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)

def zMinus():
    w.delete(ALL)
    rotateZ(curr_object.PointCloud,-5)
    drawObject(Pyramid1.Base)
    drawObject(Pyramid2.Base)
    drawObject(Cube1.Base)
    drawObject(Cube2.Base)


root = Tk()
outerframe = Frame(root)
outerframe.pack()


w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight, bg = 'turquoise')
drawObject(Pyramid1.Base)
drawObject(Pyramid2.Base)
drawObject(Cube1.Base)
drawObject(Cube2.Base)
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
