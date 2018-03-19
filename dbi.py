# debugging interface module
# script by Denver P.
# Conception: 14-03-2018
# r1: 2018-03-14
# r2: 2018-03-19

# import necessary modules
import datetime
from time import sleep
from colorThis import ct

# import extra modules

# set necessary variables
now = datetime.datetime.now

# define functions
def dbi(db,min_verb,*args):
    print_executions = False
    verb = str(db['verbosity_level'])
    req_verb = min_verb
    
    if(db['debug_active'] and db['verbosity_level'] >= req_verb): # check debug is True and level is okay
        arg_list = [item for item in args]
        prefixes = {'1': {'name': "1", 'style': 'GREEN'},
                    '2': {'name': "2", 'style': 'YELLOW'},
                    '3': {'name': "3", 'style': 'RED'}}
        message_color = prefixes[str(req_verb)]['style']
        print(
            "[%s][%s]<=[%s]: " % (
                ct(prefixes[verb]['name'],Fore=prefixes[verb]['style']), # state the parent script's verb level
                ct(prefixes[str(req_verb)]['name'],Fore=message_color),
                ct(now().isoformat('T'),Fore=message_color)), # write standard time stamp
            end='',flush=True) # state the minimum verb level to show this message
        for i in range(len(arg_list)): # for each arg supplied
            
            this_arg = arg_list[i]
            
            try:
                if(i > 0): last_arg = arg_list[i - 1]
            except: del last_arg
            else: pass
            
            try: next_arg = arg_list[i + 1]
            except: del next_arg
            else: pass
            
            #print("{i =",i,"}",end='',flush=True)
                
            if isinstance(this_arg,str): # if this item is a string

                if(this_arg[:7] == "!EXEC!:"): # if this item has an execution flag
                    if(print_executions): print(this_arg,end='',flush=True)
                    try:
                        eval(this_arg[7:]) # try executing it
                    except:
                        raise Exception("COULDN'T RUN CODE IN DBI!:",str(this_arg[7:])) # otherwise raise an exception
                
                else: # no execution flag
                    if('last_arg' in locals()): # if there's an item before this
                        print(" | ",end='',flush=True)
                    
                    print(this_arg,end='',flush=True) # print the item
        
        print(ct("",Style='RESET_ALL'))

## do an 'in-script test'
# whether to run the test
runThisTest = False
# body of code for test
if(runThisTest):
    
    def sleepyboi(dur):
        sleep(dur)

    tempVar = False
    def change():
        global tempVar
        tempVar = not tempVar

    db = {'debug_active': True, 'verbosity_level': 3}
    
    print("tempVar: ",tempVar)
    dbi(db,1,"testing level 1 verb...","doing it...",'!EXEC!:change()',"done!","finished!")
    print("tempVar: ",tempVar)
    dbi(db,2,"testing level 2 verb...","doing it...",'!EXEC!:sleepyboi(1)',"done!","finished!")
    dbi(db,3,"testing level 3 verb...","doing it...",'!EXEC!:sleepyboi(1)',"done!","finished!")

# if(runThisTest):
#     print("Without flushing the stdout stream")
#     for n in range(0,10):
#         print ("-",end="")
#         sleep(1.0)
#     print()
#     print("With flushing")
#     for n in range(0,10):
#         print("-",end="")
#         sys.stdout.flush()
#         sleep(1.0)