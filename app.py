import time
import random
import pyautogui
import rotatescreen

def move_mouse(tsec):
    start_time = time.time()
    time_elapsed = time.time() - start_time
    xsize, ysize = pyautogui.size()
    
    while time_elapsed < tsec:
        x, y = random.randrange(xsize), random.randrange(ysize)
        pyautogui.moveTo(x, y, duration=0.05)
        time_elapsed = time.time() - start_time

if __name__ == "__main__":
    pyautogui.alert(text='Click the button to continue...', title='Confirmation', button='START')
    move_mouse(7)

rot = rotatescreen.get_primary_display()
for rota in range(0,21):
    time.sleep(0.5)
    rot.rotate_to(rota*90%360)

pyautogui.alert(text='You survived the prank!', title='Message', button='END')
