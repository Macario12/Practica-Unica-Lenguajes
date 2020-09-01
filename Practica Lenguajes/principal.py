import uploadFile

pantalla_principal = """
        Pantalla Principal
Lenguajes formales y de programación
Sección: B
Carné: 201905837
"""
print(pantalla_principal)
enter = input("Presione enter para continuar.")


def GestionarCursos():
    menu = """
        Gestionar Cursos.
1. Listar Cursos.
2. Mostrar Curso.
3. Agregar Curso.
4. Editar curso.
5. Eliminar Curso.
6. Regresar a menu principal.
"""

    print(menu)

    opcion = int(input("Seleccionar una opción: "))

    if opcion == 1:
        print("Listar Cursos.")
        uploadFile.mostrarCursos()
        GestionarCursos()
    elif opcion == 2:
        uploadFile.BuscarCurso()
        GestionarCursos()
    elif opcion == 3:
        uploadFile.agregarCurso()
        GestionarCursos()
    elif opcion == 4:
        uploadFile.actualizarCurso()
        GestionarCursos()
    elif opcion == 5:
        print("Eliminar Curso")
        codigo = int(input("ingresar codigo de curso a eliminar: "))
        uploadFile.eliminarcurso(codigo)
        GestionarCursos()
    elif opcion == 6:
        menu_principal()
    else:
        print("seleccione una opción corriente.")
        GestionarCursos()

def conteoCreditos():
    menu = """
        Conteo De Creditos.
1. Conteo de creditos de cursos aprobados.
2. Conteo de creditos cursando.
3. Conteo de creditos pendientes.
4. Conteo de creditos obligatorios hasta semestre n.
5. Creditos de semestre.
6. Regresar a Menu Principal
"""

    print(menu)

    opcion = int(input("Seleccionar una opción: "))

    if opcion == 1:
       uploadFile.creditosAprobados()
       conteoCreditos()
    elif opcion == 2:
        uploadFile.creditosCursando()
        conteoCreditos()
    elif opcion == 3:
        uploadFile.creditosPendientes()
        conteoCreditos()
    elif opcion == 4:
        uploadFile.creditosSemestreN()
        conteoCreditos()
    elif opcion == 5:
        uploadFile.creditosSemestreEspecifico()
        conteoCreditos()
    elif opcion == 6:
        menu_principal()
    else:
        print("seleccione una opción corriente.")
        conteoCreditos() 

def menu_principal():
    menu = """
        Menu Principal.
1. Cargar Archivo de entrada.
2. Gestionar Cursos.
3. Conteo de Créditos.
4. Mapa de Cursos.
"""

    print(menu)

    opcion = int(input("Seleccionar una opción: "))

    if opcion == 1:
        print("Cargar Archivo de entrada.")
        uploadFile.lecturaArchivo()
        menu_principal()
    elif opcion == 2:
        GestionarCursos()
    elif opcion == 3:
        conteoCreditos()
    elif opcion == 4:
        uploadFile.Mapa()
        menu_principal()
    else:
        print("seleccione una opción corriente.")
        menu_principal()                
 
menu_principal()       

  