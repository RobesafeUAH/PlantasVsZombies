/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author jonat
 */
public class ExepcionComando {
    
    private String arg1;
    private String arg2;
    private String arg3;

    public ExepcionComando(String arg1, String arg2, String arg3) {
        this.arg1 = arg1;
        this.arg2 = arg2;
        this.arg3 = arg3;
    }

    public String getArg3() {
        return arg3;
    }

    public void setAgr3(String agr3) {
        this.arg3 = agr3;
    }


    public String getArg2() {
        return arg2;
    }

    public void setArg2(String arg2) {
        this.arg2 = arg2;
    }


    public String getArg1() {
        return arg1;
    }

    public void setArg1(String arg1) {
        this.arg1 = arg1;
    }
    public boolean comprobacion(){
        boolean comp;
        if (arg1.equals("G") || arg1.equals("L")) {
            if (Integer.parseInt(arg2)>=1 && Integer.parseInt(arg3)>=1) {
               comp=true; 
            }else{
                comp=false;
            }
        }else{
            comp=false;
        }
        return comp;
    }
}
