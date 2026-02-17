# /**
#  * EJERCICIO:
#  * ¡Los JJOO de París 2024 han comenzado!
#  * Crea un programa que simule la celebración de los juegos.
#  * El programa debe permitir al usuario registrar eventos y participantes,
#  * realizar la simulación de los eventos asignando posiciones de manera aleatoria
#  * y generar un informe final. Todo ello por terminal.
#  * Requisitos:
#  * 1. Registrar eventos deportivos.
#  * 2. Registrar participantes por nombre y país.
#  * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
#  * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
#  * 5. Mostrar los ganadores por cada evento.
#  * 6. Mostrar el ranking de países según el número de medallas.
#  * Acciones:
#  * 1. Registro de eventos.
#  * 2. Registro de participantes.
#  * 3. Simulación de eventos.
#  * 4. Creación de informes.
#  * 5. Salir del programa.
#  */



    # Atletismo
    # Bádminton
    # Baloncesto
    # Baloncesto 3x3
    # Balonmano
    # Béisbol
    # Boxeo
    # Ciclismo BMX Freestyle
    # Ciclismo BMX Racing
    # Ciclismo de Montaña
    # Ciclismo en Pista
    # Ciclismo en Ruta
    # Críquet
    # Escalada Deportiva
    # Esgrima
    # Flag Football
    # Fútbol
    # Gimnasia Artística
    # Gimnasia en Trampolín
    # Gimnasia Rítmica
    # Golf
    # Halterofilia
    # Hípica
    # Hockey Sobre Césped
    # Judo
    # Lacrosse
    # Lucha
    # Natación
    # Natación Artística
    # Natación en Aguas Abiertas
    # Pentatlón Moderno
    # Piragüismo en Eslalon
    # Piragüismo en Esprint
    # Remo
    # Remo Costero
    # Rugby Sietes
    # Saltos
    # Skateboarding
    # Sóftbol
    # Squash
    # Surf
    # Taekwondo
    # Tenis
    # Tenis de Mesa
    # Tiro
    # Tiro Con Arco
    # Triatlón
    # Vela
    # Voleibol
    # Voleibol Playa
    # Waterpolo

class Participant:
    
    def __init__(self, name, country):
        self.name = name
        self.country = country


class Olympics:
    
    def __init__(self):
        self.eventos = []
    
    def register_event(self):
        #Capturar el nombre del evento deportivo
        event = " ".join(input("Introduce el evento deportivo: ").split()).strip().lower().title()
        
        #Verificar si el evento ya ha sido registrado
        if event in self.eventos:
            print(f"El evento { event } no puede registrarse dos veces.")
            return

        #Verificar que el evento no esté vacío
        if not event:
            print("El nombre del evento no puede estar vacío.")
            return
        
        #Verificar que el evento no contenga caracteres especiales
        if not event.replace(" ", "").isalnum():
            print("El nombre del evento no puede contener caracteres especiales.")
            return
        
        #Verificar que el evento no inicie con un número
        if event[0].isdigit():
            print("El nombre del evento no puede iniciar con un número.")
            return
        
        self.eventos.append(event)
        self.list_events()
    
    def list_events(self):
        if self.eventos:
            print()
            print("Eventos registrados:")
            for index,evento in enumerate(self.eventos, 1):
                print(f"{ index } - { evento }")
        else:
            print("No hay eventos registrados.")
        print()
        
    def register_participant(self):
        name = " ".join(input("Introduce el NOMBRE del participante: ").split()).strip().lower().title()
        country = " ".join(input("Introduce el PAÍS del participante: ").split()).strip().lower().title()
        participant = Participant(name, country)
        print(f"Participante registrado: { participant.name } de { participant.country }")

olympics_2026 = Olympics()

while True:
    print("*-" * 20)
    print("1. Registro de eventos")
    print("*" * 30)
    print("2. Registro de participantes")
    print("*" * 30)
    print("3. Simulación de eventos")
    print("*" * 30)
    print("4. Creación de informes")
    print("*" * 30)
    print("5. Salir del programa")
    print("*-" * 20)
    print()

    
    option = input("Selecciona una opción: ").strip()
    
    match option:
        case "1":
            olympics_2026.register_event()
        case "2":
            olympics_2026.register_participant()
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("¡Gracias por participar en los JJOO de la UTP 2026!")
            break
        case _:
            print(f"La opción { option } no es válida. Por favor, selecciona una opción del 1 al 5.")
            print()