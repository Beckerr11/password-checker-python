import re

print("Verificador de força de senha")

senha = input("Digite uma senha: ")

forca = 0

if len(senha) >= 8:
    forca += 1

if re.search("[A-Z]", senha):
    forca += 1

if re.search("[0-9]", senha):
    forca += 1

if re.search("[!@#$%^&*()]", senha):
    forca += 1


if forca <= 1:
    print("Senha fraca")

elif forca == 2 or forca == 3:
    print("Senha média")

else:
    print("Senha forte")