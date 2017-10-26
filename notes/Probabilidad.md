# Básicos de Probabilidad
> Uriel Ramírez  
> 23 PlatziRank

Muchos de los resultados que vamos a interpretar en nuestro día a día como Data Scientist tienen que ver con reglas de probabilidad y estadística. Repasemos algunos conceptos básicos para entender mejor nuestros ejemplos: 


## Probabilidad 

La probabilidad es la forma en la que medimos que un evento suceda y siempre será un numero que se encuentre entre 0 y 1, aunque también puede representarse cómo porcentaje.

De manera de representación, la probabilidad tiene una notación muy particular: 

```
P( nombre del evento ) = 0.4.  
```
 

Lo cuál se lee como: La probabilidad del nombre del evento suceda es igual a  0.4 

 

Un ejemplo sería cuando lanzas una moneda, solo podemos tener 2 resultados: 

``` 
Sale cara o sale cruz, por lo tanto tenemos un 50% de probabilidad que salga una u otra opción. 
```
 

Algo importante que destacar aquí es que la suma de todos los eventos posibles debe ser siempre 1.0.

```
P(Cara) + P (Cruz) = 1 
```
 

Pero, ¿Cómo obtenemos la probabilidad de un evento si no la conocemos

 

La probabilidad de ese evento es igual a la población parcial de ese evento entre el numero total de toda la población, dicho de otro modo: 

 
```
P(E) = (Población de ese evento ) / Población total 
```
 

Propongamos un ejemplo

 

* En una baraja de cartas, quiero calcular la probabilidad de obtener un “ace”. Si recordamos, en toda la baraja, tenemos 4 aces, y esta compuesta por 52 cartas en total, entonces la probabilidad de obtener un Ace es de: 

 
```
P(Ace) = 4/52 = 0.077
```
 

## Probabilidad condicional

 
Cuando queremos predecir un nuevo evento dado otro que ya sucedió usamos algo llamado probabilidad condicional, y su naturaleza de predecir el futuro justo es la base de Machine Learning y de ahí la importancia de conocerla.

 

Por definición, la probabilidad de que un evento suceda dado otro es: 

 
```
P( E | F ) =  P(E∩F) / P(F) 
```
 

donde: 


* E es el evento del cuál nos interesa calcular su probabilidad 

* F es el evento que ya sucedió

* P(E∩F) Es la probabilidad donde co-existen el evento E y F 

 

Veamos esto reflejado esto con nuestro ejemplo anterior: 

 
* Ahora quiero calcular la probabilidad de que el ace de la baraja sea de color rojo. 

 
Bien, si recordamos,  solo 2 de los ace que podremos obtener en toda la baraja son rojos, por lo tanto:

 
```
P(E∩F) = 2 / 52 = 0.038
```
 

Y recordando que la probabilidad de obtener un ace cualquiera es de : 

 
```
P(Ace) = 4/52 = 0.077
```
 

Entonces, la probabilidad de que cuando salga un Ace, este sea de color rojo es de: 

 
```
P( E | F ) =   (2 / 52)  / ( 4/52 ) = 0.5
```
 
La probabilidad nos permite tener una clasificación de la información que estamos analizando y tal como hemos aprendido: es parte del ciclo de trabajo de un Data Scientist.

 

Dominar la probabilidad tambien requiere de más práctica, encontré unos ejercicios interesantes donde puedas poner todo en práctica: 

 
http://www.vitutor.com/pro/2/a_g.html
