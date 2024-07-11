from manim import *

class Formula(Scene):

    def construct(self):
        t = MathTex(r"\sum_{i=1} ^{\infty} x^i \prod_{j=1} ^{a} (i+j)", color = BLUE)
        t.generate_target()
        t.target.shift(2*UP + 3*LEFT)
        self.play(Create(t))
        self.wait(2)
        self.play(MoveToTarget(t))
        self.wait(4)

        m = MathTex(r"\sum_{i=1} ^{\infty} x^i \prod_{j=1} ^{a} (i+j) = \sum_{i=1} ^{\infty} x^i \prod_{j=1} ^{a} (i+j) \frac{i!a!}{i!a!}", color = BLUE)
        m.move_to(2*UP)
        self.play(Transform(t,m))
        self.wait(2)

        p = MathTex(r" = a!\sum_{i=1} ^{\infty} x^i \binom{i+a}{i}", color = BLUE)
        p.generate_target()
        p.target.shift(RIGHT*(1.5))
        self.play(MoveToTarget(p))
        self.wait(4)

        self.play(FadeOut(t,m,p))

        n = MathTex(r"a!\sum_{i=1} ^{\infty} x^i \binom{i+a}{i} = a!(1-x)^{-(a+1)}", color = BLUE)
        self.play(Create(n))
        self.wait(4)
        self.play(FadeOut(n))

        text = Text("By: Aadi Jain", font_size = 50, color = BLUE)
        goodbye = Text("Thank You!", font_size = 25, color = BLUE)
        goodbye.next_to(text, DOWN)
        self.play(Create(text))
        self.play(Create(goodbye))
        self.wait(4)

        

