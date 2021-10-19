import pygame as py
import random
import Preguntas

class Boton(py.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, pantalla, cursor, Texto, x, y, valor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal

        pantalla.blit(self.imagen_actual, self.rect)
        pantalla.blit(Texto, (x, y))


class Cursor(py.Rect):
    def __init__(self):
        py.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = py.mouse.get_pos()

def ganancia():
    lista = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    return lista


def Estadisticas(pantalla, cursor1, texto4):
    val = "0"
    fondo = py.image.load("imagenes/fondo00.jpg")
    pantalla.blit(fondo, (220, 60))
    fuente2 = py.font.SysFont("Comic Sans MS", 16, True, False)
    blanco = (255, 255, 255)
    valor1 = py.image.load("imagenes/remarcado.gif")
    valor2 = py.image.load("imagenes/remarcado2.gif")
    boton5 = Boton(valor1, valor2, 260, 415)
    Atext1 = fuente2.render("  EN CONSTRUCCIÓN...", 1, blanco)

    pantalla.blit(Atext1, (230, 100))
    salir = False
    while salir != True:
        cursor1.update()
        boton5.update(pantalla, cursor1, texto4, 345, 415, "1")
        py.display.update()
        if val == "0":
            val = "1"
        for event in py.event.get():
            if event.type == py.QUIT:
                salir = True
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir = True
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    salir = True


def Instrucciones(pantalla, cursor1, texto4):
    fondo = py.image.load("imagenes/fondo00.jpg")
    val = "0"
    pantalla.blit(fondo, (220, 60))
    fuente2 = py.font.SysFont("Comic Sans MS", 16, True, False)
    blanco = (255, 255, 255)
    valor1 = py.image.load("imagenes/remarcado.gif")
    valor2 = py.image.load("imagenes/remarcado2.gif")
    boton5 = Boton(valor1, valor2, 260, 425)
    Atext1 = fuente2.render("  INSTRUCCIONES", 1, blanco)
    Atext2 = fuente2.render("1. Este es un juego de preguntas, donde", 1, blanco)
    Atext3 = fuente2.render("    tendras que elegir entre cuatro opciones.", 1, blanco)
    Atext4 = fuente2.render("2. Para llegar al final, debes contestar", 1, blanco)
    Atext5 = fuente2.render("    quince preguntas seguida sin equivocarte.", 1, blanco)
    Atext6 = fuente2.render("3. Atravez de cada pregunta constestada correcta-", 1, blanco)
    Atext7 = fuente2.render("   mente se ira acomulando una ganancia en dinero", 1, blanco)

    pantalla.blit(Atext1, (230, 100))
    pantalla.blit(Atext2, (230, 140))
    pantalla.blit(Atext3, (230, 180))
    pantalla.blit(Atext4, (230, 220))
    pantalla.blit(Atext5, (230, 260))
    pantalla.blit(Atext6, (230, 300))
    pantalla.blit(Atext7, (230, 340))
    salir = False

    while salir != True:
        cursor1.update()
        boton5.update(pantalla, cursor1, texto4, 345, 435, "1")
        py.display.update()
        if val == "0":
            val = "1"
        for event in py.event.get():
            if event.type == py.QUIT:
                salir = True
                py.mixer.stop()
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir = True
                    py.mixer.stop()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton5.rect):
                    salir = True
                    py.mixer.stop()


