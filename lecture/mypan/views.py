from django.contrib.admin import display
from icecream import ic

from lecture.mypan.Quiz import MyPan


if __name__ == '__main__':
    mpd = MyPan()
    ic(display(mpd.Quiz01()))
    ic(display(mpd.Quiz02()))