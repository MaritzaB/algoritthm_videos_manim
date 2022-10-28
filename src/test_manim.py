from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class Grafo(Scene):
    def construct(self):
        circle_1 = Circle(radius=0.3).move_to(LEFT + UP)
        circle_2 = Circle(radius=0.3, color=GREEN).move_to(LEFT + DOWN)
        circle_3 = Circle(radius=0.3, color=BLUE, fill_opacity=1).move_to(RIGHT*2 + UP*2)
        circle_4 = Circle(radius=0.3, color=BLUE, fill_opacity=1).move_to(RIGHT*2 + DOWN*2)
        circle_5 = Circle(radius=0.3, color=BLUE, fill_opacity=1).move_to(UP*2)
        circle_6 = Circle(radius=0.3, color=BLUE, fill_opacity=1).move_to(DOWN*2)
        circle_6 = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        circle_group = Group(circle_1,circle_2,circle_3,circle_4,circle_5,circle_6)
        self.add(circle_group)

class Letras(Scene):
    def construct(self):
        title = Text("Minimum Spanning Tree", color=BLUE).scale(1.5)
        description = Text("Ejemplo de MST", gradient=(BLUE,GREEN)).next_to(title, DOWN)
        name = Text("Ana Maritza Bello Yañez", slant=ITALIC).next_to(title, UP).move_to(LEFT*3 + UP)
        self.add(title)
        self.play(FadeIn(description))
        self.play(Write(name))
        self.wait(2)
        self.remove(title)
        self.wait(2)
        self.remove(description)
        self.wait(5)
