def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido 

usuario = leer_archivo('usuario.txt')
contraseña = leer_archivo('claves.txt')


contador=1

def menu():
     print("* MENU PRINCIPAL *")
     print("1. Listar")
     print("2. Agregar")
     print("3. Salir")

def listar():
   archivo = open("nombre.txt","rt",encoding='utf8')
   print(archivo.read())
    

def agregar():
    print("* AGREGAR CONTENIDO A UN ARCHIVO *")
    archivoa = open("nombre.txt","at")
    nombre = input("introduce nombre de producto: ")
    archivoa.write("\n" + nombre)
    archivob = open("codigo.txt","at")
    codigo = input("introduce codigo de producto: ")
    archivob.write("\n" + codigo)
    archivoc = open("precio.txt","at")
    precio = input("introduce precio de producto: ")
    archivoc.write("\n" + precio)

def salir():
    print("Gracias... Vuelva pronto")  

def error():
    print("Opción incorrecta")
    

def validar():
    dato1 = input('ingrese usuario: ')
    dato2 = input('ingrese la clave: ')
    if usuario == dato1 and contraseña == dato2:
             return menu()
               
    else:
         while contador < 3:
            print("vuelva a ingresar los datos")
            contador == contador+1
            return validar()
validar()

opcion = 1
while opcion!=3:
    menu()
    opcion = int(input("Seleccione una opción [1-3]: "))
    if opcion ==1:
        listar()
    elif opcion == 2:
        agregar()
    elif opcion == 3:
        salir()
    else:
        error()