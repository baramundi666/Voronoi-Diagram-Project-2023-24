# parametr epsilon
eps = 10**-12
def findCircumCenter(P, Q, R):
    ax = P[0]
    ay = P[1]
    bx = Q[0]
    by = Q[1]
    cx = R[0]
    cy = R[1]
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy)

def checkPosition(P, Q, R, D):
    center = findCircumCenter(P, Q, R)
    R = (center[0]-P[0])**2 + (center[1]-P[1])**2
    dist = (center[0]-D[0])**2 + (center[1]-D[1])**2
    return dist-R<=eps

def obtuseAngle(triangle, edge):
    a = edge.A
    b = edge.B
    if triangle.a!=a and triangle.a!=b: c=triangle.a
    if triangle.b!=a and triangle.b!=b: c=triangle.b
    if triangle.c!=a and triangle.c!=b: c=triangle.c
    lengthAB = (a.x-b.x)**2 + (a.y-b.y)**2
    lengthBC = (c.x-b.x)**2 + (c.y-b.y)**2
    lengthCA = (a.x-c.x)**2 + (a.y-c.y)**2
    return lengthAB>lengthBC+lengthCA


class Point():
    def __init__(self,point,index):
        self.index = index
        self.x = point[0]
        self.y = point[1]

    def __eq__(self, other):
        return self.index==other.index
    
    def __hash__(self):
        return hash(self.index)
    
    def toCart(self):
        return (self.x, self.y)
    
class Edge():
    def __init__(self, PointA, PointB):
        self.A = PointA
        self.B = PointB

    def __eq__(self, other):
        return (self.A==other.A and self.B==other.B) or (self.A==other.B and self.B==other.A)
    
    def __hash__(self):
        return hash(self.A.index+self.B.index)
    
    def toCart(self):
        return ((self.A.x, self.A.y), (self.B.x, self.B.y))
    
class HalfLine():
    def __init__(self, PointA, PointB):
        self.A = PointA
        self.B = PointB

    def __eq__(self, other):
        return (self.A==other.A and self.B==other.B) or (self.A==other.B and self.B==other.A)
    
    def __hash__(self):
        return hash(self.A.index+self.B.index)
    
    def toCart(self):
        return ((self.A.x, self.A.y), (self.B.x, self.B.y))


class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.isCorrect = True

    def __eq__(self, other):
        return self.a==other.a and self.b==other.b and self.c==other.c
    
    def __hash__(self):
        return hash((self.a, self.b, self.c))
    
    def containsPoint(self, point):
        return self.a==point or self.b==point or self.c==point
    
    def circumcircleContainsPoint(self, point):
        P = self.a.toCart()
        Q = self.b.toCart()
        R = self.c.toCart()
        D = point.toCart()
        return checkPosition(P, Q, R, D)
    
    def getCircleCenter(self):
        P = self.a.toCart()
        Q = self.b.toCart()
        R = self.c.toCart()
        return Point(findCircumCenter(P, Q, R),-1)

    def sharesEdge(self, edge):
        x = edge.A
        y = edge.B
        trianglePoints = [self.a, self.b, self.c]
        return x in trianglePoints and y in trianglePoints