from os import system
import os

comando = "netsh wlan show profiles"

resultado = os.popen(comando)
datos = resultado.readlines()
datos.pop()

per = False

for e in range(0, len(datos)):
    datos[e] = datos[e].strip()

listuser = []

for e in datos:
    if(e == "User profiles" or e == "Perfiles de usuario"):
        per = True

    if(per == True):
        listuser.append(e)

listuser.pop(0)
listuser.pop(0)

for e in range(0, len(listuser)):
    listuser[e] = listuser[e].replace(
        "Perfil de todos los usuarios     : ", "")

listusercomand = []

for e in listuser:
    comando2 = 'netsh wlan show profile name="' + e + '" key=clear'
    listusercomand.append(comando2)


def comandpassword(e):
    comando3 = listusercomand[e]
    resultado3 = os.popen(comando3)
    datos3 = resultado3.readlines()

    for e in range(0, len(datos3)):
        datos3[e] = datos3[e].strip()

    password = ""

    for e in datos3:
        if (("clave" in e) or ("password" in e)):
            password = e
            have = True
            break

    password = password.replace("Contenido de la clave  : ", "")

    return password


listuserpassword = {}

for e in range(0, len(listuser)):
    listuserpassword[listuser[e]] = (comandpassword(e))

for clave, valor in listuserpassword.items():
  print(clave,"→",valor)
