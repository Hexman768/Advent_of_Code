import sys

def contains_banned_strs(l: str) -> bool:
    _b_str_lst = ['ab', 'cd', 'pq', 'xy']
    for i in range(len(l) - 1):
        if _b_str_lst.__contains__(l[i] + l[i + 1]): return True
    return False

def repeat_letter(l: str) -> bool:
    _ch: str = ''
    for i in range(len(l)):
        if _ch == l[i]: return True
        else: _ch = l[i]
    return False

def contains_vowel(l: str) -> bool:
    _c: int = 0
    _v_lst: list[str] = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(l)):
        if _v_lst.__contains__(l[i]): _c += 1
    return True if _c >= 3 else False

def main() -> None:
    _c_value: int = 0
    if len(sys.argv) < 2:
        print("ERROR -> MISSING INPUT ARGUMENT!")
        return
    _fn: str = sys.argv[1]
    with open(_fn) as _file:
        for line in _file.readlines():
            if contains_vowel(line) and repeat_letter(line) and not contains_banned_strs(line):
                _c_value += 1
        _file.close()
    print(f'There are {_c_value} nice strings')

main()