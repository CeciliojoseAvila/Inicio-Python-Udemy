balance = 500
if balance >0:
    print("PUEDES PAGAR")
else:
    print("No tienes saldo")

# LIKES
likes = 200
if likes == 200:
    print("EXCELENTE, TIENES 200 LIKES")

    # VERIFICAR LISTA
lenguajes = ["python", "Kotlin", "Java", "JavaScript","PHP"]

if "PHP" in lenguajes:
    print("PHP, SI EXISTE")
else:
    print("PHP, NO EXISTE")

# IF ANIDADOS
usuario_autenticado = False
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("ACCESO AL SISTEMA")
else:
    print("DEBES INICIAR SESION ")
