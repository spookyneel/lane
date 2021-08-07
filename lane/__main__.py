import asyncio
import sys
import importlib
from os.path import dirname
from sys import platform

from lane import laneClient, laneBotClient
from lane.plugins import ALL_MODULES

IMPORTED = {}

# Check sys type
if platform == "linux" or platform == "linux2":
    path_dirSec = '/'
elif platform == "win32":
    path_dirSec = '\\'

cdir = dirname(__file__) 
for mode in ALL_MODULES: 
    module = mode.replace(cdir, '').replace(path_dirSec, '.')
    imported_module = importlib.import_module('lane' + module)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    
    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")
        

if __name__ == '__main__':
    laneClient.run()
    laneBotClient.run()