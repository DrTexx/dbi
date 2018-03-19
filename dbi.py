# debugging interface module
# script by Denver P.
# Conception: 14-03-2018
# Revision 001: 14-03-2018

# import necessary modules
import datetime
import sys
import time

# set necessary variables
now = datetime.datetime.now

# define functions
def dbi(db,min_level,*args):
    if db['debug_active'] and min_level <= db['verbosity_level']: # check debug is True and level is okay
        prefixes = {'1': "lvl1!",
                    '2': "lvl2!",
                    '3': "lvl3!"}
        al = [item for item in args]
        sys.stdout.write("[%s][%s]: " % (now().isoformat('T'),prefixes[str(db['verbosity_level'])])) # write standard time stamp
        for i in range(len(al)): # for each argument supplied
            print("i =",i)
            if isinstance(al[i],str): # if this arg is a string
                print(al[i],"is a string")
                sys.stdout.write(al[i])
                if (len(al) - 1 < 0): # if a previous item exists
                    print("there's an item before this one")
                    if (isinstance(al[i + 1],str)): # if next arg is a string
                        print("there's another string after this one")
                        sys.stdout.write(" | ")
                    else: # if the next arg isn't a string
                        pass
                else: # this is the last item in the list
                    pass
            else: # if this arg isn't a string
                print("is not a string:",al[i])
                try: al[i] # try executing it
                except: raise Exception("COULDN'T RUN CODE IN DBI!") # otherwise raise an exception
        print("")

## do an 'in-script test'
# whether to run the test
runThisTest = False
# body of code for test
if(runThisTest):
    test = {'bool': True}
    
    def change(my_dict):
            time.sleep(1)
            my_dict['bool'] = False
    
    db = {'debug_active': True, 'verbosity_level': 1}
    print(test['bool'])
    dbi(db,1,"hello!","changing...",change(test),"changed!","goodbye!")
    print(test['bool'])
