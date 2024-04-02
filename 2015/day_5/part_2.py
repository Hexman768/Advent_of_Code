import sys

def contains_repeating_letters(line: str) -> bool:
    _c: int = 0
    _str: str = ''
    for i in range(len(line) - 2):
        if line[i] + line[i + 1] == _str:
            _c += 1

def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR: MISSING INPUT FILE ARGUMENT!")
        return
    with open(sys.argv[1], encoding='utf-8') as _f:
        for _line in _f:
            break
        _f.close()

main()
