import sys

def main() -> None:
    if len(sys.argv) < 2:
        print('ERROR: MISSING INPUT FILE ARGUMENT!')
        return
    
    with open(sys.argv[1]) as _file:
        _n_str = ''
        for line in _file.readlines():
            for i in range(len(line)):
                if line[i] in '0123456789':
                    _n_str += line[i]
                    break
        _file.close()

main()