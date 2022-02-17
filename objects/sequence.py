import numpy as np
from manim import *

class Sequence(VGroup):

    def __init__(self, *points, **kwargs):
        super().__init__(**kwargs)
        self.add(*points)
    
    @staticmethod
    def from_range(start, stop, num=20, **kwargs):
        '''Emulates np.linspace behaviour'''
        radius = .05
        positions = np.zeros((num, 3))
        positions[:,0] = np.linspace(start, stop, num)
        points = [Dot(pos, radius=radius) for pos in positions]
        return Sequence(*points, **kwargs)
    
    def apply_function(self, func, **kwargs):
        self.set_points(np.array([func(d, **kwargs) for d in self]))
        return self
    
    def along_function(self, func):
        centers = self.get_centers()
        centers[:,1] = func(centers[:,0])
        new_points = [d.copy() for d in self]
        [d.move_arc_center_to(c) for d, c in zip(new_points, centers)]
        return Sequence(*new_points)
        

    def get_centers(self):
        return np.array([point.get_arc_center() for point in self])

