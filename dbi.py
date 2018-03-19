# debugging interface module
# script by Denver P.
# Conception: 14-03-2018
# r1: 2018-03-14
# r2: 2018-03-19

# import necessary modules
import datetime
import sys
import time

# import extra modules
importExtra = True
if(importExtra): from colorThis import ct

# set necessary variables
now = datetime.datetime.now

# define functions
def dbi(db,min_level,*args):
    if db['debug_active'] and min_level <= db['verbosity_level']: # check debug is True and level is okay
        prefixes = {'1': ct("lvl1!",Fore="GREEN"),
                    '2': ct("lvl2!",Fore="YELLOW"),
                    '3': ct("lvl3!",Fore="RED")}
        arg_list = [item for item in args]
        sys.stdout.write("[%s][%s]: " % (now().isoformat('T'),prefixes[str(db['verbosity_level'])])) # write standard time stamp
        for i in range(len(arg_list)): # for each argument supplied
            #print("i =",i)
            if isinstance(arg_list[i],str): # if this arg is a string
                #print(arg_list[i],"is a string")
                sys.stdout.write(arg_list[i])
                if (len(arg_list) - 1 < 0): # if a previous item exists
                    print("there's an item before this one")
                    if (isinstance(arg_list[i + 1],str)): # if next arg is a string
                        #print("there's another string after this one")
                        sys.stdout.write(" | ")
                    else: # if the next arg isn't a string
                        pass
                else: # this is the last item in the list
                    pass
            else: # if this arg isn't a string
                #print("is not a string:",arg_list[i])
                try: arg_list[i] # try executing it
                except: raise Exception("COULDN'T RUN CODE IN DBI!") # otherwise raise an exception
        print("")

## do an 'in-script test'
# whether to run the test
runThisTest = True
# body of code for test
if(runThisTest):
    test = {'bool': True}
    
    def change(my_dict):
            time.sleep(1)
            my_dict['bool'] = False
    
    db = {'debug_active': True, 'verbosity_level': 3}
    print(test['bool'])
    dbi(db,1,"testing level 1 verb...",change(test),"changed!")
    dbi(db,2,"testing level 2 verb...",change(test),"changed!")
    dbi(db,3,"testing level 3 verb...",change(test),"changed!")
    print(test['bool'])
