class GrafoDirigido:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice in self.grafo:
            return "Ya está en el grafo"
        self.grafo[vertice] = []

    def agregar_arista(self, arista):
        v1 = arista.get_v1()
        v2 = arista.get_v2()
        if v1 not in self.grafo:
            raise ValueError(f'Vertice {v1.get_name()} no agregado')
        if v2 not in self.grafo:
            raise ValueError(f'Vertice {v1.get_name()} no agregado')
        self.grafo[v1].append(v2)

    def hay_vertice(self,vertice):
        return vertice in self.grafo
    
    def get_vertice(self, vertice_nombre):
        for v in self.grafo:
            if vertice_nombre == v.get_name():return v
        print(f'Vertice {vertice_nombre} no existe')

    def get_vecinos(self,vertice):
        return self.grafo[vertice]
    
    def __str__(self):
        all_aristas = ''
        for v1 in self.grafo:
            for v2 in self.grafo[v1]:
                all_aristas += v1.get_name() + ' ----> ' + v2.get_name() + '\n'

        return all_aristas        
class Arista:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2 
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def __str__(self):
        return self.v1.get_name() + ' -----> ' + self.v2.get_name()

class Vertice:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
        
g = GrafoDirigido()
def construir_grafo(grafo):
    g = grafo()
    for v in ('s', 'a','b','c','d','e','f','g'):
        g.agregar_vertice(Vertice(v))
    g.agregar_arista(Arista(g.get_vertice('s'), g.get_vertice('a')))
    g.agregar_arista(Arista(g.get_vertice('s'), g.get_vertice('b')))
    g.agregar_arista(Arista(g.get_vertice('s'), g.get_vertice('c')))
    g.agregar_arista(Arista(g.get_vertice('s'), g.get_vertice('d')))
    return g

g1 = construir_grafo(GrafoDirigido)

print(g1)