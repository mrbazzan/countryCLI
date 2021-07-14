
import click
import sqlite3

conn = sqlite3.connect('codes.db')
conn.row_factory = sqlite3.Row
db = conn.cursor()


@click.group()
def cli1():
    """Gives information about a country"""
    pass


@click.group()
def cli2():
    """Others"""
    pass


def return_country(db_conn, column):
    db_conn.execute("SELECT * FROM country_code WHERE country = (?)", (column.title(), ))
    _country = db_conn.fetchone()
    if _country is None:
        click.secho('Country does not exist. Perhaps, write the full name.', fg='red')
        return
    return _country


@cli1.command()
@click.argument('country_name')
def info(country_name):
    """Brief information about a country."""

    country = return_country(db, country_name)
    if country:
        click.echo(click.style(
            "\nInformation about {}:\n"
            "  - Two digit abbreviation: {}\n" 
            "  - Three digit abbreviation: {}".format(country['country'], country['Alpha2'], country['Alpha3'])
        , fg='green'))
    
    
@cli2.command('short')
@click.option('--abbreviate', '-ab', default='2', show_default=True,
              type=click.Choice(['2', '3']),
              help="")
@click.argument('country_name')
def short_code(country_name, abbreviate):

    """Returns the short abbreviation code of a country.
    It can be two digit or three digit country code.
    The default is two digit."""

    value = 'Alpha2' if abbreviate == '2' else 'Alpha3'
    country = return_country(db, country_name)
    if country:
        click.secho('The {0} digit country code for {1} is "{2}"'.format(abbreviate, country_name, country[value]), fg="green")


cli = click.CommandCollection(sources=[cli1, cli2])
