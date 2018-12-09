| BRANCH  | BUILD STATUS | COVERAGE |
| ---     | ---          | ---      |
| Master  | [![Build Status](https://travis-ci.org/DrTexxOfficial/dbi.svg?branch=master)](https://travis-ci.org/DrTexxOfficial/dbi) | [![Coverage Status](https://coveralls.io/repos/github/DrTexxOfficial/dbi/badge.svg?branch=master)](https://coveralls.io/github/DrTexxOfficial/dbi?branch=master) |
| Develop | [![Build Status](https://travis-ci.org/DrTexxOfficial/dbi.svg?branch=develop)](https://travis-ci.org/DrTexxOfficial/dbi) | [![Coverage Status](https://coveralls.io/repos/github/DrTexxOfficial/dbi/badge.svg?branch=develop)](https://coveralls.io/github/DrTexxOfficial/dbi?branch=develop) |

Master branch 

Develop branch:


# Debug Interface (dbi)

<img src="docs/dbi_logo.png" alt="dbi logo" width="200"/>

## Script Functionality
### User-Written Verbosity-Dependant Debug Messages
- information is only show when A and B are satisfied
    - debugging is active
    - the threshold verbosity is reached or exceeded (this threshold is specified on a per-message basis)
- verbosity can be
    - set in advanced
    - **modified on-the-fly**
- multiple **external functions** can be executed in a single-line
- users can write their own debugging messages on the status of each function's progress
- console output is colour-coded (based on verbosity levels)

## What is the purpose?
My console had become populated by indecernable walls of debugging text, all thanks to riddling my scripts with lines like ``print(str(var),var)`` for debugging.
So I created a module to maintain my sanity and save my time.
