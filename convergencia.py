import numpy as np


# Teste de convergencia 
def espectral(dec, aux, aux2, b):
    #Calculando o raio espectral do método de Jacobi
    raio_espec = -np.linalg.inv(dec).dot(aux + aux2)  
    av1, _ = np.linalg.eig(raio_espec)     
    raio_espectralJ = max(abs(av1))
    print("\nRAIO ESPECTRAL DO MÉTODO DE JACOBI.", raio_espectralJ)

    if (raio_espectralJ <= 1):
        print(" O MÉTODO CONVERGE.")
    
    else:
        print("O MÉTODO NÃO CONVERGE.")
