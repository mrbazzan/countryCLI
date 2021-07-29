
# PyNation

![GitHub](https://img.shields.io/github/license/mrbazzan/pynation)

Get information about a country. ``pynation`` is a command line application that helps users get quick information about a country.


## INSTALL
PyNation requires Python 3.7 and above

MacOS / Linux:

```shell
$ python3 -m pip install pynation
```

Windows:

```cmd
> python -m pip install pynation
```


## Using the CLI

The CLI can be invoked with the `pynation` command.

To get the help page:

```shell script
> pynation --help
```


```shell script
> pynation info `countryname`
```

```shell script
> pynation short `countryname`
```

```shell script
> pynation short `countryname` -ab=3
```

## Feedback

If you find a bug, please [file an issue](https://github.com/mrbazzan/pynation/issues).

If you have feature requests, please [file an issue](https://github.com/mrbazzan/pynation/issues)
and use the appropriate label.

## How to Contribute

Please **raise an issue** before making a PR, so that the issue and implementation can be discussed before you write any code. **This will save you time**, and increase the chances of your PR being merged without significant changes. 

Please make PR's on a **new branch**, and _not_ on main. 

Please **include tests** for any PR's that include code (unless current tests cover your code contribution).
