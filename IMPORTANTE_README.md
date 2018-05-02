# PythonArboles
Integrantes:
* Luis Esteban Murillo Claver - 20161020091
* Cristian Alejandro Gaitán Mora - 20161020067
* Diego David Romero Quiroga - 20161020082

Ejercicios de arboles
1) Recorrido desarrollado: Inorden (izquierda, raiz, derecha)
2) Nombre función: InsertarLista
3)
Restricciones laberinto: No hay restricciones sobre el uso.
Indicaciones:
* Se establece un limite de recursión alto para resolver laberintos muy extensos
* No es necesario que el laberinto esté rodeado de "1".
Análisis:
Cada laberinto se resuelve, no obstante el camino indicado puede no ser el más corto.
Una parte de la eficiencia radica en el orden en el que son añadidos los hijos al arbol;
se establece el orden derecha, abajo, izquierda, arriba para buscar los hijos. Ello quiere
decir que se dará mayor prioridad a los posibles caminos, en dicho orden, sin importar
que un camino u otro sea precisamente el más o menos corto.
