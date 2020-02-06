from display import *
from draw import *

s = new_screen()

#octants 1 and 5
c = [0, 255, 0] #green
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, int(YRES / 2), s, c)
draw_line(XRES-1, YRES-1, 0, int(YRES / 2), s, c)

#octants 8 and 4
c = [0, 255,255] #blue
draw_line(0, YRES-1, XRES-1, 0, s, c);
draw_line(0, YRES-1, XRES-1, int(YRES/2), s, c);
draw_line(XRES-1, 0, 0, int(YRES/2), s, c);

#octants 2 and 6
c = [255,0,0] #red
draw_line(0, 0, int(XRES / 2), YRES-1, s, c);
draw_line(XRES-1, YRES-1, int(XRES / 2), 0, s, c);

#octants 7 and 3
c = [255,0,255] #magenta
draw_line(0, YRES-1, int(XRES / 2), 0, s, c);
draw_line(XRES-1, 0,int(XRES / 2), YRES-1, s, c);

#horizontal and vertical
c = [255,255,0] #yellow
draw_line(0, int(YRES/2), XRES-1, int(YRES/2), s, c);
draw_line(int(XRES / 2), 0, int(XRES / 2), YRES-1, s, c);


# display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
