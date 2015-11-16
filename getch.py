#Adapted from: http://stackoverflow.com/questions/32671306/how-can-i-read-keyboard-input-in-python
#usr/bin/env python

import sys


#Tries a couple of potentialy built in packages to enable the retrival of single charecters from the keybaord.
try:
    import tty, termios
except ImportError:
    try:
        import msvcrt
    except ImportError:
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
	#Assuming it can find one it attempts to return the first keyboard key pressed.
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
