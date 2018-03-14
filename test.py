from src import dbi
import time

# dictionary containing debugging settings
db = {'debug_active': True, 'verbosity_level': 1}
# run dbi with the set parameters
dbi.dbi(db,3,"verb of 3")
dbi.dbi(db,2,"verb of 2")
dbi.dbi(db,1,"verb of 1")
dbi.dbi(db,1,"waiting for 3 seconds...",time.sleep(3),"finished waiting!")