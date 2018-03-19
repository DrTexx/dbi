"""
DEMO_TOOLS - THIS FILE WILL CHANGE BASED ON THE REQUIREMENTS OF THE PARENT SCRIPT USED
this file contains all functions, variables and imports (variable, function, etc.) required to run in-line executions
"""
from time import sleep # allows for various functions to work involving delays
import random # allows for RNG function to work
import test # allows variables to carry over from parent script


def sleepfor(x):
    sleep(x)
    
def sf1():
    sleep(1)
    
def sf3():
    sleep(3)
    
def RNG():
    test.dbi_out['RNG_out'] = random.random()
    
def printVar():
    print(test.dbi_out['RNG_out'],end='',flush=True)
    