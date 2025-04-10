lista_de_nombres = ["Gogo Yubari", "O-Ren Ishii", "Hattori Hanzo", "Crazy 88", "Boss Tanaka"]

def mostrar_menu():
    print ("Menú Interactivo")
    print ("M = Mensaje: ")
    print ("L = Lista de nombres: ")        
    print ("X = Salir")
    
def mostrar_mensaje():
            print ("Mensaje: Tu sistema respira aguantará")

while True:
    mostrar_menu()
    Opcion = input("Por favor seleccione una opción")

    if Opcion == "M":
        print ("Tu sistema respiratorio aguantará")
    elif Opcion == "L":
        print ("Lista de nombres:")
        for nombre in lista_de_nombres:
            print (f"Nombre -> {nombre}")
    elif Opcion == "X":
        print ("Haz decidido salir, ¡adiós!...pero regresa pronto.")
        break
    else:
        print ("Opción no válida, por favor intente de nuevo")
        
    
