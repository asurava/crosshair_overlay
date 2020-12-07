import win32gui
import win32api
import win32con
import win32ui

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

center_X = int(width / 2)
center_Y = int(height / 2)

distance = 10 # size of square

red = win32api.RGB(255, 0, 0) # Red

dc = win32gui.GetDC(0) # get screen's device context
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (center_X - distance, center_Y - distance, center_X + distance, center_Y + distance)

past_coordinates = monitor

while True:
    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

    # draw square
    for x in range(distance):
        win32gui.SetPixel(dc, center_X + x, center_Y, red)
        win32gui.SetPixel(dc, center_X + x, center_Y + distance, red)
    for y in range(distance):
        win32gui.SetPixel(dc, center_X, center_Y + y, red)
        win32gui.SetPixel(dc, center_X + distance, center_Y + y, red)

    past_coordinates = (center_X - distance*2, center_Y - distance*2, center_X + distance*2, center_Y + distance*2)