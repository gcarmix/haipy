# Haipy
![pylint](https://github.com/gcarmix/haipy/actions/workflows/pylint.yml/badge.svg)
## What is it?

A CLI tool to identify hash types (hash type identifier).

This project is a Python porting of "haiti" https://github.com/noraj/haiti written in Ruby.

## Features

- 500+ hash types detected
- Can be used as Python library
- Modern algorithms supported (SHA3, Keccak, Blake2, etc.)
- Hashcat and John the Ripper references
- CLI tool
- Hackable
## Usage
```
haipy [hash code to guess]
```

![terminal view](haipycli.png)

## Usage as Python Library
Haipy can be used as a Python Library like shown in the following snippet of code:

```
>>> import haipy as haipy

>>> haipy.detect("$6$qoE2letU$wWPRl.PVczjzeMVgjiA8LLy2nOyZbf7Amj3qLIL978o18gbMySdKZ7uepq9tmMQXxyTIrS12Pln.2Q/6Xscao0")

>>> [{'name': 'SHA-512 Crypt', 'hashcat': 1800, 'john': 'sha512crypt'}]
```

## Installation

To install from pypi:
```
pip install haipy
```

To install from the source directory:
```
pip install .
```

## Author

Ported by @gcarmix, derived from haiti by @noraj

