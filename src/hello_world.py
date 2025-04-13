from manimlib import *
from os import system

class TextDemo(Scene):
    def construct(self):
        tex = Text("Hello, World!", font_size=72, color=WHITE)
        animation = Write(tex)
        self.play(animation)
        self.wait(1)

if __name__ == '__main__':
    system('manimgl {} TextDemo --config_file ../custom_config.yml'.format(__file__))