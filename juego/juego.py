#pgzero
import random 

TITLE = "⛧°.⋆༺♱༻⋆.°⛧"
HEIGHT = 445
WIDTH = 765
FPS = 30

#Objetos
menu = Actor("Fondooo")
start = Actor("start", (200, 120))
controles = Actor("controles", (200, 200))
tienda = Actor("tienda", (200, 280))
instruc = Actor("instrucciones", (200, 360))
titulo = Actor("Titulo", (525, HEIGHT/2))
modo = "menu"
a = Actor("ADA", (250, 100))
d = Actor("DDA", (350, 100))
s = Actor("SDA", (450, 100))
w = Actor("WDA", (550, 100))
space = Actor("SPACEDA", (250, 275))
j = Actor("JDA", (350, 275))
k = Actor("KDA", (450, 275))
p = Actor("PDA", (550, 275))
cross = Actor("crosss", (740, 25))
salud = Actor("redpotionn", (250, 325))

correr = ["run1", "run2", "run3", "run4", "run5", "run6"]
frame_inicial = 0
corriendo = False
velocidadf = 0.09
tiempo = 0

saltar =["salto1", "salto2", "salto3", "salto4"]
frame_inicial_salto = 0
saltando = False
velocidads = 0.1
tiempo_salto = 0

saltar_left = ["saltol1", "saltol2", "saltol3", "saltol4"]
frame_salto_izquierda = 0

correr_izquierda = ["runl1", "runl2", "runl3", "runl4", "runl5", "runl6"]
frame_inicial_izquierda = 0
corriendo_izquierda = False
velocidadiz = 0.09
tiempo_izquierda = 0

atacar = ["ataque1", "ataque2", "ataque3", "ataque4", "ataque5"]
frame_inicial_ataque = 0
ataque = False
velocidada = 0.07
velocidada_menu = 0.09
tiempo_ataque = 0

atacar_izquierda = ["ataquel1", "ataquel2", "ataquel3", "ataquel4", "ataquel5"]
frame_ataque_izquierda = 0

magic = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
frame_magia = 0
mattack = False
velocidadm = 0.009
tiempo_magia = 0

magic_left = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9", "l10", "l11", "l12", "l13", "l14", "l15"]
frame_magia_left = 0

idle = ["idle1", "idle2", "idle3", "idle4"]
frame_idle = 0
quieto = True
velocidad = 0.2
tiempo_quieto = 0

idle_izquierda = ["idlel1", "idlel2", "idlel3", "idlel4"]
frame_idle_izquierda = 0

#personaje
prota = Actor(idle[frame_idle], (100, HEIGHT - 55))
derecha = True 

#salto, gravedad

altura = 100
gravedad = 6
velocidad_salto = -30
en_suelo = True
velocidad_y = 0

#UI
ui_puesta = False
heart = Actor("heart")
cantidad_h = 3
corazones = []

mana = Actor ("purple_potion")
cantidad_m = 2
potions = []

cantidad_ma = 2
matraces = []
    
#tienda

fragmento_de_almas = 0

#objetos niveles

fondo = Actor("fondo")
cementerios = Actor("graveyard")
suelos = Actor("floor")
arboles = ["tree1", "tree2", "tree3"]
tumbas = ["stone1", "stone2", "stone3", "stone4"]
cementerio_nivel = []
suelo_nivel = []
arboles_nivel = []
tumbas_nivel = []
creacion = False

#variables para animaciones
ataque_en_progreso = False
salto_en_progreso = False
ultimo_frame_salto = False
magia_en_progreso = False
magia_alcance = 600
magia_distancia = 0
magia_velocidad = 15
magia_direccion = 1
magia_pos = (0,0)

