from src import dbi

# dictionary containing debugging settings
db = {'debug_active': True, 'verbosity_level': 3}
# run dbi with the set parameters
dbi.dbi(db,3,"10+1 is",print(pow(10,2) + pow(50,7)),"okay?")
dbi.dbi(db,2,"verb of 2")
dbi.dbi(db,1,"verb of 1")