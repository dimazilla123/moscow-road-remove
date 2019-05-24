import osm2graph
import pickle

def main():
    pickle.dump(osm2graph.get_coords_by_id(), open('coord.dump', 'wb'))

main()
