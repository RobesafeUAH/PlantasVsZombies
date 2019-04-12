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
public class Arma {
    String nombre;
    int daño;
    int municionCargador;
    
    Arma(String nombre,int daño,int municionCargador){
        this.nombre=nombre;
        this.daño=daño;
        this.municionCargador=municionCargador;
    }
    String GetNombre(){
        return nombre;
    }
    int GetDaño(){
        return daño;
    }
    int GetMunicion(){
        return municionCargador;
    }
    void Disparar(Soldado objetivo){
        if (municionCargador>0){
            System.out.println(objetivo.GetNombre() + "recibe un disparo de "+ this.nombre);
            municionCargador-=1;
            objetivo.RecibirDaño(daño);
        }else{
            System.out.println(this.nombre + "no tiene municion");
   }
        
    }
    void Recargar(){
    
    }
}
