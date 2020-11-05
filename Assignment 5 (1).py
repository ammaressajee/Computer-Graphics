##################################################################################################
# Ammar Essajee
# Student ID: 102-43-821
# Date:2/19/2019
# Assignment #5
# This code creates a scene which uses ray tracing and the phong illumination model along with
# shadow feelers to portray a realistic version of the given scence.
##################################################################################################

# imports funcionality from various libraries
import sys
import math
from tkinter import *

# set the canvas height and width
CanvasWidth = 600
CanvasHeight = 600

# initialize arrays for normalizing varibales
# lighting vector
L = [1, 1, -1]
Ip = [255, 255, 255]
# rbg colors
Ired = [255, 0, 0]
Iwhite = [255, 255, 255]
Iblue = [120, 180, 0]
Igreen= [200, 100, 100]
# backgroun color 
background_blue = [150, 150, 255]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(background_blue[0] * background_blue[0] + background_blue[1] * background_blue[1] + background_blue[2] * background_blue[2])
background_bluex_norm = background_blue[0] / magnitude
background_bluey_norm = background_blue[1] / magnitude
background_bluez_norm = background_blue[2] / magnitude
# array of normalized values
background_blue_norm = [background_bluex_norm, background_bluey_norm, background_bluez_norm]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(Ired[0] * Ired[0] + Ired[1] * Ired[1] + Ired[2] * Ired[2])
Iredx_norm = Ired[0] / magnitude
Iredy_norm = Ired[1] / magnitude
Iredz_norm = Ired[2] / magnitude
# array of normalized values
Ired_norm = [Iredx_norm, Iredy_norm, Iredz_norm]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(Ip[0] * Ip[0] + Ip[1] * Ip[1] + Ip[2] * Ip[2])
Ipx_norm = Ip[0] / magnitude
Ipy_norm = Ip[1] / magnitude
Ipz_norm = Ip[2] / magnitude
# array of normalized values
Ip_norm = [Ipx_norm, Ipy_norm, Ipz_norm]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(Iwhite[0] * Iwhite[0] + Iwhite[1] * Iwhite[1] + Iwhite[2] * Iwhite[2])
Iwhitex_norm = Iwhite[0] / magnitude
Iwhitey_norm = Iwhite[1] / magnitude
Iwhitez_norm = Iwhite[2] / magnitude
# array of normalized values
Iwhite_norm = [Iwhitex_norm, Iwhitey_norm, Iwhitez_norm]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(Iblue[0] * Iblue[0] + Iblue[1] * Iblue[1] + Iblue[2] * Iblue[2])
Ibluex_norm = Iblue[0] / magnitude
Ibluey_norm = Iblue[1] / magnitude
Ibluez_norm = Iblue[2] / magnitude
# array of normalized values
Iblue_norm = [Ibluex_norm, Ibluey_norm, Ibluez_norm]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(Igreen[0] * Igreen[0] + Igreen[1] * Igreen[1] + Igreen[2] * Igreen[2])
Igreenx_norm = Igreen[0] / magnitude
Igreeny_norm = Igreen[1] / magnitude
Igreenz_norm = Igreen[2] / magnitude
# array of normalized values
Igreen_norm = [Igreenx_norm, Igreeny_norm, Igreenz_norm]
# performs a calculation to recieve a normalized value
magnitude = math.sqrt(L[0] * L[0] + L[1] * L[1] + L[2] * L[2])
Lx_norm = L[0] / magnitude
Ly_norm = L[1] / magnitude
Lz_norm = L[2] / magnitude
L_norm = [Lx_norm, Ly_norm, Lz_norm]


# rgb values
ir = 0
ig = 0
ib = 0
# distance of closest object
t = 0
# intersection points of ray and object
intersect_x = 0
intersect_y = 0
intersect_z = 0
# surface normals of objects
obj_normal_x = 0
obj_normal_y = 0
obj_normal_z = 0

# quits application
def quit_app():
    # exit
    sys.exit(0)

