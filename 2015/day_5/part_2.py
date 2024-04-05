import re
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR: MISSING INPUT FILE ARGUMENT!")
        return
    _c: int = 0
    with open(sys.argv[1], encoding='utf-8') as _f:
        for _line in _f.readlines():
            if (len(re.findall(r'([a-z]{2}).*\1', _line)) > 0 and
                len(re.findall(r'([a-z]).\1', _line)) > 0):
                _c += 1
        _f.close()
    print(f'There are {_c} nice strings')

main()
