/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jonat
 */
public class Girasol {
   
    private int coste;
    private int vida;
    private int frecuencia;
    private int daño;
    

    public Girasol() {
        this.coste = 20;
        this.vida = 1;
        this.frecuencia = 10;
        this.daño = 0;
    }
    
    public int getDaño() {
        return daño;
    }

    public void setDaño(int daño) {
        this.daño = daño;
    }


    public int getFrecuencia() {
        return frecuencia;
    }

    public void setFrecuencia(int frecuencia) {
        this.frecuencia = frecuencia;
    }


    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }


    public int getCoste() {
        return coste;
    }

    public void setCoste(int coste) {
        this.coste = coste;
    }
    public int generarSoles(int turno){
        int soles=0;
        if (turno%2==0) {
            soles=getFrecuencia();
        }
        return soles;
    }
}
