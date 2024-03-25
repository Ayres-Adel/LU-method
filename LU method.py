import numpy as np

def lu_factorization(matrix):
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

    for j in range(n):
        for i in range(j + 1):
            sum1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = matrix[i][j] - sum1

        for i in range(j, n):
            sum2 = sum(L[i][k] * U[k][j] for k in range(j))
            if U[j][j] == 0:
                print("Error: Division by zero. Please check the input matrix.")
                return None, None  
            L[i][j] = (matrix[i][j] - sum2) / U[j][j]

    return L, U                                         
def determinant(matrix):
    det=np.linalg.det(matrix)                                               
    return det
def resolution_equation(matrix, b):  
    x = np.linalg.solve(matrix, b)   
    return x                         
n = int(input("Entrez le nombre de lignes de la matrice : ")) 
matrix = np.zeros((n, n))
for i in range(n):
      for j in range(n):
         matrix[i][j] = float(input(f"Entrez l'élément ({i+1},{j+1}) de la matrice : "))  
det = determinant(matrix)       
L, U = lu_factorization(matrix)    
if det != 0:          
    print("Le déterminant de la matrice est différent de zéro.")
    print("Factorisation LU :")
    print("Matrice L :")
    print(L)     
    print("Matrice U :")
    print(U) 
    b = np.array(list(map(float, input("Entrez les éléments du vecteur b : ").split()))) 
    x = resolution_equation(matrix, b)    
    print("La solution de l'équation ax=b est :", x) 
else:
    print("Le déterminant de la matrice est égal à zéro. imposible de calcule la factorisation de lu")
