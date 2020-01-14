# actions-pytoolkit

[![PyPI](https://img.shields.io/pypi/v/actionspytoolkit)](https://pypi.org/project/actionspytoolkit/)

GitHub Actions Development Tools in Python.

## Install

```
pip install actionspytoolkit
```

## Introduction

This package allows the developer to write entry points for their Dockerized GitHub Action in Python, rather than in shell (or whatever else). Right now this package is super simple, and only wraps the commands [documented here](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/development-tools-for-github-actions).

## Usage

There are a number of commands, communicated to the runner machine, that are given as echo statements. This package just wraps those echo statements with the necessary formatting and inputs. Here are a few basic usage examples:

```python
import actionspytoolkit as aptk
aptk.logging.set_output('hello', 'world')
# prints ::set-output name=hello::world
```

```python
import actionspytoolkit as aptk
aptk.logging.warning('hello world')
# prints ::warning::hello world

aptk.logging.warning('hello world', 'main.py', 2, 1)
# prints ::warning main.py,2,1::hello world
```

## Examples

Coming Soon
