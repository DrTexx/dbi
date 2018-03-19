'''
Created on 19 Mar. 2018

@author: Denver
'''

from dbi import dbi
from time import sleep
db = {'debug_active': True,'verbosity_level': 3}

def sf1(): sleep(1)

dbi(db,1,"now we'll wait","!EXEC!:sf1()","finished waiting!")
dbi(db,2,"now we'll wait","!EXEC!:sf1()","finished waiting!")
dbi(db,3,"now we'll wait","!EXEC!:sf1()","finished waiting!")
dbi(db,3,"now we'll wait","!EXEC!:sf1()","finished waiting!")
dbi(db,2,"now we'll wait","!EXEC!:sf1()","finished waiting!")
dbi(db,2,"now we'll wait","!EXEC!:sf1()","finished waiting!")
dbi(db,1,"now we'll wait","!EXEC!:sf1()","finished waiting!")