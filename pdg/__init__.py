#!/usr/bin/python3

import pdg.pdgTable as pdgTable
import pdg.pdgListing as pdgListing
table = pdgTable.PDGTable()
pdg_listing = pdgListing.PDGListing()

import click
@click.group()
def cli():
    pass

@cli.command()
@click.argument("name", type=str)
def info(name):
    """ Get the infomation of a specific particle."""
    infomation = table.get_infomation(name)
    click.echo(infomation)

@cli.command()
@click.argument("name", type=str)
def listing(name):
    """ Get the review of a specific particle."""
    pdg_listing.lookup(name)

def main():
    cli()

__version__ = "1.1.0"
