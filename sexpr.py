'''
S-Expression object notation/syntax module.

* Note: in this module, "s" and "sexpr" are abbreviations for "S-Expression".
'''

import pyparsing
from pairwise import pairwise

str_delimiters = '\'"'

def from_s_list (list_):
    method = list_[0]
    rest = list_[1:]
    if method == 'list':
        return [from_s_data(x) for x in rest]
    elif method == 'dict':
        k_v_pairs = pairwise(rest)
        return {from_s_data(key): from_s_data(value) for key, value in k_v_pairs}
    else:
        raise ValueError('Unknown method {}'.format(str(method)))

def to_number (string):
    try:
        n = int(string)
    except ValueError:
        n = float(string)
    return n

def from_s_atom (obj):
    if type(obj) == str:
        first = obj[0]
        if first.isdigit() or first == '.':
            # Is a number
            return to_number(obj)
        elif first in str_delimiters:
            # Is a string literal
            return obj.strip(first)
    else:
        raise TypeError('obj not a str')

def from_s_data (obj):
    if type(obj) == list:
        return from_s_list(obj)
    else:
        return from_s_atom(obj)

def from_s (string):
    '''Parse a str into Python objects'''
    parse = pyparsing.OneOrMore(pyparsing.nestedExpr())
    try:
        # Try to parse a nested expression
        data = parse.parseString(string).asList()
        return from_s_data(data[0])
    except pyparsing.ParseException:
        # Otherwise retry it as an atom
        return from_s_atom(string.strip())

# S-Expression syntax Generation from Python Objects

def to_s_list (obj) -> str:
    l_obj = [to_s(x) for x in obj]
    return '(list {})'.format(' '.join(l_obj))

def to_s_dict_pair (key, value) -> str:
    return '{} {}'.format(to_s(key), to_s(value))

def to_s_dict (obj) -> str:
    pairs = [' '.join(to_s_dict_pair(k, v) for k, v in obj.items())]
    return '(dict {})'.format(' '.join(pairs))

def to_s (obj) -> str:
    '''Convert a Python object to a str with S-Expression syntax'''
    if type(obj) in (tuple, list):
        return to_s_list(obj)
    elif type(obj) == dict:
        return to_s_dict(obj)
    elif type(obj) == str:
        # Escape a string
        return '"' + obj + '"'
    else:
        return str(obj)
