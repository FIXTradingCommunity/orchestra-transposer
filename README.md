# orchestra-transposer

Converts between an Orchestra file and other artifacts.

The implementation converts between Orchestra version 1.0 and these other XML schemas:
* Simple Binary Encoding (SBE) version 1.0
* FIX Unified Repository 2010 Edition

### FIX standards and schemas
References for these standards and their XML schemas are available in GitHub.

[Orchestra](https://github.com/FIXTradingCommunity/fix-orchestra)
The XSD files for Orchestra are in module `repository` while the Unified Repository schema is in
module `repository2010`.

[Simple Binary Encoding (SBE)](https://github.com/FIXTradingCommunity/fix-simple-binary-encoding)
Currently version 1.0 is supported.


## Features

* Validate an Orchestra file against its XML schema.
* Access elements of an Orchestra file in "pythonic" data structures that are aware of XML Schema
datatypes.
* Validate an SBE message schema against its XML schema.
* Access elements of an SBE message schema in "pythonic" data structures that are aware of XML
Schema datatypes.
* Convert an Orchestra file to an SBE message schema. Support datatype customization.
* Convert an SBE message schema to an Orchestra file.
* Validate a Unified Repository file against its schema.
* Convert an Orchestra file to a Unified Repository.
* Convert a Unified Repository to an Orchestra file.

## Prerequisites

Requires [Python 3.9](https://www.python.org/downloads/release/python-390/) or later. (Earlier
versions have not been tested.)

Unit tests use the [pytest](https://docs.pytest.org/en/6.2.x/) framework.

Assuming that Python and pip are already installed, get started as follows:
1. Clone this Git repository
2. In the working directory, create a Python virtual environment, e.g. `python3 -m venv .venv`
3. Install required dependencies: `python3 -m pip install -r requirements.txt`
4. For development of this project, also install dependencies from `requirements-dev.txt`. This is required for
documentation generation and possibly other tasks.

### Documentation
To generate documentation, invoke the make utility in the `docs` directory.

## Usage

See the pytest test cases in the `tests` directory for examples of programmatic usage.


### Command line usage

A command line interface is provided by script `orchestratransposer.py`.

The arguments are patterned after Pandoc.

```
usage: python -m orchestratransposer [OPTION]...

Convert an Orchestra XML file to or from another schema

positional arguments:
  input                 Name of input file(s)

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -o, --output OUTPUT [OUTPUT ...]
                        name of output file(s)
  -f, --from {orch,unif,sbe,sbe2}
                        format of source file: Orchestra 1.0, Unified Repository, or SBE 1.0
  -t, --to {orch,unif,sbe,sbe2}
                        format of output file: Orchestra 1.0, Unified Repository, or SBE 1.0
```

Log messages are written to a file with the same path as the output file but with '.log' extension.

First example translates an Orchestra file to SBE.
```
python3 -m orchestratransposer tests/xml/OrchestraFIXLatest.xml --from orch --to sbe -o sbe_test.xml
```

Second example translates an Orchestra file to a Unified Repository
Two file names needed, starting with the name of the repository file.
```
python3 -m orchestratransposer tests/xml/OrchestraFIXLatest.xml --from orch --to unif -o FixRepository.xml FixPhrases_en.xml
```

Third example translates a Unified Repository to an Orchestra file
Two file names needed, starting with the name of the repository file.
```
python3 -m orchestratransposer tests/xml/FixRepository.xml tests/xml/FixPhrases_en.xml --from unif --t orch -o OrchestraFIXLatest.xml
```

## License

© Copyright 2026 FIX Protocol Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