# function that is called when the render button is pressed
def render_proc():
    # sets rgb to global variables
    global ir, ig, ib
    
    # maximum ray depth
    depth = 5
    
    
    # center of projection
    xs = 0
    ys = 0
    zs = -800
    
    # creates for loop for columns
    for pixel_x in range(1, CanvasWidth + 1): # +1 so it gets the very last pixel

        screen_x = pixel_x - (CanvasWidth/2)
        
        # creates for loop for rows
        for pixel_y in range (1, CanvasHeight + 1): # +1 so it gets the very last pixel
            if pixel_x % 2 == 0:
            
                screen_y = (CanvasHeight/2) - pixel_y
                
                # compute vector for ray from the center of projection through pixel
                ray_i = screen_x - xs
                ray_j = screen_y - ys
                ray_k = 0 - zs
                # trace the ray through the environment to obtain the pixel color
                trace_ray(0, depth, xs, ys, zs, ray_i, ray_j, ray_k)
                #draw the pixel
                put_pixel(pixel_x, pixel_y, ir, ig, ib)
        #updates tkinter and improves speed
        w.update_idletasks()

# function that calulates the trace rays
def trace_ray(flag, level, xs, ys, zs, ray_i, ray_j, ray_k):
    # golbalizing several variables
    global t
    global intersect_x
    global intersect_y
    global intersect_z
    global obj_normal_x
    global obj_normal_y
    global obj_normal_z
    global ir, ig, ib
    
    if level == 0:
        # initially set rgb to white
        ir = 0
        ig = 0
        ib = 0
    else:
        # check for intersection of ray with objects
        # and set rgb values corresponding to objects
        
        # set distance of closest object initially to a very large number
        t = 100000
        
        # initially no object has been intersected by the ray
        
        object_code = -1
        
        # looks for intersection in checkerboard
        if checkerboard_intersection(xs, ys, zs, ray_i, ray_j, ray_k) == 1:
            object_code = 0
            if flag == True:
                print("checkerboard")
         # looks for intersection in sphere1
        if sphere1_intersection(xs, ys, zs, ray_i, ray_j, ray_k) == 1:
            object_code = 1
        
            if flag == True:
                print("green_sphere")
         # looks for intersection in sphere2
        if sphere2_intersection(xs, ys, zs, ray_i, ray_j, ray_k) == 1:
            object_code = 2
        
            if flag == True:
                print("reflective_sphere")
        # recreates the switch/case format to check variable against object_code
        if object_code == 0:
            checkerboard_point_intensity(level, ray_i, ray_j, ray_k, intersect_x, intersect_y, intersect_z, obj_normal_x, obj_normal_y, obj_normal_z)
         # checks if == 1
        elif object_code == 1:
            ir =  200
            ig = 0
            ib = 250
            sphere1_point_intensity(level, ray_i, ray_j, ray_k, intersect_x, intersect_y, intersect_z, obj_normal_x, obj_normal_y, obj_normal_z)
        # checks if == 2
        elif object_code == 2:
            ir =  200
            ig = 0
            ib = 250
            sphere2_point_intensity(level, ray_i, ray_j, ray_k, intersect_x, intersect_y, intersect_z, obj_normal_x, obj_normal_y, obj_normal_z)
        # defalut settings for any unspecified object_code
        else:
            # set pixel color to background color(light blue)
            ir = background_blue_norm[0]
            ig = background_blue_norm[1]
            ib = background_blue_norm[2]
# calculates intersection points           
def checkerboard_intersection(xs, ys, zs, ray_x, ray_y, ray_z):
    global t, intersect_x, intersect_y, intersect_z, obj_normal_x, obj_normal_y, obj_normal_z
    
    t_object = None
    color_flag = None
    # normal of the plane
    a = 0
    b = 1
    c = 0
    # point on plane
    x1 = 0
    y1 = -500
    z1 = 0
    # compute intersection of ray wiht plane
    denom = a * ray_x + b * ray_y + c * ray_z
    
    # fabs is absolute value 
    if (math.fabs(denom) <= 0.001): # ray parallel to plane
        return 0
    else:
        d = a * x1 + b * y1 + c * z1
        t_object = -(a * xs + b * ys + c * zs -d)/denom
        x = xs + ray_x * t_object
        y = ys + ray_y * t_object
        z = zs + ray_z * t_object
        # extra decimal places fixes banding issue
        if ((z < 0.001) or (z > 8000) or (t_object < 0.001)):
            return 0 # no visible interaction
        elif (t < t_object):
            return 0 # another object is nearer
        else:
            t = t_object
            intersect_x = x
            intersect_y = y
            intersect_z = z
            obj_normal_x = a
            obj_normal_y = b
            obj_normal_z = c
            return 1
