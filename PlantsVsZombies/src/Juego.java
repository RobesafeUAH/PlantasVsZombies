
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author jonat
 */
public class Juego {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        int turno = 0;
        int filas = 0;
        int columnas = 0;
        int planta = 0;
        String s = "N";
        String per[][] = new String[30][3];
        for (int i = 0; i < 30; i++) {
            for (int j = 0; j < 3; j++) {
                switch (j) {
                    case 0:
                        per[i][j]="0";
                        break;
                    case 1:
                        per[i][j]="0";
                        break;
                    case 2:
                        per[i][j]="0";
                        break;
                }
            }
        }
        /**for (int i = 0; i < 30; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(per[i][j]);
            }
            System.out.println("");
        }*/
        while (!s.equals("S")) {
            System.out.println("(Teclear ayuda para lista de comandos.<Enter> para terminar el turno.)");
            System.out.print(">");
            String pComando = entrada.nextLine();
            String[] pSeparadas = pComando.split(" ");
            String p1 = pSeparadas[0].toUpperCase();
            if (pSeparadas.length == 4 && p1.equals("N")) {
                filas = Integer.parseInt(pSeparadas[1]);
                columnas = Integer.parseInt(pSeparadas[2]);
                System.out.println("Comenzando la partida.");
                tablero(filas, columnas, per);
                s = "S";
            } else if (p1.equals("AYUDA")) {
                ayuda();
            } else {
                System.out.println("Introduzca un mensaje correcto");
            }
        }
        s = "N";
        while (turno < 30 && !s.equals("S")) {
            turno += 1;
            System.out.println("Tienes 50 soles y es el turno " + turno);
            System.out.println("(Teclear ayuda para lista de comandos.<Enter> para terminar el turno.)");
            System.out.print(">");
            String comando = entrada.nextLine();
            String[] palabrasSeparadas = comando.split(" ");
            String com1 = palabrasSeparadas[0].toUpperCase();
            if (palabrasSeparadas.length == 3) {
                ExepcionComando exep1 = new ExepcionComando(palabrasSeparadas[0].toUpperCase(), palabrasSeparadas[1].toUpperCase(), palabrasSeparadas[2].toUpperCase());
                if (exep1.comprobacion()) {
                    if (palabrasSeparadas[0].toUpperCase().equals("G")) {
                        Girasol girasol = new Girasol();
                        per[planta][0] = "G";
                    } else {
                        LanzaGuisantes l1= new LanzaGuisantes(columnas);
                        per[planta][0] = "L";
                    }
                    per[planta][1] = palabrasSeparadas[1];
                    per[planta][2] = palabrasSeparadas[2];
                }
                /**for (int i = 0; i < 30; i++) {
                    for (int j = 0; j < 3; j++) {
                        System.out.print(per[i][j]);
                }
                    System.out.println("");
                }*/
            }
            tablero(filas, columnas, per);
            if (com1.equals("S")) {
                System.out.println("Saliendo del juego.");
                s = "S";
            }
            planta += 1;
        }
    }

    private static void tablero(int fil, int columna, String[][] per) {
        int fila = fil * 2 + 1;
        int col = columna * 2 + 1;
        String raya = "----";
        String esp = "       ";
        String sep = "|";
        String fin = "---|";
        String tablero[][] = new String[fila][col];
        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < col; j++) {
                if (i % 2 == 0) {
                    if (j == 0) {
                        tablero[i][j] = sep;
                    } else if (j == (col - 1)) {
                        tablero[i][j] = fin;
                    } else {
                        tablero[i][j] = raya;
                    }
                } else {
                    if (j == 0) {
                        tablero[i][j] = sep;
                    } else if (j == (col - 1)) {
                        tablero[i][j] = sep;
                    } else if (j % 2 == 0) {
                        tablero[i][j] = sep;
                    } else {
                        
                            tablero[i][j] = esp;
                        
                    }
                }
            }
        }
        
        for (int k=0;k<30;k++) {
            int fP = Integer.parseInt(per[k][1]);
            int cP = Integer.parseInt(per[k][2]);
            if (fP==2) {
                fP+=1;
            }else if (fP > 2) {
                fP += (fP-1);
            }
            if (cP == 2) {
                cP += 1;
            }else if (cP > 2) {
                cP += (cP-1);
            }
            if (per[k][0].equals("G") || per[k][0].equals("L")) {
                tablero[fP][cP] = " " + per[k][0] + "("+fP+","+cP+")";
            }
        }
        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(tablero[i][j]);
            }
            System.out.println("");
        }
        System.out.println("");

    }

    private static void ayuda() {
        System.out.println("N <filas> <columnas> <Dificultad>: Nueva partida (Dificultad: BAJA, MEDIA, ALTA, IMPOSIBLE).");
        System.out.println("G <fila> <columna>: colocar girasol. Únicamente se podrá añadir un nuevo Girasol por turno y si tiene el número suficiente de soles. No podrá añadir un Girasol en una casilla ocupada por otra planta o por un zombi.");
        System.out.println("L <fila> <columna>: colocar LanzaGuisantes. Únicamente se podrá añadir un nuevo LanzaGuisantes por turno y si tiene el número suficiente de soles. No podrá añadir un LanzaGuisantes en una casilla ocupada por otra planta o por un zombi.");
        System.out.println("S: Salir de la aplicación.");
        System.out.println("<Enter>: Pasar Turno");
    }
}
