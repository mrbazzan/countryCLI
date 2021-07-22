
# CountryCli

![GitHub](https://img.shields.io/github/license/mrbazzan/countryCLI)

Get information about a country. ``CountryCli`` is a command line application that helps users get quick information about a country.


## INSTALL
CountryCli requires Python 3.7 and above.

Windows:

FOR HTTPS;

```shell script
- git clone https://github.com/mrbazzan/countryCLI
```

```shell script
- cd countryCLI
```

```shell script
- python -m venv venv/
- cd venv/scripts
- activate
- cd ../..
- pip install -r requirements.txt
```

## Using the CLI

The CLI can be invoked with the `countrycli` command.

To get the help page:

```shell script
> py countrycli --help
```


```shell script
> py countrycli info `countryname`
```

```shell script
> py countrycli short `countryname`
```

```shell script
> py countrycli short `countryname` -ab=3
```

## Feedback

If you find a bug, please [file an issue](https://github.com/mrbazzan/countryCLI/issues).

If you have feature requests, please [file an issue](https://github.com/mrbazzan/countryCLI/issues)
and use the appropriate label.

## How to Contribute

Please **raise an issue** before making a PR, so that the issue and implementation can be discussed before you write any code. **This will save you time**, and increase the chances of your PR being merged without significant changes. 

Please make PR's on a **new branch**, and _not_ on main/master. 

Please **include tests** for any PR's that include code (unless current tests cover your code contribution).
