from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1 < x0:
        x1, x0 = x0, x1
        y1, y0 = y0, y1

    if x1-x0 == 0 and y1-y0 != 0: #vertical line
        for y in range(y0, y1+1):
            screen[y][x0] = color
    else:
        slope = (y1-y0)/(x1-x0)
        if slope == 0: #horizontal line
            for x in range(x0, x1+1):
                screen[y0][x] = color

        x = x0
        y = y0

        A = y1-y0
        B = -(x1-x0)

        A2 = 2*A
        B2 = 2*B

        if 0 < slope and slope < 1: #octant 1
            d = A2 + B
            while x <= x1:
                screen[y][x] = color
                if d > 0:
                    y = y + 1
                    d = d + B2
                x = x + 1
                d = d + A2

        if 1 == slope:
            while x <= x1:
                screen[y][x] = color
                y = y + 1
                x = x + 1

        if 1 < slope: # octant 2
            d = A + B2
            while y <= y1:
                screen[y][x] = color
                if d < 0:
                    x = x + 1
                    d = d + A2
                y = y + 1
                d = d + B2

        if -1 < slope and slope < 0: #octant 8
            d = A2 + B
            while x <= x1:
                screen[y][x] = color
                if d < 0:
                    y = y - 1
                    d = d - B2
                x = x + 1
                d = d + A2

        if slope == -1:
            while x <= x1:
                screen[y][x] = color
                x = x + 1
                y = y - 1

        if slope < -1: #octant 7
            d = A + B2
            while y >= y1:
                screen[y][x] = color
                if d > 0:
                    x = x + 1
                    d = d + A2
                y = y - 1
                d = d - B2
