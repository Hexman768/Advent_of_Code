from sys import argv
from typing import Any

def part_1(lines: list[str]):
    _vars = dict()
    _com: dict[str, Any] = {
        'AND': '&',
        'OR': '|',
        'LSHIFT': '<<',
        'RSHIFT': '>>',
        'NOT': '~'
    }
    for line in lines:
        (_i, _v) = line.split('->')
        _inst = _i.strip().split(' ')
        _var = _v.strip()
        print((_inst, _var))
        if len(_inst) == 1:
            _vars[_var] = _inst
        else:
            for k,v in _com.items():
                if k in line:
                    if len(_inst) > 2:
                        print(f'{_var} = {_inst[0]}{v}{_inst[2]}')
                    else:
                        print(f'{_var} = {v}{_inst[1]}')

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
