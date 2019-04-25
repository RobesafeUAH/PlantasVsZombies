/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jonat
 */
public class Jugador {
    
    private int soles;

    public Jugador() {
        this.soles = 50;
    }

    public int getSoles() {
        return soles;
    }

    public void setSoles(int soles) {
        this.soles = soles;
    }
    public void masSoles(int ingreso_sol){
        this.soles+=ingreso_sol;
    }
    public void menosSoles(int ingreso_sol){
        this.soles-=ingreso_sol;
    }
}
