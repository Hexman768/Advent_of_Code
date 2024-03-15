def day2_2(fn):
    total = 0
    for line in open(fn):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = 2 * min(l+w, w+h, h+l)
        ribbon += l*w*h
        total += ribbon
    print('Total ribbon required: ', total)

def surface_area(l, w, h):
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)
    return area + slack

def day2_1(fn):
    total = 0
    lines = open(fn).readlines()
    for line in open(fn):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area = surface_area(l,w,h)
        total += area
    print('Total area is: ', total)

def main(fn):
    day2_1(fn)
    day2_2(fn)
main('input.txt')