def Jugar(pantalla, cursor1):
    precio2 = 0
    cont1 = 0
    precio = ""
    gan = ganancia()
    fondo = py.image.load("imagenes/pregunta00.jpg")
    parche = py.image.load("imagenes/parche.gif")
    pantalla.blit(fondo, (0, 0))
    fuente2 = py.font.SysFont("Comic Sans MS", 16, True, False)
    blanco = (255, 255, 255)
    valor1 = py.image.load("imagenes/remarcado.gif")
    valor2 = py.image.load("imagenes/remarcado2.gif")
    lista = Preguntas.preguntas()
    temp = 19
    fuente1 = py.font.SysFont("Comic Sans MS", 34, True, False)
    jboton1 = Boton(valor1, valor2, 46, 421)
    jboton2 = Boton(valor1, valor2, 422, 421)
    jboton3 = Boton(valor1, valor2, 46, 496)
    jboton4 = Boton(valor1, valor2, 424, 496)
    salir = False

    while salir != True:

        for event in py.event.get():
            if event.type == py.QUIT:
                salir = True
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    salir = True
        if temp == 1:
            salir = True

        aleatorio = random.choice(range(temp))
        temp = temp - 1
        preg = lista.pop(aleatorio)
        cursor1.update()
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(parche, (115, 280))
        Atext = fuente2.render(preg[0], 1, blanco)
        Atext1 = fuente2.render(preg[1], 1, blanco)
        Atext2 = fuente2.render(preg[2], 1, blanco)
        Atext3 = fuente2.render(preg[3], 1, blanco)
        Atext4 = fuente2.render(preg[4], 1, blanco)
        precio = "GANANCIA: " + str(precio2)
        precio_cont = fuente1.render(precio, 1, blanco)
        pantalla.blit(precio_cont, (400, 40))
        pantalla.blit(Atext, (80, 300))
        jboton1.update(pantalla, cursor1, Atext1, 65, 430, "1")
        jboton2.update(pantalla, cursor1, Atext2, 450, 430, "1")
        jboton3.update(pantalla, cursor1, Atext3, 65, 508, "1")
        jboton4.update(pantalla, cursor1, Atext4, 450, 508, "1")
        py.display.update()
        salir2 = False
        resp = False
        # LOOP PRINCIPAL
        while salir2 != True:

            for event2 in py.event.get():
                if event2.type == py.QUIT:
                    salir2 = True
                if event2.type == py.KEYDOWN:
                    if event2.unicode == "s":
                        salir2 = True
                    if event2.unicode == "a":
                        salir2 = True
                        if preg[5] == 1:
                            resp = True
                        else:
                            resp = False
                    if event2.unicode == "b":
                        salir2 = True
                        if preg[5] == 2:
                            resp = True
                        else:
                            resp = False
                    if event2.unicode == "c":
                        salir2 = True
                        if preg[5] == 3:
                            resp = True
                        else:
                            resp = False
                    if event2.unicode == "d":
                        salir2 = True
                        if preg[5] == 4:
                            resp = True
                        else:
                            resp = False
                if event2.type == py.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(jboton1.rect):
                        salir2 = True
                        if preg[5] == 1:
                            resp = True
                        else:
                            resp = False
                    if cursor1.colliderect(jboton2.rect):
                        salir2 = True
                        if preg[5] == 2:
                            resp = True
                        else:
                            resp = False
                    if cursor1.colliderect(jboton3.rect):
                        salir2 = True
                        if preg[5] == 3:
                            resp = True
                        else:
                            resp = False
                    if cursor1.colliderect(jboton4.rect):
                        salir2 = True
                        if preg[5] == 4:
                            resp = True

                        else:
                            resp = False

            cursor1.update()
            pantalla.blit(fondo, (0, 0))
            pantalla.blit(parche, (115, 280))
            pantalla.blit(precio_cont, (530, 40))
            pantalla.blit(Atext, (80, 300))
            jboton1.update(pantalla, cursor1, Atext1, 65, 430, "1")
            jboton2.update(pantalla, cursor1, Atext2, 450, 430, "1")
            jboton3.update(pantalla, cursor1, Atext3, 65, 508, "1")
            jboton4.update(pantalla, cursor1, Atext4, 450, 508, "1")
            py.display.update()
        if resp == True:
            print("ACERTASTE")
            cont1 = cont1 + 1
            precio2 = gan[cont1]
        else:
            print("PERDISTE")
            IniciarJuego()


def IniciarJuego():
    py.init()
    usuario = ""
    val = "0"
    pantalla = py.display.set_mode((833, 559))
    py.display.set_caption("¿QUIEN QUIERE SER MILLONARIO?")
    icon = py.image.load("imagenes/coin.gif")
    fondo = py.image.load("imagenes/fondo01.jpg")
    valor1 = py.image.load("imagenes/remarcado.gif")
    valor2 = py.image.load("imagenes/remarcado2.gif")
    boton1 = Boton(valor1, valor2, 28, 410)
    boton2 = Boton(valor1, valor2, 444, 410)
    boton3 = Boton(valor1, valor2, 444, 495)
    boton4 = Boton(valor1, valor2, 28, 495)
    cursor1 = Cursor()
    fuente1 = py.font.SysFont("Comic Sans MS", 34, True, False)
    py.display.set_icon(icon)
    blanco = (255, 255, 255)
    texto1 = fuente1.render("         Jugar", 1, blanco)
    texto2 = fuente1.render("    Instrucciones", 1, blanco)
    texto3 = fuente1.render("     Estadisticas", 1, blanco)
    texto4 = fuente1.render("         Salir", 1, blanco)
    texto5 = fuente1.render("    Salir", 1, blanco)
    usuario = usuario
    texto6 = fuente1.render("Nick: "+usuario, 1, blanco)
    salir = False

    while salir != True:
        pantalla.blit(fondo, (0, 0))
        cursor1.update()
        boton1.update(pantalla, cursor1, texto1, 28, 415, "1")
        boton2.update(pantalla, cursor1, texto2, 444, 415, "2")
        boton3.update(pantalla, cursor1, texto4, 444, 500, "3")
        boton4.update(pantalla, cursor1, texto3, 28, 500, "4")
        pantalla.blit(texto6, (28, 20))
        py.display.update()

        for event in py.event.get():
            if event.type == py.QUIT:
                salir = True
            if event.type == py.KEYDOWN:
                if event.unicode == "s":
                    py.quit()
                if event.unicode == "j":
                    Jugar(pantalla, cursor1)
                if event.unicode == "a":
                    Estadisticas(pantalla, cursor1, texto5)
                if event.unicode == "i":
                    Instrucciones(pantalla, cursor1, texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton3.rect):
                    py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton2.rect):
                    Instrucciones(pantalla, cursor1, texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton4.rect):
                    Estadisticas(pantalla, cursor1, texto5)
            if event.type == py.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    Jugar(pantalla, cursor1)
        if val == "0":
            val = "1"
    py.quit()


if __name__=='__main__':
    IniciarJuego()

