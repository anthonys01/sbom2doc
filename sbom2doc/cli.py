# Copyright (C) 2023 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

import argparse
import os
import sys
import textwrap
from collections import ChainMap

from lib4sbom.parser import SBOMParser

import sbom2doc.generator as generator
from sbom2doc.version import VERSION

# CLI processing


def main(argv=None):

    argv = argv or sys.argv
    app_name = "sbom2doc"
    parser = argparse.ArgumentParser(
        prog=app_name,
        description=textwrap.dedent(
            """
            SBOM2doc generates documentation for a SBOM.
            """
        ),
    )
    input_group = parser.add_argument_group("Input")
    input_group.add_argument(
        "-i",
        "--input-file",
        action="store",
        default="",
        help="Name of SBOM file",
    )

    output_group = parser.add_argument_group("Output")
    output_group.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="add debug information",
    )

    output_group.add_argument(
        "--include-license",
        action="store_true",
        default=False,
        help="add license text",
    )

    output_group.add_argument(
        "--ntia-summary",
        action="store_true",
        default=False,
        help="add NTIA summary",
    )

    def file_path(path):
        if path == "" or os.path.isfile(path):
            return path
        else:
            raise argparse.ArgumentTypeError(f"No file was found at path {path}")

    output_group.add_argument(
        "--extra-text",
        type=file_path,
        action="store",
        default="",
        help="File path to extra text to add at the end of the output",
    )

    # Add format option
    output_group.add_argument(
        "-f",
        "--format",
        action="store",
        help="Output format (default: output to console)",
        choices=["console", "markdown", "pdf"],
        default="console",
    )

    output_group.add_argument(
        "-o",
        "--output-file",
        action="store",
        default="",
        help="output filename (default: output to stdout)",
    )

    parser.add_argument("-V", "--version", action="version", version=VERSION)

    defaults = {
        "input_file": "",
        "output_file": "",
        "debug": False,
        "format": "console",
        "include_license": False,
        "ntia_summary": False,
        "extra_text": ""
    }

    raw_args = parser.parse_args(argv[1:])
    args = {key: value for key, value in vars(raw_args).items() if value}
    args = ChainMap(args, defaults)

    # Validate CLI parameters

    input_file = args["input_file"]

    if input_file == "":
        print("[ERROR] SBOM name must be specified.")
        return -1

    if args["format"] != "console" and args["output_file"] == "":
        print("[ERROR] Output filename must be specified.")
        return -1

    if args["debug"]:
        print("Input file", args["input_file"])
        print("Output file", args["output_file"])
        print("Include license text", args["include_license"])

    sbom_parser = SBOMParser()
    # Load SBOM - will autodetect SBOM type
    try:
        sbom_parser.parse_file(input_file)

        generator.generate_document(
            args["format"],
            sbom_parser,
            input_file,
            args["output_file"],
            args["include_license"],
            args["ntia_summary"],
            args["extra_text"]
        )

    except FileNotFoundError:
        print(f"{input_file} not found")

    return 0


if __name__ == "__main__":
    sys.exit(main())
