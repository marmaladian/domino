#import array
from curses import keyname
from email import message
from operator import xor
from urllib import response
import pygame as pg
import numpy as np
import random

_MEMORY_SIZE = 2**16

# paletters
# red, red, red
# green, red, black, white
# white, black, cyan, redmagenta
# yellow, 
# white, purpley blue, black
# all greys


class PPU:
    # 20 x 18, 8px tiles

    def __init__(self, surf: pg.Surface):
        # self.mem = array.array('B', [0 for i in range(_MEMORY_SIZE)])
        self.surf = surf
        self.mem = pg.surfarray.array2d(surf)
        #bg 120a19, #fg c01923
        self.palette = [ self.surf.map_rgb(pg.Color(0x120A19FF)),
                         self.surf.map_rgb(pg.Color(0xC01923FF)),
                         self.surf.map_rgb(pg.Color(0xE23D69FF)),
                         
                       ]
        self.random()

    def random(self):
        with np.nditer(self.mem, op_flags=['writeonly']) as it:
            for pxl in it:
                pxl[...] = int(random.choice(self.palette))
        pg.surfarray.blit_array(self.surf, self.mem)