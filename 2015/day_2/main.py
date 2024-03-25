def day2_2(fn: str) -> None:
    total: int = 0
    for line in open(fn):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon: int = 2 * min(l+w, w+h, h+l)
        ribbon += l*w*h
        total += ribbon
    print('Total ribbon required: ', total)

def surface_area(l: int, w: int, h: int) -> int:
    area: int = 2*l*w + 2*w*h + 2*h*l
    slack: int = min(l*w, w*h, h*l)
    return area + slack

def day2_1(fn: str) -> None:
    total: int = 0
    for line in open(fn):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area: int = surface_area(l,w,h)
        total += area
    print('Total area is: ', total)

def main(fn: str) -> None:
    day2_1(fn)
    day2_2(fn)

main('input.txt')
