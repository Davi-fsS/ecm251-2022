import javax.swing.event.SwingPropertyChangeSupport;

public class Caneta{

    //Características da caneta - ATRIBUTOS
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int CARGA_INICIAL = 100;

    //Comportamentos da caneta - MÉTODOS
    void escrever(String texto){
        for(int i = 0; i < texto.length(); i++){
            if(this.carga > 0){
                System.out.print(texto.charAt(i));  //texto[i]
                this.carga -= 1;
            }
            else{
                System.out.print("\nCANETA SEM COR!!");
                break;
            }
        }
        System.out.println();
    }

    void mostrarCarga(){
        System.out.println("Carga atual:" + this.carga);
    }

    void iniciarCaneta(String cor, String modelo, double ponta){
        this.cor = cor;
        this.modelo = modelo;
        this.carga = CARGA_INICIAL;
        this.ponta = ponta;
    }

    String mostrarDados(){
        return "Modelo:" + this.modelo + 
        " - Cor:" + this.cor +
        " - Ponta:" + this.ponta +
        " - Carga:" + this.carga; 
    }
}
