import sys

lines = []
wires = {}

def get_signal(key: str) -> int:
    try:
        return int(key)
    except ValueError:
        pass
    command = wires[key].strip().split(' ')
    print(wires)
    print(command)

    if 'NOT' in command:
        print(command)
        return ~get_signal(command[1])
    elif 'AND' in command:
        return get_signal(command[0]) & get_signal(command[2])
    elif 'OR' in command:
        return get_signal(command[0]) | get_signal(command[2])
    elif 'LSHIFT' in command:
        return get_signal(command[0]) << get_signal(command[2])
    elif 'RSHIFT' in command:
        return get_signal(command[0]) >> get_signal(command[2])
    else:
        return command[0]

if len(sys.argv) < 2:
    print('[ERROR] Usage: py main.py <input file path>')
    sys.exit()
with open(sys.argv[1], encoding='utf-8') as _file:
    lines = _file.readlines()
    for line in lines:
        inst, key = line.split('->')
        wires[key.strip()] = inst.strip()
    print(get_signal('i'))
    #print(wires)
    _file.close()
