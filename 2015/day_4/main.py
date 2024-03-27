import sys
import hashlib

def validate_hash(md5: str, zrs: int) -> bool:
    for i in range(zrs):
        if md5[i] != '0':
            return False
    return True

def generate_md5(msg: str, zrs: int) -> str:
    _c_value: int = 0
    _md5: str = hashlib.md5(msg.encode('utf-8')).hexdigest()
    _msg_cpy: str = msg
    while not validate_hash(_md5, zrs):
        _c_value += 1
        msg = _msg_cpy + str(_c_value)
        _md5 = hashlib.md5(msg.encode('utf-8')).hexdigest()
    print(f'The integer required is: {_c_value}')
    return _md5


def main() -> None:
    if len(sys.argv) < 2:
        print('ERROR - MISSING COMMAND LINE ARGUMENT: Input msg key for MD5 encyrption')
        return
    _msg: str = sys.argv[1]
    print(f'Part 1: {generate_md5(_msg, 5)}')
    print(f'Part 2: {generate_md5(_msg, 6)}')

main()
