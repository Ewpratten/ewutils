from ewutils.terminal.linefmt import *
from ewutils.terminal.curses import *

import time

arrowRight("Arrows", "To", "The", "Right")
arrowLeft("Arrows", "To", "The", "Left")

inform("Normal", "foo")
inform("Warning", "foo", Urgency.Warning)
inform("Error", "foo", Urgency.Error)
inform("Success", "foo", Urgency.Success)

hideShell()
place("Hello", 5,10)
time.sleep(2)
showShell()