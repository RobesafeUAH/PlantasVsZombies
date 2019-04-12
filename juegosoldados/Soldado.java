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
public class Soldado {
    String nombre= "Desconocido";
    int vida = 100;
    int punteria= 50;
    Arma arma= null;
    String GetNombre(){
        return nombre;
    }
    int GetVida(){
        return vida;
    }
    int GetPunteria(){
        return punteria;
    }
    Arma GetArma(){
        return arma;
    }
    void SetArma(Arma armacogida){
        this.arma=armacogida;
    }
    Soldado(String nombre,int vida,int punteria){
        this.nombre=nombre;
        this.vida=vida;
        this.punteria=punteria;
    }
    void Disparar(Soldado objetivo){
        System.out.println(this.nombre + " dispara a "+ objetivo.nombre);
        arma.Disparar(objetivo);
    }
    void RecibirDaño(int daño){
        vida-= daño;
        System.out.println(this.nombre + " recibe" +daño +"daños y se queda con " + vida + " de vida.");
        if(vida<=0){
            Morir();
        }
    }
    void CurarDaño(int curacion){
        if (vida>0){
            System.out.println(this.nombre + "se cura" +curacion +"y se queda con " + vida + " de vida.");
            vida+=curacion;
        }
    }
    void Morir(){
        System.out.println(this.nombre + " ha muerto.");
    }
}
