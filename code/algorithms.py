import math

def depth_first_search(grafo, inicio, destino, fechados=frozenset(),bateria=None, consumo=None):
    # """ -> docstring
    """Depth first search, versão iterativa com uma stack

    grafo   -> representado por um dicionário
    incio   -> nó aonde o drone está quando planeia
    destino -> nó que o drone pretende alcançar / teste objetivo
    fechados -> nós (neste caso portas e barreiras) que o drone sabe estarem fechados
    bateria -> bateria atual do drone, ignora a bateria
    consumo -> consumo que o drone gasta a percorre os nós distancia / velocidade

    Devolve (caminho, nós_expandidos). caminho é None se não houver solução.
    """

    # 
    pilha = [(inicio, bateria, [inicio])]

    melhor_bateria = {}
    expandidos = 0

    while pilha:
        no, bat, caminho = pilha.pop()

        # Já expandimos este nó com bateria igual ou superior? Então não vale a pena.
        bat_comparar = 0 if bat is None else bat
        if no in melhor_bateria and bat_comparar <= melhor_bateria[no]:
            continue
        melhor_bateria[no] = bat_comparar
        expandidos += 1

        #Teste objetivo: o drone está no nó destino
        if no == destino:
            return caminho, expandidos

        for vizinho, distancia in reversed(grafo.get(no, [])):
            #O drone não sabe que o vizinho está fechado
            if vizinho in fechados:
                continue

            nova_bat = bat
            if bat is not None:
                nova_bat = bat - consumo(distancia)
                if nova_bat < 0:
                    continue

            if vizinho in caminho:
                continue
            pilha.append((vizinho, nova_bat, caminho + [vizinho]))

        return None, expandidos

        


