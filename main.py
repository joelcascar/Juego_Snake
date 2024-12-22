""""
import turtle as t
import time
# instanciamos las clases Screen() y Turtle
screen = t.Screen()
t1 = t.Turtle()
t2 = t.Turtle()

# Funciones
def movedown():
    t2.sety(t2.ycor() - 20)

def moveup():
    t2.sety(t2.ycor() + 20)

def moveleft():
    t2.setx(t2.xcor() - 20)

def moveright():
    t2.setx(t2.xcor() + 20)

screen.title("Esto es el titulo de la ventana")
screen.bgcolor("green")
screen.setup(800,600)
t1.goto(150,5)
t1.goto(-100, -30)
t1.speed(0)
t1.goto(200,30)
t1.shape("square")
t1.color("red")
t1.up()
t1.write("Esto es texto escrito en el tiempo", align="center", font=("Courier", 24, "normal"))
t2.sety(t2.ycor() + 100)
t2.fd(20)
t1.setx(t1.xcor() + 100)
t1.sety(t1.ycor() + 70)
screen.listen()
screen.onkeypress(movedown, "s")
screen.onkeypress(moveup, "w")
screen.onkeypress(moveleft, "a")
screen.onkeypress(moveright, "d")
while True:
    screen.update()
    time.sleep(0.1)
screen.mainloop()
"""

#1 Juego Snake
import turtle as t
import time
import random
class Snake:
    def __init__(self, width=600, heigth=600, color="green"):
        # Inicializa el lienzo de la pantalla
        self.pantalla = t.Screen()
        self.pantalla.setup(width, heigth)
        self.pantalla.bgcolor(color)
        self.pantalla.title("Juego Snake")
        self.pantalla.tracer(0)
        # Inicializa la serpiente
        self.serpiente = t.Turtle()
        self.serpiente.speed(0)
        self.serpiente.shape("square")
        self.serpiente.color("black")
        self.serpiente.up()
        self.serpiente.goto(0, 0)
        # Inicializar el texto que se muestra en la pantalla
        self.marcador = t.Turtle()
        self.marcador.up()
        self.marcador.speed(0)
        self.marcador.color("white")
        self.marcador.hideturtle()
        self.marcador.sety(self.marcador.ycor() + ((heigth / 2) - 40))
        # Inicializa la comida de la serpiente
        self.comida = t.Turtle()
        self.comida.speed()
        self.comida.up()
        self.comida.shape("circle")
        self.comida.color("red")
        self.comida.goto(0, 100)
        # Atributos de la clase
        self._direccion = None
        self._delay = 0.1
        self._width = width
        self._heigth = heigth
        self._score = 0
        self._high_score = 0
        self._cuerpo = []
        # Asociación de los movimientos y las teclas
        self.pantalla.listen()
        self.pantalla.onkeypress(self.arriba, "w")
        self.pantalla.onkeypress(self.abajo, "s")
        self.pantalla.onkeypress(self.derecha, "d")
        self.pantalla.onkeypress(self.izquierda, "a")
        # Sacamos el texto por pantalla
        self.imprimir_score()

    def arriba(self):
        """Este metodo define el movimiento hacia arriba de la serpiente."""
        if self._direccion != "abajo":
            self._direccion = "arriba"

    def abajo(self):
        """Este metodo define el movimiento hacia abajo de la serpiente."""
        if self._direccion != "arriba":
            self._direccion = "abajo"

    def izquierda(self):
        """Este metodo define el movimiento hacia la izquierda de la serpiente."""
        if self._direccion != "derecha":
            self._direccion = "izquierda"

    def derecha(self):
        """Este metodo define el movimiento hacia la derecha de la serpiente."""
        if self._direccion != "izquierda":
            self._direccion = "derecha"

    def move(self):
        # obtener las coordenadas de la serpiente
        hx = self.serpiente.xcor()
        hy = self.serpiente.ycor()
        # movemos el cuerpo de la serpiente
        # recorremos la lista de segmentos del cuerpo desde el último segmento.
        for i in range(len(self._cuerpo) - 1, 0, -1):
            # obtenemos las coordenadas del segmento anterior
            x = self._cuerpo[i - 1].xcor()
            y = self._cuerpo[i - 1].ycor()
            # mandamos el segmento actual a la posición del segmento anterior
            self._cuerpo[i].goto(x, y)
        # Movemos el segmento mas cercano a la cabeza de la serpiente
        if len(self._cuerpo) > 0:
            self._cuerpo[0].goto(hx, hy)
        # Definimos las acciones dependiendo de la dirección.
        if self._direccion == "arriba":
            self.serpiente.sety(hy + 20)
        elif self._direccion == "abajo":
            self.serpiente.sety(hy - 20)
        elif self._direccion == "derecha":
            self.serpiente.setx(hx + 20)
        elif self._direccion == "izquierda":
            self.serpiente.setx(hx - 20)

    def jugar(self):
        while True:
            self.pantalla.update()
            self.colision_borde()
            self.colision_comida()
            self.colision_cuerpo()
            time.sleep(self._delay)
            self.move()
        self.pantalla.mainloop()

    def colision_borde(self):
        bxcor = (self._width // 2) - 10
        bycor = (self._heigth // 2) - 10
        if self.serpiente.xcor() > bxcor or self.serpiente.xcor() < -bxcor or self.serpiente.ycor() > bycor or self.serpiente.ycor() < -bycor:
            self._reset()

    def colision_comida(self):
        if self.serpiente.distance(self.comida) < 20:
            # Mover la comida a un lugar aleatorio
            cxcor = (self._width // 2) - 20
            cycor = (self._heigth // 2) - 20
            x = random.randint(-cxcor, cxcor)
            y = random.randint(-cycor, cycor)
            self.comida.goto(x, y)
            # Incrementamos el cuerpo de la serpiente
            self.incrementar_cuerpo()
            # Reducir el delay
            self._delay -= 0.001
            # Aumentar el score
            self._score += 10
            self.imprimir_score()

    def imprimir_score(self):
        self.marcador.clear()
        self.marcador.write("Puntos: {} Record: {}".format(self._score, self._high_score), move=False, align="center",
                            font=("arial", 24, "normal"))

    def incrementar_cuerpo(self):
        # Creamos el segmento del cuerpo
        segmento = t.Turtle()
        # Inicializamos la velodicdad del segmento del cuerpo
        segmento.speed(0)
        # Cambiamos la forma del segmento del cuerpo
        segmento.shape("square")
        # Cambiamos el color del segmento del cuerpo
        segmento.color("grey")
        # Evitamos que el segmento del cuerpo pinte en el lienzo
        segmento.up()
        self._cuerpo.append(segmento)

    def _reset(self):
        time.sleep(1)
        self.serpiente.goto(0, 0)
        self._direccion = None
        # Reiniciamos el cuerpo de la serpiente
        for s in self._cuerpo:
            s.hideturtle()
        # Limpiamos la lista de segmentos
        self._cuerpo.clear()
        # Reiniciar el delay
        self._delay = 0.1
        # Reiniciar el score
        if self._score > self._high_score:
            self._high_score = self._score
            self._score = 0
            self.imprimir_score()
        # reiniciamos la comida
        self.comida.goto(0, 100)

    def colision_cuerpo(self):
        for i in range(len(self._cuerpo)):
            if self.serpiente.distance(self._cuerpo[i]) < 10:
                self._reset()
                break

juego1 = Snake()
juego1.jugar()