# calculates pixel intensity for checkerboard
def checkerboard_point_intensity(level, ray_x, ray_y, ray_z, x, y, z, nx, ny, nz):
    global ir, ig, ib
    
    # a red and white checkered plane
    # compute and color at intersection point
    if ( x >= 0.0):
        color_flag = 1
    # compute and color at intersection point
    else:
        color_flag = 0
    # compute and color at intersection point
    if ((math.fabs(math.fmod(x, 400.0))) > 200):
        if color_flag == 1:
            color_flag = 0
        else:
            color_flag = 1
    # compute and color at intersection point
    if ((math.fabs(math.fmod(z, 400.0))) > 200):
        if color_flag == 1:
            color_flag = 0
        else:
            color_flag = 1
        
        
    # normalize the incoming ray vector and the surface normal vector
    magnitude = math.sqrt(ray_x * ray_x + ray_y * ray_y + ray_z * ray_z)
    ray_x_norm = ray_x / magnitude
    ray_y_norm = ray_y / magnitude
    ray_z_norm = ray_z / magnitude
    # finds the magnitude
    magnitude = math.sqrt(nx * nx + ny * ny + nz * nz)
    # finds normals
    nx_norm = nx / magnitude
    ny_norm = ny / magnitude 
    nz_norm = nz / magnitude
     # reflection ray
    cosine_phi = (-ray_x_norm) * (nx_norm) + (-ray_y_norm) * (ny_norm) + (-ray_z_norm) * (nz_norm)
    # reflection ray
    if cosine_phi > 0: #finds the reflection vector normals
        rx = nx_norm - (-ray_x_norm) / (2 * cosine_phi)
        ry = ny_norm - (-ray_y_norm) / (2 * cosine_phi)
        rz = nz_norm - (-ray_z_norm) / (2 * cosine_phi)
    # reflection ray
    if cosine_phi == 0: #finds the reflection vector normals
        rx = ray_x_norm
        ry = ray_y_norm
        rz = ray_z_norm
    # reflection ray
    if cosine_phi < 0: #finds the reflection vector normals
        rx = -nx_norm + (-ray_x_norm) / (2 * cosine_phi)
        ry = -ny_norm + (-ray_y_norm) / (2 * cosine_phi)
        rz = -nz_norm + (-ray_z_norm) / (2 * cosine_phi)
        
    magnitude = math.sqrt(rx * rx + ry * ry + rz * rz)
    rx_norm = rx / magnitude
    ry_norm = ry / magnitude
    rz_norm = rz / magnitude
    
    #trace reflection ray
    trace_ray(0, level - 1, x, y, z, rx, ry, rz)
    
    # calculates the dot product of N . L
    angle = (nx_norm * L_norm[0]) + (ny_norm * L_norm[1]) + (nz_norm * L_norm[2])
    
    if color_flag == 1:
        # red
        ir = 0.7 * ir + 0.3 * Ired_norm[0] + Ip_norm[0] * 0.3 * angle / 1 # performs point diffuse by using formula ir
        ig = 0.7 * ig + 0.3 * Ired_norm[1] + Ip_norm[1] * 0.3 * angle / 1 # performs point diffuse by using formula ig
        ib = 0.7 * ib + 0.3 * Ired_norm[2] + Ip_norm[2] * 0.3 * angle / 1 # performs point diffuse by using formula ib

    else:
        # white
        ir = 0.7 * ir + 0.3 * Iwhite_norm[0] + Ip_norm[0] * 0.3 * angle / 1 # performs point diffuse by using formula ir
        ig = 0.7 * ig + 0.3 * Iwhite_norm[1] + Ip_norm[1] * 0.3 * angle / 1 # performs point diffuse by using formula ig
        ib = 0.7 * ib + 0.3 * Iwhite_norm[2] + Ip_norm[2] * 0.3 * angle / 1 # performs point diffuse by using formula ib
    
    
# sphere1 intersection points        
def sphere1_intersection(xs, ys, zs, ray_x, ray_y, ray_z):
    global t, intersect_x, intersect_y, intersect_z, obj_normal_x, obj_normal_y, obj_normal_z
    # center of sphere
    l = 0
    m = -400
    n = 600
    
    # radius of sphere
    r = 100
    
    # compute the intersection of ray with sphere
    asphere = ray_x * ray_x + ray_y * ray_y + ray_z * ray_z
    
    bsphere = 2 * ray_x * (xs - l) + 2 * ray_y * (ys - m) + 2 * ray_z * (zs - n)
    
    csphere = l * l + m * m + n * n + xs * xs + ys * ys + zs * zs + 2 * (-l * xs - m * ys - n * zs) - r * r
    
    disc = bsphere * bsphere - 4 * asphere * csphere
    
    if (disc < 0 ):
        return 0
    
    else:
        ts1 = (-bsphere + math.sqrt(disc))/ (2 * asphere)
        ts2 = (-bsphere - math.sqrt(disc))/ (2 * asphere)
        if ts1 >= ts2:
            tsphere = ts2
        else:
            tsphere = ts1
        
        if t < tsphere:
            return 0 # another object is closer
        
        elif (tsphere < 0.0): # no visible intersection
            return 0
        
        else:
            t = tsphere
            intersect_x = xs + ray_x * tsphere
            intersect_y = ys + ray_y * tsphere
            intersect_z = zs + ray_z * tsphere
            obj_normal_x = intersect_x - l
            obj_normal_y = intersect_y - m
            obj_normal_z = intersect_z - n
            return 1
