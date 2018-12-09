import dbi # import the dbifolder script so the function is available

# dictionary containing debugging settings
db = {'debug_active': True, 'verbosity_level': 2, 'import_tools': ['demo_tools']}

# define custom verb level
#db['verbosity_level'] = int(input("Verbosity level? (1-3):"))

dbi_out = {'my_number': 0.123456789} # user object to allow output from in-line commands

# run dbifolder with the set parameters
dbi.dbi(db,1,"~ some basic debugging information")
dbi.dbi(db,2,"~ more further advanced debugging information")
dbi.dbi(db,3,"~ lots of intricate debugging information")
dbi.dbi(db,1,"generating a random number...","!EXEC!:demo_tools.RNG()","random number generated!: ","!EXEC!:demo_tools.printRNG()")
dbi.dbi(db,2,"waiting for 3 seconds...","!EXEC!:demo_tools.sleepfor(3)","finished waiting!")
dbi.dbi(db,3,"waiting for 3 seconds...","!EXEC!:demo_tools.sleepfor(3)","finished waiting!") # although the verbosity level is be default under 3, the functions here should still execute
dbi.dbi(db,2,"finished running previous command, even if the verbosity level was lower!")
