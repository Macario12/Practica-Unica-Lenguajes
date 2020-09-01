from graphviz import Digraph
from curso import *
cursos = []
def lecturaArchivo():

    print("Ingresar ruta del archivo.")

    ruta = input()
    verifarruta = ruta.split(".")

    if(verifarruta[1]!="csv"):
        print("Ingresar un archivo .csv")
        lecturaArchivo()
    else:
        archivo = open(ruta, "r")
        tamaño = 0
        for line in archivo.readlines():
            tamaño +=1
            datos=line.split(",", maxsplit=6)
            for x in cursos:
                if int(datos[0]) == x.getCodigo():
                    cursos.remove(x)

            informacion = Curso(int(datos[0]),datos[1],datos[2],int(datos[3]),int(datos[4]),int(datos[5]),int(datos[6]))
            cursos.append(informacion)
        archivo.close()
        print("Archivo cargado Correctamente.")    

def mostrarCursos():
    for x in cursos:
        print(str(x.getCodigo())+","+x.getNombre()+","+x.getPresequisito()+","+str(x.getOpcionalidad())+","+str(x.getSemestre())+","+str(x.getCreditos())+","+str(x.getEstado()))

def BuscarCurso():
    codigo = int(input("Ingresar codigo de curso: "))
    validando = False
    for x in cursos:
        if codigo == int(x.getCodigo()):
            
            validando = True
            print("")
            print("Codigo: "+ str(x.getCodigo()))
            print("Nombre Curso: "+ x.getNombre())
            print("Prerrequisitos: "+ x.getPresequisito())
            print("Opcionalidad: "+ str(x.getOpcionalidad()))
            print("Semestre: "+ str(x.getSemestre()))
            print("Creditos: "+ str(x.getCreditos()))
            print("Estado: "+ str(x.getEstado()))
        
    if validando is False:
        print("El curso no existe")
        desicion = input("Desea buscar curso (si/no): ")
        if(desicion == "si"):
            BuscarCurso()    
        else:
            print("ah weno")

def agregarCurso():
    print("Ingresar los datos a continuación")
    codigoCurso = int(input("Curso: "))
    nombreCurso = input("Nombre: ")
    PresequisitoCurso = input("Prerrequisito: ")
    OpcionalidadCurso = int(input("Opcionalidad (1/0): "))

    while (OpcionalidadCurso >1 or OpcionalidadCurso<0):
        print("Ingresar un Opcionalidad valida")
        OpcionalidadCurso = int(input("Opcionalidad (1/0): "))

    SemestreCurso = int(input("Semestre: "))
    CreditosCursos = int(input("Créditos: "))
    EstadoCurso =  int(input("Estado: "))

    while (EstadoCurso >1 or EstadoCurso<-1):
        print("Ingresar una Estado valido (1,0,-1)")
        EstadoCurso = int(input("Estado: "))

    for x in cursos:
        if codigoCurso == x.getCodigo():
            cursos.remove(x)


    informacion = Curso(int(codigoCurso),nombreCurso,PresequisitoCurso,int(OpcionalidadCurso),int(SemestreCurso),int(CreditosCursos),int(EstadoCurso))

    cursos.append(informacion)

def eliminarcurso(codigo):
    validando = False
    for x in cursos:
        if(codigo == int(x.getCodigo())):
            validando = True
            cursos.remove(x)
            print("Curso Eliminado")

    if validando is False:
        print("El curso no existe")

