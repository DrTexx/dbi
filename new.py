'''
Created on 19 Mar. 2018

@author: Denver
'''

from time import sleep
import sys

def print_slowly(text):
    for c in text:
        print(c,end=''),
        sys.stdout.flush()
        sleep(0.5)

print_slowly('LOA')