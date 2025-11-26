"""
NumPy & SciPy = vorkompilierte Funktionen für mathematische und numerische Routinen
Alternative zu MATLAB

NumPy dient zur Bearbeitung von großen Arrays und Matrizen mit numerischen Daten
SciPy erweitert NumPy mit z.B. Funktionen wie Minimierung, Regression, Fourier-Transformation...

Standardmäßig sind beide libs nicht installiert.
Man sollte zuerts NumPy installieren:

In der Powershell:
pip install numpy

oder Download:
https://www.anaconda.com/products/individual

"""
import numpy as np

x = np.arange(1,10)
print(x) # [1 2 3 4 5 6 7 8 9] ndarray (spezieller numpy array)

# Arrays sind der zentrale Bestandteil von numpy, welche alle vom gleichen Typ sein müssen (int oder float)
# Arrays sind effizienter als Listen in Python

# Erzeugung eines Arrays aus einer Liste
arr1 = np.array([1,2,3], int)
print(arr1) # [1 2 3]

# Erzeugung 2 dimensionales Array aus Tupeln
arr2 = np.array(((11,12,13), (21,22,23), (31,32,33)))
print(arr2)
#[[11 12 13]
# [21 22 23]
# [31 32 33]]

# ndim = Auskunft über Anzahl der Dimensionen
print(arr2.ndim) # 2

# shape liefert ein Tupel mit den Array Dimensionen (Zeilen, Spalten - Anzahl)
print(arr2.shape) # (3, 3)

# ermitteln des Array Typs
print(arr2.dtype) # int32

# Arrays konkatenieren
arr3 = np.array([11,22])
arr4 = np.array([1, 2])

# default Achse (axis=0)
print(np.concatenate((arr3, arr4))) # [11 22  1  2]

# Bsp. mehrdimensiale Arrays konkateneieren
arr5 = np.array(((11,22, 33), (44,55,66)))
arr6 = np.array(((1, 2),(3,4)))

print(np.concatenate((arr5, arr6),axis = 1)) # axis gibt Dimension an, bei welcher Dim verknüpft werden soll
#[[11 22 33  1  2]
# [44 55 66  3  4]]


# Array neue Dimension hinzufügen
arr7 = np.array([2,5,8,19,4])
arr8 = arr7[:, np.newaxis]
print(arr8)
#[[ 2]
# [ 5]
# [ 8]
# [19]
# [ 4]]


# Arrays mit Nullen (np.zeros) und Einsen (np.ones) initialiseren
arr9 = np.ones((2,3)) # float ist standard
print(arr9)
#[[1. 1. 1.]
# [1. 1. 1.]]

arr10 = np.ones((2,3), dtype=int) # mit int initialiseren

"""
Matrizenarithmetik
"""
# + - * / ** % Standardoperationen
mat1 = np.array([1,2,3])
mat2 = np.array([4,5,6])
print(mat1 + mat2) # [5 7 9]
print(mat1 - mat2) # [-3 -3 -3]
print(mat1 / mat2) # [0.25 0.4  0.5 ]
print(mat1 * mat2) # [ 4 10 18]
print(mat1 % mat2) # [1 2 3]

# Vektoraddition
vec1 = np.array([3,2])
vec2 = np.array([5,1])
print(vec1 + vec2) # [8 3]

# Matrix-Klasse
# ist eine Unterklasse von ndarray, wobei nur zweidimensional ist
m1 = np.matrix( ((2,3), (3,5)) )
m2 = np.matrix( ((1,2), (5,-1)) )
print(m1 * m2)
#[[ 17  1]
# [28 1]]

# Kreuzprodukt
k1 = np.array([0,0,1])
k2 = np.array([0,1,0])
print(np.cross(k1, k2)) # [-1  0  0]

# Lineare Gleichungssysteme, Polynome in pdf 32
