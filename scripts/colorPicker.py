import pyautogui

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
MOUSE_X, MOUSE_Y = pyautogui.position()

PIXEL = pyautogui.screenshot(
    region=(MOUSE_X, MOUSE_Y, 1, 1)
)
COLOR = PIXEL.getcolors()
print("RGB: %s" % (COLOR[0][1].__str__()))