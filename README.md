# Debug Interface (dbi)
## What is dbi used for?
Scripts where
- debugging information only shows when
    - debugging is active _and_
    - the set level of detail (verbosity) is at least as high as the level specified in the line
- verbosity can be modified in advanced
- verbosity can be modified on-the-fly
- execution of multiple external functions via a single-line
- user-written feedback on the status of each function's progress
- colour-coded console output (based on verbosity levels)
## y tho?
My console had become populated by indecernable walls of debugging text, all thanks to riddling my scripts with lines like ```print(str(var),var)``` for debugging.
So I decided to create a module to solve the problem which incorporated the benefits I just listed above