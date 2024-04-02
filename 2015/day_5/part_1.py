import sys

def contains_banned_strs(l: str) -> bool:
    _b_str_lst = ['ab', 'cd', 'pq', 'xy']
    for i in range(len(l) - 1):
        if l[i] + l[i + 1] in _b_str_lst:
            return True
    return False

def repeat_letter(l: str) -> bool:
    _ch: str = ''
    for _,c in enumerate(l):
        if _ch == c:
            return True
        _ch = c
    return False

def contains_vowel(l: str) -> bool:
    _c: int = 0
    for _,c in enumerate(l):
        if c in 'aeiou':
            _c += 1
    return _c >= 3

def main() -> None:
    _c_value: int = 0
    if len(sys.argv) < 2:
        print("ERROR -> MISSING INPUT ARGUMENT!")
        return
    _fn: str = sys.argv[1]
    with open(_fn, encoding='utf-8') as _file:
        for line in _file.readlines():
            if contains_vowel(line) and repeat_letter(line) and not contains_banned_strs(line):
                _c_value += 1
        _file.close()
    print(f'There are {_c_value} nice strings')

main()
