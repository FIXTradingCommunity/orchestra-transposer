#!/usr/bin/env python3

import argparse
import logging
import os
import sys

from orchestratransposer import Orchestra2SBE, Orchestra2Unified, SBE2Orchestra, Unified2Orchestra
from orchestratransposer.sbe2orchestra import SBE2Orchestra20_10

FORMATS = ['orch', 'unif', 'sbe', 'sbe2']


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage='%(prog)s [OPTION]...',
        description='Convert an Orchestra XML file to or from another schema'
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version=f'{parser.prog} version 1.0.0'
    )
    parser.add_argument(dest="input", nargs="+", help="Name of input file(s)")
    parser.add_argument('-o', '--output', nargs="+",
                        help='name of output file(s)')
    parser.add_argument('-f', '--from', choices=FORMATS, default='orch', dest='input_format',
                        help='format of source file: Orchestra 1.0, Unified Repository, or SBE 1.0')
    parser.add_argument('-t', '--to', choices=FORMATS, default='orch', dest='output_format',
                        help='format of output file: Orchestra 1.0, Unified Repository, or SBE 1.0')

    return parser


def main() -> None:
    """
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
    """
    parser = init_argparse()
    args = parser.parse_args()
    d = vars(args)
    input_format = d['input_format']
    output_format = d['output_format']
    input_files = d['input']
    output_files = d['output']
    is_valid = True
    if input_format == output_format:
        print(f'ERROR: Input format "{input_format}" same as output format; nothing to do.',
              file=sys.stderr)
        is_valid = False
    if 'orch' not in [input_format, output_format]:
        print(f'ERROR: One of input format "{input_format}" or output format "{output_format}" must be "orch"',
              file=sys.stderr)
        is_valid = False
    if input_format == 'unif' and not len(input_files) == 2:
        print(f'ERROR: Two input files must be provided for "unif" format',
              file=sys.stderr)
        is_valid = False
    if output_format == 'unif' and not len(output_files) == 2:
        print(f'ERROR: Two output files must be provided for "unif" format',
              file=sys.stderr)
        is_valid = False
    if is_valid:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s',
                            filename=os.path.splitext(output_files[0])[0] + '.log',
                            filemode='w')
        if input_format == 'orch':
            if output_format == 'unif':
                translator = Orchestra2Unified()
                with open(output_files[0], 'wb') as unified_stream, open(output_files[1], 'wb') as phrases_stream:
                    errors = translator.orch2unified_xml(input_files[0], unified_stream, phrases_stream)
            elif output_format == 'sbe':
                translator = Orchestra2SBE()
                with open(output_files[0], 'wb') as f:
                    errors = translator.orch2sbe_xml(input_files[0], f)
        elif output_format == 'orch':
            if input_format == 'unif':
                translator = Unified2Orchestra()
                with open(output_files[0], 'wb') as f:
                    errors = translator.unified2orch_xml(input_files[0], input_files[1], f)
            elif input_format == 'sbe':
                translator = SBE2Orchestra()
                with open(output_files[0], 'wb') as f:
                    errors = translator.sbe2orch_xml(input_files[0], f)
            elif input_format == 'sbe2':
                translator = SBE2Orchestra20_10()
                with open(output_files[0], 'wb') as f:
                    errors = translator.sbe2orch_xml(input_files[0], f)
        print(f'{len(errors)} errors')


if __name__ == '__main__':
    main()
