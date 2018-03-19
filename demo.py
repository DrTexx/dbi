'''
Created on 19 Mar. 2018

@author: Denver
'''

from dbi import dbi
db = {'debug_active': True,'verbosity_level': 3,'db_imports': ['demo_tools']}

dbi(db,1,"now we'll wait","just for 1 second","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,1,"!EXEC!:demo_tools.RNG()","generated a random number!: ","!EXEC!:demo_tools.printRNG()")
dbi(db,2,"now we'll wait","!EXEC!:demo_tools.sf3()","finished command!")
dbi(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
dbi(db,1,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
