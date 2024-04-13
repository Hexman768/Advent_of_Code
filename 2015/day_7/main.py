import sys
from functools import lru_cache

lines = []
wires = {}

ops: dict = {
    'AND': lambda arg: get_signal(arg[0]) & get_signal(arg[2]),
    'OR': lambda arg: get_signal(arg[0]) | get_signal(arg[2]),
    'RSHIFT': lambda arg: (get_signal(arg[0]) >> get_signal(arg[2])) & 0xffff,
    'LSHIFT': lambda arg: (get_signal(arg[0]) << get_signal(arg[2])) & 0xffff,
    'NOT': lambda arg: (~get_signal(arg[1])) & 0xffff
}

@lru_cache
def get_signal(k: str) -> int:
    try:
        return int(k)
    except ValueError:
        pass
    command = wires[k].strip().split(' ')

    for op,bitop in ops.items():
        if op in command:
            return get_signal(bitop(command))
    return get_signal(command[0])

if len(sys.argv) < 2:
    print('[ERROR] Usage: py main.py <input file path>')
    sys.exit()
with open(sys.argv[1], encoding='utf-8') as _file:
    lines = _file.readlines()
    for line in lines:
        inst, key = line.split('->')
        wires[key.strip()] = inst.strip()
    result: int = get_signal('a')
    print(result)
    wires['b'] = str(result)
    get_signal.cache_clear()
    _file.close()
