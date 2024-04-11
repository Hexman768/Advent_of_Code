import sys
from functools import lru_cache

lines = []
wires = {}

@lru_cache
def get_signal(k: str) -> int:
    try:
        return int(k)
    except ValueError:
        pass
    command = wires[k].strip().split(' ')
    #print(wires)
    #print(command)

    if 'NOT' in command:
        #print(command)
        _temp = get_signal(command[1])
        #print(_temp)
        return (~_temp) & 0xffff
    elif 'AND' in command:
        return get_signal(command[0]) & get_signal(command[2])
    elif 'OR' in command:
        return get_signal(command[0]) | get_signal(command[2])
    elif 'LSHIFT' in command:
        return (get_signal(command[0]) << get_signal(command[2])) & 0xffff
    elif 'RSHIFT' in command:
        return (get_signal(command[0]) >> get_signal(command[2])) & 0xffff
    else:
        return get_signal(command[0])

if len(sys.argv) < 2:
    print('[ERROR] Usage: py main.py <input file path>')
    sys.exit()
with open(sys.argv[1], encoding='utf-8') as _file:
    lines = _file.readlines()
    for line in lines:
        inst, key = line.split('->')
        wires[key.strip()] = inst.strip()
    print(get_signal('a'))
    #print(wires)
    _file.close()
