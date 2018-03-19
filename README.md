# DEBUG INTERFACE (dbi)
## What is the usage case scenario for dbi?
Scripts which care to benefit from
- execution of multiple external functions via a single-line
- user-written feedback on the status of each function's progress
- simple modification of verbosity on-the-fly (or in advanced)
- colour-coded console output (based on verbosity levels)
## y tho?
My console had become populated by indecernable walls of debugging text, all thanks to riddling my scripts with lines like ```print(str(var),var)``` for debugging.
So I decided to create a module to solve the problem which incorporated the benefits I just listed above