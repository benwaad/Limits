import numpy as np
from manim import *

class Sequence(VGroup):

    def __init__(self, *points, **kwargs):
        super().__init__(**kwargs)
        self.y_lock = 0
        self.add(*points)
    
    @staticmethod
    def from_range(start, stop, num=20, radius=.05, **kwargs):
        '''Emulates np.linspace behaviour'''
        positions = np.zeros((num, 3))
        positions[:,0] = np.linspace(start, stop, num)
        points = [Dot(pos, radius=radius) for pos in positions]
        return Sequence(*points, **kwargs)
    
    @staticmethod
    def from_expression(map, num=20, radius=.05, **kwargs):
        '''map maps from naturals to sequence elements'''
        seq = map(np.arange(1, num+1))
        positions = np.zeros((num, 3))
        positions[:,0] = seq
        points = [Dot(pos, radius=radius) for pos in positions]
        return Sequence(*points, **kwargs)

    def spread(self, factor, origin=0):
        for dot in self:
            dot.set_x((dot.get_x()-origin) * factor + origin)
        return self
    
    def apply_function(self, func, **kwargs):
        '''Function is meant in the mathematical sense. Design methods
        are applied element-wise by default for VGroups'''

        for dot in self:
            y = dot.get_y()
            dot.set_y(y + func(dot.get_x(), **kwargs))
        return self
    
    def lock_y(self):
        self.y_lock = self.get_y()
    
    def collapse(self):
        for dot in self:
            dot.set_y(self.y_lock)
        return self

    
    def along_function(self, func):
        centers = self.get_centers()
        centers[:,1] = func(centers[:,0])
        new_points = [d.copy() for d in self]
        [d.move_arc_center_to(c) for d, c in zip(new_points, centers)]
        return Sequence(*new_points)
        

    def get_centers(self):
        return np.array([point.get_center() for point in self])

