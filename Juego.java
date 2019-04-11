
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
        String s = "N";
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
                tablero(filas, columnas);
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
            String com1=palabrasSeparadas[0].toUpperCase();
            tablero(filas, columnas);
            if (com1.equals("S")) {
                System.out.println("Saliendo del juego.");
                s="S";
            }           
        }
    }

    private static void tablero(int fil, int columna) {
        int fila = fil * 2 + 1;
        int col = columna * 2 + 1;
        String raya = "-------";
        String sep = "|";
        String esp = "           ";
        String tablero[][] = new String[fila][col];
        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < col; j++) {
                if (j == 0 || j == (col - 1)) {
                    tablero[i][j] = sep;
                } else if (i % 2 != 0) {
                    if (j % 2 != 0) {
                        tablero[i][j] = esp;
                    } else {
                        tablero[i][j] = sep + " ";
                    }
                } else if (i % 2 == 0) {
                    if (j != 0 && j != (col - 1)) {
                        tablero[i][j] = raya;
                    }
                }
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
