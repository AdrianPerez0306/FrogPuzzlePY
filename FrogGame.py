import pygame
import sys

# Inicializar Pygame
pygame.init()

# Constantes
LONGITUD_CARRETERA = 7
ANCHO_VENTANA = 700
ALTO_VENTANA = 200
TAMANIO_CUADRO = ANCHO_VENTANA // LONGITUD_CARRETERA

# Cargar imágenes
imagen_rana = pygame.image.load("rana.png")
imagen_rana = pygame.transform.scale(imagen_rana, (TAMANIO_CUADRO - 10, TAMANIO_CUADRO - 10))  # Redimensionar la imagen
imagen_sapo = pygame.image.load("sapo.webp")
imagen_sapo = pygame.transform.scale(imagen_sapo, (TAMANIO_CUADRO - 10, TAMANIO_CUADRO - 10))  # Redimensionar la imagen
fondo = pygame.image.load("fondo.webp")  # Cargar imagen de fondo
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))  # Redimensionar la imagen de fondo
piedra = pygame.image.load("piedra.png")  # Cargar imagen de piedra
piedra = pygame.transform.scale(piedra, (TAMANIO_CUADRO, TAMANIO_CUADRO))  # Redimensionar la imagen de piedra

# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ranas y Sapos")

# Estado del tablero: vacío, ranas o sapos
tablero = ["rana", "rana", "rana", None, "sapo", "sapo", "sapo"]

# Función para dibujar el tablero
def dibujar_tablero():
    # Dibujar el fondo
    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en toda la ventana
    
    # Dibujar las casillas y los bordes
    for i in range(LONGITUD_CARRETERA):
        x = i * TAMANIO_CUADRO
        
        # Dibujar la imagen de piedra en cada casilla
        pantalla.blit(piedra, (x, 50))  # Dibujar piedra en la casilla

    
    # Dibujar los anfibios (ranas y sapos) según su posición en el tablero
    for i, ocupante in enumerate(tablero):
        if ocupante == "rana":
            pantalla.blit(imagen_rana, (i * TAMANIO_CUADRO + TAMANIO_CUADRO // 2 - 30, 55))
        elif ocupante == "sapo":
            pantalla.blit(imagen_sapo, (i * TAMANIO_CUADRO + TAMANIO_CUADRO // 2 - 30, 55))

# Función para mover una rana
def mover_rana(pos):
    if pos < LONGITUD_CARRETERA - 1:  # Si no está en el borde derecho
        if tablero[pos + 1] is None:  # Si la posición de adelante está vacía
            tablero[pos + 1] = "rana"
            tablero[pos] = None
        elif pos < LONGITUD_CARRETERA - 2 and tablero[pos + 1] == "sapo" and tablero[pos + 2] is None:
            # Si hay un sapo en la siguiente posición y la posición dos adelante está vacía
            tablero[pos + 2] = "rana"
            tablero[pos] = None

# Función para mover un sapo
def mover_sapo(pos):
    if pos > 0:  # Si no está en el borde izquierdo
        if tablero[pos - 1] is None:  # Si la posición de atrás está vacía
            tablero[pos - 1] = "sapo"
            tablero[pos] = None
        elif pos > 1 and tablero[pos - 1] == "rana" and tablero[pos - 2] is None:
            # Si hay una rana en la posición anterior y la posición dos atrás está vacía
            tablero[pos - 2] = "sapo"
            tablero[pos] = None

# Función para manejar clics del mouse
def manejar_click(posicion_click):
    casilla = posicion_click // TAMANIO_CUADRO  # Calcular en qué casilla se hizo clic
    if 0 <= casilla < LONGITUD_CARRETERA:
        if tablero[casilla] == "rana":
            mover_rana(casilla)
        elif tablero[casilla] == "sapo":
            mover_sapo(casilla)

# Bucle principal del juego
def juego():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                manejar_click(evento.pos[0])  # Obtener la posición del clic y manejar el movimiento

        # Dibujar el tablero con ranas y sapos
        dibujar_tablero()

        # Actualizar la pantalla
        pygame.display.flip()

# Ejecutar el juego
juego()
