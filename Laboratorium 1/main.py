import numpy as np
from numpy.lib.function_base import append
import math

def cylinder_area(r:float,h:float):
    if(r < 0 or h < 0):
        return None
    return(math.pi * r**2 * h)

def fib(n:int):

    if (n <= 0 or type(n) is not int):
        return None
    output_array = np.array([1])
    if (n == 1):
        return output_array
    for i in range(n-1):
        if i == 0:
            output_array = np.append(output_array,[1])
        else:
            output_array = np.append(output_array,output_array[i] + output_array[i-1])
    return output_array

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([a,1,-a],[0,1,1],[-a,a,1])
    Minv = np.linalg.inv(M)
    Mt = np.transpose(M)
    Mdet = np.linalg.det(M)

    return M,Minv,Mt,Mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    result_matrix  = np.zeros((m,n))
    if(m < 0 or n < 0):
        return None
    for i in range(m):
        for j in range(n):
            if i > j:
                result_matrix[i,j] = i
            else:
                result_matrix[i,j] = j
    return result_matrix