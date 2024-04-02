def day3_2(fn: str) -> None:
    s_coords: list[int] = [0,0]
    rbs_coords: list[int] = [0,0]
    houses: list[list[int]] = [[0,0]]
    with open(fn, encoding='utf-8') as file:
        while 1:
            chars = file.read(2)
            if not chars:
                break

            if chars[0] == '>':
                s_coords[0] += 1
            elif chars[0] == '<':
                s_coords[0] -= 1
            elif chars[0] == '^':
                s_coords[1] -=1
            elif chars[0] == 'v':
                s_coords[1] += 1

            if chars[1] == '>':
                rbs_coords[0] += 1
            elif chars[1] == '<':
                rbs_coords[0] -= 1
            elif chars[1] == '^':
                rbs_coords[1] -=1
            elif chars[1] == 'v':
                rbs_coords[1] += 1

            if not check_houses(houses, s_coords):
                houses.append(s_coords[:])
            if not check_houses(houses, rbs_coords):
                houses.append(rbs_coords[:])
        print(f'Santa and Robo-Santa delivered presents to {len(houses)} houses')

def check_houses(h: list[list[int]], c: list[int]) -> bool:
    for house in h:
        if c[0] == house[0] and c[1] == house[1]:
            return True
    return False

def day3_1(fn: str) -> None:
    coords = [0,0]
    houses = [[0,0]]
    with open(fn, encoding='utf-8') as file:
        while 1:
            char: str = file.read(1)
            if not char:
                break
            if char == '>':
                coords[0] += 1
            elif char == '<':
                coords[0] -= 1
            elif char == '^':
                coords[1] -= 1
            elif char == 'v':
                coords[1] += 1
            if not check_houses(houses, coords):
                houses.append(coords[:])
        print(f'Santa delivered presents to {len(houses)} houses')

def main(fn: str) -> None:
    day3_1(fn)
    day3_2(fn)

main('input.txt')
