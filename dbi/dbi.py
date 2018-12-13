"""
DBI - Debugging interface module
Script by Denver P.
Conception: 2017-??:??
r1: 2018-03-14-??:??
r2: 2018-03-19-12:00
r3: 2018-03-19-23:59
r4: 2018-03-20-09:25
r5: 2018-03-31-16:10
r6: 2018-03-31-17:29
r7: 2018-03-31-17:40
"""

from colorama import init
init()
from colorama import Fore,Back,Style
from datetime import datetime
_now = datetime.now

class Dbi:
    def __init__(self,init_verb,init_debug):
        self.verb = init_verb
        self.debug = init_debug
        self._verb_styles = {1: Fore.LIGHTGREEN_EX,
                             2: Fore.LIGHTYELLOW_EX,
                             3: Fore.LIGHTRED_EX}
        self._time_style = Fore.CYAN
        self._string_seperator = " | "
    def _style_verb(self,verb):
        return("{}{}{}".format(self._verb_styles[verb],verb,Style.RESET_ALL))
    def _style_time(self,time):
        return("{}{}{}".format(self._time_style,time,Style.RESET_ALL))
    def print_message(self,min_verb,*args,return_string=False): # recommended: Dbi.print_message = dpm
        #min_verb must be an integer
        if type(min_verb) not in [int]:
            raise TypeError("Verb level must be an integer.")
        if min_verb < 1:
            raise ValueError("Verb level must 1 or greater.")
        if not self.verb >= min_verb:
            return DbiErrors.VerbTooLow
        if self.debug == False:
            return DbiErrors.DebugOff
        _prefix = "[{}][{}]<=[{}] ".format(self._style_verb(self.verb),
                                          self._style_verb(min_verb),
                                          self._style_time(_now()))
        final_string = [_prefix]
        for argument in args:
            if type(argument) not in [str]:
                raise TypeError("Arguments must be strings.")
            if not final_string[-1] == _prefix:
                final_string.append(self._string_seperator)
            final_string.append(argument)
        final_string = ''.join(final_string)
        print(final_string)
        if return_string == True: return(final_string)

class DbiErrors:
    class VerbTooLow: pass
    class DebugOff: pass

#dbi = Dbi(3,True)
#dpm = dbi.print_message
#dpm(3,"hello stranger")


# def dbi(db,min_verb,*args): # define core function
#     '''
#     In-line functions will fail to execute if they are not accessible within the scope of THIS script.
#     Thus if a function is defined in a script that imports this module, the function may not work correctly unless:
#     1 ) the function is incorporated into the code of dbifolder
#     2 ) the function can be carried over to dbifolder through [relative module name to import].[function to run] executions
#     3 ) the function becomes incorporated into the code of dbifolder in the future
#     4 ) an alternative method is found which allows dbifolder to see other functions in the script which imported it
#     
#     EXAMPLE: dbifolder(db,2,"RUNNING...","!EXEC!:demo_tools.sf1()","DONE!")
#     If the verbosity_level listed in db is >= 2, then
#     1 -> the string "RUNNING..." will be printed to the terminal line, then
#     2 -> !EXEC!:demo_tools.sf1 will be split up into parts
#     3 -> !EXEC!: will be recognized as a executable flag, so
#     4 -> the function will attempt to import the module demo_tools, then
#     5 -> the function will attempt to execute the module sf1(), once execution is completed
#     6 -> the "DONE!" string will be printed    
#     
#     '''
#     print_exec = False
#     verb = str(db['verbosity_level'])
#     if 'print_exec' in db: print_exec = db['print_exec']
#     if 'debug_active' and 'verbosity_level' in db:
#         if(db['debug_active'] and db['verbosity_level'] >= min_verb): print_strings = True # check debug is True and level is okay, set var accordingly
#         else: print_strings = False
#     else: raise Exception("passed db dict doesn't contain 'debug_active' and/or 'verbosity_level' key/s")
#         
#     arg_list = [item for item in args]
#     prefixes = {'1': {'name': "1", 'style': 'GREEN'},
#                 '2': {'name': "2", 'style': 'YELLOW'},
#                 '3': {'name': "3", 'style': 'RED'}}
#     message_color = prefixes[str(min_verb)]['style']
#     
#     if(print_strings): # if printing strings
#         print( # print verb levels and time stamp
#             "[%s][%s]<=[%s]: " % ( # format for data using string substitution
#                 ct(prefixes[verb]['name'],Fore=prefixes[verb]['style']), # state the parent script's verb level
#                 ct(prefixes[str(min_verb)]['name'],Fore=message_color), # state the verb level required to show this message
#                 ct(now().isoformat('T'),Fore=message_color)), # write standard time stamp
#             end='',flush=True) # stop the print from returning a newline character
#     
#     for i in range(len(arg_list)): # for each argument supplied
#         
#         this_arg = arg_list[i]
#         
#         try:
#             if(i > 0): last_arg = arg_list[i - 1]
#         except: del last_arg
#         else: pass
#         
#         try:
#             if(len(arg_list) > 1): next_arg = arg_list[i + 1]
#         except: del next_arg
#         else: pass
#         
#         #print("{i =",i,"}",end='',flush=True)
#         
#         if isinstance(this_arg,str): # if this item is a string
#             
#             if(this_arg[:7] == "!EXEC!:"): # if this item has an execution flag
#                 if(print_exec): print(this_arg,end='',flush=True)
#                 
#                 try:
#                     to_eval = this_arg[7:].split(".")
#                     if(print_exec): print(to_eval,end='',flush=True)
#                     demo_tools = __import__(to_eval[0],globals(),locals())
#                     eval(str(demo_tools.__name__) + "." + to_eval[1])
#                 except:
#                     raise Exception("COULDN'T RUN CODE IN DBI!:",str(this_arg[7:])) # otherwise raise an exception
#             
#             else: # no execution flag
#                 if(print_strings): # if we're printing strings
#                     if('last_arg' in locals()): # if there's an item before this
#                         if not (i == 1 and last_arg[:7] == "!EXEC!:"): # don't print a vertical line if the prior command was executed
#                             print(" | ",end='',flush=True) # print a vertical line character
#                         
#                     print(this_arg,end='',flush=True) # print the item
#     
#     if(print_strings): print(ct("",Style='RESET_ALL')) # print a character to reset all styling, acts as a catch-all
# 
# ## do an 'in-script test'
# # whether to run the test
# runThisTest = False
# # body of code for test
# if(runThisTest):
#     
#     def sleepyboi(dur):
#         sleep(dur)
#         
#     
#     db = {'debug_active': True, 'verbosity_level': 3}
#     tempVar = False
#     
#     print("tempVar: ",tempVar)
#     dbi(db,1,"testing level 1 verb...","doing it...",'!EXEC!:demo_tools.tempVar','!EXEC!:demo_tools.change()',"done!","finished!")
#     print("tempVar: ",tempVar)
#     dbi(db,2,"testing level 2 verb...","doing it...",'!EXEC!:sleepyboi(1)',"done!","finished!")
#     dbi(db,3,"testing level 3 verb...","doing it...",'!EXEC!:sleepyboi(1)',"done!","finished!")
    
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
