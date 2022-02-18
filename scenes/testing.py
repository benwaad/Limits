from manim import *
from objects.sequence import Sequence

class TestScene(Scene):
    def construct(self):
        zoom = 5
        fnc = lambda n: zoom - zoom/(np.sqrt(n))
        seq = Sequence.from_expression(fnc, num=100, radius=0.02)
        seq.set_fill(BLUE)

        self.play(
            AnimationGroup(
                *[FadeIn(dot) for dot in seq],
                lag_ratio=.001
            )
        )

        self.play(
            seq.animate.spread(3, origin=fnc(100))
        )
        self.wait()