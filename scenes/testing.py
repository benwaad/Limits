from manim import *
from objects.sequence import Sequence

class TestScene(Scene):
    def construct(self):
        seq = Sequence.from_range(-2, 2, )
        seq.set_fill(RED)
        f = lambda x: 0.2 * x**3 - 1
        along_f = seq.along_function(f)
        

        self.play(
            AnimationGroup(
                *[FadeIn(dot) for dot in seq],
                lag_ratio=.05
            )
        )
        self.play(ReplacementTransform(seq, along_f))
        self.wait()