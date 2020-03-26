import re

#primer caracter debe ser mayuscula
#los siguientes caracteres deben ser numeros
#los siguientes deben ser caracteres letras minisculas
#los ultimos tres caracteres deben ser caracteres especiales
cadena = input('')
if re.match('^[A-Z]|[0-9]{3}|[a-z]{3}|[^a-zA-Z0-9]{3}', cadena):
    print("Contrasena valida")
else:
    print("contrasena no valida")