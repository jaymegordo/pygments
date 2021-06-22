# -*- coding: utf-8 -*-
"""
    pygments.styles.abap
    ~~~~~~~~~~~~~~~~~~~~

    ABAP workbench like style.

    :copyright: Copyright 2006-2020 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import (STANDARD_TYPES, Comment, Error, Generic, Keyword,
                            Literal, Name, Number, Operator, Other, String,
                            Text, Token)


class JaymeStyle(Style):
    default_style = ""

    # dark theme
    darkblue = '#569cd6'
    lightlue = '#7ed6e2'
    lightorange = '#ffce49'
    red = '#ff7b88'
    darkgrey = '#5a5a5a'
    lightgrey = '#cfcfcf'
    strings = '#a0a0a0'
    lightpurple = '#e8aeff'
    seafoam = '#4EC9B0'
    # bg = '#000B15' # code background color
    bg = ' '  # transparent background

    styles = {
        Token: f'bg:{bg} {lightgrey}',

        Comment: f'italic {darkgrey}',
        Comment.Special: lightgrey,

        Keyword: red,
        Keyword.Constant: f'bold {darkblue}',

        Name.Class:  f'bold {seafoam}',  # 'MyClass'
        Name.ClassDef: f'nobold {seafoam}',  # 'class', custom lexer add
        Name.Builtin: darkblue,
        Name.Builtin.Special: red,
        Name.Builtin.Pseudo: darkgrey,
        Name.Decorator: lightpurple,
        Name.FunctionCall: darkblue,
        Name.Function:  f'bold {lightpurple}',  # 'my_function'
        Name.FunctionDef: f'nobold {lightpurple}',  # 'def', custom
        Name.Function.Magic: lightpurple,

        Number: lightorange,

        String: strings,
        String.Doc: darkgrey,
        String.Interpol: darkblue,
        String.FstringFormat: red,  # custom
        String.Affix: red,

        Other.FunctionArg: lightlue,  # custom lexer add, this is the important one
    }
