from node import Node
class Network:
    def __init__(self, net_id):
        self.net_id = net_id
        self.nodes: dict[str, Node] = {} #dizionario di nodi: chiave = id del nodo, valore = oggetto nodo
        self.links: dict[str, dict[str, int]] = {} #dizionario di dizionari: per ogni nodo, un dizionario con i nodi adiacenti e il costo del link

    def add_node(self, node_id):
        self.nodes[node_id] = Node(node_id)

    def remove_node(self, node_id):
        if node_id in self.nodes:
            # Rimuove i link associati al nodo
            for neighbour in list(self.links.get(node_id, {}).keys()): #prende il dizionario dei nodi adiacenti a node_id e ne prende le chiavi
                self.remove_link(node_id, neighbour) #per ogni nodo adiacente, rimuove il link
            # Rimuove il nodo stesso
            del self.nodes[node_id]
            del self.links[node_id]
        else:
            print(f"Node {node_id} not found")

    def add_link(self, node1_id, node2_id, cost):
        self.links.setdefault(node1_id, {})[node2_id] = cost
        self.links.setdefault(node2_id, {})[node1_id] = cost

        self.nodes[node1_id].dv[node2_id] = (cost, node2_id)
        self.nodes[node2_id].dv[node1_id] = (cost, node1_id)

    def remove_link(self, node1_id, node2_id):
        if node2_id in self.links.get(node1_id, {}):
            del self.links[node1_id][node2_id]
            del self.links[node2_id][node1_id]

            del self.nodes[node1_id].dv[node2_id]
            del self.nodes[node2_id].dv[node1_id]
        else:
            print(f"Link between {node1_id} and {node2_id} not found")

    def update_dvs(self):
        net_updated = True
        num_of_steps = 0
        while net_updated:
            net_updated = False
            for node_id, node in self.nodes.items():
                for neighbour_id, _ in self.links.get(node_id, {}).items():
                    neighbour_dv = self.nodes[neighbour_id].dv
                    node_updated = node.update_node_dv(neighbour_dv, neighbour_id)
            if node_updated:
                net_updated = True
            num_of_steps += 1
        print("Converged in", num_of_steps, "steps")
        
    def reset_network(self):
        self.nodes.clear()
        self.links.clear()
       

    def print_network(self):    
        print(f"Network {self.net_id}:")
        for node_id, node in self.nodes.items():
            print(f"Node {node_id}: {node.dv}")
        print(f"Links: {self.links}")
        print()
    

