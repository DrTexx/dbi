'''
Created on 19 Mar. 2018

@author: Denver
'''

from time import sleep
from dbi import dbi
db = {'debug_active': True,'verbosity_level': 3,'db_imports': ['demo_tools']}

dbi(db,1,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,2,"now we'll wait","!EXEC!:demo_tools.sf2()","finished command!")
dbi(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,1,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")