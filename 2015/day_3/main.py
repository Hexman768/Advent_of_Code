def day3_2(fn: str) -> None:
    s_coords: list[int, int] = [0,0]
    rbs_coords: list[int, int] = [0,0]
    houses: list[list[int, int]] = [[0,0]]
    with open(fn) as file:
        while 1:
            chars = file.read(2)
            if not chars:
                break
            # check Santa coords
            if chars[0] == '>':
                s_coords[0] += 1
            elif chars[0] == '<':
                s_coords[0] -= 1
            elif chars[0] == '^':
                s_coords[1] -=1
            elif chars[0] == 'v':
                s_coords[1] += 1
            # check robo_Santa coords
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
        print(len(houses))
        #print(houses)

def check_houses(h: list[list[int, int]], c: list[int, int]) -> bool:
    for house in h:
        if c[0] == house[0] and c[1] == house[1]:
            #print(c, 'is already in list')
            #print(h)
            return True
    return False

def day3_1(fn: str) -> None:
    coords = [0,0]
    houses = [[0,0]]
    with open(fn) as file:
        while 1:
            char: str = file.read(1)
            print(char)
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
                #print('Adding', coords, 'to list')
                houses.append(coords[:])
        print('Santa delivered presents to', len(houses), 'houses')

def main(fn: str) -> None:
    # day3_1(fn)
    day3_2(fn)
main('input.txt')