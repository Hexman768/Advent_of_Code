import re
import sys

def part_1(_lines: str) -> None:
    _inst: str = ''
    _min_xy: list[int] = []
    _max_xy: list[int] = []
    for _line in _lines:
        if 'on' in _line:
            _inst = 'on'
        elif 'off' in _line:
            _inst = 'off'
        else:
            _inst = 'toggle'
        print(re.findall(r'(\d+[,]\d+)', _line))
        print(_inst)
    return

def main() -> None:
    if len(sys.argv) < 2:
        print('[ERROR] Usage: main.py <input file path>')
        return
    with open(sys.argv[1], encoding='utf-8') as _file:
        _lines: str = _file.readlines()
        part_1(_lines)
        _file.close()

main()
