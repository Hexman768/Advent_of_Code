import sys

def contains_vowel(l: str) -> bool:
    _c: int = 0
    _v_lst: list[str] = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(l)):
        if _v_lst.__contains__(l[i]):
            _c += 1
    return True if _c >= 3 else False

def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR -> MISSING INPUT ARGUMENT!")
        return
    _fn: str = sys.argv[1]
    with open(_fn) as _file:
        for line in _file.readlines():
            if contains_vowel(line): print('Contains at least three vowels')
            else: print('Doesn\'t contain at least three vowels')
        _file.close()

main()