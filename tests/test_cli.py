
import pytest
import sqlite3
from countrycli.cli import cli, db, return_country
from click.testing import CliRunner

runner = CliRunner()


def test_return_country():

    assert isinstance(db.execute(
        "SELECT * FROM country_code WHERE country = 'Estonia'"
        ).fetchone(), sqlite3.Row)
    
    result = runner.invoke(cli, ['info', 'eeieidjjdl'])
    assert 'Country does not exist' in result.output

    the_country_exists = return_country(db, 'united states of America')
    assert 'United States Of America' == the_country_exists['country']


class TestCli:

    def test_info(self):
        result = runner.invoke(cli, ['info', 'Nigeria'])
        assert result.exit_code == 0
        assert "Information about" in result.output
        assert "NGA" in result.output
        assert 'NG' in result.output
    
    def test_info_two_digit(self):
        result = runner.invoke(cli, ['short', 'Nigeria'])
        assert result.exit_code == 0
        assert "NGA" not in result.output
        assert 'NG' in result.output
    
    def test_info_three_digit(self):
        result = runner.invoke(cli, ['short', 'Nigeria', '-ab=3'])
        assert result.exit_code == 0
        assert "NGA" in result.output
        assert 'NG' not in result.output.split(' ')

        result1 = runner.invoke(cli, ['short', 'NIGERIA', '-ab=4'])
        assert 'Error' in result1.output