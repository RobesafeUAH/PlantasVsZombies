/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package juegosoldados;

/**
 *
 * @author jonat
 */
public class JuegoSoldados {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Soldado soldado1= new Soldado("Adrian",100,50);
        Soldado soldado2= new Soldado("Rosalia",200,75);
        Soldado soldado3= new Soldado("Tomasa",50,100);
        
        Arma arma1= new Arma("Pistola",5,16);
        Arma arma2= new Arma("Pistola",20,4);
        Arma arma3= new Arma("Pistola",100,1);
        
        soldado1.SetArma(arma1);
        soldado2.SetArma(arma2);
        soldado3.SetArma(arma3);
        
        soldado1.Disparar(soldado2);
        soldado2.Disparar(soldado3);
        soldado3.Disparar(soldado1);
        
        
    }
    
}
