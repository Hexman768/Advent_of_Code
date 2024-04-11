from sys import argv

def get_value(vars: dict, val: str) -> int:
    try:
        return vars[val]
    except KeyError:
        return 0

def part_1(lines: list[str]):
    _vars = dict()
    _com: list[str] = [
        'AND',
        'OR',
        'LSHIFT',
        'RSHIFT',
        'NOT'
    ]
    for line in lines:
        (_i, _v) = line.split('->')
        _inst = _i.strip().split(' ')
        _var = _v.strip()
        #print((_inst, _var))
        if len(_inst) == 1:
            # have to handle setting undeclared values to variables ex. lx -> a
            print(_inst[0])
            print(line)
            _vars[_var] = int(_inst[0])
        else:
            for k in _com:
                if k in line:
                    if len(_inst) > 2:
                        print(f'{_var} = {_inst[0]}{_inst[1]}{_inst[2]}')
                        if _inst[1] == 'AND':
                            _vars[_var] = get_value(_vars, _inst[0]) & get_value(_vars, _inst[2])
                            #print(_vars[_var])
                        elif _inst[1] == 'OR':
                            _vars[_var] = get_value(_vars, _inst[0]) | get_value(_vars, _inst[2])
                        elif _inst[1] == 'LSHIFT':
                            print(_var)
                            _vars[_var] = (get_value(_vars, _inst[0]) << int(_inst[2])) & 0xffff
                        elif _inst[1] == 'RSHIFT':
                            print(_var)
                            _vars[_var] = get_value(_vars, _inst[0]) >> int(_inst[2]) & 0xffff
                    else:
                        _vars[_var] = (~get_value(_vars, _inst[1])) & 0xffff
    print(_vars)

def main() -> None:
    if len(argv) < 2:
        print('[ERROR] Usage: py main.py <input file path>')
        return
    with open(argv[1], encoding='utf-8') as _file:
        lines: list[str] = _file.readlines()
        part_1(lines)
        _file.close()

if __name__ == '__main__':
    main()
