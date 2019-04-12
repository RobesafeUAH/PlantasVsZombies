###############################################################################
#               JUEGO 4 EN RAYA DE JONATHAN MONCADA GAVILANES                 #
###############################################################################
#IMPORTAMOS LOS MODULOS NECESARIOS
import pygame as pygame
from recordclass import recordclass
#COLORES QUE UTILIZAREMOS EN EL PROGRAMA
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL=(0,0,255)
ROJO = (255, 0, 0)
#RECORDCLASS PARA GUARDAR LAS CASILLAS GANADORAS
tCasilla=recordclass("Casilla","pox posy")
#ARRAY DEL TABLERO
tablero = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
#EMPEZAMOS CON LAS FUNCIONES QUE UTILIZAREMOS EN EL JUEGO
def impresion_tablero():
    """OBJ: SOLO UTILIZAREMOS ESTE SUBPROGRAMA PARA IMPRIMIR EN LA CONSOLA EL TABLERO
    PRE:HABER CREADO ANTES EL ARRAY DEL TABLERO"""
    for i in range(0, 7):
        for e in range(0, 6):
            print(tablero[i][e], end=" ")
        print("")
    print("| " * 6)
    for j in range(1, 7):
        print("%1i" % (j), end=" ")
    print("\n")

def comprobar_horizontal():
    """OBJ:VA RECORRIENDO EL ARRAY DEL TABLERO HORIZONTALMENTE COMPROBANDO SI SE REPITEN EN 4 CASILLAS O - O X
    PRE:QUE EXISTA EL TABLERO"""
    raya = 0
    Ficha1 = tCasilla(-1, -1)
    Ficha2 = tCasilla(-1, -1)
    Ficha3 = tCasilla(-1, -1)
    Ficha4 = tCasilla(-1, -1)
    for i in range(6,-1,-1):
        for e in range(3):
            if tablero[i][e] == tablero[i][e + 1]==tablero[i][e + 2]==tablero[i][e + 3]=="-":
                Ficha1=tCasilla(i,e)
                Ficha2 = tCasilla(i, e+1)
                Ficha3 = tCasilla(i, e+2)
                Ficha4 = tCasilla(i, e+3)
                raya= 4
                print("="*30)
                print("Ha ganado el jugador AZUL")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
            elif tablero[i][e]==tablero[i][e + 1]==tablero[i][e + 2]==tablero[i][e + 3]=="x":
                Ficha1 = tCasilla(i, e)
                Ficha2 = tCasilla(i, e + 1)
                Ficha3 = tCasilla(i, e + 2)
                Ficha4 = tCasilla(i, e + 3)
                raya=4
                print("=" * 30)
                print("Ha ganado el jugador ROJO")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
    posision = [Ficha1, Ficha2, Ficha3, Ficha4]
    if raya == 4:
        final = True
    else:
        final = False
    return final,posision
def comprobar_vertical():
    """OBJ:VA RECORRIENDO EL ARRAY DEL TABLERO VERITICALMENTE COMPROBANDO SI SE REPITEN EN 4 CASILLAS O - O X
    PRE:QUE EXISTA EL TABLERO"""
    raya_vertical = 0
    Ficha1 = tCasilla(-1, - 1)
    Ficha2 = tCasilla(-1, - 1)
    Ficha3 = tCasilla(-1, - 1)
    Ficha4 = tCasilla(-1, - 1)
    for i in range(6):
        for e in range(6,3,-1):
            if tablero[e][i] == tablero[e-1][i]==tablero[e-2][i]==tablero[e-3][i]=="-":
                Ficha1 = tCasilla(i, e)
                Ficha2 = tCasilla(i, e - 1)
                Ficha3 = tCasilla(i, e - 2)
                Ficha4 = tCasilla(i, e - 3)
                raya_vertical= 4
                print("=" * 30)
                print("Ha ganado el jugador AZUL")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
            elif tablero[e][i] == tablero[e-1][i]==tablero[e-2][i]==tablero[e-3][i]=="x":
                Ficha1 = tCasilla(i, e)
                Ficha2 = tCasilla(i, e - 1)
                Ficha3 = tCasilla(i, e - 2)
                Ficha4 = tCasilla(i, e - 3)
                raya_vertical=4
                print("=" * 30)
                print("Ha ganado el jugador ROJO")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
    posision = [Ficha1, Ficha2, Ficha3, Ficha4]
    if raya_vertical == 4:
        final = True
    else:
        final = False
    return final,posision
