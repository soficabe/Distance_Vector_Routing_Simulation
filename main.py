from network import Network

def simulation1(Network):
    print("Running simulation 1")
    net.add_node("A")
    net.add_node("B")
    net.add_node("C")
    net.add_node("D")
    net.add_node("E")
    net.add_link("A", "B", 1)
    net.add_link("A", "C", 6)
    net.add_link("B", "C", 2)
    net.add_link("B", "D", 1)
    net.add_link("C", "D", 3) 
    net.add_link("C", "E", 7)
    net.add_link("D", "E", 2)

def simulation2(Network):
    print("Running simulation 2")
    net.add_node("A")
    net.add_node("B")
    net.add_node("C")
    net.add_node("D")   
    net.add_link("A", "B", 3)
    net.add_link("A", "C", 5)
    net.add_link("B", "C", 1)
    net.add_link("C", "D", 2)
    

def simulation3(Network):
    print("Running simulation 3")
    net.add_node("A")
    net.add_node("B")
    net.add_node("C")
    net.add_link("A", "B", 1)
    net.add_link("A", "C", 2)
    net.add_link("B", "C", 20)

if __name__ == "__main__":
    net = Network("net")

    simulations = {
        1: simulation1,
        2: simulation2,
        3: simulation3
    }

    while (True):
        choice = int(input("Enter a simulation number (1, 2, or 3): "))

        if choice in simulations:
            simulations[choice](net)
        else:
            print("Invalid choice")
            
        net.update_dvs()
        net.reset_network()
