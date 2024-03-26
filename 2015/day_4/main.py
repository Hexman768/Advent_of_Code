import sys
import hashlib

def validate_hash(md5: str) -> bool:
    print(md5)
    for i in range(5):
        if md5[i] != '0':
            return False
        #break
    return True

def generate_md5(msg: str) -> str:
    _c_value: int = 0
    _md5: str = hashlib.md5(msg.encode('utf-8')).hexdigest()
    while not validate_hash(_md5):
        _c_value += 1
        msg += str(_c_value)
        print(msg)
        _md5 = hashlib.md5(msg.encode('utf-8')).hexdigest()
    return _md5


def main() -> None:
    _msg: str = sys.argv[1]
    generate_md5(_msg)

main()