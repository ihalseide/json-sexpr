import json
import sexpr

def sexpr_to_json (sexpr_str: str) -> str:
    '''Covert S-Expression syntax to JSON syntax'''
    return json.dumps(sexpr.from_s(sexpr_str))

def json_to_sexpr (json_str: str) -> str:
    '''Covert JSON syntax to S-Expression syntax'''
    return sexpr.to_s(json.loads(json_str))

def __get_conversion_type (name):
    first_char = name[0].lower() 
    if first_char == 'j':
        # e.g 'JSON' or 'j' or 'js'
        return sexpr_to_json
    elif first_char in 'ls': 
        # e.g 'LISP' or 'SEXPR' or 'l'
        return json_to_sexpr
    else:
        return None

def main ():
    '''JSON and LISP command-line conversion utility'''
    import sys
    if len(sys.argv) > 1:
        in_file = sys.argv[1]
        convert_to = sys.argv[2]
        convert =  __get_conversion_type(convert_to)
        if convert is None:
            print('Invalid conversion name; please specify json or lisp', file=sys.stderr)
        else:
            in_str = open(in_file).read()
            result = convert(in_str)
            print(result)

if __name__ == '__main__':
    main()
