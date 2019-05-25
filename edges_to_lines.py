import pickle
import sys
from osm2graph import dist, distx, disty

def get_center(coords):
    sx = 0.0
    sy = 0.0
    min_x = float("inf")
    min_y = float("inf")
    for ind in coords:
        (x, y) = coords[ind]
        sx += x
        sy += y
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    #print(sx, sy)
    #print(sx / len(coords), sy / len(coords))
    #print((sx, sy), file=sys.stderr)
    #return (sx / len(coords) + min_x, sy / len(coords) + min_y)
    return (min_x, min_y)

def degree_to_decart(coord, center):
    x, y = coord
    cx, cy = center
    return (int(distx(x, cx)), int(disty(y, cy)))

def main():
    name = 'res.txt'
    f = open(name, 'r')
    f.readline()
    choses = list(map(lambda s: int(s) - 1, f.readline().split()))
    f.close()
    f = open('coord.dump', 'rb')
    coords = pickle.load(f)
    f.close()
    f = open('ways.dump', 'rb')
    ways = pickle.load(f)
    f.close()
    #print(coords, file=sys.stderr)
    center = get_center(coords)
    #print(center, file=sys.stderr)
    print(len(choses))
    for i in choses:
        (v, u, _) = ways[i]
        print(*degree_to_decart(coords[v], center), *degree_to_decart(coords[u], center))

main()
