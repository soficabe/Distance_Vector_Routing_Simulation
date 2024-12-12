class Node:
    '''
    Classe che rappresenta un nodo appartenente ad una network
    '''

    def __init__(self, node_id):
        '''
        Costruttore della classe Node

        Args:
        node_id (str): id del nodo
        '''
        self.node_id = node_id
        self.dv: dict[str, tuple[int, str]] = {} #dizionario dei nodi raggiungibili (distance vector):
                                                 #chiave = destinazione, valore = tupla (distanza dalla destinazione, next_hop)
        self.dv[node_id] = (0, node_id) #aggiunge il nodo stesso al distance vector con costo 0

    def update_node_dv(self, neigbour_dv, neighbour_id):
        '''
        Aggiorna il distance vector del nodo consultando il distance vector del vicino

        Args:
        neigbour_dv (dict[str, tuple[int, str]]): distance vector del vicino
        neighbour_id (str): id del vicino
        '''
        updated = False

        # Per ogni destinazione raggiungibile dal vicino, calcola la nuova distanza e aggiorna il distance vector del nodo se necessario
        for destination, (distance, _) in neigbour_dv.items():
            new_distance = distance + self.dv[neighbour_id][0]
            if destination not in self.dv or new_distance < self.dv[destination][0]:
                self.dv[destination] = (new_distance, self.dv[neighbour_id][1])
                updated = True
        
        return updated
    
    def print_distance_vector(self):
        '''
        Stampa il distance vector del nodo
        '''
        print(f"Distance Vector di {self.node_id}:")
        for destination, (distance, next_hop) in self.dv.items():
            print(f"  Destinazione {destination} --> Distanza = {distance}, Next Hop = {next_hop} \n")

    def print_distance_vector_after_neighbour_dv_received(self, neighbour_id):
        '''
        Stampa il distance vector del nodo specificando che è stato aggiornato dopo aver ricevuto il distance vector del vicino
        '''
        print(f"Distance Vector di {self.node_id}:")
        print(f"Dopo aver ricevuto DV({neighbour_id})")
        for destination, (distance, next_hop) in self.dv.items():
            print(f"  Destinazione {destination} --> Distanza = {distance}, Next Hop = {next_hop} \n")

