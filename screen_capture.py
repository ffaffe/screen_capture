import pyautogui as pag
from time import sleep
import random

# safety time
pag.FAILSAFE = True     # move cursor to top of screen to exit program

# def on_scrn_chk():
#     pag.onScreen(1, 210)


# adding some mouse functions
def move_mouse():
    pag.moveTo(x, y, duration=0)


# clicky click time
def sngl_click():
    pag.click(clicks=1, interval=0.1, button='left')    #(x=1, y=1, clicks=1, interval=1, button='left')


def dbl_click():
    pag.click(clicks=2, interval=0.1, button='left')


def rt_click():
    pag.click(clicks=1, interval=0.1, button='right')

def drag_mouse():
    pag.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
    pag.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position


for _ in range(1):
    m_pos = pag.position()
    screen_sz = pag.size()
    on_scrn = pag.onScreen(m_pos)
    print(on_scrn)
    print(m_pos, screen_sz)
    # random ints for mouse moves
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    move_mouse()
    sngl_click()
    rt_click()
    sleep(0)

# pag.alert('This displays some text with an OK button.')
# pag.confirm('This displays text and has an OK and Cancel button.')



# sleep(1)
#
# shot1 = pag.screenshot(region=(0,0,1920, 1080))
# shot1.show()

find_loc = pag.locateOnScreen('capture1.PNG')
find_loc




exit()


