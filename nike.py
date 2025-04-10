datos = {
    "producto": "Zapatillas Nike Air",
    "talla": 7,
    "color": "Rojo",
    "stock": 15
    }

def editar_key():
    key = input("Ingrese la key para realizar algún cambio en los datos:")
    
    if key == "p":
        nuevo_producto = input("Ingrese el nuevo producto:")
        datos["producto"] = nuevo_producto
        print(datos)
    elif key == "t":
        nueva_talla = input("Ingresa la nueva talla:")
        datos["talla"] = nueva_talla
        print(datos)
    elif key == "c":
        nuevo_color = input("Ingrese el nuevo color:")
        datos["color"] = nuevo_color
        print(datos)
    elif key == "s":
        nuevo_stock = input("Ingrese la nueva cantidad:")
        datos["stock"] = nuevo_stock
        print(datos)
    else:
        print("key no válida, ingrese una correcta")
        
def eliminar_key():
     key = input("Ingrese la key que desea eliminar:")
     
     if key == "ep":
        del datos["producto"] 
        print(datos)
     elif key == "et":
        del datos["talla"]
        print(datos)
     elif key == "ec":
        del datos["color"]
        print(datos)
     elif key == "es":
        del datos["stock"]
        print(datos)
     else:
        print("key no válida, ingrese una correcta")
                
def menu():
    while True:
        print("Menú Interactivo") 
        print("1-Eliminar")
        print("2-Editar")
        print("3-Salir")     
        opcion = input("Por favor seleccione una opción:")
        print ("Programa Beta para la marca Nike")
        print ("Menú de keys")
        print ("p = producto: ")
        print ("t = talla: ")        
        print ("c = color: ")
        print ("s = stock: ")
        print ("e = eliminar:")
        if opcion == "1":
            eliminar_key()
        elif opcion == "2":
            editar_key()
        elif opcion == "3":
            print("Haz decidido salir, ¡adiós!...pero regresa pronto.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo")
    
menu()