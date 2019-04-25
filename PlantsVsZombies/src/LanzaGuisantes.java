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

    public LanzaGuisantes(int coste, int vida, int frecuencia, int daño,int alcance) {
        super();
        this.alcance=alcance;
    }

    public int getAlcance() {
        return alcance;
    }

    public void setAlcance(int alcance) {
        this.alcance = alcance;
    }

}
