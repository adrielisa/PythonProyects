"""
Remueve los caracteres a la izquierda de nuestro texto principal:

,

:

%

_

#

Utiliza el método lstrip(). Imprime el resultado en pantalla:

",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

"""

string = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

string = string.lstrip(',:%_#')
print(string)