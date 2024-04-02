def main(fn: str) -> None:
    floor: int = 0
    with open(fn, encoding='utf-8') as file:
        while 1:
            char: str = file.read(1)
            if not char:
                break
            print(char)
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
        print("Santa is on floor: " + str(floor))

main("input.txt")
