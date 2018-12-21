from random import choice

class RandomWalk():
    """ A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributesof a walk"""
        self.num_points = num_points

        # ALL walks start(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction - choice([1, -1])
            x_distance = choice([0,1,2,3,4])
