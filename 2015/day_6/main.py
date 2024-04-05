import re
import ast
import sys

def execute(lines: str, bright: bool) -> None:
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
        for y in range(_min_xy[1], _max_xy[1] + 1):
            for x in range(_min_xy[0], _max_xy[0] + 1):
                if _inst == 'on' and not bright:
                    _lights[y][x] = 1
                elif _inst == 'on' and bright:
                    _lights[y][x] += 1
                elif _inst == 'off' and not bright:
                    _lights[y][x] = 0
                elif _inst == 'off' and bright and _lights[y][x] > 0:
                    _lights[y][x] -= 1
                elif _inst == 'toggle' and not bright:
                    _lights[y][x] = 1 if _lights[y][x] == 0 else 0
                elif _inst == 'toggle' and bright:
                    _lights[y][x] += 2
    for i in range(1000):
        for j in range(1000):
            _count += _lights[i][j]
    print(f'The total count is: {_count}')

def main() -> None:
    if len(sys.argv) < 2:
        print('[ERROR] Usage: py main.py <input file path>')
        return
    with open(sys.argv[1], encoding='utf-8') as _file:
        _lines: str = _file.readlines()
        execute(_lines, False)
        execute(_lines, True)
        _file.close()

main()
