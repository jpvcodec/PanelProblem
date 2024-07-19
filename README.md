# ¿Cuántos paneles caben?

El repositorio tiene por objetivo proponer una solución para encontrar la cantidad de paneles que caben dentro de una superficie plana.

## Instalación del proyecto

#### Requisitos Previos

Las soluciones fueron desarrolladas en [Python](https://docs.python.org/3/) versión 3.11.0, por lo que dicha tecnología debe estar instalada previamente en el ambiente en donde se vayan a ejecutar.

#### Clonar el repositorio

```
git clone https://github.com/jpvcodec/PanelProblem.git
```

## Probar las soluciones

### Superficie Rectangular

Utilizando el Makefile

```
make rectangle
```

Alternativamente, ejecutando directamente la solución con python

```
python solutions/rectangle.py
```

Una vez iniciado el programa, ingresar por consola el ancho y alto de la superficie, seguido del ancho y alto de la baldosa. Se imprimirá por pantalla el resultado.

Para cerrar el programa, ingresar un 0 luego de finalizar el cálculo de baldosas.

### Superficie Triangular

Utilizando el Makefile

```
make triangle
```

Alternativamente, ejecutando directamente la solución con python

```
python solutions/triangle.py
```

Una vez iniciado el programa, ingresar por consola la altura y base de la superficie triangular, seguido del ancho y alto de la baldosa. Se imprimirá por pantalla el resultado.

Para cerrar el programa, ingresar un 0 luego de finalizar el cálculo de baldosas.
