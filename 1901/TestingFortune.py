from foronoi import Voronoi, Polygon, Visualizer, VoronoiObserver

points = [
    (2.5, 2.5),
    (4, 7.5),
    (7.5, 2.5),
    (6, 7.5),
    (4, 4),
    (3, 3),
    (6, 3),
]

polygon = Polygon([
    (2.5, 10),
    (5, 10),
    (10, 5),
    (10, 2.5),
    (5, 0),
    (2.5, 0),
    (0, 2.5),
    (0, 5),
])

v = Voronoi(polygon)

v.attach_observer(VoronoiObserver())

v.create_diagram(points=points)

edges = v.edges
vertices = v.vertices
arcs = v.arcs
points = v.points


