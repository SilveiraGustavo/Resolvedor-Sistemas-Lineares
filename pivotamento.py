import numpy as np

def ler_matriz(n):
    M = [] # Criando uma matriz
    
    print("INFORME A MATRIZ ESTENDIDA (LINHA POR LINHA).")
    
    for i in range(n):
        linha = input("Linha {}:".format(i + 1))
        linha_num = linha.split(',')
        linha_num = [float(i) for i in linha_num]
        
        M.append(linha_num)
   
    
    M = np.array(M, dtype = 'double')
    
    return M    #Retorna a matriz já formada


#Função que escolhe qual linha será o pivô
def linha_pivo(M, linha, coluna):
    maior = abs(M[linha, coluna])  #O primeiro elemento é o maior valor
    linha_pivo = linha  #Linha pivô como a linha do primeiro elemento
    n = len(M)     #n é o número de linha da matriz
    
    for i in range(linha, n):   #Percorre-se a coluna a partir da linha
        if abs(M[i, coluna]) > maior:   #Se o elemento da linha atual for maior do que maior
            maior = abs(M[i, coluna])
            linha_pivo = i  #Atualiza-se o pivô 
        
   
    
    return linha_pivo   #Retorna a linha pivô


#Função que troca as linhas 1 e 2 de lugar
def trocar_linha(M, l1, l2):
    if l1 != l2:    #Testa se as linhas são diferentes
        print("Troca de linhas:", l1, "<->", l2)
        
        aux = np.copy(M[l1, :])
        M[l1, :] = np.copy(M[l2, :])
        M[l2, :] = aux
        
        print(M)


#Função que resolve a diagonal superior digitada pelo usuário
def resolver_diagonal_superior(M):
    n = len(M)  #n é o número de linhas da matriz
    b = np.copy(M[:, n])    #b é o vetor de termos constantes
    x = np.arange(n, dtype = 'double')  #Cria um vetor x para guardar a solução (diagonal superior da matriz)
    
    #Última linha isolada
    x[n - 1] = b[n - 1] / M[n - 1, n - 1]   #x_n = b_n / m_n,n
    
    for i in range(n - 2, -1, -1):  #Percorre as linhas em ordem decrescente e ignorando a última
        soma = 0
        
        for j in range(i + 1, n):   #Soma as incógnitas já resolvidas (depois da diagonal)
            soma += x[j] * M[i, j]  
        
        
        x[i] = (b[i] - soma) / M[i, i]  #x_i = (b_i - (soma das incógnitas)) / m_i,i
  
    
    return x    #Retorna a solução da matriz (em formato de diagonal superior)


#Função que faz o pivotamento na matriz
def pivotamento_gaussiano(M):
    n = len(M)  #n é o número de linhas da matriz m
    
    for col in range(n - 1):  #Percorre as colunas da matriz m
        print("\nColuna", col + 1)
        linha = linha_pivo(M, col, col)
        
        trocar_linha(M, linha, col)
        
        pivo = M[col, col]  #Definindo um pivô
        
        for l in range(col + 1, n):   #Percorre as linhas da matriz m
            print("L{l} <- L{l} - L{c} * ".format(l = l + 1, c = col + 1) + "{b} / {p}".format(b = M[l, col], p = pivo))
            
            M[l, :] = M[l, :] - M[col, :] * M[l, col] / pivo    #L_col = L_lin - L_col * (matriz_lin,col) / pivo
            
            print(M)
   
    
    return resolver_diagonal_superior(M)