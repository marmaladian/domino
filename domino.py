import pygame as pg
from ppu import PPU



# define a main function
def main():
    
    pg.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pg.display.set_caption("domino")
     
    # screen area
    #   20x18 tiels
    # border
    #   2x2 tiles (1 tile border)
    # debug spacing
    #   1 tile
    # debug area
    #   20x3
    # total
    #   22x23 8px tiles 176 x 184, 2x zoom = 352 x 368, 4z zoom = 704x736

    
    screen = pg.display.set_mode((704,768))

    # ppu_display = pg.image.load("640x576.png")
    dbg_display = pg.image.load("640x96.png")
    dbg_display = pg.transform.scale(dbg_display, (640, 96))

    ppu_size = (160, 144)
    zoom = 4
    ppu_zoom_size = (ppu_size[0] * zoom, ppu_size[1] * zoom)
    ppu = PPU(pg.Surface(ppu_size))



    running = True

    while running:
        # event handling, gets all event from the event queue
        for event in pg.event.get():
            # only do something if the event is of type QUIT
            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False
        screen.fill((18,10,25))
        ppu.random()
        ppu_surf_zoom = pg.Surface(ppu_zoom_size)
        pg.transform.scale(ppu.surf, ppu_zoom_size, dest_surface=ppu_surf_zoom)
        screen.blit(ppu_surf_zoom, (32,32))
        screen.blit(dbg_display, (32,640))
        pg.display.flip()
        pg.time.delay(300)
     
if __name__=="__main__":
    main()