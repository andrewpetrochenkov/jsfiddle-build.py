#!/usr/bin/env python
"""build `build.html` from jsfiddle files (`demo.css`, `demo.details`,`demo.js`,`demo.html`)"""
# -*- coding: utf-8 -*-
import click
import jsfiddle_build
import os

MODULE_NAME = "jsfiddle_build"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1, required=True)
def _cli(paths):
    cwd = os.getcwd()
    for path in list(set(paths)):
        os.chdir(cwd)
        if os.path.exists(path) and os.path.isfile(path):
            path = os.path.dirname(path)
        os.chdir(path)
        build = jsfiddle_build.Build()
        build.save("build.html")


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
