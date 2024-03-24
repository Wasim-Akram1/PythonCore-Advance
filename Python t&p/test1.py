'''import amodule1
import amodule1
import amodule1
print("I am a test Module")
import amodule1'''

import time
import importlib
import amodule1
print("Time Started")
time.sleep(30)
importlib.reload(amodule1)
print("Time Ended")
dir(lib)
