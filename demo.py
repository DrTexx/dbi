'''
Created on 19 Mar. 2018
@author: Denver
'''

from dbi import Dbi
dbi = Dbi(3,True)
dpm = dbi.print_message

def run_demo():
    dpm(1,"some basic debug info.")
    dpm(2,"more advanced debug info.")
    dpm(3,"ridiculous amounts of debug info!")
    dpm(2,"this message has a","sub-message")

if __name__ == "__main__":
    run_demo()
    

#from dbi_script.dbi_script import dbi_script
#db = {'debug_active': True,'verbosity_level': 3,'db_imports': ['demo_tools']}
#dpm(1,"generating a random number...","!EXEC!:demo_tools.RNG()","random number generated!: ","!EXEC!:demo_tools.printRNG()")
#dpm(2,"waiting for 3 seconds...","!EXEC!:demo_tools.sleepfor(3)","finished waiting!")
#dpm(3,"waiting for 3 seconds...","!EXEC!:demo_tools.sleepfor(3)","finished waiting!") # although the verbosity level is be default under 3, the functions here should still execute
#dpm(2,"finished running previous command, even if the verbosity level was lower!")
#dbi_script(db,1,"now we'll wait","just for 1 second","!EXEC!:demo_tools.sf1()","finished command!")
#dbi_script(db,1,"!EXEC!:demo_tools.RNG()","generated a random number!: ","!EXEC!:demo_tools.printRNG()")
#dbi_script(db,2,"now we'll wait","!EXEC!:demo_tools.sf3()","finished command!")
#dbi_script(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#bi(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#bi(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#dbi_script(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#dbi_script(db,1,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