def diagonal_ascendente():
    """OBJ:VA RECORRIENDO EL ARRAY DEL TABLERO DE IZQ A DERECHA COMPROBANDO SI SE REPITEN EN 4 CASILLAS DE LA DIAGONAL O - O X
        PRE:QUE EXISTA EL TABLERO"""
    raya_diagonal_asc= 0
    Ficha1 = tCasilla(-1, - 1)
    Ficha2 = tCasilla(-1, - 1)
    Ficha3 = tCasilla(-1, - 1)
    Ficha4 = tCasilla(-1, - 1)
    for i in range(3):
        for e in range(6,2,-1):
            if tablero[e][i] == tablero[e-1][i+1]==tablero[e-2][i+2]==tablero[e-3][i+3]=="-":
                Ficha1 = tCasilla(e,i)
                Ficha2 = tCasilla(e-1,i+1)
                Ficha3 = tCasilla(e-2,i+2)
                Ficha4 = tCasilla(e-3,i+3)
                raya_diagonal_asc= 4
                print("=" * 30)
                print("Ha ganado el jugador AZUL")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
            elif tablero[e][i] == tablero[e-1][i+1]==tablero[e-2][i+2]==tablero[e-3][i+3]=="x":
                Ficha1 = tCasilla(e, i)
                Ficha2 = tCasilla(e - 1, i + 1)
                Ficha3 = tCasilla(e - 2, i + 2)
                Ficha4 = tCasilla(e - 3, i + 3)
                raya_diagonal_asc=4
                print("=" * 30)
                print("Ha ganado el jugador ROJO")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
    posision = [Ficha1, Ficha2, Ficha3, Ficha4]
    if raya_diagonal_asc == 4:
        final = True
    else:
        final = False
    return final,posision
def diagonal_descendente():
    """OBJ:VA RECORRIENDO EL ARRAY DEL TABLERO DE DERECHA A IZQ COMPROBANDO SI SE REPITEN EN 4 CASILLAS DE LA DIAGONAL O - O X
            PRE:QUE EXISTA EL TABLERO"""
    raya_diagonal_des= 0
    Ficha1 = tCasilla(-1, - 1)
    Ficha2 = tCasilla(-1, - 1)
    Ficha3 = tCasilla(-1, - 1)
    Ficha4 = tCasilla(-1, - 1)
    for i in range(5,2,-1):
        for e in range(6,2,-1):
            if tablero[e][i] == tablero[e-1][i-1]==tablero[e-2][i-2]==tablero[e-3][i-3]=="-":
                Ficha1 = tCasilla(e, i)
                Ficha2 = tCasilla(e - 1, i - 1)
                Ficha3 = tCasilla(e - 2, i - 2)
                Ficha4 = tCasilla(e - 3, i - 3)
                raya_diagonal_des= 4
                print("=" * 30)
                print("Ha ganado el jugador AZUL")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ",Ficha1,Ficha2,Ficha3,Ficha4)
                print("=" * 30)
            elif tablero[e][i] == tablero[e-1][i-1]==tablero[e-2][i-2]==tablero[e-3][i-3]=="x":
                Ficha1 = tCasilla(e, i)
                Ficha2 = tCasilla(e - 1, i - 1)
                Ficha3 = tCasilla(e - 2, i - 2)
                Ficha4 = tCasilla(e - 3, i - 3)
                raya_diagonal_des=4
                print("=" * 30)
                print("Ha ganado el jugador ROJO")
                print("=" * 30)
                print("CUATRO EN RAYA EN: ", Ficha1, Ficha2, Ficha3, Ficha4)
                print("=" * 30)
    posision=[Ficha1,Ficha2,Ficha3,Ficha4]
    if raya_diagonal_des == 4:
        final = True
    else:
        final = False
    return final,posision

