# -*- coding: utf-8 -*-

import click
import os
from . import version


@click.group()
@click.version_option(version.__version__, '--version')
def cli():
    pass


@cli.command()
def convert(**kwargs):
    """ Convert from one type to another"""

    pass


if __name__ == "__main__":
    cli()
