# Algebra Lineal para Data Science
### Curso de Big Data y Ciencia de Datos
> Uriel Ramírez   
>23 PlatziRank


 
Data Science es un campo donde convergen muchas ciencias y disciplinas. Una de las más importantes sin duda es el álgebra lineal, la cuál usamos para resolver todas aquellas ecuaciones que utilizamos para nuestros modelos de Machine Learning. Entonces, haremos un repaso por los conceptos más importantes a los que se enfrenta un Data Scientist. 

 

## Valores escalares

 

Un valor escalar es un valor contenido en cualquier espacio. En programación, esto es equivalente a guardar el valor de una variable. 

 
```
x = 5; 
```

> Quiere decir que el valor escalar de X es igual a 5. 

 
## Vector 

Un vector es un arreglo / conjunto de números escalares, por ejemplo: 

 
Siendo X un vector: 

 
```
X = [X1, X2, X3 ];
```
 

> Los valores X1, X2, X3 son precisamente valores escalares. 

 

El numero de elementos que contiene el vector se llama orden o longitud. Además, ese orden representa el numero de puntos que tiene nuestro vector en el espacio.

 

 

## Matrices

 

Una matriz es un conjunto de vectores que forman su orden o longitud de acuerdo al numero de  filas y de columnas resultantes. Por ejemplo: 

 

> Siendo un vector X, Y Z, con valores [X1, X2, X3], [Y1, Y2, Y3] y  [Z1, Z2, Z3] respectivamente: 

 
```
       [X1, X2, X3],

M =    [Y1, Y2, Y3],

       [Z1, Z2, Z3],
```
 

 

M es la matriz que se forma al unir esos 3 vectores. El numero de filas y de columnas define su orden, en este caso la Matriz M es de orden 3x3. 

 

 

## Producto punto o escalar de vectores 
 
En Machine Learning, usamos mucho el producto punto o escalar. Y se trata de la suma de los productos de cada valor escalar que contiene el vector. Tengamos más claro esto con un ejemplo:

```
X = [4, 10, 12]

Y = [ 10, 0, 21]
```
 

El producto escalar es = ```(4*10)+(10*0)+(12*21) = (40) + (0) + (252) =  292```

 

## Resolviendo sistema de ecuaciones lineales 

Hablando puntualmente de álgebra lineal, el interés esta siempre en resolver sistema de ecuaciones de la forma: 

```
Ax = b
```
 

Donde: 

* A es una matriz o conjunto de vectores de entrada. 

* x es la representación de los resultados que queremos encontrar 

* b es un vector del mismo orden que el sistema de ecuaciones, en ingles conocido como “label"


Un ejemplo de cómo veríamos esto: 

 
```
[ 10 , 2 , 31 ][x1]=[1]

[ 12 , 32, 21][x2]=[3]

[ 92 , 21, 92 ][x3]=[4]
```                                    

> Y el reto es justo encontrar los valores de x1, x2, x3.

 

Para Data Science, y por la naturaleza de computar estos datos usaremos algo llamado Método Iterativo. En Machine Learning, contemos con algunos ya establecidos cómo: “Stochastic Gradient Descent”, “Conjugate Gradient Methods” y “Alternating Least Squares”. 