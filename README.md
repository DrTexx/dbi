# Debug Interface (dbi)
[dbi logo](docs/dbi_logo.png)
## What is dbi used for?
Scripts where
- debugging information only shows when
    - debugging is active
    - the set level of detail (verbosity) is at least as high as the level specified in the line
- verbosity can be modified in advanced
- **verbosity can be modified on-the-fly**
- multiple **external functions** can be executed in a single-line
- users can write their own debugging messages on the status of each function's progress
- console output is colour-coded (based on verbosity levels)
## y tho?
My console had become populated by indecernable walls of debugging text, all thanks to riddling my scripts with lines like ```print(str(var),var)``` for debugging.
So I decided to create a module to solve the problem which incorporated the benefits I just listed above