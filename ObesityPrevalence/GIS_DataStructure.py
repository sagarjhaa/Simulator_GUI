""" this is global class for three files """
class City:
    def __init__(self, cityPoint, cityName = None):
        self.Color = "white"
        self.X = cityPoint[0][0]
        self.Y = cityPoint[0][1]
        self.Name = cityName;

class County:
    def __init__(self, polygon, polygonName = None):
        self.Color = "white"
        self.Coordinate = polygon
        self.Name = polygonName

class Highway:
    def __init__(self, roadSet, roadName = None):
        self.Color = "red"
        self.Coordinate = roadSet
        self.Name = roadName