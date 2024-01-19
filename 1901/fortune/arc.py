from decimal import Decimal

from foronoi.graph.coordinate import Coordinate


class Arc:
    def __init__(self, origin: Coordinate, circle_event=None):
        self.origin = origin
        self.circle_event = circle_event

    def __repr__(self):
        return f"Arc({self.origin.name})"

    def get_plot(self, x, sweep_line):

        sweep_line = float(sweep_line)
        i = self.origin

        if i.y - sweep_line == 0:
            return None

        # Calculate the y value for each element of the x vector

        u = 2 * (i.y - sweep_line)
        v = (x ** 2 - 2 * i.x * x + i.x ** 2 + i.y ** 2 - sweep_line ** 2)
        y = v/u

        return y
