| BRANCH  | BUILD STATUS | COVERAGE | ISSUES | OPEN PRs |
| ---     | :---:        | :---:    | :---:  | :---:    |
| Master  | [![Build Status](https://travis-ci.org/DrTexxOfficial/dbi.svg?branch=master)](https://travis-ci.org/DrTexxOfficial/dbi) | [![codecov](https://codecov.io/gh/DrTexxOfficial/dbi/branch/master/graph/badge.svg)](https://codecov.io/gh/DrTexxOfficial/dbi) | [![GitHub issues](https://img.shields.io/github/issues/DrTexxOfficial/dbi.svg?branch=master)](https://GitHub.com/DrTexxOfficial/dbi/issues/) | [![GitHub pull-requests](https://img.shields.io/github/issues-pr/DrTexxOfficial/dbi.svg?branch=master)](https://GitHub.com/DrTexxOfficial/dbi/pull/) |
| Develop | [![Build Status](https://travis-ci.org/DrTexxOfficial/dbi.svg?branch=develop)](https://travis-ci.org/DrTexxOfficial/dbi) | [![codecov](https://codecov.io/gh/DrTexxOfficial/dbi/branch/develop/graph/badge.svg)](https://codecov.io/gh/DrTexxOfficial/dbi) | [![GitHub issues](https://img.shields.io/github/issues/DrTexxOfficial/dbi.svg?branch=develop)](https://GitHub.com/DrTexxOfficial/dbi/issues/) | [![GitHub pull-requests](https://img.shields.io/github/issues-pr/DrTexxOfficial/dbi.svg?branch=develop)](https://GitHub.com/DrTexxOfficial/dbi/pull/) |

# Debug Interface - DBI [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![PyPI version fury.io](https://badge.fury.io/py/dbi.svg)](https://pypi.python.org/pypi/dbi/)
[![GitHub license](https://img.shields.io/github/license/DrTexxOfficial/dbi.svg?branch=master)](https://github.com/DrTexxOfficial/dbi/blob/master/LICENSE)

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

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
