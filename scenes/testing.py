from manim import *
from objects.sequence import Sequence

class TestScene(Scene):
    def pfunc(self, t):
        return np.array([t, np.cos(3*t), 0])
    def construct(self):
        graph = ParametricFunction(
            self.pfunc,
            t_range=np.array([-5,5]),
            stroke_width=1
        )
        expr = lambda n: 2*PI/3 - 3/(n+1)
        seq = Sequence.on_graph(graph, expr, num=50, radius=.05).set_color(BLUE)
        
        
        self.add(graph)
        self.play(Create(seq), run_time=1.2)
        self.wait()






