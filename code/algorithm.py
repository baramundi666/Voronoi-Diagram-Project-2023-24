from utils import *

def Bowyer_Watson(points):
    lowerX = points[0][0]
    lowerY = points[0][1]
    upperX = points[0][0]
    upperY = points[0][1]
    pointList = []
    n = len(points)
    for i in range(n):
        newPoint = Point(points[i], i)
        pointList.append(newPoint)
        if points[i][0]<lowerX: lowerX = points[i][0]
        if points[i][1]<lowerY: lowerY = points[i][1]
        if points[i][0]>upperX: upperX = points[i][0]
        if points[i][1]>upperY: upperY = points[i][1]


    triangleList = []
    # Prostokąt
    lowerX-=100
    lowerY-=100
    upperX+=100
    upperY+=100
    superA = Point((lowerX, lowerY), -2)
    superB = Point((lowerX, upperY), -3)
    superC = Point((upperX, upperY), -4)
    superD = Point((upperX, lowerY), -5)
    # Dwa trójkąty
    superTriangle1 = Triangle(superA, superB, superC)
    superTriangle2 = Triangle(superC, superD, superA)
    triangleList.append(superTriangle1)
    triangleList.append(superTriangle2)

    # Główna pętla algorytmu
    for point in pointList:
        # klucz: krawedz, wartość: zbiór trójkątów
        edgeList = {}

        # Wyznaczenie trójkątów do usunięcia
        for triangle in triangleList:
            if triangle.circumcircleContainsPoint(point):
                triangle.isCorrect=False
                a = triangle.a
                b = triangle.b
                c = triangle.c
                edgeAB = Edge(a, b)
                edgeBC = Edge(b, c)
                edgeCA = Edge(c, a)
                if edgeAB in edgeList.keys():
                    edgeList[edgeAB].add(triangle)
                else:
                    edgeList[edgeAB] = set()
                    edgeList[edgeAB].add(triangle)
                if edgeBC in edgeList.keys():
                    edgeList[edgeBC].add(triangle)
                else:
                    edgeList[edgeBC] = set()
                    edgeList[edgeBC].add(triangle)
                if edgeCA in edgeList.keys():
                    edgeList[edgeCA].add(triangle)
                else:
                    edgeList[edgeCA] = set()
                    edgeList[edgeCA].add(triangle)

        # Usunięcie nieprawidłowych trójkątów
        newTriangleList = []
        for triangle in triangleList:
            if triangle.isCorrect==True: newTriangleList.append(triangle)
        triangleList = newTriangleList

        # Usunięcie przecinających się krawędzi
        newEdgeList = dict(edgeList)
        for edge in edgeList.keys():
            if len(edgeList[edge])>1:
                newEdgeList.pop(edge)
        edgeList = newEdgeList

        # Utworzenie nowych trójkątów - wypełnienie pustego wielokąta
        for edge in edgeList:
            triangle = Triangle(edge.A, edge.B, point)
            triangleList.append(triangle)

    
    # Usunięcie trójkątów zawierających sztuczne punkty początkowe
    finalTriangleList = list(triangleList)
    for triangle in triangleList:
        if triangle.containsPoint(superA) or triangle.containsPoint(superB) or triangle.containsPoint(superC) or triangle.containsPoint(superD):
            finalTriangleList.remove(triangle)

    # Zwracanie reprezentacji wieloboków Voronoi
    triangleList = finalTriangleList
    voronoiDiagram = []
    edgeList = {}

    for triangle in triangleList:
        a = triangle.a
        b = triangle.b
        c = triangle.c
        edgeAB = Edge(a, b)
        edgeBC = Edge(b, c)
        edgeCA = Edge(c, a)
        for edge in [edgeAB, edgeBC, edgeCA]:
            if edge in edgeList.keys():
                edgeList[edge].add(triangle)
            else:
                edgeList[edge] = set()
                edgeList[edge].add(triangle)

    for triangle in triangleList:
        a = triangle.a
        b = triangle.b
        c = triangle.c
        edgeAB = Edge(a, b)
        edgeBC = Edge(b, c)
        edgeCA = Edge(c, a)
        voronoiPoint = triangle.getCircleCenter()
        voronoiDiagram.append(voronoiPoint)
        for edge in [edgeAB, edgeBC, edgeCA]:
            if len(edgeList[edge])>1:
                for otherTriangle in edgeList[edge]:
                    if otherTriangle!=triangle:
                        voronoiDiagram.append(Edge(voronoiPoint, otherTriangle.getCircleCenter()))
            else:
                middle = Point(((edge.A.x+edge.B.x)/2, (edge.A.y+edge.B.y)/2),-2)
                MV = (voronoiPoint.toCart()[0]-middle.toCart()[0], voronoiPoint.toCart()[1]-middle.toCart()[1])
                if obtuseAngle(triangle, edge):
                    newPoint = Point((voronoiPoint.toCart()[0]+MV[0], voronoiPoint.toCart()[1]+MV[1]),-2)
                    voronoiDiagram.append(HalfLine(voronoiPoint, newPoint))
                else:
                    voronoiDiagram.append(HalfLine(voronoiPoint,middle))
   


    return triangleList, voronoiDiagram 