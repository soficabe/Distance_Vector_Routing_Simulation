class Node:
    '''
    Classe nodo per rappresentare un nodo della network

    Attributi:
    node_id (string): id del nodo
    dv (dict): dizionario che rappresenta il distance vector del nodo, contiene i nodi vicini e i relativi costi per raggiungerli
    '''
    def __init__(self, node_id):
        self.node_id = node_id
        self.dv: dict[str, tuple[int, str]] = {} #dizionario dei nodi raggiungibili e relativi costi e next hop

    def update_node_dv(self, neigbour_dv, neighbour_id):
        '''
        Aggiorna il distance vector del nodo con il distance vector del vicino

        Args:
        neigbour_dv (dict): distance vector del vicino
        '''
        updated = False

        for destination, (distance, _) in neigbour_dv.items():
            if destination not in self.dv or self.dv[neighbour_id][0] + distance < self.dv[destination][0]:
                self.dv[destination] = (distance, neighbour_id)
                updated = True
        
        return updated
    
    def print_distance_vector(self):
        print(f"Distance Vector del Nodo {self.node_id}:")
        for destination, (distance, next_hop) in self.dv.items():
            print(f"  Destinazione {destination} --> Distanza = {distance}, Next Hop = {next_hop} \n")

