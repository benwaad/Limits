import numpy as np
from manim import *

class Sequence(VGroup):

    def __init__(self, *points, **kwargs):
        super().__init__(**kwargs)
        self.add(*points)
    
    @staticmethod
    def from_range(start, stop, num=20, radius=.05, **kwargs):
        '''Emulates np.linspace behaviour'''
        positions = np.zeros((num, 3))
        positions[:,0] = np.linspace(start, stop, num)
        points = [Dot(pos, radius=radius) for pos in positions]
        return Sequence(*points, **kwargs)
    
    @staticmethod
    def from_expression(map, num=20, radius=.05):
        '''map maps from naturals to sequence elements'''
        pass
    
    def apply_function(self, func, **kwargs):
        '''Function is meant in the mathematical sense. Design methods
        are applied element-wise by default for VGroups'''
        centers = self.get_centers()
        shifts = func(centers[:,0], **kwargs)
        for dot, sh in zip(self, shifts):
            dot.shift(sh * UP)
        return self

    
    def along_function(self, func):
        centers = self.get_centers()
        centers[:,1] = func(centers[:,0])
        new_points = [d.copy() for d in self]
        [d.move_arc_center_to(c) for d, c in zip(new_points, centers)]
        return Sequence(*new_points)
        

    def get_centers(self):
        return np.array([point.get_arc_center() for point in self])

