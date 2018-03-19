# DEBUG INTERFACE (dbi)
## What is the usage case scenario for dbi?
Scripts which care to benefit from
- execution of multiple external functions via a single-line
- user-driven per-function status feedback
- colour-coded console output (based on verbosity levels)
## y tho?
I often riddle my scripts with lines such as ```print(str(var),var)```, however eventually led to indecernable walls of debugging text
So I decided to create a module to provide the benefits listed above