def juego():
    """OBJ: CREAR YA LA INTERFAZ GRAFICA CON EL MODULO PYGAME"""
    #AQUI CREAMOS UNA VARIABLE PANTALLA PARA DEFINIR LA VENTANA DONDE VAMOS A CREAR TODOS LOS ELEMENTOS DE PYGAME
    pantalla = pygame.display.set_mode((750, 480))
    #DIFERENTES VARIABLES QUE UTILIZAREMOS EN ESTE SUBPROGRAMA
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    #VARIABLES PARA LA CREACION DEL RECTANGULO DONDE INGRESAREMOS EL TEXTO
    input_box = pygame.Rect(475, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    activa = False
    columna = ''
    final = False
    #TITULO DE LA VENTANA
    pygame.display.set_caption("Conecta 4")
    #VARIABLES PARA QUE EL JUEGO PUEDA DARSE
    turno=1
    contador_col1 = 6
    contador_col2 = 6
    contador_col3 = 6
    contador_col4 = 6
    contador_col5 = 6
    contador_col6 = 6
    numero=""
    palabra=""
    #IMPRIMIMOS EL TABLERO UNA VEZ AL PRINCIPIO PARA QUE APAREZCA EL TABLERO ORIGINAL
    impresion_tablero()
    #EMPEZAMOS CON EL BUCLE GENERAL DEL JUEGO, Y VA A SER EL QUE NOS MOSTRARA TAMBIEN LOS DIFERENTES ELEMENTOS EN PANTALLA
    while not final:
        #UTILIZAMOS ESTA COMPRABACION PARA DEFINIR QUE FICHA INTRODUCIR EN CADA TURNO
        if turno % 2 == 0:
            ficha = "x"
        else:
            ficha = "-"
        #CON ESTE BUCLE LO QUE HACEMOS ES CAPTAR TODOS LOS EVENTOS DE PYGAME
        #CONFIGURAMOS LAS DISTINTAS FUENTES PARA LOS TEXTOS QUE UTILIZAREMOS
        fuenteBásica = pygame.font.SysFont(None, 48)
        fuente2 = pygame.font.SysFont(None, 20)
        fuente3 = pygame.font.SysFont(None, 30)
        texto1 = fuenteBásica.render('Tu turno', True, BLANCO)
        texto2 = fuenteBásica.render("Tu turno", True, BLANCO)
        texto3=fuenteBásica.render("CUATRO EN RAYA",True,(130,12,161))
        texto4=fuente2.render("PON UNA COLUMNA DEL 1 AL 6",True,(229,93,19))
        texto5=fuente2.render("COLUMNA INCORRECTA",True,BLANCO)
        texto6=fuente3.render("A jugar!!",True,BLANCO)
        # Establecemos el fondo de pantalla.
        pantalla.fill((30, 30, 30))
        # REDERIZAMOS EL TEXTO
        txt_pantalla = font.render(columna, True, color)
        # AGRANDAMOS EL RECUADRO SI EL TEXTO ES MUY GRANDE
        width = max(200, txt_pantalla.get_width()+10)
        input_box.w = width
        # PONEMOS EL TEXTO EN PANTALLA
        pantalla.blit(txt_pantalla, (input_box.x+5, input_box.y+5))
        # DIBUJAMOS EL RECUADRO DEL TEXTO
        pygame.draw.rect(pantalla, color, input_box, 2)
        for evento in pygame.event.get():
            #CON ESTO HACEMOS QUE EL USUARIO SI PINCHA EN LA X DE LA VENTANA, ESTA SE CIERRE Y SE TERMINE EL BUCLE
            if evento.type == pygame.QUIT:
                final = True
            #COMPROBACIONES DE LA CAJA DE ENTRADA DE DATOS
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # SI EL USUARIO PINCHA EN LA CAJA DE ENTRADA DE DATOS.
                if input_box.collidepoint(evento.pos):
                    # CREAMOS UNA VARIBLE PARA CUANDO LA CAJA ESTE ACTIVA
                    activa = not activa
                else:
                    activa = False
                # CAMBIAMOS EL COLOR DE LA CAJA DE TEXTO
                color = color_active if activa else color_inactive
            #CAPTAMOS CUANDO UN USUARIO PULSA TECLAS
            if evento.type == pygame.KEYDOWN:
                if activa:
                    #CUANDO PULSA ENTER VAMOS INTRODUCIR LAS FICHAS EN SU RESPECTIVO SITIO
                    if evento.key == pygame.K_RETURN:
                        if columna in ("1", "2", "3", "4", "5", "6"):
                            palabra=columna
                            numero=int(columna)-1
                        else:
                            palabra = columna
                            numero=8
                        if 0<=numero<7:
                            if numero == 0 and columna in ("1", "2", "3", "4", "5", "6"):
                                tablero[contador_col1][numero] = ficha
                                contador_col1 -= 1
                            elif numero == 1 and columna in ("1", "2", "3", "4", "5", "6"):
                                tablero[contador_col2][numero] = ficha
                                contador_col2 -= 1
                            elif numero == 2  and columna in ("1", "2", "3", "4", "5", "6"):
                                tablero[contador_col3][numero] = ficha
                                contador_col3 -= 1
                            elif numero == 3 and columna in ("1", "2", "3", "4", "5", "6"):
                                tablero[contador_col4][numero] = ficha
                                contador_col4 -= 1
                            elif numero == 4 and columna in ("1", "2", "3", "4", "5", "6"):
                                tablero[contador_col5][numero] = ficha
                                contador_col5 -= 1
                            elif numero == 5 and columna in ("1", "2", "3", "4", "5", "6"):
                                tablero[contador_col6][numero] = ficha
                                contador_col6 -= 1
                            #HACEMOS LAS COMPORABCIONES PARA VER SI ALGUIEN HA GANADO
                            parar1,posicion1=comprobar_horizontal()
                            parar2,posicion2=comprobar_vertical()
                            parar3,posicion3=diagonal_ascendente()
                            parar4,posicion4=diagonal_descendente()
                            if parar1 == True:
                                final=True
                                #podemos poner esta parte de codigo si quermos que aparezca un mensaje con quien es el ganador y la posicion de las fihcas
                                """texto8 = fuente2.render("Ganador AZUL!!", True, (229, 93, 19))
                                texto7 = fuente2.render(str(posicion1), True, (229, 93, 19))
                                texto9=fuente2.render("GANADOR ROJO!!",True,(229,93,19))
                                if turno%2==0:
                                    pantalla.blit(texto8,(525,360))
                                    pantalla.blit(texto7,(525,390))
                                else:
                                    pantalla.blit(texto9, (525, 360))
                                    pantalla.blit(texto7, (525, 390))"""
                            elif parar2 == True:
                                final = True
                            elif parar3 == True:
                                final = True
                            elif parar4 == True:
                                final = True
                            elif contador_col1 < -1 or contador_col2 < -1 or contador_col3 < -1 or contador_col4 < -1 or contador_col5 < -1 or contador_col6 < -1:
                                final = True
                            turno += 1
                        columna = ''
                        impresion_tablero()
                    elif evento.key == pygame.K_BACKSPACE:
                        columna = columna[:-1]
                    else:
                        columna += evento.unicode
        # DIBUJAMOS LOS ELEMENTOS
        pygame.draw.circle(pantalla, ROJO, (495, 250), 20, 0)
        pygame.draw.circle(pantalla, AZUL, (495, 350), 20, 0)
        #COMPROBAMOS SI EL NUMERO ES UNA COLUMNA CORRECTA O NO
        if numero in(0,1,2,3,4,5) or numero=="" or palabra=="":
            pantalla.blit(texto6, (475, 200))
        else:
            pantalla.blit(texto5, (475, 200))
        if turno%2==0:
            pantalla.blit(texto1, (525, 235))
        else:
            pantalla.blit(texto2, (525, 335))
        pantalla.blit(texto3,(20,15))
        pygame.draw.line(pantalla,(130,12,161),(20,45),(320,45),3)
        pantalla.blit(texto4,(475,130))
        #COLOCAMOS EN LA VENTANA LOS CIRCULOS ROJOS O AZULES DEPENDIENDO DEL MOVIMEINTO DEL JUGADOR
        #Fila6
        if tablero[6][0]=="-":
            pygame.draw.circle(pantalla, AZUL,(40,440), 20, 0)
        elif tablero[6][0]=="x":
            pygame.draw.circle(pantalla, ROJO, (40, 440), 20, 0)
        if tablero[6][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105, 440), 20, 0)
        elif tablero[6][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105, 440), 20, 0)
        if tablero[6][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165, 440), 20, 0)
        elif tablero[6][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165, 440), 20, 0)
        if tablero[6][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225, 440), 20, 0)
        elif tablero[6][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225, 440), 20, 0)
        if tablero[6][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285, 440), 20, 0)
        elif tablero[6][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285, 440), 20, 0)
        if tablero[6][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350, 440), 20, 0)
        elif tablero[6][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350, 440), 20, 0)
        #FILA 5
        if tablero[5][0]=="-":
            pygame.draw.circle(pantalla, AZUL,(40,388), 20, 0)
        elif tablero[5][0]=="x":
            pygame.draw.circle(pantalla, ROJO, (40, 388), 20, 0)
        if tablero[5][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105, 388), 20, 0)
        elif tablero[5][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105, 388), 20, 0)
        if tablero[5][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165, 388), 20, 0)
        elif tablero[5][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165, 388), 20, 0)
        if tablero[5][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225, 388), 20, 0)
        elif tablero[5][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225, 388), 20, 0)
        if tablero[5][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285, 388), 20, 0)
        elif tablero[5][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285, 388), 20, 0)
        if tablero[5][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350, 388), 20, 0)
        elif tablero[5][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350, 388), 20, 0)
        # FILA 4
        if tablero[4][0] == "-":
            pygame.draw.circle(pantalla, AZUL, (40, 336), 20, 0)
        elif tablero[4][0] == "x":
            pygame.draw.circle(pantalla, ROJO, (40, 336), 20, 0)
        if tablero[4][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105, 336), 20, 0)
        elif tablero[4][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105, 336), 20, 0)
        if tablero[4][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165, 336), 20, 0)
        elif tablero[4][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165, 336), 20, 0)
        if tablero[4][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225, 336), 20, 0)
        elif tablero[4][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225, 336), 20, 0)
        if tablero[4][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285, 336), 20, 0)
        elif tablero[4][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285, 336), 20, 0)
        if tablero[4][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350, 336), 20, 0)
        elif tablero[4][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350, 336), 20, 0)
        # FILA 3
        if tablero[3][0] == "-":
            pygame.draw.circle(pantalla, AZUL, (40, 284), 20, 0)
        elif tablero[3][0] == "x":
            pygame.draw.circle(pantalla, ROJO, (40, 284), 20, 0)
        if tablero[3][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105,284), 20, 0)
        elif tablero[3][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105,284), 20, 0)
        if tablero[3][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165,284), 20, 0)
        elif tablero[3][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165,284), 20, 0)
        if tablero[3][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225,284), 20, 0)
        elif tablero[3][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225,284), 20, 0)
        if tablero[3][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285,284), 20, 0)
        elif tablero[3][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285,284), 20, 0)
        if tablero[3][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350,284), 20, 0)
        elif tablero[3][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350,284), 20, 0)
        # FILA 2
        if tablero[2][0] == "-":
            pygame.draw.circle(pantalla, AZUL, (40, 232), 20, 0)
        elif tablero[2][0] == "x":
            pygame.draw.circle(pantalla, ROJO, (40, 232), 20, 0)
        if tablero[2][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105,232), 20, 0)
        elif tablero[2][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105,232), 20, 0)
        if tablero[2][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165,232), 20, 0)
        elif tablero[2][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165,232), 20, 0)
        if tablero[2][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225,232), 20, 0)
        elif tablero[2][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225,232), 20, 0)
        if tablero[2][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285,232), 20, 0)
        elif tablero[2][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285,232), 20, 0)
        if tablero[2][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350,232), 20, 0)
        elif tablero[2][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350,232), 20, 0)
        # FILA 1
        if tablero[1][0] == "-":
            pygame.draw.circle(pantalla, AZUL, (40, 180), 20, 0)
        elif tablero[1][0] == "x":
            pygame.draw.circle(pantalla, ROJO, (40, 180), 20, 0)
        if tablero[1][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105,180), 20, 0)
        elif tablero[1][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105,180), 20, 0)
        if tablero[1][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165,180), 20, 0)
        elif tablero[1][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165,180), 20, 0)
        if tablero[1][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225,180), 20, 0)
        elif tablero[1][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225,180), 20, 0)
        if tablero[1][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285,180), 20, 0)
        elif tablero[1][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285,180), 20, 0)
        if tablero[1][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350,180), 20, 0)
        elif tablero[1][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350,180), 20, 0)
        # FILA 0
        if tablero[0][0] == "-":
            pygame.draw.circle(pantalla, AZUL, (40, 128), 20, 0)
        elif tablero[0][0] == "x":
            pygame.draw.circle(pantalla, ROJO, (40, 128), 20, 0)
        if tablero[0][1] == "-":
            pygame.draw.circle(pantalla, AZUL, (105,128), 20, 0)
        elif tablero[0][1] == "x":
            pygame.draw.circle(pantalla, ROJO, (105,128), 20, 0)
        if tablero[0][2] == "-":
            pygame.draw.circle(pantalla, AZUL, (165,128), 20, 0)
        elif tablero[0][2] == "x":
            pygame.draw.circle(pantalla, ROJO, (165,128), 20, 0)
        if tablero[0][3] == "-":
            pygame.draw.circle(pantalla, AZUL, (225,128), 20, 0)
        elif tablero[0][3] == "x":
            pygame.draw.circle(pantalla, ROJO, (225,128), 20, 0)
        if tablero[0][4] == "-":
            pygame.draw.circle(pantalla, AZUL, (285,128), 20, 0)
        elif tablero[0][4] == "x":
            pygame.draw.circle(pantalla, ROJO, (285,128), 20, 0)
        if tablero[0][5] == "-":
            pygame.draw.circle(pantalla, AZUL, (350,128), 20, 0)
        elif tablero[0][5] == "x":
            pygame.draw.circle(pantalla, ROJO, (350,128), 20, 0)
        #numeros
        fuente_num=pygame.font.SysFont(None,30)
        num1=fuente_num.render("1",True,ROJO)
        num2 = fuente_num.render("2", True, ROJO)
        num3 = fuente_num.render("3", True, ROJO)
        num4 = fuente_num.render("4", True, ROJO)
        num5 = fuente_num.render("5", True, ROJO)
        num6 = fuente_num.render("6", True, ROJO)
        reglas=fuente2.render("¡¡Pulsa en el cuadro para jugar hasta que se ilumine!!",True,(229,93,19))
        num7=fuente_num.render("7",True,ROJO)
        pantalla.blit(num1,(35,78))
        pantalla.blit(num1, (390,435))
        pantalla.blit(num2, (96,78))
        pantalla.blit(num2, (390,380))
        pantalla.blit(num3, (157,78))
        pantalla.blit(num3, (390,328))
        pantalla.blit(num4, (218,78))
        pantalla.blit(num4, (390,276))
        pantalla.blit(num5, (279,78))
        pantalla.blit(num5, (390,224))
        pantalla.blit(num6, (340,78))
        pantalla.blit(num6, (390,172))
        pantalla.blit(num7,(390,115))
        pantalla.blit(reglas,(415,115))
        # tablero
        pygame.draw.line(pantalla, NEGRO, (10, 100), (10, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (72, 100), (72, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (133, 100), (133, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (194, 100), (194, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (255, 100), (255, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (316, 100), (316, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 100), (380, 100), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 152), (380, 152), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 204), (380, 204), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 256), (380, 256), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 308), (380, 308), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 360), (380, 360), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 412), (380, 412), 3)
        pygame.draw.line(pantalla, NEGRO, (380, 100), (380, 470), 3)
        pygame.draw.line(pantalla, NEGRO, (10, 470), (380, 470), 3)
        pygame.display.flip()
        clock.tick(30)

#iniciamos las funciones para que se inicie el juego
pygame.init()
juego()
pygame.quit()

#Faltan cosillas como poner un mensaje al final de quien ha ganado y un boton de volver a reiniciar el juego
