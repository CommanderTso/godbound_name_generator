Godbound Name Generator
=======================

This is a simple command-line utility to create random names for the tabletop role-playing game, _Godbound_.  Developed and tested on OSX only.

Currently this only has the options for Ancalian names from the core _Godbound_ rules and the setting book, _Ancalia: The Broken Towers_.

If you're interested in Godbound, please check out [the free PDF edition on DriveThruRPG.com](https://www.drivethrurpg.com/product/185959/Godbound-A-Game-of-Divine-Heroes-Free-Edition).

Requirements
------------

- This script assumes you have `virtualenv` installed on your machine for Python3

Installation & Running the Script
------------

- Install `virtualenv` for Python
- Clone this repo
- In the repo directory, `virtualenv venv`
- Run the script via `./gen_name.py` with appropriate flags

Flags
-----

| Flags        | Description                             |
| ------------ | --------------------------------------- |
| -h; --help   | Shows the in-line help                  |
| -m; --male   | Generate a male first and last name     |
| -f; --female | Generate a female first and last name   |
