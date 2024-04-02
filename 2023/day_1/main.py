import sys

def part_1(lines: list[str]) -> None:
    _sum: int = 0
    for line in lines:
        _n_str: str = ''
        for i,_ in enumerate(line):
            if line[i].isdigit():
                _n_str += line[i]
        _n_str = _n_str[0] + _n_str[len(_n_str) - 1]
        _sum += int(_n_str)
    print(f'Sum is {_sum}')

def part_2(lines: list[str]) -> None:
    _n_line_lst: list[str] = []
    _num_vect: dict = {'one':'o1e',
                       'two':'t2o',
                       'three':'t3e',
                       'four':'f4r',
                       'five':'f5e',
                       'six':'s6x',
                       'seven':'s7n',
                       'eight':'e8t',
                       'nine':'n9e'}
    for line in lines:
        for k,_ in _num_vect.items():
            line = line.replace(k, _num_vect.get(k))
        _n_line_lst.append(line)
    part_1(_n_line_lst)

def main() -> None:
    if len(sys.argv) < 2:
        print('ERROR: MISSING INPUT FILE ARGUMENT!')
        return
    with open(sys.argv[1], encoding='utf-8') as _file:
        _lines: list[str] = _file.readlines()
        part_1(_lines)
        part_2(_lines)
    _file.close()

main()
