import osm2graph
import pickle

def main():
    coords = osm2graph.get_coords_by_id()
    compr = osm2graph.compress_coords(coords)
    ways = osm2graph.get_ways(coords)
    pickle.dump(coords, open('coord.dump', 'wb'))
    pickle.dump(compr, open('compr.dump', 'wb'))
    pickle.dump(ways, open('ways.dump', 'wb'))

main()
