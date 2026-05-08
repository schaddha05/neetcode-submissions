class CountSquares:
    from collections import defaultdict
    def __init__(self):
        self.points = defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # for diagonal points of square we know abs(x1-x2) = abs(y1-y2)
        # that absolute difference is the side length, so if we find the diagonals we can find the other points
        res = 0 
        qx = point[0]
        qy = point[1]
        # query point can be top left/right or bottom left/right
        for p in self.points:
            if abs(p[0] - qx) == abs(p[1] - qy) and abs(p[0] - qx) != 0: # if diagonal
                if (qx, p[1]) in self.points and (p[0], qy) in self.points: 
                    res += self.points[(qx, p[1])] * self.points[(p[0], qy)] * self.points[p]
        return res



