import re
import ast
import sys

def part_1(lines: str) -> None:
    _inst: str = ''
    _count: int = 0
    _min_xy: tuple[int] = []
    _max_xy: tuple[int] = []
    _coords: list[str] = []
    _lights: list[int] = [[0 for i in range(1000)] for j in range(1000)]
    for _line in lines:
        if 'on' in _line:
            _inst = 'on'
        elif 'off' in _line:
            _inst = 'off'
        else:
            _inst = 'toggle'
        _coords = re.findall(r'(\d+[,]\d+)', _line)
        _min_xy = ast.literal_eval(_coords[0])
        _max_xy = ast.literal_eval(_coords[1])
        print(_min_xy)
        print(_max_xy)
        for y in range(_min_xy[1], _max_xy[1] + 1):
            for x in range(_min_xy[0], _max_xy[0] + 1):
                #print(f'X: {x} Y: {y}')
                if _inst == 'on':
                    _lights[y][x] = 1
                elif _inst == 'off':
                    _lights[y][x] = 0
                else:
                    _lights[y][x] = 1 if _lights[y][x] == 0 else 0
    for i in range(1000):
        for j in range(1000):
            if _lights[i][j] == 1:
                _count += 1
    print(f'There are {_count} lights turned on currently')

def main() -> None:
    if len(sys.argv) < 2:
        print('[ERROR] Usage: main.py <input file path>')
        return
    with open(sys.argv[1], encoding='utf-8') as _file:
        _lines: str = _file.readlines()
        part_1(_lines)
        _file.close()

main()
