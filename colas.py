class Consulta:
    def __init__(self, nombre, correo, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.mensaje = mensaje

    def __str__(self):
        return f"Consulta{{nombre={self.nombre}, correo={self.correo}, mensaje={self.mensaje}}}"


class GestorConsultas:
    def __init__(self):
        self.cola = []

    def nuevaConsulta(self, c):
        self.cola.append(c)

    def atenderConsultas(self):
        print(str(self.cola[0]))
        self.cola.pop(0)

    def consultaPendiente(self):
        return len(self.cola)


gestor = GestorConsultas()
for i in range(5):
    nombre = input("Ingresa tu nombre: ")
    correo = input("Ingresa tu correo: ")
    consulta = input("Ingresa el motivo de tu consulta: ")
    gestor.nuevaConsulta(Consulta(nombre, correo, consulta))

print("Existen:", gestor.consultaPendiente(), "consultas pendientes")
while gestor.consultaPendiente() > 0:
    bandera = input("Si desea atender la consulta, presione 1: ")
    if bandera == "1":
        gestor.atenderConsultas()
        print("Existen:", gestor.consultaPendiente(), "consultas pendientes")