# calculates rgb intensities for sphere1       
def sphere1_point_intensity(level, ray_x, ray_y, ray_z, x, y, z, nx, ny, nz):
    global ir, ig, ib
    # normalize the incoming ray vector and the surface normal vector
    magnitude = math.sqrt(ray_x * ray_x + ray_y * ray_y + ray_z * ray_z)
    ray_x_norm = ray_x / magnitude
    ray_y_norm = ray_y / magnitude
    ray_z_norm = ray_z / magnitude
    # finds the magnitude
    magnitude = math.sqrt(nx * nx + ny * ny + nz * nz)
    nx_norm = nx / magnitude
    ny_norm = ny / magnitude 
    nz_norm = nz / magnitude
    
    # calculate reflection vector
    
    cosine_phi = (-ray_x_norm) * (nx_norm) + (-ray_y_norm) * (ny_norm) + (-ray_z_norm) * (nz_norm)
    
    if cosine_phi > 0: #finds the reflection vector normals
        rx = nx_norm - (-ray_x_norm) / (2 * cosine_phi)
        ry = ny_norm - (-ray_y_norm) / (2 * cosine_phi)
        rz = nz_norm - (-ray_z_norm) / (2 * cosine_phi)
    
    if cosine_phi == 0: #finds the reflection vector normals
        rx = ray_x_norm
        ry = ray_y_norm
        rz = ray_z_norm
        
    if cosine_phi < 0: #finds the reflection vector normals
        rx = -nx_norm + (-ray_x_norm) / (2 * cosine_phi)
        ry = -ny_norm + (-ray_y_norm) / (2 * cosine_phi)
        rz = -nz_norm + (-ray_z_norm) / (2 * cosine_phi)
    
    #trace reflection ray
    trace_ray(0, level - 1, x, y, z, rx, ry, rz)
    
    # calculates the dot product of N . L
    angle = (nx_norm * L_norm[0]) + (ny_norm * L_norm[1]) + (nz_norm * L_norm[2])
    
    # add effect of local color
    ir = 0.7 * ir + 0.3 * Iblue_norm[0] + Ip_norm[0] * 0.3 * angle / 1
    ig = 0.7 * ig + 0.3 * Iblue_norm[1] + Ip_norm[1] * 0.3 * angle / 1
    ib = 0.7 * ib + 0.3 * Iblue_norm[2] + Ip_norm[2] * 0.3 * angle / 1
    
# finds sphere2 intersection point
def sphere2_intersection(xs, ys, zs, ray_x, ray_y, ray_z):
    global t, intersect_x, intersect_y, intersect_z, obj_normal_x, obj_normal_y, obj_normal_z
    # center of sphere
    l = -200
    m = -300
    n = 1000
    
    # radius of sphere
    r = 250
    
    # compute intersection of ray with sphere
    asphere = ray_x * ray_x + ray_y * ray_y + ray_z * ray_z
    
    bsphere = 2 * ray_x * (xs - l) + 2 * ray_y * (ys - m) + 2 * ray_z * (zs - n)
    
    csphere = l * l + m * m + n * n + xs * xs + ys * ys + zs * zs + 2 * (-l * xs - m * ys - n * zs) - r * r
    
    disc = bsphere * bsphere - 4 * asphere * csphere
    
    if (disc < 0 ):
        return 0
    
    else:
        ts1 = (-bsphere + math.sqrt(disc))/ (2 * asphere)
        ts2 = (-bsphere - math.sqrt(disc))/ (2 * asphere)
        if ts1 >= ts2:
            tsphere = ts2
        else:
            tsphere = ts1
        
        if t < tsphere:
            return 0 # another object is closer
        
        elif (tsphere < 0.0): # no visible intersection
            return 0
        
        else:
            t = tsphere
            intersect_x = xs + ray_x * tsphere
            intersect_y = ys + ray_y * tsphere
            intersect_z = zs + ray_z * tsphere
            obj_normal_x = intersect_x - l
            obj_normal_y = intersect_y - m
            obj_normal_z = intersect_z - n
            return 1 
