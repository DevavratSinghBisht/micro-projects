import rotatescreen
import time

def rotate_screen(angle = 90, no_of_rotations = 4):
    """
    A function that rotates the screen given number of time by a given angle
    angle : (int) angle of each rotation
    no_of_rotation : (int) total number of rotations to be performed
    """
    screen = rotatescreen.get_primary_display()
    for i in range(no_of_rotations):
        time.sleep(1)
        screen.rotate_to(i*angle%360)
