import sys

def main() -> None:
    _sum: int = 0
    if len(sys.argv) < 2:
        print('ERROR: MISSING INPUT FILE ARGUMENT!')
        return
    
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

main()
