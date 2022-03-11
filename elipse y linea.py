import cv2 as draw, numpy as np 
def draw_line():
    window = np.ones ((550,770,3), dtype = np.uint8)*40
    draw.line(window(120,270),
              (600,250),
              (160,93,20),
              5)
    )
    draw.imshow('line', window)
    draw.waitkey()
    draw.destroyAllwindows()
    
    def draw_elipse():
        window = np.ones((550,770,3),dtype=np.uint8)*40
        draw.elipse(window,(350,250),
                    (200,150),
                    0,
                    0,
                    360,
                    (150,83,20)
                    ,5
                    )
        draw.imshow('elipse',window)
        draw.waitkey()
        draw.destroyAllwindows()
draw_line()
draw_elipse()        