#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by hypevr,,,
# Copyright (c) 2016 hypevr,,,
#
# License: MIT
#

"""This module exports the Lesshint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Lesshint(NodeLinter):
    """Provides an interface to lesshint."""

    cmd = 'lesshint @'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.1.1'
    regex = (
        r'((?P<error>Error)|(?P<warning>Warning))+?:(?P<file>.+)'
        r': line (?P<line>\d+),'
        r' col (?P<col>\d+),'
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'less'
    error_stream = util.STREAM_BOTH
    defaults = {
        "selector": "source.less"
    }
    word_re = None
    defaults = {}
