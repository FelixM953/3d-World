class Cube:
    def __init__(self, position, scale):
        self.origin = position
        self.vertecies = [
            (-scale/2, -scale/2, -scale/2), (scale/2, -scale/2, -scale/2), (scale/2, scale/2, -scale/2), (-scale/2, scale/2, -scale/2),
            (-scale/2, -scale/2,  scale/2), (scale/2, -scale/2,  scale/2), (scale/2, scale/2,  scale/2), (-scale/2, scale/2,  scale/2)
            ]
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
                 ]
