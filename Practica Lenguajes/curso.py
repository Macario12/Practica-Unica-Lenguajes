class Curso:
    Codigo = 0
    Nombre = ""
    Presequisito = 0
    Opcionalidad = True
    Semestre = 0
    Creditos = 0
    Estado = 0

    def __init__(self,Codigo,Nombre,Presequisito,Opcionalidad,Semestre,Creditos,Estado):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Presequisito = Presequisito
        self.Opcionalidad = Opcionalidad
        self.Semestre = Semestre
        self.Creditos = Creditos
        self.Estado = Estado

    def getCodigo(self):
        return self.Codigo
    def getNombre(self):
        return self.Nombre    
    def getPresequisito(self):
        return self.Presequisito
    def getOpcionalidad(self):
        return self.Opcionalidad    
    def getSemestre(self):
        return self.Semestre
    def getCreditos(self):
        return self.Creditos
    def getEstado(self):
        return self.Estado

    def setCodigo(self,nuevoCodigo):
        self.Codigo=nuevoCodigo
        
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    def setPresequisito(self, Presequisito):
        self.Presequisito = Presequisito
    def setOpcionalidad(self, Opcionalidad):
        self.Opcionalidad = Opcionalidad
    def setSemestre(self, Semestre):
        self.Semestre = Semestre
    def setCreditos(self, Creditos):
        self.Creditos = Creditos
    def setEstado(self, Estado):
        self.Estado = Estado
  

   