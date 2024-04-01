import sys

def part_1(lines: list[str]) -> None:
    _sum: int = 0
    for line in lines:
        _n_str: str = ''
        #print(line)
        for i in range(len(line)):
            if line[i].isdigit():
                _n_str += line[i]
        #print(_n_str)
        _n_str = _n_str[0] + _n_str[len(_n_str) - 1]
        _sum += int(_n_str)
        #print(_n_str)
        print(f'Sum is {_sum}')

def part_2(lines: list[str]) -> None:
    _sum: int = 0
    _n_line_lst: list[str] = []
    _num_vect: dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for line in lines:
        for key in _num_vect.keys():
            print(f'Checking if {key} in {line}')
            if key in line:
                line = line.replace(key, _num_vect.get(key))
        _n_line_lst.append(line)
        print(_n_line_lst)
        part_1(_n_line_lst)
    return

def main() -> None:
    if len(sys.argv) < 2:
        print('ERROR: MISSING INPUT FILE ARGUMENT!')
        return
    _file = open(sys.argv[1])
    _lines: list[str] = _file.readlines()
    _file.close()
    part_1(_lines)
    #part_2(_lines)
    return

main()
