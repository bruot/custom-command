# custom-command

This is a template Python package that provides a custom executable command written in Python.


## Installation

```bash
$ pip install git+https://github.com/bruot/custom-command.git@main
```


## Usage

As an example, the exposed command is called `get-status-code` and returns the HTTP status code when querying a URL.  Example usage:

```bash
$ get-status-code https://www.python.org/
```


## Development

### Test the command

Assuming you already have all dependencies installed, the command can be tested without installing the package with:

```bash
$ cd src
$ python -m custom_command.get_status_code https://www.python.org/
```

It should print `200`.


### Install the package locally

Package can be installed locally with:

```bash
$ pip install .
```


### Edit dependencies

Dependencies to other Python packages are specified in the _pyproject.toml_ file.  To edit them, change the `dependencies` setting under `[project]`.


### Fork the project

When forking the project, be sure to apply all these changes to create your own package and command(s):

* Review _pyproject.toml_.  The command is defined in the `[project.scripts]` section.
* Review _LICENSE_ and match the license with the license classifier in _pyproject.toml_.
* Review _README.md_.
* Rename the _src/custom_command_ directory to match your package name.
* Rename the _src/custom_command/get_status_code.py_ file, and edit with your command code.
