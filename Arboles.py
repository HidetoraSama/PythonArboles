import sys

class Arbol:
    def __init__(self, val, izq = None, der = None):
        self.valor = val
        self.izquierda = izq
        self.derecha = der

def rInorden(arbol):
    if (arbol == None):
        return []
    else:
        return rInorden(arbol.izquierda) + [arbol.valor] + rInorden(arbol.derecha)

def insertar(valor, arbol):
    if arbol == None:
        return Arbol(valor)
    if (valor > arbol.valor):
        return Arbol(arbol.valor, arbol.izquierda, insertar(valor, arbol.derecha))           
    return Arbol(arbol.valor, insertar(valor, arbol.izquierda), arbol.derecha)

def insertarLista(lista, arbol):
    if lista == []:
        return arbol
    return insertarLista(lista[1:], insertar(lista[0], arbol))

class NArio:
    def __init__(self, valor = ("", (0, 0)), hijos = []):
        self.valor = valor
        self.hijos = hijos
        
    def __str__(self, nivel = 0):
        if nivel == 0:
            rep = "├\t" * (nivel - 1) + repr(self.valor) + "\n"
        else:
            rep = "│\t" * (nivel - 1) + "├────" + repr(self.valor) + "\n"

        for hijo in self.hijos:
            rep += hijo.__str__(nivel + 1)

        return rep

def buscar(nodo, valor, camino):
    if nodo == None:
        return False

    if nodo.valor[0] == valor:
        camino.append(nodo.valor[1])
        return True

    if nodo.hijos == []:
        return False

    if buscar(nodo.hijos[0], valor, camino) or buscar(nodo.hijos[1], valor, camino)\
    or buscar(nodo.hijos[2], valor, camino) or buscar(nodo.hijos[3], valor, camino):
        camino.append(nodo.valor[1])
        return reversar(camino)

    return False

def reversar(lista):
    if len(lista) == 0:
        return []

    return [lista[-1]] + reversar(lista[:-1])

def enLista(lista, valor):
    if lista == []:
        return False

    return lista[0] == valor or enLista(lista[1:], valor)

def enListaDeListas(lista, v, f, c):
    if len(lista) == f:
        return 0, -1

    if len(lista[f]) == c:
        return enListaDeListas(lista, v, f + 1, 0)

    if (lista[f][c] == v):
        return f, c

    return enListaDeListas(lista, v, f, c + 1)

def agregar(valor, lista):
    lista.append(valor)
    return lista

def parametros(lista):
    return (lista,*enListaDeListas(lista, "x", 0, 0))

def arbolizar(lista, f, c, lcoords):
    if f == len(lista) or c == len(lista[0]) or f < 0 or c < 0:
        return NArio((" ", (f, c)), [])

    if enLista(lcoords, (f, c)):
        return NArio((lista[f][c], (f, c)), [])

    if lista[f][c] == "1":
        return NArio(("1", (f, c)), [])

    if lista[f][c] == "y":
        return NArio(("y", (f, c)), [])

    if lista[f][c] == "0" or lista[f][c] == "x":    
        return NArio((lista[f][c], (f, c)),[
                    arbolizar(lista, f, c + 1, agregar((f, c), lcoords)),
                    arbolizar(lista, f + 1, c, agregar((f, c), lcoords)),
                    arbolizar(lista, f, c - 1, agregar((f, c), lcoords)),
                    arbolizar(lista, f - 1, c, agregar((f, c), lcoords))])

    print ("Formato de laberinto incorrecto (use únicamente 1,0,x,y)")
    return NArio(("Soy el problema: " + lista[f][c], (0, 0)), [])

sys.setrecursionlimit(5000)

arbol = Arbol(10, Arbol(5), Arbol(50, Arbol(30, Arbol(20), Arbol(40))))
print(rInorden(arbol))
print(rInorden(insertar(5, arbol)))
print(rInorden(insertarLista([1,5,8,4,2], arbol)))

print("Laberinto arbolizado desde posición X")
print(str(arbolizar(*parametros([x.strip("\n").split(" ") for x in open("laberinto.txt", "r").readlines()]),[])))

print("Camino a la salida:")
print(buscar(arbolizar(*parametros([x.strip("\n").split(" ") for x in open("laberinto.txt", "r").readlines()]),[]),"y",[]))