# finds rgb intensities for sphere2
def sphere2_point_intensity(level, ray_x, ray_y, ray_z, x, y, z, nx, ny, nz):
    global ir, ig, ib
    # normalize the incoming ray vector and the surface normal vector
    magnitude = math.sqrt(ray_x * ray_x + ray_y * ray_y + ray_z * ray_z)
    ray_x_norm = ray_x / magnitude
    ray_y_norm = ray_y / magnitude
    ray_z_norm = ray_z / magnitude
    
    magnitude = math.sqrt(nx * nx + ny * ny + nz * nz)
    nx_norm = nx / magnitude
    ny_norm = ny / magnitude 
    nz_norm = nz / magnitude
    
    # calculate reflection vector
    
    cosine_phi = (-ray_x_norm) * (nx_norm) + (-ray_y_norm) * (ny_norm) + (-ray_z_norm) * (nz_norm)
    
    if cosine_phi > 0: # finds the reflection vector normals
        rx = nx_norm - (-ray_x_norm) / (2 * cosine_phi)
        ry = ny_norm - (-ray_y_norm) / (2 * cosine_phi)
        rz = nz_norm - (-ray_z_norm) / (2 * cosine_phi)
    
    if cosine_phi == 0: # finds the reflection vector normals
        rx = ray_x_norm
        ry = ray_y_norm
        rz = ray_z_norm
        
    if cosine_phi < 0: # finds the reflection vector normals
        rx = -nx_norm + (-ray_x_norm) / (2 * cosine_phi)
        ry = -ny_norm + (-ray_y_norm) / (2 * cosine_phi)
        rz = -nz_norm + (-ray_z_norm) / (2 * cosine_phi)
    
    #trace reflection ray
    trace_ray(0, level - 1, x, y, z, rx, ry, rz)
    
    # calculates the dot product of N . L
    angle = (nx_norm * L_norm[0]) + (ny_norm * L_norm[1]) + (nz_norm * L_norm[2])
    
    # add effect of local color
    ir = 0.7 * ir + 0.3 * Igreen_norm[0] + Ip_norm[0] * 0.3 * angle / 1 # performs point diffuse by using formula ir
    ig = 0.7 * ig + 0.3 * Igreen_norm[1] + Ip_norm[1] * 0.3 * angle / 1 # performs point diffuse by using formula ig
    ib = 0.7 * ib + 0.3 * Igreen_norm[2] + Ip_norm[2] * 0.3 * angle / 1 # performs point diffuse by using formula ib
    

    
# draws pixel (create_oval)
def put_pixel(pixel_x, pixel_y, ir, ig, ib):
    ir2 = ir * 255 # un-normalizes rgb values
    ig2 = ig * 255
    ib2 = ib * 255
    
    # clip out of range color intensities
    if (int(ir2) > 244):
        ir = 244
    if (int(ig2) > 244):
        ig = 244
    if (int(ib2) > 244):
        ib = 244
    if (int(ir2) < 80):
        ir = 80
    if (int(ig2) < 80):
        ig = 80
    if (int(ib2) < 80):
        ib = 80
        
    color = '#%02x%02x%02x' % (int(ir2), int(ig2), int(ib2)) # converts to pixel color
    # plot pixel on screen
    w.create_oval(pixel_x, pixel_y, pixel_x, pixel_y, outline = color, fill = color, width = 1)
    #print(color)
    
# establishes Tkinter canvas
root = Tk()
outerframe = Frame(root)
outerframe.pack()
 
# draws the blank canvas
w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight, bg = 'white')

w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()
# creating render button
rendercontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
rendercontrols.pack(side=LEFT)

rendercontrolslabel = Label(rendercontrols, text="Render")
rendercontrolslabel.pack()
# indicates function that render calls
renderButton = Button(rendercontrols, text="Render", fg="black", bg="turquoise", command=render_proc)
renderButton.pack(side=RIGHT)
# creating quit button
quitcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
quitcontrols.pack(side=LEFT)

quitcontrolslabel = Label(quitcontrols, text="Quit")
quitcontrolslabel.pack()
# sets the function the button calls
quitButton = Button(quitcontrols, text="Quit", fg="black", bg="turquoise", command=quit_app)
quitButton.pack(side=RIGHT)


root.mainloop()

