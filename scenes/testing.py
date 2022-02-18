from manim import *
from objects.sequence import Sequence

class TestScene(Scene):
    def construct(self):
        seq = Sequence.from_range(-4, 4, num=400, radius=0.05)
        seq.set_fill(RED)
        f = lambda x: np.sin(2*x)
        g = lambda x: .2*np.cos(10*x)
        # along_f = seq.along_function(f)
        # along_gf = along_f.along_function(g)

        
        #creations = [FadeIn(dot) for dot in seq]
        self.play(
            AnimationGroup(
                *[FadeIn(dot) for dot in seq],
                lag_ratio=.001
            )
        )
        # Make animations before play

        #self.play(*creations, run_time=1)
        self.play(seq.animate.apply_function(f))
        self.play(seq.animate.apply_function(g))
        self.wait()