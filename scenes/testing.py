from manim import *
from objects.sequence import Sequence

class TestScene(Scene):
    def construct(self):
        def pfunc(t):
            return np.array([t, np.cos(3*t), 0])
        graph = ParametricFunction(
            pfunc,
            t_range=np.array([-5,5]),
            stroke_width=1
        )
        expr = lambda n: 2*PI/3 - 3/(n+1)
        seq = Sequence.on_graph(graph, expr, num=50, radius=.05).set_color(BLUE)
        
        self.play(Create(graph))
        self.play(ShowIncreasingSubsets(seq, rate_func=rate_functions.ease_in_quad), run_time=2)
        self.wait()






