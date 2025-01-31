# SBOM2DOC

SBOM2DOC documents and summarises the components within an SBOM (Software Bill of Materials). SBOMS are supported in a number of formats including
[SPDX](https://www.spdx.org) and [CycloneDX](https://www.cyclonedx.org).

## Installation

To install use the following command:

`pip install sbom2doc`

Alternatively, just clone the repo and install dependencies using the following command:

`pip install -U -r requirements.txt`

The tool requires Python 3 (3.7+). It is recommended to use a virtual python environment especially
if you are using different versions of python. `virtualenv` is a tool for setting up virtual python environments which
allows you to have all the dependencies for the tool set up in a single environment, or have different environments set
up for testing using different versions of Python.

## Usage

```
usage: sbom2doc [-h] [-i INPUT_FILE] [--debug] [--include-license] [-f {console,markdown,pdf}] [-o OUTPUT_FILE] [-V]

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit

Input:
  -i INPUT_FILE, --input-file INPUT_FILE
                        Name of SBOM file

Output:
  --debug               add debug information
  --include-license     add license text
  -f {console,markdown,pdf}, --format {console,markdown,pdf}
                        Output format (default: output to console)
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        output filename (default: output to stdout)
```
					
## Operation

The `--input-file` option is used to specify the SBOM to be processed. The format of the SBOM is determined according to
the following filename conventions.

| SBOM      | Format    | Filename extension |
| --------- | --------- |--------------------|
| SPDX      | TagValue  | .spdx              |
| SPDX      | JSON      | .spdx.json         |
| SPDX      | YAML      | .spdx.yaml         |
| SPDX      | YAML      | .spdx.yml          |
| CycloneDX | JSON      | .json              |

The `--output-file` option is used to control the destination of the output generated by the tool. The
default is to report to the console, but it can also be stored in a file (specified using `--output-file` option).

The `--include-license` option is used to indicate if the text for the licenses is to be included in the output.

## Example

Given the following SBOM (flask.spdx)

```bash
SPDXVersion: SPDX-2.3
DataLicense: CC0-1.0
SPDXID: SPDXRef-DOCUMENT
DocumentName: Python-flask
DocumentNamespace: http://spdx.org/spdxdocs/Python-flask-0d6084b4-1a7b-42f7-97e2-65bc4b109783
LicenseListVersion: 3.20
Creator: Tool: sbom4python-0.9.0
Created: 2023-03-31T11:01:17Z
CreatorComment: <text>This document has been automatically generated.</text>
##### 

PackageName: flask
SPDXID: SPDXRef-Package-1-flask
PackageVersion: 2.2.2
PackageSupplier: Person: Armin Ronacher (armin.ronacher@active-4.com)
PackageDownloadLocation: https://pypi.org/project/Flask/2.2.2
FilesAnalyzed: false
PackageHomePage: https://palletsprojects.com/p/flask
PackageLicenseDeclared: BSD-3-Clause
PackageLicenseConcluded: BSD-3-Clause
PackageCopyrightText: NOASSERTION
PackageSummary: A simple framework for building complex web applications.
ExternalRef: PACKAGE-MANAGER purl pkg:pypi/flask@2.2.2
ExternalRef: SECURITY cpe23Type cpe:2.3:a:armin_ronacher:flask:2.2.2:*:*:*:*:*:*:*
##### 

PackageName: click
SPDXID: SPDXRef-Package-2-click
PackageVersion: 8.0.3
PackageSupplier: Person: Armin Ronacher (armin.ronacher@active-4.com)
PackageDownloadLocation: https://pypi.org/project/click/8.0.3
FilesAnalyzed: false
PackageHomePage: https://palletsprojects.com/p/click/
PackageLicenseDeclared: BSD-3-Clause
PackageLicenseConcluded: BSD-3-Clause
PackageCopyrightText: NOASSERTION
PackageSummary: Composable command line interface toolkit
ExternalRef: PACKAGE-MANAGER purl pkg:pypi/click@8.0.3
ExternalRef: SECURITY cpe23Type cpe:2.3:a:armin_ronacher:click:8.0.3:*:*:*:*:*:*:*
##### 

PackageName: itsdangerous
SPDXID: SPDXRef-Package-3-itsdangerous
PackageVersion: 2.1.2
PackageSupplier: Person: Armin Ronacher (armin.ronacher@active-4.com)
PackageDownloadLocation: https://pypi.org/project/itsdangerous/2.1.2
FilesAnalyzed: false
PackageHomePage: https://palletsprojects.com/p/itsdangerous/
PackageLicenseDeclared: BSD-3-Clause
PackageLicenseConcluded: BSD-3-Clause
PackageCopyrightText: NOASSERTION
PackageSummary: Safely pass data to untrusted environments and back.
ExternalRef: PACKAGE-MANAGER purl pkg:pypi/itsdangerous@2.1.2
ExternalRef: SECURITY cpe23Type cpe:2.3:a:armin_ronacher:itsdangerous:2.1.2:*:*:*:*:*:*:*
##### 

PackageName: jinja2
SPDXID: SPDXRef-Package-4-jinja2
PackageVersion: 3.0.2
PackageSupplier: Person: Armin Ronacher (armin.ronacher@active-4.com)
PackageDownloadLocation: https://pypi.org/project/Jinja2/3.0.2
FilesAnalyzed: false
PackageHomePage: https://palletsprojects.com/p/jinja/
PackageLicenseDeclared: BSD-3-Clause
PackageLicenseConcluded: BSD-3-Clause
PackageCopyrightText: NOASSERTION
PackageSummary: A very fast and expressive template engine.
ExternalRef: PACKAGE-MANAGER purl pkg:pypi/jinja2@3.0.2
ExternalRef: SECURITY cpe23Type cpe:2.3:a:armin_ronacher:jinja2:3.0.2:*:*:*:*:*:*:*
##### 

PackageName: markupsafe
SPDXID: SPDXRef-Package-5-markupsafe
PackageVersion: 2.1.1
PackageSupplier: Person: Armin Ronacher (armin.ronacher@active-4.com)
PackageDownloadLocation: https://pypi.org/project/MarkupSafe/2.1.1
FilesAnalyzed: false
PackageHomePage: https://palletsprojects.com/p/markupsafe/
PackageLicenseDeclared: BSD-3-Clause
PackageLicenseConcluded: BSD-3-Clause
PackageCopyrightText: NOASSERTION
PackageSummary: Safely add untrusted strings to HTML/XML markup.
ExternalRef: PACKAGE-MANAGER purl pkg:pypi/markupsafe@2.1.1
ExternalRef: SECURITY cpe23Type cpe:2.3:a:armin_ronacher:markupsafe:2.1.1:*:*:*:*:*:*:*
##### 

PackageName: werkzeug
SPDXID: SPDXRef-Package-6-werkzeug
PackageVersion: 2.2.2
PackageSupplier: Person: Armin Ronacher (armin.ronacher@active-4.com)
PackageDownloadLocation: https://pypi.org/project/Werkzeug/2.2.2
FilesAnalyzed: false
PackageHomePage: https://palletsprojects.com/p/werkzeug/
PackageLicenseDeclared: BSD-3-Clause
PackageLicenseConcluded: BSD-3-Clause
PackageCopyrightText: NOASSERTION
PackageSummary: The comprehensive WSGI web application library.
ExternalRef: PACKAGE-MANAGER purl pkg:pypi/werkzeug@2.2.2
ExternalRef: SECURITY cpe23Type cpe:2.3:a:armin_ronacher:werkzeug:2.2.2:*:*:*:*:*:*:*
##### 

Relationship: SPDXRef-DOCUMENT DESCRIBES SPDXRef-Package-1-flask
Relationship: SPDXRef-Package-1-flask DEPENDS_ON SPDXRef-Package-2-click
Relationship: SPDXRef-Package-1-flask DEPENDS_ON SPDXRef-Package-3-itsdangerous
Relationship: SPDXRef-Package-1-flask DEPENDS_ON SPDXRef-Package-4-jinja2
Relationship: SPDXRef-Package-1-flask DEPENDS_ON SPDXRef-Package-6-werkzeug
Relationship: SPDXRef-Package-4-jinja2 DEPENDS_ON SPDXRef-Package-5-markupsafe
Relationship: SPDXRef-Package-6-werkzeug DEPENDS_ON SPDXRef-Package-5-markupsafe
```

The following commands will generate a summary of the contents of the SBOM to the console.

```bash
sbom2doc --input flask.spdx 

│ SBOM Summary │
╰──────────────╯
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Item          ┃ Details                ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ SBOM File     │ /tmp/flask.spdx        │
│ SBOM Type     │ spdx                   │
│ Version       │ SPDX-2.3               │
│ Name          │ Python-flask           │
│ Creator       │ Tool:sbom4python-0.9.0 │
│ Created       │ 2023-03-31T11:01:17Z   │
│ Files         │ 0                      │
│ Packages      │ 6                      │
│ Relationships │ 7                      │
└───────────────┴────────────────────────┘
╭─────────────────╮
│ Package Summary │
╰─────────────────╯
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Name         ┃ Version ┃ Supplier                                     ┃ License      ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ flask        │ 2.2.2   │ Armin Ronacher (armin.ronacher@active-4.com) │ BSD-3-Clause │
│ click        │ 8.0.3   │ Armin Ronacher (armin.ronacher@active-4.com) │ BSD-3-Clause │
│ itsdangerous │ 2.1.2   │ Armin Ronacher (armin.ronacher@active-4.com) │ BSD-3-Clause │
│ jinja2       │ 3.0.2   │ Armin Ronacher (armin.ronacher@active-4.com) │ BSD-3-Clause │
│ markupsafe   │ 2.1.1   │ Armin Ronacher (armin.ronacher@active-4.com) │ BSD-3-Clause │
│ werkzeug     │ 2.2.2   │ Armin Ronacher (armin.ronacher@active-4.com) │ BSD-3-Clause │
└──────────────┴─────────┴──────────────────────────────────────────────┴──────────────┘
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Name         ┃ Version ┃ Download                                    ┃ Copyright ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ flask        │ 2.2.2   │ https://pypi.org/project/Flask/2.2.2        │ -         │
│ click        │ 8.0.3   │ https://pypi.org/project/click/8.0.3        │ -         │
│ itsdangerous │ 2.1.2   │ https://pypi.org/project/itsdangerous/2.1.2 │ -         │
│ jinja2       │ 3.0.2   │ https://pypi.org/project/Jinja2/3.0.2       │ -         │
│ markupsafe   │ 2.1.1   │ https://pypi.org/project/MarkupSafe/2.1.1   │ -         │
│ werkzeug     │ 2.2.2   │ https://pypi.org/project/Werkzeug/2.2.2     │ -         │
└──────────────┴─────────┴─────────────────────────────────────────────┴───────────┘
╭─────────────────╮
│ License Summary │
╰─────────────────╯
┏━━━━━━━━━━━━━━┳━━━━━━━┓
┃ License      ┃ Count ┃
┡━━━━━━━━━━━━━━╇━━━━━━━┩
│ BSD-3-Clause │ 6     │
└──────────────┴───────┘
╭──────────────╮
│ NTIA Summary │
╰──────────────╯
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Element                            ┃ Status ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ All file information provided?     │ True   │
│ All package information provided?  │ True   │
│ Creator identified?                │ True   │
│ Creation time identified?          │ True   │
│ Dependency relationships provided? │ True   │
└────────────────────────────────────┴────────┘

NTIA conformant True
                                                                    
```

## Licence

Licenced under the Apache 2.0 Licence.

## Limitations

The tool has the following limitations

- SBOMs in RDF (SPDX) and XML (SPDX and CycloneDX) formats are not supported.

- Invalid SBOMs will result in unpredictable results.

## Feedback and Contributions

Bugs and feature requests can be made via GitHub Issues.