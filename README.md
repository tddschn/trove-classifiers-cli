# Trove Classifiers CLI

CLI for PyPI Trove Classifiers

- [Trove Classifiers CLI](#trove-classifiers-cli)
	- [Installation](#installation)
		- [pipx](#pipx)
		- [pip](#pip)
	- [Usage](#usage)
	- [Examples](#examples)
		- [Basic usage](#basic-usage)
		- [--tree](#--tree)
		- [--quoted-list](#--quoted-list)

## Installation

### pipx

This is the recommended installation method.

```
$ pipx install trove-classifiers-cli
```

### [pip](https://pypi.org/project/trove-classifiers-cli/)

```
$ pip install trove-classifiers-cli
```

## Usage

```
$ trove-classifiers --help
usage: trove-classifiers [-h] [-I] [-q] [-t] [MATCH ...]

CLI for PyPI Trove Classifiers

positional arguments:
  MATCH              String(s) to search for (default: [None])

options:
  -h, --help         show this help message and exit
  -I, --case         Perform case sensitive matching. (default: False)
  -q, --quoted-list  Output a quoted list (default: False)
  -t, --tree         Format output as a tree (default: False)
```

## Examples

### Basic usage
```
$ trove-classifiers macos
Environment :: MacOS X
Environment :: MacOS X :: Aqua
Environment :: MacOS X :: Carbon
Environment :: MacOS X :: Cocoa
Operating System :: MacOS
Operating System :: MacOS :: MacOS 9
Operating System :: MacOS :: MacOS X
```

### --tree
```
$ trove-classifiers macos -t
Environment :: MacOS X
        Environment :: MacOS X :: Aqua
        Environment :: MacOS X :: Carbon
        Environment :: MacOS X :: Cocoa
Operating System :: MacOS
        Operating System :: MacOS :: MacOS 9
        Operating System :: MacOS :: MacOS X
```

### --quoted-list
```
$ trove-classifiers macos -q
"Environment :: MacOS X",
"Environment :: MacOS X :: Aqua",
"Environment :: MacOS X :: Carbon",
"Environment :: MacOS X :: Cocoa",
"Operating System :: MacOS",
"Operating System :: MacOS :: MacOS 9",
"Operating System :: MacOS :: MacOS X",
```