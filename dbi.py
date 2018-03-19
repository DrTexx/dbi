# debugging interface module
# script by Denver P.
# Conception: 14-03-2018
# r1: 2018-03-14
# r2: 2018-03-19

# import necessary modules
import datetime
import sys
import time
from colorThis import ct

# import extra modules

# set necessary variables
now = datetime.datetime.now

# define functions
def dbi(db,min_verb,*args):
    state_iteration=False
    verb = str(db['verbosity_level'])
    req_verb = min_verb
    
    if(db['debug_active'] and db['verbosity_level'] >= req_verb): # check debug is True and level is okay
        arg_list = [item for item in args]
        prefixes = {'1': ct("1",Fore="GREEN"),
                    '2': ct("2",Fore="YELLOW"),
                    '3': ct("3",Fore="RED")}
        print(
            "[%s][%s<=%s]: " % (now().isoformat('T'), # write standard time stamp
                                prefixes[verb], # state the parent script's verb level
                                prefixes[str(req_verb)]),
        end='') # state the minimum verb level to show this message
        sys.stdout.flush()
        for i in range(len(arg_list)): # for each arg supplied
            
            this_arg = arg_list[i]
            
            try: last_arg = arg_list[i - 1]
            except: del last_arg
            else: pass
            
            try: next_arg = arg_list[i + 1]
            except: del next_arg
            else: pass
            
            if(state_iteration):
                print("{i =",i,"}",end='')
                sys.stdout.flush()
                
            if isinstance(this_arg,str): # if this item is a string
                print(this_arg,end='')
                sys.stdout.flush()
                
                if('next_arg' in locals()): # if there's an item after this
                    
                    if (isinstance(next_arg,str)): # and it's a string
                        print(" | ",end='')
                        sys.stdout.flush()
                
            else: # if this arg isn't a string
                #print("is not a string:",arg_list[arg])
                try:
                    eval(this_arg[0]) # try executing it
                    sys.stdout.flush()
                except:
                    raise Exception("COULDN'T RUN CODE IN DBI!") # otherwise raise an exception
        print("")

## do an 'in-script test'
# whether to run the test
runThisTest = True
# body of code for test
if(runThisTest):
    
    db = {'debug_active': True, 'verbosity_level': 3}
    dbi(db,1,"testing level 1 verb...","doing it... ",['time.sleep(3)'],"changed!")
    dbi(db,2,"testing level 2 verb...","doing it... ",['time.sleep(3)'],"changed!")
    dbi(db,3,"testing level 3 verb...","doing it... ",['time.sleep(3)'],"changed!")

# if(runThisTest):
#     print("Without flushing the stdout stream")
#     for n in range(0,10):
#         print ("-",end="")
#         time.sleep(1.0)
#     print()
#     print("With flushing")
#     for n in range(0,10):
#         print("-",end="")
#         sys.stdout.flush()
#         time.sleep(1.0)