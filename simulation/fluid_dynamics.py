import numpy as np

class SurfboardHydrodynamics:

    def __init__(self, length, width, rocker):

        self.length = length
        self.width = width
        self.rocker = rocker

    def drag_force(self, velocity):

        rho = 1025
        Cd = 0.08
        area = self.length * self.width

        drag = 0.5 * rho * velocity**2 * Cd * area

        return drag

    def lift(self, velocity):

        rho = 1025
        Cl = 0.3
        area = self.length * self.width

        lift = 0.5 * rho * velocity**2 * Cl * area

        return lift

    def performance_score(self, velocity):

        drag = self.drag_force(velocity)
        lift = self.lift(velocity)

        score = lift / (drag + 1)

        return score
