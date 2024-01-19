import heapq
from typing import List, Tuple
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rot(self):
        return Point(-self.y, self.x)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def len(self):
        return math.hypot(self.x, self.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def __mul__(self, f):
        return Point(self.x * f, self.y * f)

class Arc:
    def __init__(self, p, q, i):
        self.p = p
        self.q = q
        self.id = i

    def get_y(self, x):
        if self.q.y == float('inf'):
            return float('inf')
        x += 1e-12
        med = (self.p + self.q) * 0.5
        direction = (self.p - med).rot()
        D = (x - self.p.x) * (x - self.q.x)
        return med.y + ((med.x - x) * direction.x + (D**0.5) * direction.len()) / direction.y

    def __lt__(self, y):
        return self.get_y(sweepx) < y

    def __lt__(self, other):
        return self.get_y(sweepx) < other.get_y(sweepx)

    def __repr__(self):
        return f"Arc({self.p}, {self.q}, {self.id})"
    
    def __len__(self):
        return math.isfinite(self.q.y)

def beach_comparator(arc):
    return arc.get_y(sweepx)

class Event:
    def __init__(self, x, event_id, arc_iterator):
        self.x = x
        self.id = event_id
        self.it = arc_iterator

    def __lt__(self, other):
        return self.x < other.x

    def __repr__(self):
        return f"Event({self.x}, {self.id}, {self.it})"

class Fortune:
    def __init__(self, points: List[Point]):
        self.line = []  # Using a list instead of a multiset
        self.v = [(pt, i) for i, pt in enumerate(points)]
        self.Q = []  # Priority queue of point and vertex events
        self.edges = []  # Delaunay edges
        self.valid = []  # valid[-id] == True if the vertex event with corresponding id is valid
        self.n = len(points)
        self.ti = 0  # Next available vertex ID
        self.solve()

    def collinear(self, a, b):
        return abs(a.cross(b)) < 1e-12

    def lineline(self, a, b, c, d):
        return a + (b - a) * ((c - a).cross(d - c) / (b - a).cross(d - c))

    def circumcenter(self, a, b, c):
        b = (a + b) * 0.5
        c = (a + c) * 0.5
        return self.lineline(b, b + (b - a).rot(), c, c + (c - a).rot())

    def upd(self, arc_iterator):
        if arc_iterator.id == -1:
            return
        self.valid[-arc_iterator.id] = False
        a = self.line[arc_iterator.index - 1] if arc_iterator.index > 0 else None
        if a and self.collinear(arc_iterator.q - arc_iterator.p, a.p - arc_iterator.p):
            return
        arc_iterator.id = -self.ti
        self.valid.append(True)
        c = self.circumcenter(arc_iterator.p, arc_iterator.q, a.p)
        x = c.x + (c - arc_iterator.p).len()
        if x > sweepx - 1e-12 and a.get_y(x) + 1e-12 > arc_iterator.get_y(x):
            heapq.heappush(self.Q, Event(x, arc_iterator.id, arc_iterator))

    def add_edge(self, i, j):
        if i == -1 or j == -1:
            return
        self.edges.append((self.v[i][1], self.v[j][1]))

    def add(self, i):
        p = self.v[i][0]
        c = next((arc for arc in sorted(self.line, key=beach_comparator) if arc.get_y(p.y + 1e-12) > p.y - 1e-12), None)
        b = self.line.insert(c.index, Arc(p, c.p, i))
        a = self.line.insert(b.index, Arc(c.p, p, c.id))
        self.add_edge(i, c.id)
        self.upd(a)
        self.upd(b)
        self.upd(c)

    def remove(self, arc_iterator):
        a = self.line[arc_iterator.index - 1]
        b = self.line[arc_iterator.index + 1] if arc_iterator.index + 1 < len(self.line) else None
        self.line.pop(arc_iterator.index)
        a.q = b.p
        self.add_edge(a.id, b.id)
        self.upd(a)
        self.upd(b)

    def solve(self, X=1e6):
        X *= 3
        self.line.append(Arc(Point(-X, -X), Point(-X, X), -1))
        self.line.append(Arc(Point(-X, X), Point(float('inf'), float('inf')), -1))

        for i in range(self.n):
            heapq.heappush(self.Q, Event(self.v[i][0].x, i, None))

        self.ti = 0
        self.valid = [False]

        while self.Q:
            e = heapq.heappop(self.Q)
            global sweepx
            sweepx = e.x

            if e.id >= 0:
                self.add(e.id)
            elif self.valid[-e.id]:
                self.remove(e.it)

    def print_edges(self):
        print("Delaunay Edges:")
        for edge in self.edges:
            print(f"{edge[0]} - {edge[1]}")

# Sample points for demonstration
points_sample = [
    Point(9.0, 3.0),
    Point(1.0, 4.0),
    Point(3.0, 1.0)]

delaunay_triangulation = Fortune(points_sample)

# Compute the Delaunay triangulation
delaunay_triangulation.print_edges()