#funcion niveles
def niveles():
    global suelo_nivel, arboles_nivel,cementerios_nivel, creacion
    if not creacion:
        suelo_nivel = []
        arboles_nivel = []
        cementerios_nivel = []
        for i in range(0, WIDTH, suelos.width):
            suelo = Actor("floor", (i + suelos.width // 2, HEIGHT - suelos.height // 2))
            suelo_nivel.append(suelo)
        for j in range(5):
            tipo = random.choice(arboles)
            xpos = random.randint(0, WIDTH)
            ypos = HEIGHT - suelos.height - 50  
            arbol = Actor(tipo, (xpos,ypos))
            arboles_nivel.append(arbol)
        for k in range(15):
            tipo_s = random.choice (tumbas)
            xpos = random.randint(0, WIDTH)
            ypos = HEIGHT - suelos.height - 10
            tumba = Actor(tipo_s,(xpos,ypos))
            tumbas_nivel.append(tumba)
        for l in range(0, WIDTH + 200, cementerios.width):
            cementerio = Actor("graveyard", (l + suelos.width // 2, HEIGHT - cementerios.height //2))
            cementerio_nivel.append(cementerio)
        creacion = True
        
#funcion INTERFAZ DE USUARIO
        
def ui():
    global corazones, potions, ui_puesta
    if not ui_puesta:
        for f in range(cantidad_h):
            x_pos_heart = 50 + f * (heart.width + 5)
            y_pos_heart = 40
            corazon = Actor("heart",(x_pos_heart, y_pos_heart))
            corazones.append(corazon)
            
        for p in range(cantidad_m):
            x_pos_potion = 50 + p * (mana.width + 5)
            y_pos_potion = 65
            pocion = Actor("purple_potion",(x_pos_potion, y_pos_potion))
            potions.append(pocion)
            
        for g in range (cantidad_ma):
            x_pos_matraz = 50 + g * (salud.width + 5)
            y_pos_matraz = 95
            matraz = Actor("redpotionn", (x_pos_matraz, y_pos_matraz))
            matraces.append(matraz)
            ui_puesta = True
        
# Teclas  
        
def on_key_down(key):
    global ataque, frame_inicial_ataque, ataque_en_progreso
    global saltando, salto_en_progreso, frame_inicial_salto, en_suelo
    global magia_en_progreso, cantidad_m, magia_pos, magia_direccion, derecha
    
    
    if key == keys.J and not ataque and en_suelo:  
        ataque = True
        ataque_en_progreso = True
        frame_inicial_ataque = 0 
        
    if key == keys.W and en_suelo:
        if not ataque: 
            saltando = True
            salto_en_progreso = True
            frame_inicial_salto = 0
            
    if key == keys.K and not ataque and cantidad_m > 0:
        magia_en_progreso = True
        cantidad_m -= 1
        if potions:
            potions.pop()
        magia_pos = (prota.x, prota.y - 10)
        magia_direccion = 1 if derecha else -1  

        
def update(dt):
    global frame_inicial, tiempo, corriendo
    global saltando, tiempo_salto, frame_inicial_salto
    global frame_inicial_izquierda, corriendo_izquierda,tiempo_izquierda
    global frame_inicial_ataque, tiempo_ataque, ataque
    global frame_ataque_izquierda, tiempo_ataque 
    global frame_magia, mattack, tiempo_magia, magia_en_progreso, magia_pos, magia_distancia, magia_velocidad, magia_direccion, frame_magia_left
    global frame_idle, quieto, velocidad, tiempo_quieto
    global frame_idle_izquierda, quieto_izquierda, velocidad_q, tiempo_quieto_izquierda
    global derecha, ataque_en_progreso, salto_en_progreso, prota
    global en_suelo, velocidad_y, ultimo_frame_salto, frame_salto_izquierda
    
    if modo == "controles":
        corriendo = True
        saltando = True
        corriendo_izquierda = True
        ataque = True
        mattack = True
        if corriendo:
            tiempo += dt
            if tiempo > velocidadf:
                frame_inicial = (frame_inicial + 1) % len(correr)
                tiempo = 0
        if saltando:
            tiempo_salto += dt
            if tiempo_salto > velocidads:
                frame_inicial_salto = (frame_inicial_salto + 1) % len(saltar)
                tiempo_salto = 0
        if corriendo_izquierda:
            tiempo_izquierda += dt
            if tiempo_izquierda > velocidadiz:
                frame_inicial_izquierda = (frame_inicial_izquierda + 1) % len(correr_izquierda)
                tiempo_izquierda = 0
        if ataque:
            tiempo_ataque += dt
            if tiempo_ataque > velocidada_menu:
                frame_inicial_ataque = (frame_inicial_ataque + 1) % len(atacar)
                tiempo_ataque = 0
                
        if mattack:
            tiempo_magia += dt
            if tiempo_magia > velocidadm:
                frame_magia = (frame_magia +1) % len(magic)
                tiempo_magia = 0
    else: 
        corriendo = False
        saltando = False
        corriendo_izquierda = False
        ataque = False
        mattack = False
        
    if modo == "juego":
        
        if magia_en_progreso:
            magia_pos = (magia_pos[0] + magia_velocidad * magia_direccion, magia_pos[1])
            if magia_direccion == 1:
                frame_magia = (frame_magia + 1) % len(magic)
            else:
                frame_magia_left = (frame_magia_left + 1) % len(magic_left)
            if magia_pos[0] < 0 or magia_pos[0] > WIDTH:
                magia_en_progreso = False
            
        if ataque_en_progreso:
            tiempo_ataque += dt
            if tiempo_ataque > velocidada:
                tiempo_ataque = 0
                if derecha:
                    if frame_inicial_ataque < len(atacar):
                        prota.image = atacar[frame_inicial_ataque]
                        frame_inicial_ataque += 1
                    else:
                        ataque = False
                        ataque_en_progreso = False
                        frame_inicial_ataque = 0
                else:
                    if frame_ataque_izquierda < len(atacar_izquierda):
                        prota.image = atacar_izquierda[frame_ataque_izquierda]
                        frame_ataque_izquierda += 1
                    else:
                        ataque = False
                        ataque_en_progreso = False
                        frame_ataque_izquierda = 0
            return
        
        if en_suelo:
        
            if keyboard.d:
                prota.x += 5
                derecha = True
                corriendo = True
                quieto = False
                tiempo += dt
                if tiempo > velocidadf:
                    frame_inicial = (frame_inicial + 1) % len(correr)
                    tiempo = 0
                prota.image = correr[frame_inicial]
            elif keyboard.a:
                prota.x -= 5
                derecha = False 
                corriendo_izquierda = True
                quieto = False
                tiempo_izquierda += dt
                if tiempo_izquierda > velocidadiz:
                    frame_inicial_izquierda = (frame_inicial_izquierda + 1) % len(correr_izquierda)
                    tiempo_izquierda = 0
                prota.image = correr_izquierda[frame_inicial_izquierda]
                
            elif keyboard.s:
                quieto = False
                corriendo = False
                corriendo_izquierda = False
                if derecha:
                    prota.image = "crouch"
                else:
                    prota.image = "crouchl"
                
            else:
                if not quieto and en_suelo:
                        quieto = True
                        corriendo = False
                        corriendo_izquierda = False
                        if derecha:
                            prota.image = idle[frame_idle]
                        else:
                            prota.image = idle_izquierda[frame_idle_izquierda]
                        tiempo_quieto = 0
                else:
                    if quieto and en_suelo:
                        tiempo_quieto += dt
                        if tiempo_quieto > velocidad:
                            if derecha:
                                frame_idle = (frame_idle + 1) % len(idle)
                                prota.image = idle[frame_idle]
                                
                            else: 
                                frame_idle_izquierda = (frame_idle_izquierda + 1) % len(idle)
                                prota.image = idle_izquierda[frame_idle_izquierda]
                            tiempo_quieto = 0
            
            
            if salto_en_progreso:
                velocidad_y = velocidad_salto 
                en_suelo = False
                salto_en_progreso = False
                frame_inicial_salto = 0

        else:
            
            if keyboard.d:
                prota.x += 7  
            elif keyboard.a:
                prota.x -= 7  
            
            if derecha:
                prota.image = saltar[min(frame_inicial_salto, len(saltar) - 1)]
            else:
                prota.image = saltar_left[min(frame_salto_izquierda, len(saltar_left) - 1)]
                
        
        
        if not en_suelo:
            prota.y += velocidad_y
            velocidad_y += gravedad 
        
            if prota.y >= HEIGHT - 55:
                prota.y = HEIGHT - 55
                en_suelo = True
                velocidad_y = 0
            
            
            if not en_suelo:
                tiempo_salto += dt
                if tiempo_salto > velocidads:
                    if derecha:
                        frame_inicial_salto = min(frame_inicial_salto + 1, len(saltar) - 1)
                    else:
                        frame_salto_izquierda = min(frame_salto_izquierda + 1, len(saltar_left) - 1)
                    tiempo_salto = 0

        return


def draw():
    if modo == "menu":
        menu.draw()
        start.draw()
        controles.draw()
        titulo.draw()
        tienda.draw()
        instruc.draw()
        
    elif modo == "controles":
        menu.draw()
        a.draw()
        d.draw()
        s.draw()
        w.draw()
        space.draw()
        j.draw()
        k.draw()
        p.draw()
        cross.draw()
        runner = Actor(correr[frame_inicial], (350,150))
        runner.draw()
        jumper = Actor(saltar[frame_inicial_salto], (550,150))
        jumper.draw()
        runnerleft = Actor(correr_izquierda[frame_inicial_izquierda], (250, 150))
        runnerleft.draw()
        crouch = Actor("crouch", (450, 150))
        crouch.draw()
        attack = Actor(atacar[frame_inicial_ataque], (350, 325))
        attack.draw()
        mago = Actor (magic[frame_magia], (450, 325))
        mago.draw()
        salud.draw()
    
    elif modo == "juego":
        fondo.draw()
        niveles()
        for cementerio in cementerio_nivel:
            cementerio.draw()
        for arbol in arboles_nivel:
            arbol.draw()
        for tumba in tumbas_nivel:
            tumba.draw()
        for suelo in suelo_nivel:
            suelo.draw()
        prota.draw()
        ui()
        for corazon in corazones:
            corazon.draw()
        for potion in potions:
            potion.draw()
        for matraz in matraces:
            matraz.draw()
        if magia_en_progreso:
            if magia_direccion == 1:
                magiaa = Actor(magic[frame_magia], magia_pos)
            else:
                magiaa = Actor(magic_left[frame_magia_left], magia_pos)
            magiaa.draw()
            
def on_mouse_move(pos):
    global menu
    if modo == "menu":
        if start.collidepoint(pos):
            start.image = "starth"
        else:
            start.image = "start"
        if controles.collidepoint(pos):
            controles.image = "controlesh"
        else:
            controles.image = "controles"
        if tienda.collidepoint(pos):
            tienda.image = "tiendah"
        else:
            tienda.image = "tienda"
        if instruc.collidepoint(pos):
            instruc.image = "Instruccionesh"
        else: 
            instruc.image = "instrucciones"
            
def on_mouse_down(button, pos):
    global modo
    if button == mouse.left:
        if modo == "menu":
            if start.collidepoint(pos):
                modo = "juego"
        if modo == "menu":
            if controles.collidepoint(pos):
                modo = "controles"
        if modo == "controles":
            if cross.collidepoint(pos):
                modo = "menu"
            