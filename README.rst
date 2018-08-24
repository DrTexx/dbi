#####################
Debug Interface (dbi)
#####################
.. image:: docs/dbi_logo.png
    :height: 100px
    :width: 100px
    :alt: dbi logo
====================
Script Functionality
====================
-----------------------------------------------
User-Written Verbosity-Dependant Debug Messages
-----------------------------------------------
- information is only show when A and B are satisfied
    - debugging is active
    - the threshold verbosity is reached or exceeded (this threshold is specified on a per-message basis)
- verbosity can be
    - set in advanced
    - **modified on-the-fly**
- multiple **external functions** can be executed in a single-line
- users can write their own debugging messages on the status of each function's progress
- console output is colour-coded (based on verbosity levels)
====================
What is the purpose?
====================
My console had become populated by indecernable walls of debugging text, all thanks to riddling my scripts with lines like ``print(str(var),var)`` for debugging.
So I created a module to maintain my sanity and save my time.
