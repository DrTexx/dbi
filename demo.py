'''
Created on 19 Mar. 2018
@author: Denver
'''

def run_demo():
    from dbi.dbi import Dbi
    dbi = Dbi(3,True) # arg1: inital verbosity, arg2: if messages should print
    dpm = dbi.print_message # shorthand alternative
    print("verbosity = 3")
    print("all messages should print")
    dpm(1,"<basic debug info>")
    dpm(2,"<advanced debug info>")
    dpm(3,"<expert debug info>")
    dpm(1,"this message has a","sub-message")
    dpm(2,"User","John34","changed first name to","John")
    dpm(3,"User","John34","opened email in interface","new front-end proposal")
    print("verbosity = 2")
    dbi.verb = 2
    print("only messages with min_verb 2 or lower will print...")
    dpm(1,"<basic debug info>")
    dpm(2,"<advanced debug info>")
    dpm(3,"<expert debug info>")
    dpm(1,"this message has a","sub-message")
    dpm(2,"User","John34","changed first name to","John")
    dpm(3,"User","John34","opened email in interface","new front-end proposal")
    print("end of demo")

if __name__ == "__main__":
    run_demo()
    

#dpm(1,"generating a random number...","!EXEC!:demo_tools.RNG()","random number generated!: ","!EXEC!:demo_tools.printRNG()")
#dpm(2,"waiting for 3 seconds...","!EXEC!:demo_tools.sleepfor(3)","finished waiting!")
#dpm(3,"waiting for 3 seconds...","!EXEC!:demo_tools.sleepfor(3)","finished waiting!") # although the verbosity level is be default under 3, the functions here should still execute
#dbi_script(db,1,"!EXEC!:demo_tools.RNG()","generated a random number!: ","!EXEC!:demo_tools.printRNG()")
#dbi_script(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#bi(db,3,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#dbi_script(db,2,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
#dbi_script(db,1,"now we'll wait","!EXEC!:demo_tools.sf1()","finished command!")
