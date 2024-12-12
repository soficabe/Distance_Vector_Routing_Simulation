from network import Network
"""
Questo script simula il routing di diverse topologie di rete utilizzando l'algoritmo di Distance Vector Routing.
L'utente può scegliere tra 3 simulazioni diverse, o uscire dal programma.
"""

# Funzioni che configurano tre diverse topologie di rete
def simulation1(Network):
    print("SIMULATION 1 ----------------------------------------------------\n")
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
    print("SIMULATION 2 ----------------------------------------------------\n")
    net.add_node("A")
    net.add_node("B")
    net.add_node("C")
    net.add_node("D")   
    net.add_link("A", "B", 3)
    net.add_link("A", "C", 5)
    net.add_link("B", "C", 1)
    net.add_link("C", "D", 2)
    

def simulation3(Network):
    print("SIMULATION 3 ----------------------------------------------------\n")
    net.add_node("A")
    net.add_node("B")
    net.add_node("C")
    net.add_link("A", "B", 1)
    net.add_link("A", "C", 2)
    net.add_link("B", "C", 20)


if __name__ == "__main__":
    # Inizio del programma principale
    # Crea un'istanza della rete e definisce le simulazioni disponibili per essere eseguite
    net = Network("net")

    simulations = {
        1: simulation1,
        2: simulation2,
        3: simulation3,
    }

    # Ciclo principale per selezionare e avviare le simulazioni
    # L'utente può scegliere tra 3 simulazioni da eseguire o uscire dal programma inserendo 0
    while (True):
        choice = int(input("Inserisci un numero di simulazione (1, 2 o 3), oppure 0 per uscire: "))

        if choice in simulations:
            simulations[choice](net)
        elif choice == 0:
            print("EXIT\n")
            break

        net.update_dvs() # Funzione principale che scambia e aggiorna i distance vectors dei nodi finche' la rete non converge
        net.reset_network() # Resetta la rete per la prossima simulazione
