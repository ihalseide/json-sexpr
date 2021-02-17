import json
import sexpr

def sexpr_to_json (sexpr_str: str) -> str:
    '''Covert S-Expression syntax to JSON syntax'''
    return json.dumps(sexpr.from_s(sexpr_str))

def json_to_sexpr (json_str: str) -> str:
    '''Covert JSON syntax to S-Expression syntax'''
    return sexpr.to_s(json.loads(json_str))

if __name__ == '__main__':
    import sys

    def _get_conversion_type (name):
        if name:
            first_char = name[0].lower() 
            if 'j' == first_char:
                return sexpr_to_json
            elif 's' == first_char: 
                return json_to_sexpr

    def _print_usage (): 
        print('Usage:', sys.argv[0], '[filename]', '-[j|s]')
    
    if len(sys.argv) == 3:
        in_file = sys.argv[1]
        convert_to = sys.argv[2][1:]
        convert =  _get_conversion_type(convert_to)
        if convert is None:
            print(sys.argv[0], ': invalid conversion type', file=sys.stderr)
            sys.exit(-1)
        else:
            in_str = open(in_file).read()
            result = convert(in_str)
            print(result)
    elif len(sys.argv) == 2 and sys.argv[1][:2] == '-h':
        print('Help for:', sys.argv[0])
        print('\nThis utility is for converting JSON or S-Expression formatted files into the other format. Output is printed to stdout.\n')
        _print_usage()
        print('\t-j to convert S-Expressions to JSON')
        print('\t-s to convert JSON to S-Expressions')
    else:
        _print_usage()
        sys.exit(-1)
    sys.exit(0)
