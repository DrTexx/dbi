'''
Created on 19 Mar. 2018

@author: Denver
'''

from dbi import dbi
from time import sleep
db = {'debug_active': True,'verbosity_level': 3}

dbi(db,1,"now we'll wait","!EXEC!:sleep(1)","finished waiting!")