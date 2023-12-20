def orient(a, b, c):
    return (b.x-a.x)*(c.y-b.y) - (b.y-a.y)*(c.x-b.x)

# parametr epsilon
eps = 10*-12

class Point():
    def __init__(self,point):
        self.x = point[0]
        self.y = point[1]

    def __eq__(self, other):
        return abs(self.x-other.x)<eps and abs(self.y-other.y)<eps


class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.isCorrect = True

    def __eq__(self, other):
        return self.a==other.a and self.b==other.b and self.c==other.c
    
    def containsPoint(self, point):
        side1 = orient(self.a, self.b, point)
        side2 = orient(self.b, self.c, point)
        side3 = orient(self.c, self.a, point)
        isOnLeft = side1<0 and side2<0 and side3<0
        isOnRight = side1>0 and side2>0 and side3>0
        return isOnLeft or isOnRight
    
    def circumcircleContainsPoint(self, point):
        ax_ = self.a.x-point.x
        ay_ = self.a.y-point.y
        bx_ = self.b.x-point.x
        by_ = self.b.y-point.y
        cx_ = self.c.x-point.x
        cy_ = self.c.y-point.y
        return (
            (ax_*ax_ + ay_*ay_) * (bx_*cy_-cx_*by_) -
            (bx_*bx_ + by_*by_) * (ax_*cy_-cx_*ay_) +
            (cx_*cx_ + cy_*cy_) * (ax_*by_-bx_*ay_)
        ) > 0
    
    def sharesEdge(self, edge):
        x = Point(edge[0])
        y = Point(edge[1])
        trianglePoints = [self.a, self.b, self.c]
        return x in trianglePoints and y in trianglePoints
        


# https://www.baeldung.com/cs/voronoi-diagram
def Bowyer_Watson(points):
    pointList = []
    for point in points:
        newPoint = Point(point)
        pointList.append(newPoint)

    # print("!")
    # print(pointList)
    triangleList = []
    superA = Point((1000,-1000))
    superB = Point((-1000,-1000))
    superC = Point((0,1000))
    superTriangle = Triangle(superA, superB, superC)

    for point in pointList:
        edgeList = set()
        for triangle in triangleList:
            if triangle.circumcircleContainsPoint(point):
                triangle.isCorrect=False
                a = triangle.a
                b = triangle.b
                c = triangle.c
                edgeList.add((Point(a), Point(b)))
                edgeList.add( (Point(b), Point(c)))
                edgeList.add((Point(c), Point(a)))

        for triangle in triangleList:
            if triangle.isCorrect==False: triangleList.remove(triangle)

        # to do
        #for edge in edgeList:
            # if edge is shared by any other triangles:
            #    edgeList.remove(edge)

        for edge in edgeList:
            triangle = Triangle(edge[0], edge[1], point)
            triangleList.append(triangle)
    
    a = superTriangle.a
    b = superTriangle.b
    c = superTriangle.c
    for triangle in triangleList:
        if triangle.containsPoint(a) or triangle.containsPoint(b) or triangle.containsPoint(c):
            triangleList.remove(triangle)

    return triangleList

#Bowyer_Watson([(0, 1)])
