# JSON-SExpr

Convert between Javascript Object Notation and S-Expressions.

This is not a Python package yet.

The Python script "json_sexpr.py" can be used as a command line utility or a Python module.

# Command-line utility

The command line takes 2 positional arguments: file_in and format. The format determines which format the input file converts to, and it should be json or lisp or sexpr.

# Module functions

`json_to_sexpr(string) -> string`

`sexpr_to_json(string) -> string`
