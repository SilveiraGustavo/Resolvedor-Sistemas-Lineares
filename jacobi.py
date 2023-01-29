
import numpy as np

def jacobi(M,b,x0,tol,iteracoes):
    n = len(M)
    x = np.zeros(n, dtype='double')
    xant =  x0
    for k in range(iteracoes):

        for i in range(n):
            x[i] = b[i]

            for j in range(i):
                x[i] -= M[i,j]*xant[j]

            for j in range(i + 1, n):
                x[i] -= M[i,j]* xant[j]

            x[i] /= M[i,i]
        erro = np.linalg.norm( x - xant, np.inf)
        print("Iteração {k:3d}: ".format(k=k+1) +
              "x={x}, ".format(x=np.round(x,8)) +
              "Erro={e:+5.8f}".format(e=erro))
        
        if (erro < tol):
            return x
        xant = np.copy(x)
 