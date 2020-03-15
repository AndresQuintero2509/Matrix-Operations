class Operaciones:
    def leer_adyacencia(self):
        """ Lee pesos en una matriz de adyacencia """
        matriz = []
        n = int(input("Longitud de la Matriz: "))

        for i in range(n):
            matriz.append([])
            for j in range(n):
                matriz[i].append(int(input(f'Peso en la posición ({i},{j}): ')))
        print(f'Matriz de Adyacencia: ')
        self.print_matriz(matriz)
        self.transformar_arcos_pesos(matriz, n)

    def leer_arcos_pesos(self):
        """ Lee pesos en una matriz de Arcos y Pesos """
        matriz = []
        data = []
        n = int(input("Longitud de la Matriz: "))
        for i in range(n):
            for j in range(n):
                data.append(i)
                data.append(j)
                data.append(int(input(f'Peso en la posición ({i},{j}): ')))
                matriz.append(data)
                data = []
        print(f'Matriz de Arcos y Pesos: ')
        self.print_matriz(matriz)
        self.transformar_adyacencia(matriz, n)
    
    def transformar_adyacencia(self, matriz, n):
        """ Transforma una matriz de Arcos y Pesos en una matriz de Adyacencia """
        matriz_adyacencia = []
        for i in range(n):
            matriz_adyacencia.append([])
            for j in range(n):
                matriz_adyacencia[i].append(matriz[0][2])
                matriz.pop(0)
        print(f'Matriz de Adyacencia: ')
        self.print_matriz(matriz_adyacencia)
    
    def transformar_arcos_pesos(self, matriz, n):
        """ Transforma una matriz de Adyacencia en una matriz de Arcos y Pesos """
        data = []
        matriz_arcos = []
        for i in range(n):
            for j in range(n):
                data.append(i)
                data.append(j)
                data.append(matriz[i][j])
                matriz_arcos.append(data)
                data = []
        print(f'Matriz de Arcos y Pesos: ')
        self.print_matriz(matriz_arcos)

    def print_matriz(self, matriz):
        for fila in matriz:
            print(fila)

if __name__ == "__main__":
    try:
        opt = int(input(f'[0] Ingresar una Matriz de Adyacencia \n[1] Ingresar Matriz de Arcos y Pesos \nIngrese opción: '))
        Operaciones().leer_adyacencia() if opt == 0 else Operaciones().leer_arcos_pesos()
    except Exception as error:
        print(f'[ERROR] {error}')
    