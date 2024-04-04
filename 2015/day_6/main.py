import re
import ast
import sys

def extract_coords(coords_str: list[str]) -> None:
    x1,y1,x2,y2 = 0,0,0,0
    temp = tuple([x for x in coords_str])
    #print(tuple([a for a in temp]))
    return

def part_1(lines: str) -> None:
    _inst: str = ''
    _min_xy: list[int] = []
    _max_xy: list[int] = []
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
    extract_coords(_coords)
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
