from manimlib import *
from os import system

class TextDemo(Scene):
    def construct(self):
        tex = Tex("君安。")
        animation = Write(tex)
        self.play(animation)
        self.wait(1)

if __name__ == '__main__':
    system('manimgl {} TextDemo --config_file ../custom_config.yml'.format(__file__))