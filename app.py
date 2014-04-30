import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
print sys.path

from flow.server import *

app_start()
