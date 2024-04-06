from sys import argv
from re import findall
from typing import Any

def execute(lines: str, bright: bool) -> None:
    _count: int = 0
    _lights: list[int] = [[0 for i in range(1000)] for j in range(1000)]
    _actions: dict[str, Any] = {
        'turn on': lambda x: x + 1 if bright else 1,
        'turn off': lambda x: x - 1 if x > 0  and bright else 0,
        'toggle': lambda x: x + 2 if bright else 1 if x == 0 else 0
    }
    for _line in lines:
        _instructions = findall(r'(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)',
                                _line)
        for action,x1,y1,x2,y2 in _instructions:
            _coords = [(x,y) for x in range(int(x1), int(x2) + 1)
                       for y in range(int(y1), int(y2) + 1)]
            for (x,y) in _coords:
                _lights[y][x] = _actions[action](_lights[y][x])
    for i in range(1000):
        for j in range(1000):
            _count += _lights[i][j]
    print(f'The total count is: {_count}')

def main() -> None:
    if len(argv) < 2:
        print('[ERROR] Usage: py main.py <input file path>')
        return
    with open(argv[1], encoding='utf-8') as _file:
        _lines: str = _file.readlines()
        execute(_lines, False)
        execute(_lines, True)
        _file.close()

main()
