import pyautogui as pag


# mouse functions
# move
def move_mouse():
    pag.moveTo(x, y, duration=0)


# clicks
def sngl_click():
    pag.click(clicks=1, interval=1, button='left')    #(x=1, y=1, clicks=1, interval=1, button='left')


def dbl_click():
    pag.click(clicks=2, interval=1, button='left')


def rt_click():
    pag.click(clicks=1, interval=1, button='right')