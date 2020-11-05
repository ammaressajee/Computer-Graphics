##################################################################################################
# Ammar Essajee
# Student ID: 102-43-821
# Date:12/18/2018
# Assignment #1
# This code allows the user to transform an object on a canvas: rotate, scale, and translate.
##################################################################################################



import math
from tkinter import *

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Pyramid Object ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [-50,-50,50]
base2 = [50,-50,50]
base3 = [50,-50,150]
base4 = [-50,-50,150]

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
frontpoly = [apex,base1,base2]
rightpoly = [apex,base2,base3]
backpoly = [apex,base3,base4]
leftpoly = [apex,base4,base1]
bottompoly = [base4,base3,base2,base1]

# Definition of the object
Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]

# Definition of the Pyramid's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4]
#************************************************************************************

# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud

# this function transforms the pyramid to its original size, shape and location.
def resetPyramid():
    # Accesses the PyramidPointCloud array.
    # The first [] is used to access the elements in 'PyramidPointCloud' (apex, base1...)
    # The second [] is used to access the elements within apex, base1, base2... which are integers (0, 50, 100)
    
    PyramidPointCloud[0][0] = 0
    PyramidPointCloud[0][1] = 50
    PyramidPointCloud[0][2] = 100
    
    # [1] accesses the second element in 'PyramidPointCloud' (base1) followed by [] for each element in base1
    PyramidPointCloud[1][0] = -50
    PyramidPointCloud[1][1] = -50
    PyramidPointCloud[1][2] = 50
    
    # [2] accesses the third element in 'PyramidPointCloud' (base2) followed by [] for each element in base2
    PyramidPointCloud[2][0] = 50
    PyramidPointCloud[2][1] = -50
    PyramidPointCloud[2][2] = 50
    
    # [3] accesses the fourth element in 'PyramidPointCloud' (base3) followed by [] for each element in base3
    PyramidPointCloud[3][0] = 50
    PyramidPointCloud[3][1] = -50
    PyramidPointCloud[3][2] = 150
    
    # [4] accesses the second element in 'PyramidPointCloud' (base4) followed by [] for each element in base4
    PyramidPointCloud[4][0] = -50
    PyramidPointCloud[4][1] = -50
    PyramidPointCloud[4][2] = 150


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

# changes the size of the object without changing the location/shape
def scale(object,scalefactor):
    
    s = 0 # initializes counter
    for a in object:  # iterates 'a' for the number of elements in the object
        i = 0 # initializes second counter
        for x in a: # iterates 'x' for each element in 'a'
            object[s][i] = scalefactor * a[i] # equation for scaling, multiplies ith element by scalefactor
            i = i + 1 # increments counter to scroll through elements
        s = s + 1 # increments counter to scroll through elements
        

# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]

# rotates the object around the Z axis without changing size/shape
def rotateZ(object,degrees):
    degrees = (math.radians(degrees)) # converts degrees to radians
    s = 0 # initializes counter
    for a in object: 
        object[s][0] = ((math.cos(degrees) * a[0]) - (math.sin(degrees) * a[1])) # changes values for X using formula 
        object[s][1] = ((math.sin(degrees) * a[0]) + (math.cos(degrees) * a[1])) # changes values for Y using formula
        s = s + 1 # increments counter to scroll through elements
    
# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.

# rotates the object around the Y axis without changing size/shape
def rotateY(object,degrees): 
    degrees = (math.radians(degrees)) * -1 # radians to degrees. multiplied by -1 to rotate clockwise
    s = 0
    for a in object:
        object[s][0] = ((math.cos(degrees) * a[0]) - (math.sin(degrees) * a[2])) # changes values for X using formula
        object[s][2] = ((math.sin(degrees) * a[0]) + (math.cos(degrees) * a[2])) # changes values for Z using formula
        s = s + 1 # increments counter

# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.

# rotates the object around the Y axis without changing size/shape
def rotateX(object,degrees):
    degrees = (math.radians(degrees)) # degrees to radians
    s = 0
    for a in object:
        object[s][1] = (math.cos(degrees) * a[1]) - (math.sin(degrees) * a[2]) # changes values for Y using formula
        object[s][2] = (math.sin(degrees) * a[1]) + (math.cos(degrees) * a[2]) # changes values for Z using formula
        s = s + 1 # increments counter
                

# The function will draw an object by repeatedly callying drawPoly on each polygon in the object
def drawObject(object):
    drawPoly(object[1]) # draws frontpoly by calling drawPoly
    drawPoly(object[2]) # draws rightpoly by calling drawPoly
    drawPoly(object[3]) # draws backpoly by calling drawPoly
    drawPoly(object[4]) # draws leftpoly by calling drawPoly
    drawPoly(object[0]) # draws bottompoly by calling drawPoly


# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly):
    for a in range(len(poly) - 1): # iterates 'a' for the number of elements except the last in the object
        drawLine(poly[a], poly[a+1]) # draws a line for each point (ie; 0 to 1, 1 to 2...)
    i = len(poly) - 1 # variable to find the one before the last element
    drawLine(poly[i], poly[0]) # connects the final point to the initial point
    

# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start,end):

    startdisplay = convertToDisplayCoordinates(project(start)) # projects the first point and then converts to display coordinate
    #print(startdisplay)
    enddisplay = convertToDisplayCoordinates(project(end)) # projects the second point and then converts to display coordinate
    #print(enddisplay)
    
    w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1]) # creates the line
    

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
    displayXY.append(point[0] + 200) # changes the X axis to the center of tkinter canvas
    displayXY.append(((-1) * (point[1])) + 200) # inverts the Y axis and centers it onto the canvas
    return displayXY
    

# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    resetPyramid()
    drawObject(Pyramid)

def larger():
    w.delete(ALL)
    scale(PyramidPointCloud,1.1)
    drawObject(Pyramid)

def smaller():
    w.delete(ALL)
    scale(PyramidPointCloud,.9)
    drawObject(Pyramid)

def forward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,5])
    drawObject(Pyramid)

def backward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,-5])
    drawObject(Pyramid)

def left():
    w.delete(ALL)
    translate(PyramidPointCloud,[-5,0,0])
    drawObject(Pyramid)

def right():
    w.delete(ALL)
    translate(PyramidPointCloud,[5,0,0])
    drawObject(Pyramid)

def up():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,5,0])
    drawObject(Pyramid)

def down():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,-5,0])
    drawObject(Pyramid)

def xPlus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,5)
    drawObject(Pyramid)

def xMinus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,-5)
    drawObject(Pyramid)

def yPlus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,5)
    drawObject(Pyramid)

def yMinus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,-5)
    drawObject(Pyramid)

def zPlus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,5)
    drawObject(Pyramid)

def zMinus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,-5)
    drawObject(Pyramid)

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawObject(Pyramid)
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

root.mainloop()