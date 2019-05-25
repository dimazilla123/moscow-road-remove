from xml.etree import ElementTree
from math import cos, hypot, pi

def get_coords_by_id(name='map.osm'):
    ret = {}
    data = ElementTree.parse(name)
    root = data.getroot()
    for node in root:
        if node.tag == 'node':
            ret[int(node.attrib['id'])] = (float(node.attrib['lon']), float(node.attrib['lat']))
    return ret

def get_ways(coords, name='map.osm'):
    ret = []
    data = ElementTree.parse(name)
    root = data.getroot()
    for way in root:
        if way.tag == 'way':
            curr_way = []
            for nd in way:
                if nd.tag == 'nd':
                    curr_way.append(int(nd.attrib['ref']))
            for i in range(len(curr_way) - 1):
                ret.append((curr_way[i], curr_way[i + 1], dist(coords[curr_way[i]], coords[curr_way[i + 1]])))
    return ret


def compress_coords(coords):
    compress = list(coords.keys())
    compress.sort()
    ret = {}
    i = 0
    for n in compress:
        ret[n] = i
        i += 1
    return ret

def dist1d(a, b):
    return abs(a - b) * (40074000 / 360 / 2)

def distx(x1, x2, y=0):
    return abs(x1 - x2) * (40074000 * cos(y * pi / 180)) / 360

def disty(y1, y2):
    return abs(y1 - y2) * (40074000 / 360)

def dist(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return hypot(distx(x1, x2, y1), disty(y1, y2))

def main():
    coords = get_coords_by_id()
    compr = compress_coords(coords)
    ways = get_ways(coords)
    #print(ways)
    for i in range(len(ways)):
        to, frm, l = ways[i]
        ways[i] = (compr[to], compr[frm], l)
    print(len(compr), len(ways))
    for way in ways:
        print(way[0] + 1, way[1] + 1, way[2])
if __name__ == '__main__':
    main()
