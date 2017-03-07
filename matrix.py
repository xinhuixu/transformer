import math

def int_all( matrix):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[r][c] = int(matrix[r][c])

def make_translate( x, y, z ):
    m = new_matrix()
    
    ident(m)

    m[3][0] = x
    m[3][1] = y
    m[3][2] = z

    return m

def make_scale( x, y, z ):
    m = new_matrix()
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    m[3][3] = 1
    return m
        
def make_rotZ( theta ):    
    m = new_matrix()
    theta = math.radians(theta)
    m[0][0] = math.cos(theta)
    m[1][0] = -1*math.sin(theta)
    m[0][1] = math.sin(theta)
    m[1][1] = math.cos(theta)
    m[2][2] = 1
    m[3][3] = 1
    int_all(m)
    return m

def make_rotY( theta ):
    m = new_matrix()
    theta = math.radians(theta)
    m[0][0] = math.cos(theta)
    m[2][0] = math.sin(theta)
    m[1][1] = 1
    m[0][2] = -1*math.sin(theta)
    m[2][2] = math.cos(theta)
    m[3][3] = 1
    int_all(m)
    return m

def make_rotX( theta ):
    m = new_matrix()
    theta = math.radians(theta)
    m[0][0] = 1
    m[1][1] = math.cos(theta)
    m[2][1] = -1* math.sin(theta)
    m[1][2] = math.sin(theta)
    m[2][2] = math.cos(theta)
    m[3][3] = 1
    int_all(m)
    return m
    
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
