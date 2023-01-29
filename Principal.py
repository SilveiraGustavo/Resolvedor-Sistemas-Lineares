import numpy as np
import pivotamento as pvt
from jacobi import jacobi
from convergencia import espectral

# Autor: Gustavo Silveira Dias
# Instituição: Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais
# Disciplina: Cálculo Numérico

# Enquanto é verdadeiro
while True:
    # Entrada da quantidade de variáveis do sistema 
    n = int(input('INFORME O NÚMERO DE VARIÁVEIS DO SISTEMA.'))

    Mat = np.array (pvt.ler_matriz(n),  dtype='double')
    # Entrada da tolerancia utilizado no Método de jacobi
    tol = float(input('INFORME A TOLERANCIA.'))
    # Entrada das iterações  utilizado no Método de jacobi
    iteracoes = int(input('INFORME O NÚMERO MÁXIMO DE ITERAÇÕES.'))
    x0 = np.zeros(len(Mat))

    print('================================================')
    print('             MATRIZ ORIGINAL                    ')
    print('================================================')
    print(Mat)

    b = np.array([x[-1] for x in Mat], dtype='double')

    print('================================================')
    print('             DECOMPOSIÇÃO                       ')
    

    dec = np.diag(np.diag(Mat))
    print('================================================')
    print('             DIAGONAL PRINCIPAL                 ')
    print('================================================\n')
    print(dec)

    modificar_Mat = Mat[:, : -1]
    aux = np.tril(modificar_Mat) - dec
    print('================================================')
    print('       DIAGONAL PRINCIPAL / TRIANGULAR SUP.     ')
    print('================================================\n')
    print(aux)

    aux2 = np.triu(modificar_Mat) - dec
    print('================================================')
    print('       DIAGONAL PRINCIPAL / TRIANGULAR INF.     ')
    print('================================================\n')
    print(aux2)
    
    espectral(dec,aux,aux2,b)
    # Pergunta para o usuário se ele deseja continuar
    entrada_User = input(' VOCÊ DESEJA CONTINUAR COM O PROGRAMA? (s/n)')
    # Caso o usuário deseja continuar, faço a chamada do PIVOTAMENTO
    if entrada_User == 's':
        print('================================================')
        print('                  PIVOTAMENTO                    ')
        print('================================================\n')
        # Chamada do Método do pivotamento 
        x = pvt.pivotamento_gaussiano(Mat)
        
        print('\n')
        # Print da solução do pivotamento
        print('========== EXISTE SOLUÇÃO ============')
        print("\n SOLUÇÃO: ")
        n = len(x)
        for i in range (n):
            print("x{i} = {valor}".format(i = i, valor = x[i]))
        
        print('================================================')
        print('                 MÉTODO DE JACOBI                   ')
        print('================================================\n')

        x = jacobi(Mat,b = b,x0 =x0,tol=tol,iteracoes=iteracoes)
        print('SOLUÇÃO APROXIMADA ENCONTRADA')
        print('X = ' ,x)
    # Caso o usuário não desejar continuar no programa 
    # o programa é encerrado
    elif entrada_User == 'n':
        break