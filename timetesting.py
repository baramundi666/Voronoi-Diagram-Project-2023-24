from foronoi import *
import time
import numpy as np 
from algorithms import Bowyer_Watson

def voronoiBowyer_Watson(points):
    '''
    parameters: points = [(x1, y1), (x2, y2), ...]
    return: voronoiPoints = [(a1, b1), (a2, b2), ...]
    '''
    voronoiPoints = []
    triangulation = Bowyer_Watson(points)
    for triangle in triangulation:
        voronoiPoints.append(triangle.getCircleCenter().toCart())
    return voronoiPoints

def generate_uniform_points(left, right, n = 10 ** 5):
    tab =[]
    for _ in range(n):
        x = np.random.uniform(left, right)
        y = np.random.uniform(left, right)
        tab.append((x, y))
    return tab

def get_boundary(points):  
    lowerX = points[0][0]
    lowerY = points[0][1]
    upperX = points[0][0]
    upperY = points[0][1]
    n = len(points)
    for i in range(n):
        if points[i][0]<lowerX: lowerX = points[i][0]
        if points[i][1]<lowerY: lowerY = points[i][1]
        if points[i][0]>upperX: upperX = points[i][0]
        if points[i][1]>upperY: upperY = points[i][1]
    return lowerX, lowerY, upperX, upperY

def measure_time(data,n):
    lowerX, lowerY, upperX, upperY = get_boundary(data)
    polygon = Polygon([
        (lowerX,lowerY),
        (lowerX,upperY),
        (upperX,lowerY),
        (upperX,upperY),
    ])
    start_time = time.time()
    voronoiPoints = voronoiBowyer_Watson(data)
    print('Bowyer-Watson:','liczba punktów:',n ,'czas:', (time.time() - start_time))
    start_time = time.time()
    v = Voronoi(polygon) 
    v.create_diagram(points=data)
    print('Fortune:','liczba punktów:',n ,'czas:', (time.time() - start_time))

for n in [10, 50, 100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 10000]: 
    randomPoints = generate_uniform_points(-1000, 1000, n)
    measure_time(randomPoints, n)    

    