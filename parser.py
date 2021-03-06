from display import *
from matrix import *
from draw import *
import time
import string

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.readlines()
#    print lines
    i = 0
    while i < len(lines):

        line = lines[i][:-1]

        if line[0].isdigit() or line[2].isdigit():
            cmd = lines[i - 1][:-1]
            p = line.split(" ")
            for j in range(len(p)):
                if p[j].isdigit():
                    p[j] = int(p[j])
            if cmd == "line":
                add_edge_helper(points, p)
            elif cmd == "move":
                t = make_translate(p[0], p[1], p[2])
                matrix_mult(t, transform)
            elif cmd == "scale":
                t = make_scale(p[0], p[1], p[2])
                matrix_mult(t, transform)
            elif cmd == "rotate":                
                if p[0] == "x":
                    t = make_rotX(p[1])
                elif p[0] == "y":
                    t = make_rotY(p[1])
                elif p[1] == "z":
                    t = make_rotZ(p[1])
                matrix_mult(t, transform)
            elif line == "save":
                fname = p[0]
                print "fname: ", fname
                #clear_screen(screen)
                #draw_lines(points, screen, color)
                save_extension(screen, fname)
                time.sleep(1)
        #end if two lines
        else:
            if line == "apply":
                print "applying..."
                matrix_mult(transform, points)
            if line == "ident":                
                ident(transform)
            elif line == "display":
                clear_screen(screen)

                #print "ABOUT TO DRAW..."
                #print_matrix(points)
                round_all(points)

                draw_lines(points, screen, color)
                print "ABOUT TO DISPLAY THIS: "
                print_matrix(points)
                display(screen)
                time.sleep(1)

        #end if solo cmd
        
        i += 1
