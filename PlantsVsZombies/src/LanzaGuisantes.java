/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jonat
 */
public class LanzaGuisantes extends Girasol{
    
    private int alcance;

    public LanzaGuisantes(int alcance) {
        this.coste = 50;
        this.vida = 3;
        this.frecuencia = 1;
        this.daño = 1;
        this.alcance=alcance;
    }

    public int getAlcance() {
        return alcance;
    }

    public void setAlcance(int alcance) {
        this.alcance = alcance;
    }

}
