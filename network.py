from node import Node
class Network:
    '''
    Classe che rappresenta una rete di nodi Node.
    Contiene i nodi della rete e i link tra di essi.
    '''
    def __init__(self, net_id):
        '''
        Costruttore della classe Network

        Args:
        net_id (str): id della rete
        '''
        self.net_id = net_id
        self.nodes: dict[str, Node] = {} #dizionario dei nodi della rete: chiave = id del nodo, valore = oggetto Node relativo
        self.links: dict[str, dict[str, int]] = {} # dizionario di dizionari che rappresenta i link tra i nodi: 
                                                   # chiave = id del nodo, valore = dizionario dei nodi adiacenti con costo associato

    def add_node(self, node_id):
        '''
        Aggiunge un nodo alla rete

        Args:
        node_id (str): id del nodo
        '''
        self.nodes[node_id] = Node(node_id)

    def add_link(self, node1_id, node2_id, cost):
        '''
        Aggiunge alla rete un link tra due nodi con il relativo costo. 
        Poi aggiorna anche i distance vectors dei nodi coinvolti, in questo modo 
        i distance vectors sono inizializzati con i costi dei link diretti.

        Args:
        node1_id (str): id del primo nodo
        node2_id (str): id del secondo nodo
        cost (int): costo del link
        '''
        self.links.setdefault(node1_id, {})[node2_id] = cost
        self.links.setdefault(node2_id, {})[node1_id] = cost

        self.nodes[node1_id].dv[node2_id] = (cost, node2_id)
        self.nodes[node2_id].dv[node1_id] = (cost, node1_id)

    def update_dvs(self):
        '''
        Funzione principale che aggiorna i distance vectors dei nodi finche' la rete non converge.

        Ad ogni iterazione ogni nodo riceve i distance vectors dei vicini e 
        in base a questi aggiorna il proprio distance vector se necessario.
        Dopo ogni aggiornamento, il nodo stampa il proprio distance vector.
    
        La funzione termina quando non ci sono più aggiornamenti da fare in nessun nodo.
        '''
        print("DV INIZIALI: \n")
        self.print_all_dvs()
        net_updated = True
        iterations = 0
        while net_updated:
            net_updated = False
            iterations += 1
            print(f"ITERAZIONE {iterations} ----------------------------------------------------\n")
            for node_id, node in self.nodes.items():
                for neighbour_id, _ in self.links.get(node_id).items():
                    neighbour_dv = self.nodes.get(neighbour_id).dv
                    node_route_updated = node.update_node_dv(neighbour_dv, neighbour_id)
                    if node_route_updated:
                        net_updated = True
                        node.print_distance_vector_after_neighbour_dv_received(neighbour_id)
                    

        print(f"NESSUN AGGIORNAMENTO, la CONVERGENZA è stata ottenuta in {iterations-1} iterazioni\n")
        print("DV FINALI: \n")
        self.print_all_dvs()
        
    def reset_network(self):
        '''
        Resetta la rete per la prossima simulazione
        '''
        self.nodes.clear()
        self.links.clear()
       
    def print_all_dvs(self):
        '''
        Stampa i distance vectors di tutti i nodi della rete
        '''
        for node_id, node in self.nodes.items():
            node.print_distance_vector()
    

