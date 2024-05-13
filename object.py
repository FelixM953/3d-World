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
        
class Pyramid:
    def __init__(self, position, width, height):
        self.origin = position
        self.vertecies = [
            (-width/2, height/2, -width/2), (width/2, height/2, -width/2), (width/2, height/2, width/2), (-width/2, height/2, width/2),
            (0, -height/2, 0)
        ]
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (0, 4), (1, 4), (2, 4), (3, 4)
        ]
