# Copyright (C) 2023 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from sbom2doc.docbuilder.docbuilder import DocBuilder


class ConsoleBuilder(DocBuilder):
    def __init__(self):
        pass

    def heading(self, level, title, number=True):
        print(Panel(title, style="bold", expand=False))

    def paragraph(self, text):
        print(f"\n{text}")

    def createtable(self, header, validate=None):
        # Layout is [headings, ....]
        self.table = Table()
        for h in header:
            self.table.add_column(h, overflow="fold")

    def addrow(self, data):
        if len(data) > 5:
            print("Ooops - too much data!")
        else:
            # Add row to table
            self.table.add_row(*data)

    def showtable(self, widths=None):
        console = Console(width=150)
        console.print(self.table)