def actualizarCurso():
        print("Actualizando Curso")
        codigo = int(input("Codigo Curso: "))
        validando = False
        for x in cursos:
            if codigo == int(x.getCodigo()):
            
                validando = True
                print("")
                print("1. Codigo: "+ str(x.getCodigo()))
                print("2. Nombre Curso: "+ x.getNombre())
                print("3. Prerrequisitos: "+ x.getPresequisito())
                
                print("4. Opcionalidad: "+ str(x.getOpcionalidad()))
                print("5. Semestre: "+ str(x.getSemestre()))
                print("6.Creditos: "+ str(x.getCreditos()))
                print("7. Estado: "+ str(x.getEstado()))

                eleccion = int(input("Seleccione dato a editar: "))
                datoedit = input("Dato a editar: ")

                if eleccion is 1:
                    x.setCodigo(datoedit)
                elif eleccion is 2:
                    x.setNombre(datoedit)
                elif eleccion is 3:
                    x.setPresequisito(datoedit)
                elif eleccion is 4:
                    x.setOpcionalidad(datoedit)
                elif eleccion is 5:
                    x.setSemestre(datoedit)
                elif eleccion is 6:
                    x.setCreditos(datoedit)
                elif eleccion is 7:
                    x.setEstado(datoedit)
                else:
                    print("ingresar una ocpion valida")   

        if validando is False:
            print("El curso no existe")
            desicion = input("Desea editar curso (si/no): ")
            if(desicion == "si"):
                actualizarCurso()    
            else:
                print("ah weno")
            

def creditosAprobados():
    cursosAprobados = 0
    
    for x in cursos:
        if int(x.getEstado()) == 0:
            cursosAprobados += int(x.getCreditos())

    print("La cantidad de creditos Aprobados son: "+str(cursosAprobados)+" Creditos.")

def creditosCursando():
    cursosCursando = 0
    
    for x in cursos:
        if int(x.getEstado()) == 1:
            cursosCursando += int(x.getCreditos())

    print("La cantidad de creditos Cursando son: "+str(cursosCursando)+" Creditos.")

def creditosPendientes():

    cursosPendientes = 0

    for x in cursos:
        if int(x.getEstado()) == -1 and int(x.getOpcionalidad()) == 1:
            cursosPendientes += int(x.getCreditos())

    print("La cantidad de creditos Pendientes son: " + str(cursosPendientes)+" Creditos.")        

def creditosSemestreN():

    creditosSemestre = 0
    print("Creditos Semestres")
    semestre = int(input("Ingresar el semestre deseado: "))

    for x in cursos:
        if(int(x.getSemestre())<=semestre and int(x.getOpcionalidad())==1):
            creditosSemestre += int(x.getCreditos())

    print("La cantidad de creditos desde el Semestre 1 Hasta el semestre "+str(semestre)+" es " + str(creditosSemestre)+" Creditos.") 

def creditosSemestreEspecifico():
    validando = False
    creditoSemstreEspeAprobados = 0
    creditosSemestreEspePendientes = 0
    print("Creditos Semestre")
    semestre = int(input("Ingresar el semestre deseado: "))

    for x in cursos:
        if(int(x.getSemestre())==semestre and int(x.getEstado())==0):
            creditoSemstreEspeAprobados += int(x.getCreditos())  
            validando = True
        if(int(x.getSemestre())==semestre and int(x.getEstado())==-1):
            creditosSemestreEspePendientes += int(x.getCreditos()) 
            validando = True
    
    if(validando is True):

        print("La cantidad de creditos Aprobados del semestre"+str(semestre)+" es " + str(creditoSemstreEspeAprobados)+" Creditos.")
        print("La cantidad de creditos Pendiente del semestre"+str(semestre)+" es " + str(creditosSemestreEspePendientes)+" Creditos.") 
    else:
        print("El semestre no existe")
        creditosSemestreEspecifico()     

def Mapa():
    g = Digraph('filled', filename='Malla.gv', node_attr={'shape': 'record'})
    g.attr(rankdir='LR')
    with g.subgraph(name='malla') as c:

    
        for x in cursos:
            if x.getEstado() == 0:
                g.node(str(x.getCodigo())+" || "+str(x.getNombre()),color='cadetblue')
            if x.getEstado() == 1:
                g.node(str(x.getCodigo())+" || "+str(x.getNombre()),color='green')
            if x.getEstado() == -1:
                g.node(str(x.getCodigo())+" || "+str(x.getNombre()),color='darkslategray')
            
            
            for y in cursos:
                
                presequisitos = y.getPresequisito().split(";")
                for z in presequisitos:
                    if z == '':
                        z = 0
                    if(int(z) == int(x.getCodigo())):
                        print(y.getNombre())
                        
                        g.edge(str(x.getCodigo())+" || "+str(x.getNombre()),str(y.getCodigo())+" || "+str(y.getNombre()),fillcolor='red')
                        

    g.view()