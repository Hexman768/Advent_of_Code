import sys

def part_1() -> None:
    _sum: int = 0
    with open(sys.argv[1]) as _file:
        for line in _file.readlines():
            _n_str: str = ''
            #print(line)
            for i in range(len(line)):
                if line[i] in '0123456789':
                    _n_str += line[i]
            #print(_n_str)
            _n_str = _n_str[0] + _n_str[len(_n_str) - 1]
            _sum += int(_n_str)
            print(_n_str)
            print(f'Sum is {_sum}')
        _file.close()

def part_2() -> None:
    _sum: int = 0
    _n_line_lst: list[str] = []
    _num_vect: dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    with open(sys.argv[1]) as _file:
        for line in _file.readlines():
            for key in _num_vect.keys():
                print(f'Checking if {key} in {line}')
                if key in line:
                    line = line.replace(key, _num_vect.get(key))
            _n_line_lst.append(line)
            print(line)
        _file.close()
    return

def main() -> None:
    if len(sys.argv) < 2:
        print('ERROR: MISSING INPUT FILE ARGUMENT!')
        return
    part_2()
    return

main()
