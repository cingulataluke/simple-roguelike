import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20  #for use in real time
libtcod.console_set_custom_font('terminal.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INCOL)  #loads custom font
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)  #window init

while not libtcod.console_is_window_closed():  #main loop, each time it loops = 1 turn
    libtcod.console_set_default_foreground(0, libtcod.white)  #set text to white
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)  #puts an @ in (1,1)
    libtcod.console_flush()  #refreshes the window so you can see the changes made in the loop